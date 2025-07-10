import sqlite3
from datetime import datetime

class students_DB:
    def __init__(self):
        self.conn = sqlite3.connect("students_data.db")
        self.create_table()

    def create_table(self):
        query  = """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            major TEXT NOT NULL
            
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def create(self, name, age, major):
        query = "INSERT INTO students (name,age,major) VALUES (?, ?, ?)"
        self.conn.execute(query, (name,age,major))
        self.conn.commit()

    def read_all(self):
        query = "SELECT * FROM students"
        return self.conn.execute(query).fetchall()

    def update(self, record_id,name, age, major):
        query = "UPDATE students SET name = ?, age = ?, major = ? WHERE id = ?"
        self.conn.execute(query, (name, age, major,record_id))
        self.conn.commit()
    def delete(self, record_id):
        query = "DELETE FROM students WHERE id = ?"
        self.conn.execute(query, (record_id,))
        self.conn.commit()