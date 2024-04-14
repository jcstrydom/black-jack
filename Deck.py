class Deck():
	"""
	DOCSTRING: this is only the Deck object
	"""

	def __init__(self):
		print('\tNew deck chosen...')
		self.cardPoints = {'A':11,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}

		self.pack = []
		for suit in ('Di','Cl','Hr','Sp'):
			for value in self.cardPoints.keys():
				self.pack.append(f"{suit} {value}")