
class Book:

    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn

    def book_details(self):
        print(f"Book Details:\nTitle\t: {self.title}\nAuthor\t: {self.author}\nISBN No : {self.isbn}")

b=Book(input("Enter the name of Book Title:\n"),input("Enter the Name of the Book Author :\n"),input("Enter the ISBN Code of the Book :\n"))
b.book_details()

g=Book("Harry Potter and the Goblet of Fire","J.K.Rowling","3324-dert-3f3d-wg76")
g.book_details()