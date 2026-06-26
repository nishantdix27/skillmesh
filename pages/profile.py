import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import database as db
from components.ui import avatar_html, skill_badge, AVATAR_COLORS, DOMAINS, LEVELS

def show():
    u = st.session_state.user
    st.markdown('<div class="page-title">👤 My Profile</div>', unsafe_allow_html=True)

    skills       = db.get_user_skills(u["id"])
    followers    = db.get_followers(u["id"])
    following    = db.get_following(u["id"])
    posts        = db.get_user_posts(u["id"])
    public_count = db.count_public_skills(u["id"])

    # ── Stats row ──────────────────────────────────
    c1, c2, c3, c4 = st.columns(4)
    for col, num, label in [
        (c1, len(skills),       "Total Skills"),
        (c2, public_count,      "Public Skills"),
        (c3, len(followers),    "Followers"),
        (c4, len(following),    "Following"),
    ]:
        with col:
            st.markdown(f"""
            <div class="stat-box">
              <div class="stat-num">{num}</div>
              <div class="stat-lbl">{label}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("---")

    tab1, tab2, tab3 = st.tabs(["🎯 Skills", "📰 My Posts", "⚙️ Edit Profile"])

    # ── Tab 1: Skills ──────────────────────────────
    with tab1:
        with st.expander("➕ Add New Skill", expanded=not skills):
            with st.form("add_skill"):
                col1, col2 = st.columns(2)
                with col1:
                    skill_name = st.text_input("Skill Name", placeholder="e.g. SQL, Guitar, Cooking")
                    domain     = st.selectbox("Domain", DOMAINS)
                with col2:
                    level     = st.selectbox("Your Level", LEVELS)
                    is_public = st.checkbox("Make Public", value=True,
                                            help="Public skills help others find and match with you")
                if st.form_submit_button("Add Skill", use_container_width=True):
                    if skill_name.strip():
                        db.add_skill(u["id"], skill_name.strip(), domain, level, is_public)
                        st.success(f"'{skill_name}' added!")
                        st.rerun()

        if not skills:
            st.markdown('<div style="color:#6B6B8A;text-align:center;padding:2rem">No skills yet. Add your first one!</div>',
                        unsafe_allow_html=True)
        else:
            # Group by domain
            domains = {}
            for s in skills:
                domains.setdefault(s["domain"], []).append(s)

            for domain, domain_skills in domains.items():
                st.markdown(f'<div style="font-size:0.78rem;color:#6B6B8A;text-transform:uppercase;letter-spacing:.08em;margin:0.8rem 0 0.4rem">{domain}</div>',
                            unsafe_allow_html=True)
                for s in domain_skills:
                    vis = "🌍" if s["is_public"] else "🔒"
                    col1, col2 = st.columns([5, 1])
                    with col1:
                        st.markdown(f"""
                        <div style="display:flex;align-items:center;gap:8px;
                                    background:#1C1C30;border:1px solid #2A2A45;
                                    border-radius:8px;padding:0.5rem 0.8rem;margin-bottom:4px">
                          {skill_badge(s['skill_name'], s['level'])}
                          <span style="font-size:0.78rem;color:#6B6B8A">{s['level']}</span>
                          <span style="margin-left:auto;font-size:0.78rem">{vis}</span>
                        </div>""", unsafe_allow_html=True)
                    with col2:
                        if st.button("🗑️", key=f"del_{s['id']}", help="Remove skill"):
                            db.delete_skill(s["id"])
                            st.rerun()

    # ── Tab 2: Posts ───────────────────────────────
    with tab2:
        from components.ui import render_post_card
        if not posts:
            st.markdown('<div style="color:#6B6B8A;text-align:center;padding:2rem">No posts yet. Share something on the Feed!</div>',
                        unsafe_allow_html=True)
        else:
            for post in posts:
                render_post_card(post, u["id"], db)

    # ── Tab 3: Edit Profile ────────────────────────
    with tab3:
        with st.form("edit_profile"):
            full_name = st.text_input("Full Name", value=u.get("full_name",""))
            bio       = st.text_area("Bio", value=u.get("bio",""), height=100)
            st.markdown("**Pick your avatar color**")
            color_cols = st.columns(len(AVATAR_COLORS))
            chosen_color = u.get("avatar_color", AVATAR_COLORS[0])
            for i, color in enumerate(AVATAR_COLORS):
                with color_cols[i]:
                    st.markdown(f"""
                    <div style="width:28px;height:28px;border-radius:50%;
                                background:{color};margin:auto;
                                border:{'3px solid white' if color==chosen_color else '2px solid #2A2A45'}">
                    </div>""", unsafe_allow_html=True)

            new_color = st.selectbox("Avatar Color", AVATAR_COLORS,
                                      index=AVATAR_COLORS.index(chosen_color) if chosen_color in AVATAR_COLORS else 0)

            if st.form_submit_button("Save Changes", use_container_width=True):
                db.update_profile(u["id"], full_name, bio, new_color)
                st.session_state.user = db.get_user_by_id(u["id"])
                st.success("Profile updated!")
                st.rerun()