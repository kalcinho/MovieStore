import sqlite3

class Database:

    def __init__(self, db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS movie (id INTEGER PRIMARY KEY,title text,director text,year integer, isbn integer)")
        self.conn.commit()

    def insert(self,title,director,year,isbn):
        self.cur.execute("INSERT INTO movie VALUES (NULL,?,?,?,?)",(title,director,year,isbn))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM movie")
        rows=self.cur.fetchall()
        return rows

    def search(self,title="",director="",year="",isbn=""):
        self.cur.execute("SELECT * FROM movie WHERE title=? OR director=? OR year=? OR isbn=?", (title,director,year,isbn))
        rows = self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM movie WHERE id=?", (id,))
        self.conn.commit()

    def update(self,id,title,director,year,isbn):
        self.cur.execute("UPDATE movie SET title=?,director=?,year=?,isbn=? WHERE id=?", (title,director,year,isbn,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


#insert("Jurassic Park","Steven Spielberg",1993,463287947)
#delete(2)
#update(1,"28 Days Later","Danny Boyle",2002,135461985)
#print(view())
#print(search(director="James Cameron"))