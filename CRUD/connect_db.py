import sqlite3


class connectDB:
    def __init__(self):
        self.connect = sqlite3.connect('database.db')

    def create_table(self):
        con = self.connect.cursor()

        con.execute("""create table if not exists book (
                 id_book integer primary key autoincrement ,
                 name text,
                 author text,
                 launch text,
                 edition text,
                 publishing_company text,
                 genre text)""")
        self.connect.commit()
        con.close()