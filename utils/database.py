import sqlite3
import json
from datetime import datetime

def init_db():
    """Initialize SQLite database"""
    conn = sqlite3.connect('english_practice.db')
    c = conn.cursor()
    
    # Create users table
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            level TEXT,
            streak INTEGER DEFAULT 0,
            total_points INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create vocabulary table
    c.execute('''
        CREATE TABLE IF NOT EXISTS vocabulary (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            word TEXT,
            meaning TEXT,
            phonetic TEXT,
            example TEXT,
            category TEXT,
            difficulty TEXT,
            mastery INTEGER DEFAULT 0,
            added_date TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    
    # Create conversations table
    c.execute('''
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            topic TEXT,
            user_input TEXT,
            ai_response TEXT,
            feedback TEXT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    
    # Create progress table
    c.execute('''
        CREATE TABLE IF NOT EXISTS progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            date DATE,
            practice_minutes INTEGER DEFAULT 0,
            new_words INTEGER DEFAULT 0,
            accuracy REAL DEFAULT 0,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    
    conn.commit()
    conn.close()

def get_user_stats(user_id=1):
    """Get user statistics"""
    conn = sqlite3.connect('english_practice.db')
    c = conn.cursor()
    
    # Get user basic info
    c.execute('SELECT streak, total_points FROM users WHERE id = ?', (user_id,))
    user = c.fetchone()
    
    if user:
        streak, total_points = user
    else:
        streak, total_points = 0, 0
    
    # Get vocabulary count
    c.execute('SELECT COUNT(*) FROM vocabulary WHERE user_id = ?', (user_id,))
    vocabulary_count = c.fetchone()[0]
    
    # Get today's practice minutes
    today = datetime.now().date()
    c.execute('SELECT SUM(practice_minutes) FROM progress WHERE user_id = ? AND date = ?', 
              (user_id, today))
    practice_minutes = c.fetchone()[0] or 0
    
    # Get conversation count
    c.execute('SELECT COUNT(*) FROM conversations WHERE user_id = ?', (user_id,))
    conversation_count = c.fetchone()[0]
    
    conn.close()
    
    return {
        'streak': streak,
        'points': total_points,
        'vocabulary': vocabulary_count,
        'practice_time': practice_minutes,
        'conversations': conversation_count
    }