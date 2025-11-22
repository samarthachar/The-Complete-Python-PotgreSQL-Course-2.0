# class BookShelf:
#     def __init__(self, quantity):
#         self.quantity = quantity

#     def __str__(self):
#         return f"BookShelf with {self.quantity} books."
    
# shelf = BookShelf(300)

# class Book(BookShelf):
#     def __init__(self, name, quantity):
#         super().__init__(quantity)
#         self.name = name


# book = Book("Itachi Shinden", 19)
# print(book)

class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books."
    

class Book:
    def __init__(self, name):
        self.name = name


book = Book("Itachi Shinden")
book2 = Book("JJK Manga")

shelf = BookShelf(book, book2)
