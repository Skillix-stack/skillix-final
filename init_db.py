import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS professionals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    profession TEXT NOT NULL,
    city TEXT NOT NULL
)
''')

cursor.executemany('INSERT INTO professionals (name, profession, city) VALUES (?, ?, ?)', [
    ('Иван Петров', 'Електротехник', 'София'),
    ('Георги Димов', 'Бояджия', 'Пловдив'),
    ('Мария Николова', 'ВиК специалист', 'Варна')
])

conn.commit()
conn.close()