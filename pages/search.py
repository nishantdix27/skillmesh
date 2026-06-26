import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import database as db
from components.ui import avatar_html, skill_badge, DOMAINS

def show():
    u = st.session_state.user
    st.markdown('<div class="page-title">🔍 Search Skills & People</div>', unsafe_allow_html=True)

    query = st.text_input("Search by skill, domain, or username",
                           placeholder="e.g. Python, Guitar, Machine Learning, Spanish...")

    tab1, tab2 = st.tabs(["🎯 Search by Skill", "👤 Search People"])

    with tab1:
        if query:
            results = db.search_by_skill(query)
            if not results:
                st.markdown(f'<div style="color:#6B6B8A;padding:1rem">No one found learning "{query}" yet. You could be the first!</div>',
                            unsafe_allow_html=True)
            else:
                st.markdown(f'<div style="color:#6B6B8A;font-size:0.85rem;margin-bottom:1rem">{len(results)} learner(s) found</div>',
                            unsafe_allow_html=True)
                # Group by user
                seen = {}
                for r in results:
                    uid = r["id"]
                    if uid not in seen:
                        seen[uid] = {"user": r, "skills": []}
                    seen[uid]["skills"].append({"name": r["skill_name"], "level": r["level"]})

                for uid, data in seen.items():
                    usr = data["user"]
                    already_following = db.is_following(u["id"], uid)

                    st.markdown(f"""
                    <div class="sm-card">
                      <div style="display:flex;align-items:center;gap:12px;margin-bottom:0.6rem">
                        {avatar_html(usr['full_name'] or usr['username'], usr['avatar_color'])}
                        <div style="flex:1">
                          <div class="sm-username">{usr['full_name'] or usr['username']}</div>
                          <div class="sm-handle">@{usr['username']}</div>
                          {f'<div style="color:#9898B0;font-size:0.82rem;margin-top:2px">{usr["bio"]}</div>' if usr.get("bio") else ''}
                        </div>
                      </div>
                      <div>{''.join(skill_badge(s['name'], s['level']) for s in data['skills'])}</div>
                    </div>
                    """, unsafe_allow_html=True)

                    col1, col2 = st.columns([1, 4])
                    with col1:
                        if uid != u["id"]:
                            label = "✅ Following" if already_following else "➕ Follow"
                            if st.button(label, key=f"follow_s_{uid}"):
                                if already_following:
                                    db.unfollow_user(u["id"], uid)
                                else:
                                    db.follow_user(u["id"], uid)
                                st.rerun()
                    with col2:
                        if uid != u["id"]:
                            if st.button("💬 Message", key=f"msg_s_{uid}"):
                                st.session_state.chat_with = uid
                                st.session_state.page = "messages"
                                st.rerun()
        else:
            # Show domain quick picks
            st.markdown('<div class="section-header">Browse by Domain</div>', unsafe_allow_html=True)
            cols = st.columns(3)
            for i, domain in enumerate(DOMAINS):
                with cols[i % 3]:
                    if st.button(domain, key=f"domain_{domain}", use_container_width=True):
                        pass  # could filter

    with tab2:
        if query:
            results = db.search_users(query)
            if not results:
                st.markdown(f'<div style="color:#6B6B8A;padding:1rem">No users found for "{query}"</div>',
                            unsafe_allow_html=True)
            else:
                for usr in results:
                    if usr["id"] == u["id"]:
                        continue
                    user_skills = db.get_user_skills(usr["id"])
                    public_skills = [s for s in user_skills if s["is_public"]]
                    already_following = db.is_following(u["id"], usr["id"])

                    st.markdown(f"""
                    <div class="sm-card">
                      <div style="display:flex;align-items:center;gap:12px;margin-bottom:0.6rem">
                        {avatar_html(usr['full_name'] or usr['username'], usr['avatar_color'])}
                        <div style="flex:1">
                          <div class="sm-username">{usr['full_name'] or usr['username']}</div>
                          <div class="sm-handle">@{usr['username']}</div>
                          {f'<div style="color:#9898B0;font-size:0.82rem;margin-top:2px">{usr["bio"]}</div>' if usr.get("bio") else ''}
                        </div>
                        <div style="font-size:0.78rem;color:#6B6B8A">{len(public_skills)} public skills</div>
                      </div>
                      <div>{''.join(skill_badge(s['skill_name'], s['level']) for s in public_skills[:5])}</div>
                    </div>
                    """, unsafe_allow_html=True)

                    col1, col2 = st.columns([1, 4])
                    with col1:
                        label = "✅ Following" if already_following else "➕ Follow"
                        if st.button(label, key=f"follow_u_{usr['id']}"):
                            if already_following:
                                db.unfollow_user(u["id"], usr["id"])
                            else:
                                db.follow_user(u["id"], usr["id"])
                            st.rerun()
                    with col2:
                        if st.button("💬 Message", key=f"msg_u_{usr['id']}"):
                            st.session_state.chat_with = usr["id"]
                            st.session_state.page = "messages"
                            st.rerun()