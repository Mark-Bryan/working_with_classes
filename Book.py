class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def get_info(self):
        return f" The book is called {self.title} and it was written by {self.author} with {self.pages} pages"
