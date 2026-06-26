import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import database as db
from components.ui import avatar_html, skill_badge

def show():
    u = st.session_state.user
    st.markdown('<div class="page-title">🤝 Peer Matches</div>', unsafe_allow_html=True)
    st.markdown('<div style="color:#6B6B8A;margin-bottom:1.2rem">People learning the same skills as you — ranked by overlap</div>',
                unsafe_allow_html=True)

    matches = db.get_peer_matches(u["id"])

    if not matches:
        st.markdown("""
        <div style="text-align:center;padding:3rem;color:#6B6B8A">
          <div style="font-size:2.5rem">🌐</div>
          <div style="margin-top:0.5rem">No matches yet.</div>
          <div style="font-size:0.85rem;margin-top:0.3rem">Add more skills to your profile to find your peers!</div>
        </div>""", unsafe_allow_html=True)
        return

    for match in matches:
        already_following = db.is_following(u["id"], match["id"])
        skills_html = "".join(
            f'<span class="skill-badge skill-badge-green">{s.strip()}</span>'
            for s in match["matched_skills"].split(",")
        )

        st.markdown(f"""
        <div class="match-card">
          <div style="display:flex;align-items:center;gap:12px">
            {avatar_html(match['full_name'] or match['username'], match['avatar_color'])}
            <div style="flex:1">
              <div class="sm-username">{match['full_name'] or match['username']}</div>
              <div class="sm-handle">@{match['username']}</div>
              {f'<div style="color:#9898B0;font-size:0.82rem;margin-top:2px">{match["bio"]}</div>' if match.get("bio") else ''}
            </div>
            <div>
              <span class="match-score">🎯 {match['match_count']} match{'es' if match['match_count']>1 else ''}</span>
            </div>
          </div>
          <div style="margin-top:0.7rem">
            <div style="font-size:0.75rem;color:#6B6B8A;margin-bottom:4px">SHARED SKILLS</div>
            {skills_html}
          </div>
        </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 1, 4])
        with col1:
            label = "✅ Following" if already_following else "➕ Follow"
            if st.button(label, key=f"match_follow_{match['id']}"):
                if already_following:
                    db.unfollow_user(u["id"], match["id"])
                else:
                    db.follow_user(u["id"], match["id"])
                st.rerun()
        with col2:
            if st.button("💬 Chat", key=f"match_chat_{match['id']}"):
                st.session_state.chat_with = match["id"]
                st.session_state.page = "messages"
                st.rerun()