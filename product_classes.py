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

class Casserole_Po�le(Ustensiles_Cuisine):
	def __init__(self, materiaux, cost, price, marque):
		super().__init__(materiaux, cost, price, marque)

class Batterie_Cuisine(Ustensiles_Cuisine):
	def __init__(self, materiaux, cost, price, marque):
		super().__init__(materiaux, cost, price, marque)

class V�tements_Accessoires(Biens_Consommation):
	def __init__(self, cost, price, marque):
		super().__init__(cost, price, marque)

class V�tements(V�tements_Accessoires):
	def __init__(self, cost, price, marque):
		super().__init__(cost, price, marque)

class Haut(V�tements):
	def __init__(self, taille, couleur, matiere, cost, price, marque):
		super().__init__(taille, couleur, matiere, cost, price, marque)

class Pantalon(V�tements):
	def __init__(self, taille, couleur, matiere, cost, price, marque):
		super().__init__(taille, couleur, matiere, cost, price, marque)

class Robe(V�tements):
	def __init__(self, taille, couleur, matiere, cost, price, marque):
		super().__init__(taille, couleur, matiere, cost, price, marque)

class Accessoires(V�tements_Accessoires):
	def __init__(self, cost, price, marque):
		super().__init__(cost, price, marque)

class Chaussures(V�tements_Accessoires):
	def __init__(self, cost, price, marque):
		super().__init__(cost, price, marque)

