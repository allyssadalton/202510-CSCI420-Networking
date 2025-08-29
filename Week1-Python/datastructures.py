# CSCI 420 Python Demo
# Paul Talaga
# Aug 28, 2025

a = [1,2,6,4,8, "bob", 8.5]

a = a + a

def confusion(b):
	print(f"B is {b}")
	b[0] = 99

print(a)
confusion(a)
print(a)
