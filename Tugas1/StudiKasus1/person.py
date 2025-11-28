from address import address

class person:
    def __init__(self, name, phoneNumber, emailaddress, address: address):
        self.name = name
        self.phoneNumber = phoneNumber
        self.emailaddress = emailaddress
        self.address = address

    def purchaseParkingPass(self):
        return f"{self.name} has purchased a parking pass."

    def showInfo(self):
        return (
            f"Name: {self.name}, Phone: {self.phoneNumber}, "
            f"Email: {self.emailaddress}, Address: {self.address.outputAsLabel()}"
        )
