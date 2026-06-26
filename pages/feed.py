import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import database as db
from components.ui import apply_global_css, render_post_card, render_milestone_card, skill_badge, POST_TYPES, DOMAINS

def show():
    u = st.session_state.user

    st.markdown('<div class="page-title">🏠 Feed</div>', unsafe_allow_html=True)

    # ── New Post ──────────────────────────────────────
    with st.expander("✏️ Share something with your network", expanded=False):
        with st.form("new_post"):
            content = st.text_area("What are you learning or working on?", height=100,
                                    placeholder="e.g. Just mastered SQL window functions! Here's what I learned...")
            col1, col2, col3 = st.columns(3)
            with col1:
                ptype_label = st.selectbox("Type", list(POST_TYPES.keys()))
            with col2:
                skill_tag = st.text_input("Skill tag (optional)", placeholder="e.g. SQL, Guitar")
            with col3:
                is_public = st.checkbox("Public", value=True)

            if st.form_submit_button("Post", use_container_width=True):
                if content.strip():
                    db.create_post(u["id"], content.strip(), skill_tag.strip() or None,
                                   POST_TYPES[ptype_label], is_public)
                    st.success("Posted!")
                    st.rerun()

    st.markdown("---")

    # ── Feed tabs ─────────────────────────────────────
    tab1, tab2 = st.tabs(["📰 Posts", "🏆 Milestones"])

    with tab1:
        posts = db.get_feed_posts(u["id"])
        if not posts:
            st.markdown("""
            <div style="text-align:center;padding:3rem;color:#6B6B8A">
              <div style="font-size:2rem">🌱</div>
              <div>Your feed is empty. Follow people or add skills to get started!</div>
            </div>""", unsafe_allow_html=True)
        else:
            for post in posts:
                render_post_card(post, u["id"], db)

    with tab2:
        milestones = db.get_milestones(public_only=True)
        if not milestones:
            st.markdown('<div style="color:#6B6B8A;text-align:center;padding:2rem">No milestones yet. Be the first!</div>',
                        unsafe_allow_html=True)
        else:
            for m in milestones:
                render_milestone_card(m)