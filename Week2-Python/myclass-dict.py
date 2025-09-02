# CSCI 420 Python Demo
# Paul Talaga
# Sept 2, 2025

class Bank:
	def __init__(self, name = "None given"):
		self.customers = {} # Now a dictionary is used to store customers for speed
		self.name = name

	def printCustomers(self):
		print(f"There are {len(self.customers)} in bank {self.name}")
		for c in self.customers.keys():
			print(f"{c}: {self.customers[c]}")

	def addCustomer(self, customer):
		self.customers[customer] = 0

	def addMoney(self, customer, amt):
		if customer not in self.customers.keys():
			print(f"{customer} is not a customer in this bank")
			return False
		self.customers[customer] += amt

		







boa = Bank("Bank of America")
boa.addCustomer("Rainey")
boa.addMoney("Rainey", 20.25)
boa.addMoney("Rainey", 1.25)

bmo = Bank("Bank of Montreal")
bmo.addMoney("Rainey", 1.25)

chase = Bank("Chase Bank")

boa.printCustomers()
bmo.printCustomers()
chase.printCustomers()