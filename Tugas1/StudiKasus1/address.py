class address:
    def __init__(self, street, city, state, postalCode, country):
        self.street = street
        self.city = city
        self.state = state
        self.postalCode = postalCode
        self.country = country

    def validate(self):
        return isinstance(self.postalCode, int) and len(str(self.postalCode)) >= 4

    def outputAsLabel(self):
        return f"{self.street}, {self.city}, {self.state}, {self.postalCode}, {self.country}"
