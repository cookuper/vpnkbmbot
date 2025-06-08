import sqlite3

def init_db():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_user(user_id, username):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO users (user_id, username) VALUES (?, ?)", (user_id, username))
    conn.commit()
    conn.close()

def user_exists(user_id):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT 1 FROM users WHERE user_id = ?", (user_id,))
    exists = c.fetchone() is not None
    conn.close()
    return exists

def get_all_users():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT user_id FROM users")
    users = c.fetchall()
    conn.close()
    return [str(user[0]) for user in users]

def get_masked_users():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT user_id, username FROM users")
    users = c.fetchall()
    conn.close()

    masked = []
    for user_id, username in users:
        if username and username.strip():
            name_len = len(username)
            hide_len = max(3, name_len // 2)  # скрываем минимум 3 символа или половину имени
            visible = username[hide_len:]
            hidden = "*" * hide_len
            masked.append("@" + hidden + visible)
        else:
            uid = str(user_id)
            hide_len = max(3, len(uid) // 2)
            visible = uid[hide_len:]
            hidden = "*" * hide_len
            masked.append(hidden + visible)
    return masked
