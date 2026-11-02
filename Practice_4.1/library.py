class Book:
    def __init__(self, title, author, isbn, year, pages):
        if pages <= 0:
            raise ValueError("Страниц должно быть больше 0")
        self._title = title
        self._author = author
        self._isbn = isbn
        self._year = year
        self._pages = pages
        self._is_available = True
        self._last_read_pages = 0

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def isbn(self):
        return self._isbn

    @property
    def year(self):
        return self._year

    @property
    def pages(self):
        return self._pages

    @property
    def is_available(self):
        return self._is_available

    @property
    def last_read_pages(self):
        return self._last_read_pages

    def borrow(self):
        if self._is_available == False:
            raise ValueError("Книга уже выдана")
        self._is_available = False

    def give_back(self, pages_read):
        if self._is_available == True:
            raise ValueError("Книга и так на полке")
        if pages_read < 0 or pages_read > self._pages:
            raise ValueError("Некорректное количество страниц")
        self._last_read_pages = pages_read
        self._is_available = True

    def __eq__(self, other):
        return self._isbn == other._isbn

    def __lt__(self, other):
        return self._year < other._year

    def __repr__(self):
        return f"Book('{self._title}', '{self._author}', '{self._isbn}', {self._year}, {self._pages})"


class Reader:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.pages_read = 0


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def find_by_isbn(self, isbn):
        for book in self._books:
            if book._isbn == isbn:
                return book
        return None

    def find_by_author(self, author):
        result = []
        for book in self._books:
            if book._author == author:
                result.append(book)
        return result

    def lend(self, isbn, reader):
        book = self.find_by_isbn(isbn)
        if book is None:
            raise KeyError("Книга не найдена")
        if book._is_available == False:
            raise ValueError("Книга уже выдана")
        book.borrow()
        reader.books.append(book)

    def take_back(self, isbn, reader, pages_read):
        book = self.find_by_isbn(isbn)
        if book not in reader.books:
            raise ValueError("У читателя нет этой книги")
        if pages_read < 0 or pages_read > book._pages:
            raise ValueError("Некорректное количество страниц")
        book._last_read_pages = pages_read
        book._is_available = True
        reader.books.remove(book)
        reader.pages_read = reader.pages_read + pages_read

    def available(self):
        result = []
        for book in self._books:
            if book._is_available == True:
                result.append(book)
        return result

    def unfinished(self):
        result = []
        for book in self._books:
            if book._last_read_pages > 0 and book._last_read_pages < book._pages:
                result.append(book)
        return result

    def __len__(self):
        return len(self._books)
