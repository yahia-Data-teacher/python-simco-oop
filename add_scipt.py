#################################@@

# Define a function that prompts the user to enter values for a given class
def prompt_for_instance(cls):
    # Get the names of the constructor arguments
    arg_names = cls.__init__.__code__.co_varnames[1:]
    # Prompt the user for the values of the arguments 
    print(cls.__name__,":")
    args = [input("Enter the value for {}: ".format(name)) for name in arg_names]
    # Create an instance of the class using the entered values
    return cls(*args)

#################################@@

def sep():
    print("\n====================\n")
    
sep()

# Prompt the user to create instances of the Biens_Consommation, Articles_Menagers, and Meubles classes
#biens_consommation = prompt_for_instance(Biens_Consommation)
#articles_menagers = prompt_for_instance(Articles_Menagers)
"""
chaussures = prompt_for_instance(Chaussures)
print(vars(chaussures))
"""
#################################

class InventoryProductEntry:
	def __init__(self, product:Product, quantity):
		self.product = product
		self.quantity = quantity
		self.sales = 0
		self.expenses = 0

	def sell(self, quantity):
		if self.quantity < quantity:
			print(f"Not enough {self.product.name} stock")
		else:
			self.quantity -= quantity
			self.sales += quantity * self.product.price

	def restock(self, quantity):
		self.quantity += quantity
		self.expenses += quantity * self.product.cost

	def __repr__(self):
		return "{} ({}): {} in stock,  price:{}".format(type(self.product).__name__, self.product.marque, self.quantity, self.product.price)

#################################@@

#################################@@


class ProfitTracker:

	def __init__(self):
		self.inventory_manager= InventoryManager()
		self.total_revenue=0
		self.total_profit = 0
		self.total_cost = 0
		self.balance= 1000

	def buy_product(self, product:Product,quantity):
		if self.balance < product.cost * quantity:
			print("Not enough money to restock")
		else:
			self.balance= self.balance - (product.cost * quantity)
			print("balance aprés achat", self.balance)
	def sell_pr(self, product:Product,quantity):
		self.balance= self.balance + (product.price * quantity)
		print("balance aprés vente",self.balance)

	def calcul_revenue(self):
		for inventory_product_entry_key in inventory_manager.inventory:
			self.total_revenue += inventory_manager.inventory[inventory_product_entry_key].sales
			self.total_cost += inventory_manager.inventory[inventory_product_entry_key].expenses

		return self.total_revenue - self.total_cost

	def calcul_profit(self):
		self.total_profit = self.calcul_revenue()
		return self.total_profit

		#################################@@
from typing import Dict

class InventoryManager:
	def __init__(self):

		self.inventory : Dict[str, InventoryProductEntry] = {}

	def product_exists(self,product:Product):
		for inventory_product_entry_key in self.inventory:
			if (inventory_product_entry_key == product.name):
				return True
		return False
		
	def add_product(self, product:Product, quantity):
		#if product exists inventory, increase quantity 
		if self.product_exists(product):
			self.inventory[product.name].quantity+=quantity
		else:
			inventory_product_entry = InventoryProductEntry(product, quantity)
			self.inventory[product.name]=inventory_product_entry
			
	def remove_product(self, product:Product):
		if self.product_exists(product):
				self.inventory.pop(product.name)

	def sell_product(self, product:Product, quantity, profit_tracker):
		for inventory_product_entry_key in self.inventory:
			if inventory_product_entry_key == product.name:
				self.inventory[inventory_product_entry_key].sell(quantity)
				profit_tracker.sell_pr(product, quantity)
				return
		print(f"product {product.name} not found")

	def restock_product(self, product:Product, quantity, profit_tracker):
		for inventory_product_entry_key in self.inventory:
			if self.product_exists(product):
				self.inventory[inventory_product_entry_key].restock(quantity)
				profit_tracker.buy_product(product, quantity)
				return
		print(f"product {product.name} not found")

	def get_product(self, name):
		for inventory_product_entry_key in self.inventory:
			if inventory_product_entry_key == name:
				return self.inventory[inventory_product_entry_key].product
		print(f"product {name} not found")

	def list_products(self):
		for inventory_product_entry_key in self.inventory:
			print(self.inventory[inventory_product_entry_key])


# Create an instance of the inventory manager and profit manager
p = ProfitTracker()
inventory_manager = InventoryManager()
# Add some products to the inventory
inventory_manager.add_product(Canapes("materiau1", "couleur1", "dimension1", 100, 200, "marque1"), 10)
inventory_manager.add_product(Chaise("materiau2", "couleur2", "dimension2", 50, 100, "marque2"), 20)
inventory_manager.add_product(Table("materiau3", "couleur3", "dimension3", 150, 180,"BULTEX"),12)

inventory_manager.sell_product(inventory_manager.get_product("Chaise"),6, p)

inventory_manager.restock_product(inventory_manager.get_product("Canapes"),4, p)

#print(inventory_manager.revenue_tracker.get_revenue())

#print(inventory_manager.revenue_tracker.get_sales())

inventory_manager.list_products()


#canap = Canapes("materiau1", "couleur1", "dimension1", 100, 200, "marque1")

#profit_tracker= ProfitTracker()
print("Profit : ",p.calcul_profit())
print("Revenue : ",p.total_revenue, ", Cost : ",p.total_cost,", Profit : ",p.total_profit,", Balance : ",  p.balance)