import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Users Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    skills TEXT,
    interests TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# Courses Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT NOT NULL,
    category TEXT NOT NULL,
    platform TEXT NOT NULL,
    course_link TEXT
)
""")

# Skill Assessments Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS assessments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    skill_name TEXT,
    score INTEGER,
    assessment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES users(id)
)
""")

# Progress Tracking Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS progress (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    course_name TEXT,
    completion_percentage INTEGER,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES users(id)
)
""")

# Insert Sample Courses
cursor.execute("""
INSERT OR IGNORE INTO courses
(id, course_name, category, platform, course_link)
VALUES
(1,'Python for Everybody','Python','Coursera',
'https://coursera.org'),
(2,'Java Programming Masterclass','Java','Udemy',
'https://udemy.com'),
(3,'Machine Learning','Machine Learning','Coursera',
'https://coursera.org'),
(4,'Full Stack Web Development','Web Development','Udemy',
'https://udemy.com'),
(5,'Data Science with Python','Data Science','Coursera',
'https://coursera.org')
""")

conn.commit()
conn.close()

print("Database created successfully!")