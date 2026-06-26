import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

def show():
    st.markdown("""
    <div style="text-align:center;padding:2.5rem 1rem 1.5rem">
      <div style="font-family:'Space Grotesk',sans-serif;font-size:2.8rem;font-weight:700;
                  background:linear-gradient(135deg,#6C63FF,#43C6AC);
                  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
                  margin-bottom:0.4rem">SkillMesh</div>
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

    st.markdown("""
    <div style="background:#1C1C30;border:1px solid #2A2A45;border-left:4px solid #FF6584;
                border-radius:12px;padding:1.4rem 1.6rem;margin-bottom:1.2rem">
      <div style="font-family:'Space Grotesk',sans-serif;font-size:1.1rem;font-weight:700;
                  color:#FF8FA3;margin-bottom:0.6rem">😕 The Problem</div>
      <div style="color:#C8C8DC;line-height:1.8;font-size:0.95rem">
        When you're learning something new — SQL, Python, guitar, a new language, cooking, anything —
        you're mostly learning <strong style="color:#E8E8F0">alone</strong>.<br><br>
        LinkedIn shows what people already achieved. YouTube teaches you but doesn't connect you.
        Discord has communities but they're not personalized to your journey.<br><br>
        There is no place to find someone learning the <em>exact same thing</em> as you, right now.
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background:#1C1C30;border:1px solid #2A2A45;border-left:4px solid #43C6AC;
                border-radius:12px;padding:1.4rem 1.6rem;margin-bottom:1.2rem">
      <div style="font-family:'Space Grotesk',sans-serif;font-size:1.1rem;font-weight:700;
                  color:#43C6AC;margin-bottom:0.6rem">💡 The Solution — SkillMesh</div>
      <div style="color:#C8C8DC;line-height:1.8;font-size:0.95rem">
        SkillMesh is a <strong style="color:#E8E8F0">skill-based social learning network</strong>
        where people share what they are currently learning — not just what they've already mastered.<br><br>
        Add your active skills → get matched with peers → follow, chat, share progress → celebrate wins together.<br><br>
        Works for <strong style="color:#E8E8F0">any domain</strong> — tech, music, finance, languages, cooking, fitness.
      </div>
    </div>
    """, unsafe_allow_html=True)

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
        but by <span style="color:#43C6AC">what they're trying to learn</span>."
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background:#1C1C30;border:1px solid #2A2A45;border-radius:12px;
                padding:1.4rem 1.6rem;margin-bottom:1rem">
      <div style="font-size:0.78rem;color:#6B6B8A;text-transform:uppercase;
                  letter-spacing:.08em;margin-bottom:0.8rem">👤 Built By</div>
      <div style="display:flex;align-items:center;gap:14px;margin-bottom:1rem">
        <div style="width:56px;height:56px;border-radius:50%;
                    background:linear-gradient(135deg,#6C63FF,#43C6AC);
                    display:flex;align-items:center;justify-content:center;
                    font-size:1.4rem;font-weight:700;color:white;flex-shrink:0">N</div>
        <div>
          <div style="font-size:1.05rem;font-weight:700;color:#E8E8F0">Nishant Dixit</div>
          <div style="font-size:0.85rem;color:#9898B0;margin-top:2px">
            Master's in Data Analytics · Aspiring Data Analyst
          </div>
          <div style="font-size:0.82rem;color:#6B6B8A;margin-top:2px">📍 Canada</div>
        </div>
      </div>
      <div style="color:#C8C8DC;line-height:1.7;font-size:0.9rem;margin-bottom:1rem">
        This app was born from a real experience — learning Data Analytics, Python, SQL,
        and navigating a job search, all at the same time, often feeling isolated in that journey.
        The idea is simple: no one should have to learn alone. Whether you're studying for a
        certification, switching careers, or picking up a new hobby — there's someone out there
        on the exact same path. SkillMesh helps you find them.
      </div>
      <div style="display:flex;gap:10px;flex-wrap:wrap">
        <a href="https://github.com/nishantdix27" target="_blank"
           style="display:inline-flex;align-items:center;gap:6px;
                  background:#6C63FF22;border:1px solid #6C63FF55;
                  color:#A89CFF;border-radius:8px;padding:6px 14px;
                  font-size:0.82rem;font-weight:500;text-decoration:none">
          🐙 GitHub: nishantdix27
        </a>
        <a href="mailto:nishantdixit894@gmail.com"
           style="display:inline-flex;align-items:center;gap:6px;
                  background:#43C6AC22;border:1px solid #43C6AC55;
                  color:#43C6AC;border-radius:8px;padding:6px 14px;
                  font-size:0.82rem;font-weight:500;text-decoration:none">
          📧 nishantdixit894@gmail.com
        </a>
      </div>
    </div>
    """, unsafe_allow_html=True)