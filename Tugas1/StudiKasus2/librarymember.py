class librarymember:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_items = []

    def borrow_item(self, item):
        self.borrowed_items.append(item)
        return f"{self.name} borrowed {item.title}"

    def return_item(self, item):
        if item in self.borrowed_items:
            self.borrowed_items.remove(item)
            return f"{self.name} returned {item.title}"
        return f"{item.title} is not in borrowed items"

    def display_info(self):
        borrowed_titles = ', '.join([item.title for item in self.borrowed_items])
        return f"Member: {self.name}, Borrowed Items: [{borrowed_titles}]"
