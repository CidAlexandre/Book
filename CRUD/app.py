from book import Book
from tkinter import *


class App:
    def __init__(self, master=None):
        self.fonte = ("Lucida Sans", "10")

        self.conteiner1 = Frame(master)
        self.conteiner1["padx"] = 10
        self.conteiner1.pack()
        self.conteiner2 = Frame(master)
        self.conteiner2["padx"] = 20
        self.conteiner2["pady"] = 5
        self.conteiner2.pack()
        self.conteiner3 = Frame(master)
        self.conteiner3["padx"] = 20
        self.conteiner3["pady"] = 5
        self.conteiner3.pack()
        self.conteiner4 = Frame(master)
        self.conteiner4["padx"] = 20
        self.conteiner4["pady"] = 5
        self.conteiner4.pack()
        self.conteiner5 = Frame(master)
        self.conteiner5["padx"] = 20
        self.conteiner5["pady"] = 5
        self.conteiner5.pack()
        self.conteiner6 = Frame(master)
        self.conteiner6["padx"] = 20
        self.conteiner6["pady"] = 5
        self.conteiner6.pack()
        self.conteiner7 = Frame(master)
        self.conteiner7["padx"] = 20
        self.conteiner7["pady"] = 5
        self.conteiner7.pack()
        self.conteiner8 = Frame(master)
        self.conteiner8["padx"] = 20
        self.conteiner8["pady"] = 5
        self.conteiner8.pack()
        self.conteiner9 = Frame(master)
        self.conteiner9["padx"] = 20
        self.conteiner9["pady"] = 10
        self.conteiner9.pack()
        self.conteiner10 = Frame(master)
        self.conteiner10["pady"] = 15
        self.conteiner10.pack()

        self.titulo = Label(self.conteiner1, text="Informe o livro: ")
        self.titulo["font"] = ("calibri", "12", "bold")
        self.titulo.pack()

        self.lbl_id_book = Label(self.conteiner2, text="ID do Livro: ")
        self.lbl_id_book.pack(side=LEFT)
        self.txt_id_book = Entry(self.conteiner2)
        self.txt_id_book["width"] = 10
        self.txt_id_book["font"] = self.fonte
        self.txt_id_book.pack(side=LEFT)

        self.btn_search = Button(self.conteiner2, text="Buscar", font=self.fonte, width=10)
        self.btn_search["command"] = self.search_book
        self.btn_search.pack(side=LEFT)

        self.lbl_name = Label(self.conteiner3, text="Nome do Livro: ")
        self.lbl_name.pack(side=LEFT)
        self.txt_name = Entry(self.conteiner3)
        self.txt_name["width"] = 30
        self.txt_name["font"] = self.fonte
        self.txt_name.pack(side=LEFT)

        self.lbl_author = Label(self.conteiner4, text="Nome do autor: ")
        self.lbl_author.pack(side=LEFT)
        self.txt_author = Entry(self.conteiner4)
        self.txt_author["width"] = 30
        self.txt_author["font"] = self.fonte
        self.txt_author.pack(side=LEFT)

        self.lbl_launch = Label(self.conteiner5, text="Lançamento: ")
        self.lbl_launch.pack(side=LEFT)
        self.txt_launch = Entry(self.conteiner5)
        self.txt_launch["width"] = 30
        self.txt_launch["font"] = self.fonte
        self.txt_launch.pack(side=LEFT)

        self.lbl_edition = Label(self.conteiner6, text="Edição nº: ")
        self.lbl_edition.pack(side=LEFT)
        self.txt_edition = Entry(self.conteiner6)
        self.txt_edition["width"] = 30
        self.txt_edition["font"] = self.fonte
        self.txt_edition.pack(side=LEFT)

        self.lbl_publishing_company = Label(self.conteiner7, text="Editora: ")
        self.lbl_publishing_company.pack(side=LEFT)
        self.txt_publishing_company = Entry(self.conteiner7)
        self.txt_publishing_company["width"] = 30
        self.txt_publishing_company["font"] = self.fonte
        self.txt_publishing_company.pack(side=LEFT)

        self.lbl_genre = Label(self.conteiner8, text="Gênero: ")
        self.lbl_genre.pack(side=LEFT)
        self.txt_genre = Entry(self.conteiner8)
        self.txt_genre["width"] = 30
        self.txt_genre["font"] = self.fonte
        self.txt_genre.pack(side=LEFT)

        self.btn_update = Button(self.conteiner9, text="Atualizar", font=self.fonte, width=12)
        self.btn_update["command"] = self.update
        self.btn_update.pack(side=LEFT)

        self.btn_create = Button(self.conteiner9, text="Inserir", font=self.fonte, width=12)
        self.btn_create["command"] = self.create
        self.btn_create.pack(side=LEFT)

        self.btn_delete = Button(self.conteiner9, text="Deletar", font=self.fonte, width=12)
        self.btn_delete["command"] = self.delete
        self.btn_delete.pack(side=LEFT)

        self.lbl_msg = Label(self.conteiner10, text="")
        self.lbl_msg["font"] = ("Lucida Sans", "10", "italic")
        self.lbl_msg.pack()

    def __clean(self):
        self.txt_id_book.delete(0, END)
        self.txt_name.delete(0, END)
        self.txt_author.delete(0, END)
        self.txt_launch.delete(0, END)
        self.txt_edition.delete(0, END)
        self.txt_publishing_company.delete(0, END)
        self.txt_genre.delete(0, END)

    def create(self):
        book = Book()
        book.name = self.txt_name.get()
        book.author = self.txt_author.get()
        book.launch = self.txt_launch.get()
        book.edition = self.txt_edition.get()
        book.publishing_company = self.txt_publishing_company.get()
        book.genre = self.txt_genre.get()
        self.__clean()
        self.lbl_msg["text"] = book.insert_book()

    def update(self):
        book = Book()
        book.id_book = self.txt_id_book.get()
        book.name = self.txt_name.get()
        book.author = self.txt_author.get()
        book.launch = self.txt_launch.get()
        book.edition = self.txt_edition.get()
        book.publishing_company = self.txt_publishing_company.get()
        book.genre = self.txt_genre.get()
        self.lbl_msg["text"] = book.update_book()
        self.__clean()

    def delete(self):
        book = Book()
        book.id_book = self.txt_id_book.get()
        self.lbl_msg["text"] = book.delete_book()
        self.__clean()

    def search_book(self):
        book = Book()
        book_id = self.txt_id_book.get()
        self.lbl_msg["text"] = book.select_book(book_id)
        self.__clean()
        self.txt_id_book.insert(INSERT, book.id_book)
        self.txt_name.insert(INSERT, book.name)
        self.txt_author.insert(INSERT, book.author)
        self.txt_launch.insert(INSERT, book.launch)
        self.txt_edition.insert(INSERT, book.edition)
        self.txt_publishing_company.insert(INSERT, book.publishing_company)
        self.txt_genre.insert(INSERT, book.genre)


root = Tk()
App(root)
root.mainloop()
