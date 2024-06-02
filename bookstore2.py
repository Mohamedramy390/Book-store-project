from abc import ABC, abstractmethod
class Database: 
    books = []
    magazines = []
    dvds = []
    users = []
    authors = []
    directors = []

    def __init__(self):
        pass

    def add_book(self, b):
        self.books.append(b)

    def add_magazine(self, m):
        self.magazines.append(m)

    def add_dvd(self, d):
        self.dvds.append(d)

    def add_user(self, u):
        self.users.append(u)

    def add_author(self, a):
        self.authors.append(a)

    def add_director(self, d):
        self.directors.append(d)

    def booksList(self):
        for x in self.books:
            print(x.display())
    def magazinesList(self):
        for x in self.magazines:
            print(x.display())
    def dvdsList(self):
        for x in self.dvds:
            print(x.display())

    # Search methods
    def search_book(self, name):
        for x in self.books:
            if x.getName() == name:
                return x
        return False

    def search_magazine(self, name):
        for x in self.magazines:
            if x.getName() == name:
                return x
        return False

    def search_dvd(self, name):
        for x in self.dvds:
            if x.getName() == name:
                return x
        return False

    def search_user(self, id):
        for x in self.users:
            if x.getId() == id:
                return x
        return False

    def search_author(self, id):
        for x in self.authors:
            if x.getId() == id:
                return x
        return False

    def search_director(self, id):
        for x in self.directors:
            if x.getId() == id:
                return x
        return False


class item(ABC):
    def __init__(self):
        self.__name = ""
        self.__price = 0.0
    def setName(self):
        try:
            name = input("Enter item name: ")
        except ValueError:
            print("invalid name")
        except TypeError:
            print("invalid name")
        else:
            self.__name = name
    def setPrice(self):
        while True:
            try:
                price = float(input("Enter item price: "))
            except ValueError:
                print("invalid price")
            except TypeError:
                print("invalid price")
            else:
                self.__price = price
                break
    def getName(self):
        return self.__name
    def getPrice(self):
        return self.__price
    @abstractmethod
    def display(self):
        pass

class book(item):
    def __init__(self):
        super().__init__()
        self.__author = ""
        self.__ISBN = ""
    def setISBN(self):
        try:
            ISBN = input("enter ISBN: ")
        except ValueError:
            print("invalid ISBN")
        except TypeError:
            print("invalid ISBN")
        else:
            self.__ISBN = ISBN
    def getISBN(self):
        return self.__ISBN
    def setauthor(self, author):
        self.__author = author
    def getauthor(self):
        return self.__author
    def display(self):
        print("name: ", self.getName())
        print("price: ", self.getPrice())
        print("author: ", self.getauthor())
        print("ISBN: ", self.getISBN())

class magazine(item):
    def __init__(self):
        super().__init__()
        self.__issue = ""
        self.__date = ""
    def setdate(self):
        try:
            date = input("enter date: ")
        except ValueError:
            print("invalid date")
        except TypeError:
            print("invalid date")
        else:
            self.__date = date
    def setissue(self):
        try:
            issue = input("enter issue: ")
        except ValueError:
            print("invalid type")
        except TypeError:
            print("invalid type")
        else:
            self.__issue = issue
    def getdate(self):
        return self.__date
    def getissue(self):
        return self.__issue
    def display(self):
        print("name: ", self.getName())
        print("price: ", self.getPrice())
        print("issue: ", self.getissue())
        print("date: ", self.getdate())

class dvd(item):
    def __init__(self):
        super().__init__()
        self.__director = ""
    def setdirector(self, name):
        self.__director = name
    def getdirector(self):
        return self.__director
    def display(self):
        print("name: ", self.getName())
        print("price: ", self.getPrice())
        print("director: ", self.getdirector())

class person(ABC):
    def __init__(self):
        self.__name = ""
        self.__id = ""
        self.db = Database()
    def setName(self):
        try:
            name = input("enter your name: ")
            self.__name = name
        except ValueError:
            print("invalid name")
        except TypeError:
            print("invalid name")

    def setId(self):
        while True:
            try:
                id = input("enter yuor id: ")
                self.__id = id
            except ValueError:
                print("invalid id")
            except TypeError:
                print("invalid id")
            else:
                break
    def getName(self):
        return self.__name
    def getId(self):
        return self.__id
    @abstractmethod
    def login(self):
        pass
    @abstractmethod
    def sign_up(self):
        pass

class user(person):
    def __init__(self):
        super().__init__()
        self.__cart = []
    def addToCart(self, item):
        self.__cart.append(item)
    def getcart(self):
        for x in self.__cart:
            x.display()
    def cashOut(self):
        total = 0
        for x in self.__cart:
            total += x.getPrice()
        return total
    def login(self):
            print("-------------------------------------")
            name = input("enter your name: ")
            id = input("enter your id: ")
            if self.db.search_user(id):
                return True
            else:
                return False
    def sign_up(self):
        self.u = user()
        self.u.setName()
        self.u.setId()
        self.db.add_user(self.u)

class author(person):
    def __init__(self):
        super().__init__()
        self.__book = ""
        # self.__currentAuthor = author()
        self.db = Database()
    def setBook(self):
        self.b = book()
        self.b.setName()
        self.b.setPrice()
        self.b.setauthor(self.__currentAuthor.getName())
        self.b.setISBN()
        self.db.add_book(self.b)
    def setmagazine(self):
        self.m = magazine()
        self.m.setName()
        self.m.setPrice()
        self.m.setissue()
        self.m.setdate()
        self.db.add_magazine(self.m)
    def getBook(self):
        return self.__book
    def login(self):
            print("-------------------------------------")
            name = input("enter your name: ")
            id = input("enter your id: ")
            if self.db.search_author(id):
                self.__currentAuthor = self.db.search_author(id)
                return True
            else:
                return False
    def sign_up(self):
        self.a = author()
        self.a.setName()
        self.a.setId()
        self.db.add_author(self.a)
        self.__currentAuthor = self.a

class director(person):
    def __init__(self):
        super().__init__()
        self.__dvd = ""
        self.__currentDirector = director()
        self.db = Database()
    def setDvd(self):
        self.d = dvd()
        self.d.setName()
        self.d.setPrice()
        self.d.setdirector(self.__currentDirector.getName())
        self.db.add_dvd(self.d)
    def getDvd(self):
        return self.__dvd
    def login(self):
            print("-------------------------------------")
            name = input("enter your name: ")
            id = input("enter your id: ")
            if self.db.search_director(id):
                self.__currentDirector = self.db.search_director(id)
                return True
            else:
                return False
    def sign_up(self):
        self.d = director()
        self.d.setName()
        self.d.setId()
        self.db.add_director(self.d)
        self.__currentDirector = self.d

class menus:
    def __init__(self):
        self.db = Database()
    def startmeun(self):
        print("-------------------------------------")
        print("1 - login \n2 - signup")
        while True:
            num = input("choose 1 or 2 \n")
            if num == "1" or num == "2":
                return num
            print("invalid input")

    def whoareyou(self):
        print("-------------------------------------")
        print("1 - user \n2 - author \n3 - director \n4 - back - \n5 - quit -")
        while True:
            num = input("choose 1 or 2 or 3 or 4 or 5\n")
            if num == "1" or num == "2" or num == "3" or num == "4" or num == "5":
                return num
            print("invalid input")
    def usermenu(self):
        print("-------------------------------------")
        print("1 - books \n2 - magazines \n3 - dvds \n4 - search for book \n5 - search for magazine\n6 - search for dvd \n7 - cart\n8 - back \n9 - quit")
        while True:
            num = input("choose 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8\n")
            if num == "1" or num == "2" or num == "3" or num == "4" or num == "5" or num == "6"or num == "7" or num == "8"  or num == "9":
                return num
            print("invalid input")
    def booklist(self):
        print("------------------------------------")
        print("books")
        print("------------------------------------")
        self.db.booksList()
    def magazinelist(self):
        print("------------------------------------")
        print("magazines")
        print("------------------------------------")
        self.db.magazinesList()
    def dvdlist(self):
        print("------------------------------------")
        print("dvds")
        print("------------------------------------")
        self.db.dvdsList()
    def authormenu(self):
        print("------------------------------------")
        print("1 - add book\n2 - add magazine\n3 - back \n4 - quit")
        while True:
            num = input("choose 1 or 2 or 3\n")
            if num == "1" or num == "2" or num == "3" or num == "4":
                return num
            print("invalid input")
    def directormenu(self):
        print("------------------------------------")
        print("1 - add dvd \n2 - back \n3 - quit")
        while True:
            num = input("choose 1 or 2 or 3\n")
            if num == "1" or num == "2" or num == "3":
                return num
            print("invalid input")
    def addToCart(self):
        print("------------------------------------")
        print("1 - add to cart \n2 - back \n3 - quit")
        while True:
            num = input("choose 1 or 2 or 3\n")
            if num == "1" or num == "2" or num == "3":
                return num
            print("invalid input")


class Program:
    def __init__(self):
        self.db = Database()
        self.m = menus()

    def start(self):
        s = self.m.startmeun()
        self.whoareyou(s)

    def menu(self, s, obj):
        if s == "1":
            z = self.m.usermenu()
            self.usermain(z, obj)
        elif s == "2":
            z = self.m.authormenu()
            self.author_main(z, obj)
        elif s == "3":
            z = self.m.directormenu()
            self.director_main(z, obj)
        elif s == "4":
            self.start()
        elif s == "5":
            return

    def whoareyou(self, s):
        y = self.m.whoareyou()
        if s == "1" and y == "1":
            u = user()
            if u.login():
                self.menu(y, u)
            else:
                print("---------------------------------")
                print("you are not saved in our system")
                print("---------------------------------")
                self.start()
        elif s == "2" and y == "1":
            u = user()
            u.sign_up()
            self.menu(y, u)
        elif s == "1" and y == "2":
            a = author()
            if a.login():
                self.menu(y, a)
            else:
                print("---------------------------------")
                print("you are not saved in our system")
                print("---------------------------------")
                self.start()
        elif s == "2" and y == "2":
            a = author()
            a.sign_up()
            self.menu(y, a)
        elif s == "1" and y == "3":
            d = director()
            if d.login():
                self.menu(y, d)
            else:
                print("---------------------------------")
                print("you are not saved in our system")
                print("---------------------------------")
                self.start()
        elif s == "2" and y == "3":
            d = director()
            d.sign_up()
            self.menu(y, d)
        elif y == "4":
            self.start()
        elif y == "5":
            return
        else:
            print("invalid input")
            return self.whoareyou(s)

    def director_main(self, z, obj):
        if z == "1":
            obj.setDvd()
            self.menu("3", obj)
        elif z == "2":
            return self.whoareyou("2")
        elif z == "3":
            return
        else:
            print("invalid input")

    def author_main(self, z, obj):
        if z == "1":
            obj.setBook()
            self.menu("2", obj)
        elif z == "2":
            obj.setmagazine()
            self.menu("2", obj)
        elif z == "3":
            self.whoareyou("2")
        elif z == "4":
            return

    def usermain(self, z, obj):
        if z == "1":
            self.m.booklist()
            self.addToCart("book", obj)
        elif z == "2":
            self.m.magazinelist()
            self.addToCart("magazine", obj)
        elif z == "3":
            self.m.dvdlist()
            self.addToCart("dvd", obj)
        elif z == "4":
            name = input("enter the name of the book\n")
            if self.db.search_book(name):
                print("---------------------------------------------")
                print("-----------------book found------------------")
                print("---------------------------------------------")
                print(self.db.search_book(name).display())
                self.addToCart("book", obj)
            else:
                print("---------------------------------------------")
                print("---------------book not found----------------")
                print("---------------------------------------------")
                self.menu("1", obj)
        elif z == "5":
            name = input("enter the name of the magazine\n")
            if self.db.search_magazine(name):
                print("---------------------------------------------")
                print("---------------magazine found----------------")
                print("---------------------------------------------")
                print(self.db.search_magazine(name).display())
                self.addToCart("magazine", obj)
            else:
                print("---------------------------------------------")
                print("-------------magazine not found--------------")
                print("---------------------------------------------")
                self.menu("1", obj)
        elif z == "6":
            name = input("enter the name of the dvd\n")
            if self.db.search_dvd(name):
                print("---------------------------------------------")
                print("-----------------dvd found-------------------")
                print("---------------------------------------------")
                print(self.db.search_dvd(name).display())
                self.addToCart("dvd", obj)
            else:
                print("---------------------------------------------")
                print("----------------dvd not found----------------")
                print("---------------------------------------------")
                self.menu("1", obj)
        elif z == "7":
            print("---------------------------------------------")
            print("-------------------cart----------------------")
            print("---------------------------------------------")
            obj.getcart()
            print("---------------------------------------------")
            print(f"total price: {obj.cashOut()}")
            print("---------------------------------------------")
            self.menu("1", obj)
        elif z == "8":
            self.whoareyou("2")
        elif z == "9":
            return 0
        else:
            print("invalid input")

    def addToCart(self, item, obj):
        num = self.m.addToCart()
        if item == "book":
            if num == "1":
                try:
                    name = input(f"enter the name of the {item}\n")
                    if self.db.search_book(name):
                        obj.addToCart(self.db.search_book(name))
                        print("---------------------------------------------")
                        print("----------------added to cart----------------")
                        print("---------------------------------------------")
                        self.menu("1", obj)
                    else:
                        print("---------------------------------------------")
                        print(f"--------------{item} not found--------------")
                        print("---------------------------------------------")
                        self.menu("1", obj)
                except ValueError:
                    print("invalid input")
                except TypeError:
                    print("invalid input")
            elif num == "2":
                    self.menu("1", obj)
            elif num == "3":
                    return 0
        elif item == "magazine":
            if num == "1":
                try:
                    name = input(f"enter the name of the {item}\n")
                    if self.db.search_magazine(name):
                        obj.addToCart(self.db.search_magazine(name))
                        print("---------------------------------------------")
                        print("----------------added to cart----------------")
                        print("---------------------------------------------")
                        self.menu("1", obj)
                    else:
                        print("---------------------------------------------")
                        print(f"-------------{item} not found---------------")
                        print("---------------------------------------------")
                        self.menu("1", obj)
                except ValueError:
                    print("invalid input")
                except TypeError:
                    print("invalid input")
            elif num == "2":
                    self.menu("1", obj)
            elif num == "3":
                    return 0
        elif item == "dvd":
            if num == "1":
                try:
                    name = input(f"enter the name of the {item}\n")
                    if self.db.search_dvd(name):
                        obj.addToCart(self.db.search_dvd(name))
                        print("---------------------------------------------")
                        print("----------------added to cart----------------")
                        print("---------------------------------------------")
                        self.menu("1", obj)
                    else:
                        print("---------------------------------------------")
                        print(f"-------------{item} not found---------------")
                        print("---------------------------------------------")
                        self.menu("1", obj)
                except ValueError:
                    print("invalid input")
                except TypeError:
                    print("invalid input")
            elif num == "2":
                    self.menu("1", obj)
            elif num == "3":
                    return 0
        



p = Program()
p.start()





