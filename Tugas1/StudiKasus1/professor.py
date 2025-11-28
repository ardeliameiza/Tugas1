from person import person

class professor(person):
    def __init__(self, name, phoneNumber, emailaddress, address, salary, staffNumber, yearsOfService, numberOfClasses):
        super().__init__(name, phoneNumber, emailaddress, address)
        self.salary = salary
        self.staffNumber = staffNumber
        self.yearsOfService = yearsOfService
        self.numberOfClasses = numberOfClasses

    def supervises(self, student):
        return f"{self.name} supervises {student.name}"

    def showInfo(self):
        base = super().showInfo()
        return f"{base}, Staff No: {self.staffNumber}, Classes: {self.numberOfClasses}, Salary: {self.salary}"
