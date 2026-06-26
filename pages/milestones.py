import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import database as db
from components.ui import render_milestone_card

def show():
    u = st.session_state.user
    st.markdown('<div class="page-title">🏆 Milestones</div>', unsafe_allow_html=True)
    st.markdown('<div style="color:#6B6B8A;margin-bottom:1.2rem">Celebrate achievements — big or small, in any field</div>',
                unsafe_allow_html=True)

    with st.expander("🎉 Share a Milestone", expanded=False):
        with st.form("add_milestone"):
            title = st.text_input("Milestone Title", placeholder="e.g. Completed my first SQL project!")
            desc  = st.text_area("More details (optional)", height=80)
            col1, col2 = st.columns(2)
            with col1:
                skill_tag = st.text_input("Related Skill (optional)", placeholder="e.g. SQL")
            with col2:
                is_public = st.checkbox("Make Public", value=True)
            if st.form_submit_button("Share Milestone 🎉", use_container_width=True):
                if title.strip():
                    db.add_milestone(u["id"], title.strip(), desc.strip(), skill_tag.strip() or None, is_public)
                    st.balloons()
                    st.success("Milestone shared!")
                    st.rerun()

    st.markdown("---")

    tab1, tab2 = st.tabs(["🌍 Community", "🙋 Mine"])

    with tab1:
        milestones = db.get_milestones(public_only=True)
        if not milestones:
            st.markdown('<div style="color:#6B6B8A;text-align:center;padding:2rem">No milestones yet — share yours!</div>',
                        unsafe_allow_html=True)
        for m in milestones:
            render_milestone_card(m)

    with tab2:
        my_milestones = db.get_milestones(user_id=u["id"])
        if not my_milestones:
            st.markdown('<div style="color:#6B6B8A;text-align:center;padding:2rem">You haven\'t shared any milestones yet.</div>',
                        unsafe_allow_html=True)
        for m in my_milestones:
            render_milestone_card(m)