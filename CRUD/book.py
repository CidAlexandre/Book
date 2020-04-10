import traceback

from connect_db import connectDB


class Book(object):
    def __init__(self, name="", author="", launch="", edition="", publishing_company="", genre="", id_book=0):
        self.info = {}
        self.id_book = id_book
        self.name = name
        self.author = author
        self.launch = launch
        self.edition = edition
        self.publishing_company = publishing_company
        self.genre = genre

    def insert_book(self):
        db = connectDB()
        try:
            con = db.connect.cursor()

            con.execute("insert into book(name, author, launch, edition, publishing_company, "
                        "genre) values('" + self.name + "', '" +
                        self.author + "', '" + self.launch + "', '" +
                        self.edition + "', '" + self.publishing_company + "', '" + self.genre + "')")
            db.connect.commit()
            con.close()
            return "Livro cadastrado com sucesso"
        except:
            return "Ocorreu um erro no cadastro do livro"

    def update_book(self):
        db = connectDB()
        try:
            con = db.connect.cursor()
            con.execute(
                '''UPDATE book SET name=?, author=?, launch=?, edition=?, publishing_company=?, genre=? WHERE id_book=? ''', [self.name, self.author, self.launch, self.edition, self.publishing_company, self.genre,
                 str(self.id_book)])
            db.connect.commit()
            con.close()
            return "livro atualizado com sucesso"
        except:
            tb = traceback.format_exc()
            print(tb)
            return "Ocorreu um erro na atualização"

    def delete_book(self):
        db = connectDB()
        try:
            con = db.connect.cursor()
            con.execute("delete from book where id_book = " + self.id_book + "")
            db.connect.commit()
            con.close()
            return "Livro excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão"

    def select_book(self, book_id):
        db = connectDB()
        try:
            con = db.connect.cursor()
            con.execute("select * from book where id_book= " + book_id + " ")
            for line in con:
                self.id_book = line[0]
                self.name = line[1]
                self.author = line[2]
                self.launch = line[3]
                self.edition = line[4]
                self.publishing_company = line[5]
                self.genre = line[6]

            con.close()
            return "Busca feita com sucesso"
        except:
            return "ocorreu um erro na busca de livro"
