class author:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def get_age(self, current_year):
        return current_year - self.birth_year

    def display_info(self):
        return f"Author: {self.name}, Birth Year: {self.birth_year}"