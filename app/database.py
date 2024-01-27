import sqlite3

from app.types import Application


class Database:
    connection = None
    cursor = None

    def initialize_db(self):
        self.connection = sqlite3.connect("database.db", check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.create_applications_table()

    def create_applications_table(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS applications (id INTEGER PRIMARY KEY, name TEXT UNIQUE, url TEXT)"
        )
        self.connection.commit()

    def retrieve_applications_list_from_db(self):
        res = self.cursor.execute("SELECT * FROM applications")
        rows = res.fetchall()
        applications = []
        for row in rows:
            applications.append(Application(id=row[0], name=row[1], url=row[2]))
        return applications

    def retrieve_application_from_db(self, id):
        res = self.cursor.execute("SELECT * FROM applications WHERE id = ?", (id,))
        row = res.fetchone()
        return Application(id=row[0], name=row[1], url=row[2])

    def create_application_in_db(self, application):
        self.cursor.execute(
            "INSERT INTO applications (name, url) VALUES (?, ?)",
            (application.name, application.url),
        )
        self.connection.commit()
        return self.retrieve_application_from_db(self.cursor.lastrowid)


instance = Database()
