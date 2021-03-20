import sqlite3

class Todo:
    def __init__(self, gorev, kategori, gun, yer, saat, id=0):
        self.id = id
        self.gorev = gorev
        self.kategori = kategori
        self.gun = gun
        self.yer = yer
        self.saat = saat

    def __str__(self):
        return """
            İD: {}
            Görev: {}
            Kategori: {}
            Gün: {}
            Yer: {}
            Saat: {}
        """.format(self.id, self.gorev, self.kategori, self.gun, self.yer, self.saat)


class Liste:

    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("Todo.db")
        self.cursor = self.baglanti.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS yapılacaklar (İD INT, Görev TEXT, Kategori TEXT, Gün TEXT, Yer TEXT, Saat TEXT)")
        self.baglanti.commit()

    def baglantiyi_kes(self):
        self.baglanti.close()

    def todo_listele(self):
        self.cursor.execute("Select * From yapılacaklar")
        todolar = self.cursor.fetchall()

        if len(todolar) == 0:
            print("Yapılacaklar listeniz boş!")
        else:
            for i in todolar:
                todo = Todo(i[1], i[2], i[3], i[4], i[5], i[0])
                print(todo)

    def todo_ekle(self, todo):
        self.cursor.execute("Select İD From yapılacaklar")
        idler = self.cursor.fetchall()

        if len(idler) == 0:
            id = 1
        else:
            id = max([i[0] for i in idler])
            id += 1
        self.cursor.execute("INSERT INTO yapılacaklar Values(?, ?, ?, ?, ?, ?)", (id, todo.gorev, todo.kategori, todo.gun, todo.yer, todo.saat))
        self.baglanti.commit()
        print("Todo başarıyla eklendi!")

    def tamamla(self, id):
        self.cursor.execute("Select İD From yapılacaklar")
        idler = self.cursor.fetchall()
        idler = [i[0] for i in idler]
        sayac = 0
        for i in idler:
            if i == id:
                self.cursor.execute("DELETE FROM yapılacaklar where İD = ?", (id,))
                self.baglanti.commit()
                print("{} id'li todo başarıyla silindi!".format(id))
                sayac += 1

        if sayac == 0:
            print("Bu id'ye ait todo bulunmamaktadır...")
        else:
            idler = sorted(idler)
            for i in idler:
                if i > id:
                    self.cursor.execute("UPDATE yapılacaklar SET İD = ? where İD = ?", (i - 1, i))
                    self.baglanti.commit()
    def gune_gore(self, gun):
        self.cursor.execute("Select * From yapılacaklar where Gün = ?", (gun,))
        todos = self.cursor.fetchall()

        if len(todos) == 0:
            print("Seçilen güne ait yapılacak iş bulunmamaktadır!")
        else:
            for i in todos:
                todo = Todo(i[1], i[2], i[3], i[4], i[5], i[0])
                print(todo)

    def kategoriye_gore(self, kategori):
        self.cursor.execute("Select * From yapılacaklar where Kategori = ?", (kategori,))
        todos = self.cursor.fetchall()

        if len(todos) == 0:
            print("Seçilen kategoride yapılacak iş bulunmamaktadır!")
        else:
            for i in todos:
                todo = Todo(i[1], i[2], i[3], i[4], i[5], i[0])
                print(todo)

    def saate_gore(self, saat):
        self.cursor.execute("Select * From yapılacaklar where Saat = ?", (saat,))
        todos = self.cursor.fetchall()

        if len(todos) == 0:
            print("Seçilen saatte yapılacak iş bulunmamaktadır!")
        else:
            for i in todos:
                todo = Todo(i[1], i[2], i[3], i[4], i[5], i[0])
                print(todo)
    def yere_gore(self, yer):
        self.cursor.execute("Select * From yapılacaklar where Yer = ?", (yer,))
        todos = self.cursor.fetchall()

        if len(todos) == 0:
            print("Seçilen yerde yapılacak iş bulunmuyor!")
        else:
            for i in todos:
                todo = Todo(i[1], i[2], i[3], i[4], i[5], i[0])
                print(todo)

    def tam_bilgi(self):
        self.cursor.execute("Select * From yapılacaklar")
        todos = self.cursor.fetchall()

        if len(todos) == 0:
            print("Bilgisi tam olan iş bulunmamaktadır!")
        else:
            for i in todos:
                if not("Belirtilmedi!" in i):
                    todo = Todo(i[1], i[2], i[3], i[4], i[5], i[0])
                    print(todo)
