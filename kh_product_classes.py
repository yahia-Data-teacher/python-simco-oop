class Product:
	def __init__(self, cost, price, marque):
		self.cost = cost
		self.price = price
		self.marque = marque
		self.name=type(self).__name__
	
class Biens_Consommation(Product):
	def __init__(self,cost, price, marque):
		super().__init__(cost, price, marque)
		

class Articles_Menagers(Biens_Consommation):
	def __init__(self, cost, price, marque):
		super().__init__(cost, price, marque)

class Meubles(Articles_Menagers):
	def __init__(self, materiaux, couleur, dimension, cost, price, marque):
		super().__init__(cost, price, marque)
		self.materiaux = materiaux
		self.couleur = couleur
		self.dimension = dimension

class Canapes(Meubles):
	def __init__(self, materiaux, couleur, dimension, cost, price, marque):
		super().__init__(materiaux, couleur, dimension, cost, price, marque)

class Chaise(Meubles):
	def __init__(self, materiaux, couleur, dimension, cost, price, marque):
		super().__init__(materiaux, couleur, dimension, cost, price, marque)

class Table(Meubles):
	def __init__(self, materiaux, couleur, dimension, cost, price, marque):
		super().__init__(materiaux, couleur, dimension, cost, price, marque)

class Appareils_Electromenagers(Articles_Menagers):
	def __init__(self, capacites, cost, price, marque):
		super().__init__(cost, price, marque)
		self.capacites = capacites

class Refrigerateur(Appareils_Electromenagers):
	def __init__(self, efficacite, capacites, cost, price, marque):
		super().__init__(capacites, cost, price, marque)
		self.efficacite = efficacite

class Lave_vaisselle(Appareils_Electromenagers):
	def __init__(self, programme, capacites, cost, price, marque):
		super().__init__(capacites, cost, price, marque)
		self.programme = programme

class Lave_linge(Appareils_Electromenagers):
	def __init__(self, programme, capacites, cost, price, marque):
		super().__init__(capacites, cost, price, marque)
		self.programme = programme

class Ustensiles_Cuisine(Articles_Menagers):
	def __init__(self, materiaux, cost, price, marque):
		super().__init__(cost, price, marque)
		self.materiaux = materiaux

class Casserole_Poele(Ustensiles_Cuisine):
	def __init__(self, diametre, materiaux, cost, price, marque):
		super().__init__(materiaux, cost, price, marque)
		self.diametre = diametre

class Batterie_Cuisine(Ustensiles_Cuisine):
	def __init__(self, nombre_pieces, materiaux, cost, price, marque):
		super().__init__(materiaux, cost, price, marque)
		self.nombre_pieces = nombre_pieces

class Vetements_Accessoires(Biens_Consommation):
	def __init__(self, cost, price, marque):
		super().__init__(cost, price, marque)

class Vetements(Vetements_Accessoires):
	def __init__(self, taille, couleur, matiere, cost, price, marque):
		super().__init__(cost, price, marque)
		self.taille = taille
		self.couleur = couleur
		self.matiere = matiere

class Haut(Vetements):
	def __init__(self, taille, couleur, matiere, cost, price, marque):
		super().__init__(taille, couleur, matiere, cost, price, marque)

class Pantalon(Vetements):
	def __init__(self, taille, couleur, matiere, cost, price, marque):
		super().__init__(taille, couleur, matiere, cost, price, marque)

class Robe(Vetements):
	def __init__(self, taille, couleur, matiere, cost, price, marque):
		super().__init__(taille, couleur, matiere, cost, price, marque)

class Accessoires(Vetements_Accessoires):
	def __init__(self, couleur, cost, price, marque):
		super().__init__(cost, price, marque)
		self.couleur = couleur

class Chaussures(Vetements_Accessoires):
	def __init__(self, pointure, cost, price, marque):
		super().__init__(cost, price, marque)
		self.pointure = pointure

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
			return
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
		self.inventory_manager = InventoryManager()
		self.total_revenue=0
		self.total_profit = 0
		self.total_cost = 0
		self.balance= 1000

	def buy_product(self, product:Product,quantity):
		self.balance= self.balance - (product.cost * quantity)

	def sell_product(self, product:Product,quantity):
		self.balance= self.balance + (product.price * quantity)

	def calcul_revenue(self):
		for inventory_product_entry_key in self.inventory:
			self.total_revenue = self.inventory[inventory_product_entry_key].sales
			self.total_cost = self.inventory[inventory_product_entry_key].expenses

		return self.total_revenue + self.total_cost

	def calcul_profit(self):
		self.total_profit = self.calcul_revenue()
		return self.total_profit

		#################################@@
from typing import Dict

class InventoryManager:
	def __init__(self):

		self.profit_tracker = ProfitTracker()
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

	def sell_product(self, product:Product, quantity):
		for inventory_product_entry_key in self.inventory:
			if inventory_product_entry_key == product.name:
				self.inventory[inventory_product_entry_key].sell(quantity)
				self.profit_tracker.sell_product(product, quantity)
				return
		print(f"product {product.name} not found")

	def restock_product(self, product:Product, quantity):
		for inventory_product_entry_key in self.inventory:
			if self.product_exists(product):
				self.inventory[inventory_product_entry_key].restock(quantity)
				self.profit_tracker.buy_product(product, quantity)
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
	

# Create an instance of the inventory manager
inventory_manager = InventoryManager()

# Add some products to the inventory
inventory_manager.add_product(Canapes("materiau1", "couleur1", "dimension1", 100, 200, "marque1"), 10)
inventory_manager.add_product(Chaise("materiau2", "couleur2", "dimension2", 50, 100, "marque2"), 5)
inventory_manager.add_product(Table("materiau3", "couleur3", "dimension3", 150, 180,"BULTEX"),12)

inventory_manager.sell_product(inventory_manager.get_product("Chaise"),6)

#inventory_manager.restock_product(inventory_manager.get_product("Canapes"),4)

#print(inventory_manager.revenue_tracker.get_revenue())

#print(inventory_manager.revenue_tracker.get_sales())

inventory_manager.list_products()


#canap = Canapes("materiau1", "couleur1", "dimension1", 100, 200, "marque1")

profit_tracker= ProfitTracker()
print(profit_tracker.calcul_profit())