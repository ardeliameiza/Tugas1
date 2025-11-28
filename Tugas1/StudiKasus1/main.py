from address import address
from student import student
from professor import professor

# Create Address object
addr = address("Jl. Giri Puspa", "Jimbaran", "Bali", 80361, "Indonesia")
addr1 = address("Jl. pemecutan", "Denpasar", "Bali", 80363, "Indonesia")

# Create Student and Professor objects
s1 = student("Ardelia", "085792608652", "ardeliameiza09@gmail.com", addr, "230030593", 89)
p1 = professor("prof puritan", "08129876543", "profpuritan@gmail.com", addr1, 12000000, "5", 2,3 )

print("=== Person Info ===")
print(s1.showInfo())
print(p1.showInfo())

print("\nAddress Valid:", addr.validate())
print("Parking Pass:", s1.purchaseParkingPass())
print("Eligible to Enroll:", s1.isEligibleToEnroll())
print("Supervision:", p1.supervises(s1))
