class Biens_Consommation:
	def __init__(self, cost, price, marque):
		self.cost = cost
		self.price = price
		self.marque = marque

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

# Define a function that prompts the user to enter values for a given class
def prompt_for_instance(cls):
    # Get the names of the constructor arguments
    arg_names = cls.__init__.__code__.co_varnames[1:]
    # Prompt the user for the values of the arguments 
    print(cls.__name__,":")
    args = [input("Enter the value for {}: ".format(name)) for name in arg_names]
    # Create an instance of the class using the entered values
    return cls(*args)

# Prompt the user to create instances of the Biens_Consommation, Articles_Menagers, and Meubles classes
#biens_consommation = prompt_for_instance(Biens_Consommation)
#articles_menagers = prompt_for_instance(Articles_Menagers)
def sep():
    print("\n====================\n")
    
sep()

#chaussures = prompt_for_instance(Chaussures)
#print(vars(chaussures))


class InventoryItem:
	def __init__(self, product, quantity, cost, price):
		self.product = product
		self.quantity = quantity
		self.cost = cost
		self.price = price
		self.sales = 0

	def sell(self, quantity):
		if self.quantity < quantity:
			raise ValueError("Not enough stock")
		self.quantity -= quantity
		self.sales += quantity * self.price

	def restock(self, quantity):
		self.quantity += quantity

	def __repr__(self):
		return "{} ({}): {} in stock, {} sold, {} revenue".format(type(self.product).__name__, self.product.marque, self.quantity, self.sales / self.price, self.sales)

class RevenueTracker:
    def __init__(self):
        self.sales = {}
        self.revenue = 0

    def add_sale(self, item,quantity):
        if item not in self.sales:
            self.sales[item] = 0
        self.sales[item] += 1
        self.revenue += item.price*quantity

    def get_sales(self):
        return self.sales

    def get_revenue(self):
        return self.revenue

class InventoryManager:
	def __init__(self):
		self.revenue_tracker = RevenueTracker()
		self.inventory = []

	@staticmethod
	def ItemsEqual(inventory_item, item):
		return type(inventory_item.product).__name__ == type(item.product).__name__

	def add_item(self, item, quantity, cost, price):
		inventory_item = InventoryItem(item, quantity, cost, price)
		self.inventory.append(inventory_item)

	def remove_item(self, item):
		for inventory_item in self.inventory:
			if self.ItemsEqual(inventory_item, item):
				self.inventory.remove(inventory_item)

	def sell_item(self, item, quantity):
		for inventory_item in self.inventory:
			if self.ItemsEqual(inventory_item, item):
				inventory_item.sell(quantity)
				self.revenue_tracker.add_sale(item, quantity)
				return
		raise ValueError("Item not found")

	def restock_item(self, item, quantity):
		for inventory_item in self.inventory:
			if self.ItemsEqual(inventory_item, item):
				inventory_item.restock(quantity)
				return
		raise ValueError("Item not found")

	def get_item(self, name):
		for inventory_item in self.inventory:
			if type(inventory_item.product).__name__ == name:
				return inventory_item
		raise ValueError("Item not found")

	def list_items(self):
		for inventory_item in self.inventory:
			print(inventory_item)

	# Create an instance of the inventory manager
inventory_manager = InventoryManager()

# Add some items to the inventory
inventory_manager.add_item(Canapes("materiau1", "couleur1", "dimension1", 100, 200, "marque1"), 5, 80, 150)
inventory_manager.add_item(Chaise("materiau2", "couleur2", "dimension2", 50, 100, "marque2"), 10, 20, 50)
inventory_manager.add_item(Table("materiau3", "couleur3", "dimension3", 150, 180,"BULTEX"),10,15,20)


inventory_manager.sell_item(inventory_manager.get_item("Chaise"),6)

inventory_manager.restock_item(inventory_manager.get_item("Canapes"),7)

print(inventory_manager.revenue_tracker.get_revenue())

print(inventory_manager.revenue_tracker.get_sales())

inventory_manager.list_items()