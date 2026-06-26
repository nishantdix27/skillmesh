import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

import database as db
from components.ui import apply_global_css, avatar_html, AVATAR_COLORS

st.set_page_config(
    page_title="SkillMesh",
    page_icon="🔗",
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_global_css()
db.init_db()

# ── Session defaults ──────────────────────────────────
for key, val in {
    "user": None,
    "page": "feed",
    "chat_with": None,
    "view_profile": None,
}.items():
    if key not in st.session_state:
        st.session_state[key] = val


# ── Auth screens ──────────────────────────────────────
def show_auth():
    st.markdown("""
    <div style="text-align:center;padding:2rem 0 1rem">
      <div style="font-family:'Space Grotesk',sans-serif;font-size:2.6rem;font-weight:700;
                  background:linear-gradient(135deg,#6C63FF,#43C6AC);
                  -webkit-background-clip:text;-webkit-text-fill-color:transparent">
        SkillMesh
      </div>
      <div style="color:#6B6B8A;font-size:1rem;margin-top:0.3rem">
        Connect · Learn · Grow — in any domain
      </div>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["Sign In", "Create Account"])

    with tab1:
        with st.form("login"):
            u = st.text_input("Username")
            p = st.text_input("Password", type="password")
            if st.form_submit_button("Sign In", use_container_width=True):
                user = db.login_user(u, p)
                if user:
                    st.session_state.user = user
                    st.rerun()
                else:
                    st.error("Invalid username or password.")

    with tab2:
        with st.form("register"):
            fn = st.text_input("Full Name")
            un = st.text_input("Username")
            bio = st.text_area("Short Bio (optional)", height=80)
            pw = st.text_input("Password", type="password")
            pw2= st.text_input("Confirm Password", type="password")
            if st.form_submit_button("Create Account", use_container_width=True):
                if pw != pw2:
                    st.error("Passwords don't match.")
                elif not un or not fn:
                    st.error("Name and username are required.")
                else:
                    ok, msg = db.register_user(un, pw, fn, bio)
                    if ok:
                        user = db.login_user(un, pw)
                        st.session_state.user = user
                        st.rerun()
                    else:
                        st.error(msg)


# ── Sidebar nav ───────────────────────────────────────
def show_sidebar():
    u = st.session_state.user
    unread = db.get_unread_count(u["id"])

    with st.sidebar:
        # Logo
        st.markdown("""
        <div style="padding:0.5rem 0 1.2rem">
          <span style="font-family:'Space Grotesk',sans-serif;font-size:1.4rem;font-weight:700;
                       background:linear-gradient(135deg,#6C63FF,#43C6AC);
                       -webkit-background-clip:text;-webkit-text-fill-color:transparent">
            SkillMesh
          </span>
        </div>
        """, unsafe_allow_html=True)

        # User mini profile
        st.markdown(f"""
        <div style="display:flex;align-items:center;gap:10px;
                    background:#1C1C30;border-radius:10px;padding:0.7rem;margin-bottom:1rem">
          {avatar_html(u['full_name'] or u['username'], u['avatar_color'])}
          <div>
            <div style="font-weight:600;font-size:0.88rem;color:#E8E8F0">{u['full_name'] or u['username']}</div>
            <div style="font-size:0.75rem;color:#6B6B8A">@{u['username']}</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

        nav_items = [
            ("feed",      "🏠", "Feed"),
            ("search",    "🔍", "Search Skills"),
            ("matches",   "🤝", "Peer Matches"),
            ("messages",  "💬", f"Messages{'  🔴' if unread else ''}"),
            ("profile",   "👤", "My Profile"),
            ("milestones","🏆", "Milestones"),
            ("about",     "ℹ️",  "About SkillMesh"),
        ]

        for page_key, icon, label in nav_items:
            active = st.session_state.page == page_key
            style = "background:#6C63FF22;border-left:3px solid #6C63FF;" if active else ""
            if st.sidebar.button(f"{icon}  {label}", key=f"nav_{page_key}",
                                  use_container_width=True):
                st.session_state.page = page_key
                st.session_state.chat_with = None
                st.session_state.view_profile = None
                st.rerun()

        st.markdown("---")
        if st.sidebar.button("🚪  Sign Out", use_container_width=True):
            for k in ["user","page","chat_with","view_profile"]:
                st.session_state[k] = None if k != "page" else "feed"
            st.session_state.user = None
            st.rerun()


# ── Page router ───────────────────────────────────────
def route():
    page = st.session_state.page

    if page == "feed":
        from pages.feed import show
    elif page == "search":
        from pages.search import show
    elif page == "matches":
        from pages.matches import show
    elif page == "messages":
        from pages.messages import show
    elif page == "profile":
        from pages.profile import show
    elif page == "milestones":
        from pages.milestones import show
    elif page == "about":
        from pages.about import show
    elif page == "view_profile":
        from pages.view_profile import show
    else:
        from pages.feed import show

    show()


# ── Entry ─────────────────────────────────────────────
if not st.session_state.user:
    show_auth()
else:
    # Refresh user data
    st.session_state.user = db.get_user_by_id(st.session_state.user["id"])
    show_sidebar()
    route()