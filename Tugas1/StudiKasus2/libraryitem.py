class libraryitem:
    def __init__(self, item_id, title):
        self.item_id = item_id
        self.title = title

    def display_info(self):
        return f"ID: {self.item_id}, Title: {self.title}"

    def calculate_late_fee(self, days_late):
        return days_late * 2000  # Ambil biaya denda per hari 2000
