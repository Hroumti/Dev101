import sqlite3

class manager:
    def __init__(self):
        self.conn = sqlite3.connect("data.db")
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            priority TEXT NOT NULL,
            status TEXT NOT NULL,
            due_date TEXT NOT NULL
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def create(self, title, description, priority,status, due_date):
        query = "INSERT INTO users (title, description, priority,status, due_date) VALUES (?, ?, ?, ?, ?)"
        self.conn.execute(query, (title, description, priority,status, due_date))
        self.conn.commit()

    def read_all(self):
        query = "SELECT * FROM users"
        return self.conn.execute(query).fetchall()

    def update(self, record_id,title, description, priority,status, due_date):
        query = "UPDATE users SET title = ?, description = ?, priority = ?,status = ?, due_date = ? WHERE id = ?"
        self.conn.execute(query, (title, description, priority,status, due_date, record_id))
        self.conn.commit()
    def delete(self, record_id):
        query = "DELETE FROM users WHERE id = ?"
        self.conn.execute(query, (record_id,))
        self.conn.commit()