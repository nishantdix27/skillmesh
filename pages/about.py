import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

def show():
    st.markdown("""
    <!-- Hero Section -->
    <div style="text-align:center;padding:2.5rem 1rem 1.5rem">
      <div style="font-family:'Space Grotesk',sans-serif;font-size:2.8rem;font-weight:700;
                  background:linear-gradient(135deg,#6C63FF,#43C6AC);
                  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
                  margin-bottom:0.4rem">
        SkillMesh
      </div>
      <div style="font-size:1.15rem;color:#9898B0;margin-bottom:0.6rem">
        Connect · Learn · Grow — in any domain
      </div>
      <div style="display:inline-block;background:#6C63FF22;border:1px solid #6C63FF55;
                  color:#A89CFF;border-radius:20px;padding:6px 18px;font-size:0.85rem;font-weight:500">
        🌱 Built for learners, by a learner
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # ── The Problem ───────────────────────────────────
    st.markdown("""
    <div style="background:#1C1C30;border:1px solid #2A2A45;border-left:4px solid #FF6584;
                border-radius:12px;padding:1.4rem 1.6rem;margin-bottom:1.2rem">
      <div style="font-family:'Space Grotesk',sans-serif;font-size:1.1rem;font-weight:700;
                  color:#FF8FA3;margin-bottom:0.6rem">
        😕 The Problem
      </div>
      <div style="color:#C8C8DC;line-height:1.8;font-size:0.95rem">
        When you're learning something new — SQL, Python, guitar, a new language, cooking, anything —
        you're mostly learning <strong style="color:#E8E8F0">alone</strong>.<br><br>
        You search on Google. You watch YouTube videos. You struggle through errors by yourself.
        And when you look around for someone who is going through the <em>exact same thing</em> as you,
        right now, at the same level — there's no easy way to find them.<br><br>
        <strong style="color:#FF8FA3">LinkedIn</strong> shows what people already achieved —
        not what they're currently learning.<br>
        <strong style="color:#FF8FA3">YouTube & courses</strong> teach you — but don't connect you.<br>
        <strong style="color:#FF8FA3">Reddit & Discord</strong> have communities — but not personalized to your journey.
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ── The Solution ──────────────────────────────────
    st.markdown("""
    <div style="background:#1C1C30;border:1px solid #2A2A45;border-left:4px solid #43C6AC;
                border-radius:12px;padding:1.4rem 1.6rem;margin-bottom:1.2rem">
      <div style="font-family:'Space Grotesk',sans-serif;font-size:1.1rem;font-weight:700;
                  color:#43C6AC;margin-bottom:0.6rem">
        💡 The Solution — SkillMesh
      </div>
      <div style="color:#C8C8DC;line-height:1.8;font-size:0.95rem">
        SkillMesh is a <strong style="color:#E8E8F0">skill-based social learning network</strong>
        where people share <em>what they are currently learning</em> — not just what they've already mastered.<br><br>
        You add your active skills. The app finds your <strong style="color:#43C6AC">peers</strong> —
        people on the same journey right now.
        You follow them, chat privately, share your progress, ask questions,
        and celebrate each other's wins.<br><br>
        It works for <strong style="color:#E8E8F0">any domain</strong> —
        tech, music, finance, languages, cooking, fitness — anything you're working on.
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ── How It Works ──────────────────────────────────
    st.markdown('<div style="font-family:\'Space Grotesk\',sans-serif;font-size:1.1rem;font-weight:700;color:#E8E8F0;margin:1.4rem 0 0.8rem">⚙️ How It Works</div>', unsafe_allow_html=True)

    steps = [
        ("1", "#6C63FF", "Add Your Skills",
         "Tell SkillMesh what you're currently learning — SQL, Python, guitar, Spanish, anything. Set your level and make it public so others can find you."),
        ("2", "#F7971E", "Get Matched with Peers",
         "The app automatically finds people learning the same skills as you, ranked by how much overlap you share. Your learning tribe — found instantly."),
        ("3", "#43C6AC", "Follow, Post & Discuss",
         "Follow your peers. Share updates, tips, questions and resources on the feed. Tag your skill so the right people see your post."),
        ("4", "#FF6584", "Chat Privately",
         "Message anyone directly. Discuss problems, share solutions, or just motivate each other. Your own personal learning network."),
        ("5", "#6C63FF", "Celebrate Milestones",
         "Share your achievements — big or small. Got your first job interview? Finished a project? Let your network celebrate with you."),
    ]

    for num, color, title, desc in steps:
        st.markdown(f"""
        <div style="display:flex;gap:14px;align-items:flex-start;
                    background:#1C1C30;border:1px solid #2A2A45;
                    border-radius:10px;padding:1rem 1.2rem;margin-bottom:0.7rem">
          <div style="width:36px;height:36px;border-radius:50%;background:{color}22;
                      border:2px solid {color};color:{color};
                      display:flex;align-items:center;justify-content:center;
                      font-family:'Space Grotesk',sans-serif;font-weight:700;
                      font-size:0.95rem;flex-shrink:0">{num}</div>
          <div>
            <div style="font-weight:600;color:#E8E8F0;margin-bottom:3px">{title}</div>
            <div style="color:#9898B0;font-size:0.88rem;line-height:1.6">{desc}</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

    # ── Who Is It For ─────────────────────────────────
    st.markdown('<div style="font-family:\'Space Grotesk\',sans-serif;font-size:1.1rem;font-weight:700;color:#E8E8F0;margin:1.4rem 0 0.8rem">🎯 Who Is It For?</div>', unsafe_allow_html=True)

    personas = [
        ("👨‍💻", "Students & Learners", "Anyone learning a new skill — tech or non-tech — who wants to learn with others, not alone."),
        ("🔄", "Career Switchers", "People upskilling into a new field who want guidance from others on the same path."),
        ("🎨", "Hobbyists", "Learning guitar, painting, cooking, a new language? Find your community here."),
        ("💼", "Job Seekers", "Share your job search journey, swap tips on resumes, interviews and platforms with others in the same boat."),
    ]

    col1, col2 = st.columns(2)
    for i, (icon, title, desc) in enumerate(personas):
        with (col1 if i % 2 == 0 else col2):
            st.markdown(f"""
            <div style="background:#1C1C30;border:1px solid #2A2A45;border-radius:10px;
                        padding:1rem;margin-bottom:0.8rem;height:100%">
              <div style="font-size:1.6rem;margin-bottom:0.4rem">{icon}</div>
              <div style="font-weight:600;color:#E8E8F0;margin-bottom:4px">{title}</div>
              <div style="color:#9898B0;font-size:0.85rem;line-height:1.5">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    # ── What Makes It Different ───────────────────────
    st.markdown('<div style="font-family:\'Space Grotesk\',sans-serif;font-size:1.1rem;font-weight:700;color:#E8E8F0;margin:1.4rem 0 0.8rem">🆚 What Makes SkillMesh Different?</div>', unsafe_allow_html=True)

    st.markdown("""
    <div style="overflow-x:auto">
    <table style="width:100%;border-collapse:collapse;font-size:0.88rem">
      <thead>
        <tr style="background:#16162A">
          <th style="padding:10px 14px;text-align:left;color:#6B6B8A;border-bottom:1px solid #2A2A45">Platform</th>
          <th style="padding:10px 14px;text-align:left;color:#6B6B8A;border-bottom:1px solid #2A2A45">What It Does</th>
          <th style="padding:10px 14px;text-align:left;color:#6B6B8A;border-bottom:1px solid #2A2A45">What's Missing</th>
        </tr>
      </thead>
      <tbody>
        <tr style="border-bottom:1px solid #2A2A45">
          <td style="padding:10px 14px;color:#C8C8DC">LinkedIn</td>
          <td style="padding:10px 14px;color:#9898B0">Professional history & job hunting</td>
          <td style="padding:10px 14px;color:#FF8FA3">Not about current learning journey</td>
        </tr>
        <tr style="border-bottom:1px solid #2A2A45">
          <td style="padding:10px 14px;color:#C8C8DC">YouTube / Udemy</td>
          <td style="padding:10px 14px;color:#9898B0">Teaches skills through content</td>
          <td style="padding:10px 14px;color:#FF8FA3">No peer connection or community</td>
        </tr>
        <tr style="border-bottom:1px solid #2A2A45">
          <td style="padding:10px 14px;color:#C8C8DC">Discord / Reddit</td>
          <td style="padding:10px 14px;color:#9898B0">Topic-based communities</td>
          <td style="padding:10px 14px;color:#FF8FA3">Not personalized to your level/journey</td>
        </tr>
        <tr>
          <td style="padding:10px 14px;color:#A89CFF;font-weight:600">✨ SkillMesh</td>
          <td style="padding:10px 14px;color:#43C6AC">Live skill feed + peer matching by what you're learning NOW</td>
          <td style="padding:10px 14px;color:#43C6AC">✅ This gap is filled</td>
        </tr>
      </tbody>
    </table>
    </div>
    """, unsafe_allow_html=True)

    # ── One Line Pitch ────────────────────────────────
    st.markdown("""
    <div style="text-align:center;margin:2rem 0;
                background:linear-gradient(135deg,#6C63FF11,#43C6AC11);
                border:1px solid #6C63FF44;border-radius:16px;padding:2rem">
      <div style="font-size:0.8rem;color:#6B6B8A;text-transform:uppercase;
                  letter-spacing:.1em;margin-bottom:0.6rem">One Line Summary</div>
      <div style="font-family:'Space Grotesk',sans-serif;font-size:1.3rem;
                  font-weight:600;color:#E8E8F0;line-height:1.5">
        "SkillMesh connects people not by
        <span style="color:#FF8FA3">what they know</span>,<br>
        but by
        <span style="color:#43C6AC">what they're trying to learn</span>."
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Creator Note ──────────────────────────────────
    st.markdown("""
    <div style="background:#1C1C30;border:1px solid #2A2A45;border-radius:12px;
                padding:1.2rem 1.4rem;margin-bottom:1rem">
      <div style="font-size:0.78rem;color:#6B6B8A;text-transform:uppercase;
                  letter-spacing:.08em;margin-bottom:0.5rem">👤 A Note from the Creator</div>
      <div style="color:#C8C8DC;line-height:1.7;font-size:0.9rem">
        This app was born from a real experience — learning Data Analytics, Python, SQL,
        and navigating a job search, all at the same time, often feeling isolated in that journey.
        The idea is simple: <em>no one should have to learn alone.</em>
        Whether you're studying for a certification, switching careers, or picking up a new hobby —
        there's someone out there on the exact same path. SkillMesh helps you find them.
      </div>
    </div>
    """, unsafe_allow_html=True)