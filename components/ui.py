import streamlit as st
from datetime import datetime

AVATAR_COLORS = [
    "#6C63FF", "#FF6584", "#43C6AC", "#F7971E", "#4776E6",
    "#11998E", "#F953C6", "#B91D73", "#1D976C", "#ee0979"
]

DOMAINS = [
    "Technology", "Data & Analytics", "Design", "Marketing",
    "Finance", "Language Learning", "Arts & Music", "Science",
    "Business", "Health & Fitness", "Education", "Other"
]

LEVELS = ["Beginner", "Intermediate", "Advanced", "Expert"]

POST_TYPES = {
    "📢 Update": "update",
    "❓ Question": "question",
    "💡 Tip": "tip",
    "🔗 Resource Share": "resource",
}

def apply_global_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Background */
    .stApp {
        background: #0F0F1A;
        color: #E8E8F0;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: #16162A !important;
        border-right: 1px solid #2A2A45;
    }

    /* Cards */
    .sm-card {
        background: #1C1C30;
        border: 1px solid #2A2A45;
        border-radius: 12px;
        padding: 1.2rem 1.4rem;
        margin-bottom: 1rem;
        transition: border-color 0.2s;
    }
    .sm-card:hover { border-color: #6C63FF44; }

    .sm-card-highlight {
        background: linear-gradient(135deg, #1C1C30 0%, #1A1A2E 100%);
        border: 1px solid #6C63FF55;
        border-radius: 12px;
        padding: 1.2rem 1.4rem;
        margin-bottom: 1rem;
    }

    /* Avatar */
    .sm-avatar {
        width: 42px; height: 42px;
        border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 700; font-size: 1rem;
        color: white; flex-shrink: 0;
    }

    .sm-avatar-lg {
        width: 72px; height: 72px;
        border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 700; font-size: 1.6rem;
        color: white;
    }

    /* Skill badge */
    .skill-badge {
        display: inline-block;
        background: #6C63FF22;
        border: 1px solid #6C63FF55;
        color: #A89CFF;
        border-radius: 20px;
        padding: 3px 12px;
        font-size: 0.78rem;
        font-weight: 500;
        margin: 2px;
    }

    .skill-badge-green {
        background: #43C6AC22;
        border: 1px solid #43C6AC55;
        color: #43C6AC;
    }

    .skill-badge-orange {
        background: #F7971E22;
        border: 1px solid #F7971E55;
        color: #F7971E;
    }

    /* Post type tags */
    .tag-update  { background:#6C63FF22; color:#A89CFF; border:1px solid #6C63FF44; }
    .tag-question{ background:#F7971E22; color:#F7971E; border:1px solid #F7971E44; }
    .tag-tip     { background:#43C6AC22; color:#43C6AC; border:1px solid #43C6AC44; }
    .tag-resource{ background:#FF658422; color:#FF8FA3; border:1px solid #FF658444; }

    .post-tag {
        display:inline-block; border-radius:20px;
        padding:2px 10px; font-size:0.72rem; font-weight:600;
    }

    /* Username */
    .sm-username { font-weight:600; color:#E8E8F0; font-size:0.95rem; }
    .sm-handle   { color:#6B6B8A; font-size:0.8rem; }
    .sm-time     { color:#6B6B8A; font-size:0.75rem; }

    /* Stat box */
    .stat-box {
        background:#1C1C30; border:1px solid #2A2A45; border-radius:10px;
        padding:0.8rem; text-align:center;
    }
    .stat-num { font-size:1.6rem; font-weight:700; color:#6C63FF; font-family:'Space Grotesk',sans-serif; }
    .stat-lbl { font-size:0.72rem; color:#6B6B8A; text-transform:uppercase; letter-spacing:.05em; }

    /* Section header */
    .section-header {
        font-family:'Space Grotesk',sans-serif;
        font-size:1.1rem; font-weight:600;
        color:#E8E8F0; margin-bottom:0.8rem;
        padding-bottom:0.4rem;
        border-bottom:1px solid #2A2A45;
    }

    /* Milestone */
    .milestone-card {
        background: linear-gradient(135deg,#1C1C30,#16162A);
        border:1px solid #43C6AC44;
        border-left:3px solid #43C6AC;
        border-radius:10px; padding:1rem 1.2rem; margin-bottom:0.8rem;
    }

    /* Inputs */
    .stTextInput input, .stTextArea textarea, .stSelectbox select {
        background:#1C1C30 !important;
        border:1px solid #2A2A45 !important;
        color:#E8E8F0 !important;
        border-radius:8px !important;
    }

    /* Buttons */
    .stButton>button {
        background: linear-gradient(135deg,#6C63FF,#4776E6);
        color:white; border:none; border-radius:8px;
        font-weight:600; transition:opacity 0.2s;
    }
    .stButton>button:hover { opacity:0.85; }

    /* Message bubble */
    .msg-sent {
        background:#6C63FF22; border:1px solid #6C63FF44;
        border-radius:12px 12px 2px 12px;
        padding:0.6rem 1rem; margin:4px 0; max-width:80%;
        margin-left:auto; color:#E8E8F0;
    }
    .msg-recv {
        background:#1C1C30; border:1px solid #2A2A45;
        border-radius:12px 12px 12px 2px;
        padding:0.6rem 1rem; margin:4px 0; max-width:80%;
        color:#E8E8F0;
    }

    /* Match card */
    .match-card {
        background:#1C1C30; border:1px solid #2A2A45;
        border-radius:12px; padding:1rem 1.2rem; margin-bottom:0.8rem;
    }
    .match-score {
        background:#6C63FF; color:white;
        border-radius:20px; padding:2px 10px;
        font-size:0.78rem; font-weight:700;
    }

    /* Page title */
    .page-title {
        font-family:'Space Grotesk',sans-serif;
        font-size:1.6rem; font-weight:700;
        color:#E8E8F0; margin-bottom:1.2rem;
    }

    /* Divider */
    hr { border-color:#2A2A45 !important; }

    /* Toast-like */
    .sm-success {
        background:#43C6AC22; border:1px solid #43C6AC55;
        color:#43C6AC; border-radius:8px; padding:0.6rem 1rem;
        font-size:0.88rem; margin-bottom:0.6rem;
    }

    /* Hide streamlit branding */
    #MainMenu, footer { visibility:hidden; }
    </style>
    """, unsafe_allow_html=True)


def avatar_html(name, color, size="sm"):
    initial = (name or "?")[0].upper()
    cls = "sm-avatar-lg" if size == "lg" else "sm-avatar"
    return f'<div class="{cls}" style="background:{color}">{initial}</div>'


def skill_badge(skill_name, level=""):
    level_class = {
        "Intermediate": "skill-badge-green",
        "Advanced": "skill-badge-orange",
        "Expert": "skill-badge-orange",
    }.get(level, "")
    return f'<span class="skill-badge {level_class}">{skill_name}</span>'


def time_ago(ts_str):
    try:
        ts = datetime.strptime(ts_str[:19], "%Y-%m-%d %H:%M:%S")
        diff = datetime.now() - ts
        s = diff.total_seconds()
        if s < 60: return "just now"
        if s < 3600: return f"{int(s//60)}m ago"
        if s < 86400: return f"{int(s//3600)}h ago"
        return f"{int(s//86400)}d ago"
    except:
        return ""


def post_type_tag(post_type):
    icons = {"update":"📢","question":"❓","tip":"💡","resource":"🔗"}
    classes = {"update":"tag-update","question":"tag-question","tip":"tag-tip","resource":"tag-resource"}
    icon = icons.get(post_type, "📢")
    cls  = classes.get(post_type, "tag-update")
    return f'<span class="post-tag {cls}">{icon} {post_type.capitalize()}</span>'


def render_post_card(post, current_user_id, db):
    liked = db.user_liked_post(current_user_id, post["id"])
    heart = "❤️" if liked else "🤍"

    st.markdown(f"""
    <div class="sm-card">
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:0.6rem">
        {avatar_html(post['full_name'] or post['username'], post['avatar_color'])}
        <div>
          <div class="sm-username">{post['full_name'] or post['username']}</div>
          <div class="sm-handle">@{post['username']} · <span class="sm-time">{time_ago(post['created_at'])}</span></div>
        </div>
        <div style="margin-left:auto">{post_type_tag(post['post_type'])}</div>
      </div>
      <div style="color:#C8C8DC;line-height:1.6;margin-bottom:0.6rem">{post['content']}</div>
      {'<div>' + skill_badge(post["skill_tag"]) + '</div>' if post.get("skill_tag") else ''}
      <div style="margin-top:0.8rem;color:#6B6B8A;font-size:0.8rem">
        {heart} {post['like_count']} likes
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Show image if post has one
    if post.get("image_data"):
        st.image(post["image_data"], use_column_width=True)

    col1, col2 = st.columns([1, 6])
    with col1:
        if st.button(heart, key=f"like_{post['id']}"):
            db.toggle_like(current_user_id, post["id"])
            st.rerun()


def render_milestone_card(m):
    st.markdown(f"""
    <div class="milestone-card">
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:0.4rem">
        {avatar_html(m['full_name'] or m['username'], '#43C6AC')}
        <div>
          <div class="sm-username">🏆 {m['title']}</div>
          <div class="sm-handle">@{m['username']} · {time_ago(m['created_at'])}</div>
        </div>
        {'<div style="margin-left:auto">' + skill_badge(m["skill_tag"]) + '</div>' if m.get("skill_tag") else ''}
      </div>
      {f'<div style="color:#C8C8DC;font-size:0.88rem;margin-top:0.4rem">{m["description"]}</div>' if m.get("description") else ''}
    </div>
    """, unsafe_allow_html=True)