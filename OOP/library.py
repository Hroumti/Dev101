import re
import json
import csv
from abc import abstractmethod, ABC
class InvalidDate(Exception):
    pass
class document(ABC):
    def __init__(self, id: int, title: str, author: str, publication_year: int):
        self.id = id
        self.title = title
        self.author = author
        self.publication_year = publication_year
        if self.publication_year < 1990 or self.publication_year > 2025:
            raise InvalidDate
        if id < 0:
            raise ValueError
    @abstractmethod
    def show_details(self):
        pass
    def modify_details(self, new_title=None, new_author=None, new_publication_year=None):
        if new_title is not None:
            self.title = new_title
        if new_author is not None:
            self.author = new_author
        if new_publication_year is not None:
            self.publication_year = new_publication_year
    @abstractmethod
    def __str__(self):
        pass
class book(document):
    def __init__(self, id: int, title: str, author: str, publication_year: int, isbn: str, number_of_pages: int):
        super().__init__(id, title, author, publication_year)
        if len(isbn) != 13 and not re.match(r'^[0-9]{3}-[0-9]{1}-[0-9]{2}-[0-9]{6}-[0-9]{1}$', isbn):
            raise ValueError
        self.isbn = isbn
        self.number_of_pages = number_of_pages

    def show_details(self):
        print(f"ID: {self.id}\nTitle: {self.title}\nAuthor: {self.author}\nPublication Year: {self.publication_year}\nISBN: {self.isbn}\nNumber of pages: {self.number_of_pages}\n")

    def __str__(self):
        return f"ID: {self.id}\nTitle: {self.title}\nAuthor: {self.author}\nPublication Year: {self.publication_year}\nISBN: {self.isbn}\nNumber of pages: {self.number_of_pages}\n"
    def modify_details(self, new_title=None, new_author=None, new_publication_year=None, new_isbn=None, new_number_of_pages=None):
        super().modify_details(new_title, new_author, new_publication_year)
        if new_isbn is not None:
            self.isbn = new_isbn
        if new_number_of_pages is not None:
            self.number_of_pages = new_number_of_pages
        
class review(document):
    def __init__(self, id: int, title: str, author: str, publication_year: int, number: int, frequency: str):
        super().__init__(id, title, author, publication_year)
        self.number = number
        self.frequency = frequency

    def show_details(self):
        print(f"ID: {self.id}\nTitle: {self.title}\nAuthor: {self.author}\nPublication Year: {self.publication_year}\nNumber: {self.number}\nFrequency: {self.frequency}\n")

    def __str__(self):
        return f"ID: {self.id}\nTitle: {self.title}\nAuthor: {self.author}\nPublication Year: {self.publication_year}\nNumber: {self.number}\nFrequency: {self.frequency}\n"
    def modify_details(self, new_title=None, new_author=None, new_publication_year=None, new_number=None, new_frequency=None):
        super().modify_details(new_title, new_author, new_publication_year)
        if new_number is not None:
            self.number = new_number
        if new_frequency is not None:
            self.frequency = new_frequency
class cd(document):
    def __init__(self, id: int, title: str, author: str, publication_year: int, music_genre: str, duration: float):
        super().__init__(id, title, author, publication_year)
        self.music_genre = music_genre
        self.duration = duration
        if self.duration < 0:
            raise ValueError

    def show_details(self):
        print(f"ID: {self.id}\nTitle: {self.title}\nAuthor: {self.author}\nPublication Year: {self.publication_year}\nMusic Genre: {self.music_genre}\nDuration: {self.duration}\n")
    
    def __str__(self):
        return f"ID: {self.id}\nTitle: {self.title}\nAuthor: {self.author}\nPublication Year: {self.publication_year}\nMusic Genre: {self.music_genre}\nDuration: {self.duration}\n"
    def modify_details(self, new_title=None, new_author=None, new_publication_year=None, new_music_genre=None, new_duration=None):
        super().modify_details(new_title, new_author, new_publication_year)
        if new_music_genre is not None:
            self.music_genre = new_music_genre
        if new_duration is not None:
            self.duration = new_duration
class library:
    def __init__(self):
        self.documents = []
        self.reviews = []
        self.books = []
        self.cds = []

    def add_document(self, document):
        self.documents.append(document)
        if isinstance(document, review):
            self.reviews.append(document)
        elif isinstance(document, book):
            self.books.append(document)
        elif isinstance(document, cd):
            self.cds.append(document)
    

    def delete_document(self, id):
        for document in self.documents:
            if document.id == id:
                if document in self.reviews:
                    self.reviews.remove(document)
                elif document in self.books:
                    self.books.remove(document)
                elif document in self.cds:
                    self.cds.remove(document)
                self.documents.remove(document)
                return
        print("Document not found")

    def modify_document(self, id, new_title=None, new_author=None, new_publication_year=None):
        for document in self.documents:
            if document.id == id:
                document.modify_details(new_title, new_author, new_publication_year)
                return
        print("Document not found")

    def show_documents(self):
        for document in self.documents:
            print(document)

    def filter_documents(self, criteria, value):
        filtered_documents = []
        if criteria == "year":
            for document in self.documents:
                if document.publication_year == value:
                    filtered_documents.append(document)
        elif criteria == "genre":
            for document in self.documents:
                if document.music_genre == value:
                    filtered_documents.append(document)
        else:
            print("Invalid criteria")
        for document in filtered_documents:
            print(document)

    def serialize(self, filename):
        data = []
        for document in self.documents:
            data.append(document.__dict__)
        with open(filename, "w") as f:
            json.dump(data, f)
        print("Documents serialized successfully")
    def save_csv(self, filename):
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            for document in self.documents:
                writer.writerow(document.__dict__.values())
        print("Documents saved successfully")

lll = library()
lll.add_document(book(1, "The Great Gatsby", "F. Scott Fitzgerald", 1995, "978-3-16-148410-0", 208))
lll.add_document(review(2, "The Great Gatsby", "F. Scott Fitzgerald", 1995, 5, "Monthly"))
lll.add_document(cd(3, "The Great Gatsby", "F. Scott Fitzgerald", 1995, "Pop", 120))
lll.add_document(book(4, "The Great Gatsby", "F. Scott Fitzgerald", 1995, "978-3-16-148410-0", 208))
lll.add_document(review(5, "The Great Gatsby", "F. Scott Fitzgerald", 1995, 5, "Monthly"))
lll.add_document(cd(6, "The Great Gatsby", "F. Scott Fitzgerald", 1995, "Pop", 120))
lll.add_document(book(7, "The Great Gatsby", "F. Scott Fitzgerald", 1995, "978-3-16-148410-0", 208))
lll.add_document(review(8, "The Great Gatsby", "F. Scott Fitzgerald", 1995, 5, "Monthly"))
lll.add_document(cd(9, "The Great Gatsby", "F. Scott Fitzgerald", 1995, "Pop", 120))
lll.add_document(book(10, "The Great Gatsby", "F. Scott Fitzgerald", 1995, "978-3-16-148410-0", 208))

lll.delete_document(1)
lll.modify_document(2, new_author="F. Scott Fitzgerald", new_publication_year=2000)
lll.serialize("library.json")
lll.save_csv("library.csv")
lll.show_documents()


    
        