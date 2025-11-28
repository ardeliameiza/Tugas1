from author import author
from book import book
from librarymember import librarymember

author1 = author("Tere Liye", 1979)
book1 = book(1, "Bumi", "978602", author1)

member1 = librarymember(101, "Ardelia")

print(book1.display_info())
print("Late Fee (5 days):", book1.calculate_late_fee(5))
print()

print(author1.display_info(), ", Age:", author1.get_age(2025))
print()

print(member1.borrow_item(book1))
print(member1.display_info())

print(member1.return_item(book1))
print(member1.display_info())
