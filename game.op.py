import sqlite3

def init_db():
    conn = sqlite3.connect('rpg_game_data.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_activity (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT NOT NULL,
        login_time DATETIME NOT NULL,
        logout_time DATETIME
    )
    ''')
    conn.commit()
    conn.close()

init_db()
