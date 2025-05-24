import sqlite3

def init_db():
    conn = sqlite3.connect("data/leaderboard.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS scores (user_id INTEGER, time REAL)")
    conn.commit()
    conn.close()

def save_time(user_id, time_score):
    conn = sqlite3.connect("data/leaderboard.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO scores (user_id, time) VALUES (?, ?)", (user_id, time_score))
    conn.commit()
    conn.close()