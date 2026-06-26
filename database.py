import sqlite3
import hashlib
import os
from datetime import datetime

DB_PATH = "skillmesh.db"

def get_conn():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_conn()
    c = conn.cursor()

    c.executescript("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            full_name TEXT,
            bio TEXT,
            avatar_color TEXT DEFAULT '#6C63FF',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS skills (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            skill_name TEXT NOT NULL,
            domain TEXT DEFAULT 'General',
            level TEXT DEFAULT 'Beginner',
            is_public INTEGER DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_id) REFERENCES users(id)
        );

        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            content TEXT NOT NULL,
            skill_tag TEXT,
            post_type TEXT DEFAULT 'update',
            is_public INTEGER DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_id) REFERENCES users(id)
        );

        CREATE TABLE IF NOT EXISTS milestones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            description TEXT,
            skill_tag TEXT,
            is_public INTEGER DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_id) REFERENCES users(id)
        );

        CREATE TABLE IF NOT EXISTS follows (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            follower_id INTEGER NOT NULL,
            following_id INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(follower_id, following_id),
            FOREIGN KEY(follower_id) REFERENCES users(id),
            FOREIGN KEY(following_id) REFERENCES users(id)
        );

        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender_id INTEGER NOT NULL,
            receiver_id INTEGER NOT NULL,
            content TEXT NOT NULL,
            is_read INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(sender_id) REFERENCES users(id),
            FOREIGN KEY(receiver_id) REFERENCES users(id)
        );

        CREATE TABLE IF NOT EXISTS likes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            post_id INTEGER,
            milestone_id INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    conn.commit()
    conn.close()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# ── AUTH ──────────────────────────────────────────────
def register_user(username, password, full_name, bio=""):
    conn = get_conn()
    try:
        conn.execute(
            "INSERT INTO users (username, password, full_name, bio) VALUES (?,?,?,?)",
            (username, hash_password(password), full_name, bio)
        )
        conn.commit()
        return True, "Account created!"
    except sqlite3.IntegrityError:
        return False, "Username already taken."
    finally:
        conn.close()

def login_user(username, password):
    conn = get_conn()
    user = conn.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, hash_password(password))
    ).fetchone()
    conn.close()
    return dict(user) if user else None

def get_user_by_id(user_id):
    conn = get_conn()
    user = conn.execute("SELECT * FROM users WHERE id=?", (user_id,)).fetchone()
    conn.close()
    return dict(user) if user else None

def update_profile(user_id, full_name, bio, avatar_color):
    conn = get_conn()
    conn.execute(
        "UPDATE users SET full_name=?, bio=?, avatar_color=? WHERE id=?",
        (full_name, bio, avatar_color, user_id)
    )
    conn.commit()
    conn.close()

# ── SKILLS ────────────────────────────────────────────
def add_skill(user_id, skill_name, domain, level, is_public):
    conn = get_conn()
    conn.execute(
        "INSERT INTO skills (user_id, skill_name, domain, level, is_public) VALUES (?,?,?,?,?)",
        (user_id, skill_name, domain, level, int(is_public))
    )
    conn.commit()
    conn.close()

def get_user_skills(user_id):
    conn = get_conn()
    skills = conn.execute(
        "SELECT * FROM skills WHERE user_id=? ORDER BY created_at DESC", (user_id,)
    ).fetchall()
    conn.close()
    return [dict(s) for s in skills]

def delete_skill(skill_id):
    conn = get_conn()
    conn.execute("DELETE FROM skills WHERE id=?", (skill_id,))
    conn.commit()
    conn.close()

def count_public_skills(user_id):
    conn = get_conn()
    count = conn.execute(
        "SELECT COUNT(*) FROM skills WHERE user_id=? AND is_public=1", (user_id,)
    ).fetchone()[0]
    conn.close()
    return count

# ── SEARCH ────────────────────────────────────────────
def search_by_skill(query):
    conn = get_conn()
    results = conn.execute("""
        SELECT u.id, u.username, u.full_name, u.bio, u.avatar_color,
               s.skill_name, s.domain, s.level
        FROM skills s
        JOIN users u ON s.user_id = u.id
        WHERE s.is_public=1 AND (
            LOWER(s.skill_name) LIKE LOWER(?) OR
            LOWER(s.domain) LIKE LOWER(?)
        )
        ORDER BY u.username
    """, (f"%{query}%", f"%{query}%")).fetchall()
    conn.close()
    return [dict(r) for r in results]

def search_users(query):
    conn = get_conn()
    results = conn.execute("""
        SELECT DISTINCT u.id, u.username, u.full_name, u.bio, u.avatar_color
        FROM users u
        WHERE LOWER(u.username) LIKE LOWER(?) OR LOWER(u.full_name) LIKE LOWER(?)
    """, (f"%{query}%", f"%{query}%")).fetchall()
    conn.close()
    return [dict(r) for r in results]

# ── POSTS ─────────────────────────────────────────────
def create_post(user_id, content, skill_tag, post_type, is_public):
    conn = get_conn()
    conn.execute(
        "INSERT INTO posts (user_id, content, skill_tag, post_type, is_public) VALUES (?,?,?,?,?)",
        (user_id, content, skill_tag, post_type, int(is_public))
    )
    conn.commit()
    conn.close()

def get_feed_posts(current_user_id, limit=30):
    conn = get_conn()
    posts = conn.execute("""
        SELECT p.*, u.username, u.full_name, u.avatar_color,
               (SELECT COUNT(*) FROM likes WHERE post_id=p.id) as like_count
        FROM posts p
        JOIN users u ON p.user_id = u.id
        WHERE p.is_public=1 OR p.user_id=? OR p.user_id IN (
            SELECT following_id FROM follows WHERE follower_id=?
        )
        ORDER BY p.created_at DESC
        LIMIT ?
    """, (current_user_id, current_user_id, limit)).fetchall()
    conn.close()
    return [dict(p) for p in posts]

def get_user_posts(user_id):
    conn = get_conn()
    posts = conn.execute("""
        SELECT p.*, u.username, u.full_name, u.avatar_color,
               (SELECT COUNT(*) FROM likes WHERE post_id=p.id) as like_count
        FROM posts p JOIN users u ON p.user_id=u.id
        WHERE p.user_id=? ORDER BY p.created_at DESC
    """, (user_id,)).fetchall()
    conn.close()
    return [dict(p) for p in posts]

def toggle_like(user_id, post_id):
    conn = get_conn()
    existing = conn.execute(
        "SELECT id FROM likes WHERE user_id=? AND post_id=?", (user_id, post_id)
    ).fetchone()
    if existing:
        conn.execute("DELETE FROM likes WHERE user_id=? AND post_id=?", (user_id, post_id))
    else:
        conn.execute("INSERT INTO likes (user_id, post_id) VALUES (?,?)", (user_id, post_id))
    conn.commit()
    conn.close()
    return not bool(existing)

def user_liked_post(user_id, post_id):
    conn = get_conn()
    r = conn.execute("SELECT id FROM likes WHERE user_id=? AND post_id=?", (user_id, post_id)).fetchone()
    conn.close()
    return bool(r)

# ── MILESTONES ────────────────────────────────────────
def add_milestone(user_id, title, description, skill_tag, is_public):
    conn = get_conn()
    conn.execute(
        "INSERT INTO milestones (user_id, title, description, skill_tag, is_public) VALUES (?,?,?,?,?)",
        (user_id, title, description, skill_tag, int(is_public))
    )
    conn.commit()
    conn.close()

def get_milestones(user_id=None, public_only=False):
    conn = get_conn()
    if user_id and not public_only:
        rows = conn.execute("""
            SELECT m.*, u.username, u.full_name, u.avatar_color FROM milestones m
            JOIN users u ON m.user_id=u.id WHERE m.user_id=? ORDER BY m.created_at DESC
        """, (user_id,)).fetchall()
    else:
        rows = conn.execute("""
            SELECT m.*, u.username, u.full_name, u.avatar_color FROM milestones m
            JOIN users u ON m.user_id=u.id WHERE m.is_public=1 ORDER BY m.created_at DESC
        """).fetchall()
    conn.close()
    return [dict(r) for r in rows]

# ── FOLLOWS ───────────────────────────────────────────
def follow_user(follower_id, following_id):
    conn = get_conn()
    try:
        conn.execute("INSERT INTO follows (follower_id, following_id) VALUES (?,?)",
                     (follower_id, following_id))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def unfollow_user(follower_id, following_id):
    conn = get_conn()
    conn.execute("DELETE FROM follows WHERE follower_id=? AND following_id=?",
                 (follower_id, following_id))
    conn.commit()
    conn.close()

def is_following(follower_id, following_id):
    conn = get_conn()
    r = conn.execute("SELECT id FROM follows WHERE follower_id=? AND following_id=?",
                     (follower_id, following_id)).fetchone()
    conn.close()
    return bool(r)

def get_followers(user_id):
    conn = get_conn()
    rows = conn.execute("""
        SELECT u.* FROM users u
        JOIN follows f ON f.follower_id=u.id WHERE f.following_id=?
    """, (user_id,)).fetchall()
    conn.close()
    return [dict(r) for r in rows]

def get_following(user_id):
    conn = get_conn()
    rows = conn.execute("""
        SELECT u.* FROM users u
        JOIN follows f ON f.following_id=u.id WHERE f.follower_id=?
    """, (user_id,)).fetchall()
    conn.close()
    return [dict(r) for r in rows]

# ── PEER MATCHING ─────────────────────────────────────
def get_peer_matches(user_id):
    conn = get_conn()
    my_skills = conn.execute(
        "SELECT LOWER(skill_name) as skill FROM skills WHERE user_id=?", (user_id,)
    ).fetchall()
    my_skill_list = [s["skill"] for s in my_skills]

    if not my_skill_list:
        conn.close()
        return []

    placeholders = ",".join(["?" for _ in my_skill_list])
    rows = conn.execute(f"""
        SELECT u.id, u.username, u.full_name, u.bio, u.avatar_color,
               GROUP_CONCAT(s.skill_name, ', ') as matched_skills,
               COUNT(s.id) as match_count
        FROM skills s JOIN users u ON s.user_id=u.id
        WHERE u.id != ? AND s.is_public=1
          AND LOWER(s.skill_name) IN ({placeholders})
        GROUP BY u.id ORDER BY match_count DESC LIMIT 20
    """, [user_id] + my_skill_list).fetchall()
    conn.close()
    return [dict(r) for r in rows]

# ── MESSAGES ──────────────────────────────────────────
def send_message(sender_id, receiver_id, content):
    conn = get_conn()
    conn.execute(
        "INSERT INTO messages (sender_id, receiver_id, content) VALUES (?,?,?)",
        (sender_id, receiver_id, content)
    )
    conn.commit()
    conn.close()

def get_conversation(user1_id, user2_id):
    conn = get_conn()
    msgs = conn.execute("""
        SELECT m.*, u.username, u.full_name FROM messages m
        JOIN users u ON m.sender_id=u.id
        WHERE (m.sender_id=? AND m.receiver_id=?)
           OR (m.sender_id=? AND m.receiver_id=?)
        ORDER BY m.created_at ASC
    """, (user1_id, user2_id, user2_id, user1_id)).fetchall()
    conn.execute(
        "UPDATE messages SET is_read=1 WHERE sender_id=? AND receiver_id=?",
        (user2_id, user1_id)
    )
    conn.commit()
    conn.close()
    return [dict(m) for m in msgs]

def get_inbox(user_id):
    conn = get_conn()
    rows = conn.execute("""
        SELECT DISTINCT u.id, u.username, u.full_name, u.avatar_color,
               (SELECT COUNT(*) FROM messages WHERE sender_id=u.id AND receiver_id=? AND is_read=0) as unread
        FROM messages m JOIN users u ON (
            CASE WHEN m.sender_id=? THEN m.receiver_id ELSE m.sender_id END = u.id
        )
        WHERE m.sender_id=? OR m.receiver_id=?
    """, (user_id, user_id, user_id, user_id)).fetchall()
    conn.close()
    return [dict(r) for r in rows]

def get_unread_count(user_id):
    conn = get_conn()
    count = conn.execute(
        "SELECT COUNT(*) FROM messages WHERE receiver_id=? AND is_read=0", (user_id,)
    ).fetchone()[0]
    conn.close()
    return count