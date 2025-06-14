import sqlite3
import os

def create_knowledge_base_db():
    conn = sqlite3.connect("knowledge_base.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS knowledge (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL
        )
    ''')
    # Add sample data or implement your data insertion logic here
    sample_data = [
        ("Sample knowledge content 1",),
        ("Sample knowledge content 2",),
        ("Sample knowledge content 3",)
    ]
    c.executemany('INSERT INTO knowledge (content) VALUES (?)', sample_data)
    conn.commit()
    conn.close()
    print("Knowledge base database created and populated.")

if __name__ == "__main__":
    create_knowledge_base_db()
