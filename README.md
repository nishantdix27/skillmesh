# 🔗 SkillMesh

> **"SkillMesh connects people not by what they know, but by what they're trying to learn."**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://skillmesh.streamlit.app)

---

## 🌍 Live Demo
👉 **[skillmesh.streamlit.app](https://skillmesh.streamlit.app)**

---

## 😕 The Problem
When you're learning something new — SQL, Python, guitar, a new language — you're mostly learning **alone**. LinkedIn shows what people already achieved. YouTube teaches you but doesn't connect you. There's no place to find someone learning the exact same thing as you, right now, at the same level.

## 💡 The Solution
SkillMesh is a **skill-based social learning network** where people share what they're *currently learning* — not just what they've already mastered. Add your active skills, get matched with peers, follow them, chat privately, share progress, and celebrate wins together.

Works for **any domain** — tech, music, finance, languages, cooking, fitness — anything.

---

## ✨ Features

| Feature | Description |
|---|---|
| 👤 **User Profiles** | Add current skills with domain and level |
| 📰 **Skill Feed** | Share updates, tips, questions, resources with images |
| 🔍 **Smart Search** | Find people by skill or username |
| 🤝 **Peer Matching** | Auto-matched with people sharing your skills |
| 💬 **Direct Messages** | Private chat with your learning peers |
| 🏆 **Milestones** | Share and celebrate achievements |
| ℹ️ **About Page** | Full app story and creator info |

---

## 🛠️ Tech Stack

- **Frontend** — Streamlit (Python)
- **Database** — SQLite
- **Auth** — SHA-256 hashed passwords
- **Hosting** — Streamlit Cloud (free)

---

## 🚀 Run Locally

```bash
# Clone the repo
git clone https://github.com/nishantdix27/skillmesh.git
cd skillmesh

# Install dependencies
pip install streamlit

# Run the app
streamlit run app.py
```

Open your browser at `http://localhost:8501`

---

## 📁 Project Structure

```
skillmesh/
├── app.py              # Main entry + auth + routing
├── database.py         # SQLite database + all queries
├── requirements.txt
├── components/
│   └── ui.py           # Design system + reusable components
└── pages/
    ├── feed.py         # Home feed + post creation + image upload
    ├── search.py       # Skill & user search
    ├── matches.py      # Peer matching
    ├── messages.py     # Direct messaging
    ├── profile.py      # Profile + skills management
    ├── milestones.py   # Milestone sharing
    └── about.py        # App story + creator info
```

---

## 🗺️ Roadmap

- [ ] Profile picture upload
- [ ] Skill endorsements
- [ ] Group skill rooms
- [ ] AI skill suggestions
- [ ] Mobile app (React Native)
- [ ] Cloud database for persistence

---

## 👤 Built By

**Nishant Dixit**
Master's in Data Analytics · Aspiring Data Analyst · Canada

- 🐙 GitHub: [nishantdix27](https://github.com/nishantdix27)
- 📧 Email: nishantdixit894@gmail.com

---

## © Copyright & License

**© 2025 Nishant Dixit. All Rights Reserved.**

This project and its source code are the intellectual property of Nishant Dixit.
No part of this project may be copied, modified, distributed, or used in any form
without explicit written permission from the author.

For collaboration or licensing enquiries, contact: nishantdixit894@gmail.com

---

⭐ **If you find this useful, please star the repo!**