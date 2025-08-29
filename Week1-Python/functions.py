# CSCI 420 Python Demo
# Paul Talaga
# Aug 28, 2025

def myfunction(a,b = 10):
	print(f"I got {a}")
	return a + 1


print("hello world")
myfunction(5)
b = myfunction(10)
myfunction(1,2)
print(f"B is {b}")