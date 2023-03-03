class Biens_Consommation:
	pass

class Articles_Menagers(Biens_Consommation):
	def __init__(self, cost, price, marque):
		super().__init__(cost, price, marque)

class Meubles(Articles_Menagers):
	def __init__(self, cost, price, marque):
		super().__init__(cost, price, marque)

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
	def __init__(self, cost, price, marque):
		super().__init__(cost, price, marque)

class Refrigerateur(Appareils_Electromenagers):
	def __init__(self, capacites, cost, price, marque):
		super().__init__(capacites, cost, price, marque)

class Lave_vaisselle(Appareils_Electromenagers):
	def __init__(self, capacites, cost, price, marque):
		super().__init__(capacites, cost, price, marque)

class Lave_linge(Appareils_Electromenagers):
	def __init__(self, capacites, cost, price, marque):
		super().__init__(capacites, cost, price, marque)

class Ustensiles_Cuisine(Articles_Menagers):
	def __init__(self, cost, price, marque):
		super().__init__(cost, price, marque)

class Casserole_Poêle(Ustensiles_Cuisine):
	def __init__(self, materiaux, cost, price, marque):
		super().__init__(materiaux, cost, price, marque)

class Batterie_Cuisine(Ustensiles_Cuisine):
	def __init__(self, materiaux, cost, price, marque):
		super().__init__(materiaux, cost, price, marque)

class Vêtements_Accessoires(Biens_Consommation):
	def __init__(self, cost, price, marque):
		super().__init__(cost, price, marque)

class Vêtements(Vêtements_Accessoires):
	def __init__(self, cost, price, marque):
		super().__init__(cost, price, marque)

class Haut(Vêtements):
	def __init__(self, taille, couleur, matiere, cost, price, marque):
		super().__init__(taille, couleur, matiere, cost, price, marque)

class Pantalon(Vêtements):
	def __init__(self, taille, couleur, matiere, cost, price, marque):
		super().__init__(taille, couleur, matiere, cost, price, marque)

class Robe(Vêtements):
	def __init__(self, taille, couleur, matiere, cost, price, marque):
		super().__init__(taille, couleur, matiere, cost, price, marque)

class Accessoires(Vêtements_Accessoires):
	def __init__(self, cost, price, marque):
		super().__init__(cost, price, marque)

class Chaussures(Vêtements_Accessoires):
	def __init__(self, cost, price, marque):
		super().__init__(cost, price, marque)

