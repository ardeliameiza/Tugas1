from person import person

class student(person):
    def __init__(self, name, phoneNumber, emailaddress, address, studentNumber, averageMark):
        super().__init__(name, phoneNumber, emailaddress, address)
        self.studentNumber = studentNumber
        self.averageMark = averageMark

    def isEligibleToEnroll(self):
        return self.averageMark >= 50

    def showInfo(self):
        base = super().showInfo()
        return f"{base}, Student Number: {self.studentNumber}, Average Mark: {self.averageMark}"
