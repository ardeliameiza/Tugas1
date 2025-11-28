from libraryitem import libraryitem
from author import author

class book(libraryitem):
    def __init__(self, item_id, title, isbn, author: author):
        super().__init__(item_id, title)
        self.isbn = isbn
        self.author = author

    def display_info(self):
        base = super().display_info()
        return f"{base}, ISBN: {self.isbn}, Author: {self.author.name}"

    def calculate_late_fee(self, days_late):
        return days_late * 3000  # Buku lebih mahal dendanya
