from xml.dom import minidom
from deuces import Evaluator
from deuces import Card

class Table:
	
	def __init__(self):
		self.pot = 0
		self.players = 0
		self.hand = ["",""]
		self.handClass = ""
		self.dealer = 0

	def reset(self):
		print "reset"

	def setHandClass(self):
		if(self.hand[0][1]==self.hand[1][1]):
			self.handClass = self.hand[0][0] , self.hand[1][0] , "s"
		else:
			self.handClass = str(self.hand[0][0]) + str(self.hand[1][0]) + "o"

	def out(self):
		print "pot:" , self.pot
		print "players:" , self.players
		print "hand:" , self.hand[0] , self.hand[1]
		print "hand class:" , self.handClass

	def getPlayers(self, players):
		num = 0
		for node in players:
			if("p" in node.getAttribute('states')):
				for char in node.getAttribute('states'):
					if char=='p':
						num += 1
				return num
	def setPot(self, pots):
		for newPot in pots:
			if(newPot.getAttribute('total_pot') != ""):
				self.pot = newPot.getAttribute('total_pot')

	def parse(self, data):
		# parse the packet data
		dom = minidom.parse("hands.txt")
		# reset state if theres a new hand
		if "newhand" in data:
			self.reset()
			self.players = self.getPlayers(dom.getElementsByTagName('table'))
			if "pcard" in data:
				cards = dom.getElementsByTagName('pcard')
				cardsSet = 0
				for node in cards:
					if(node.getAttribute('card')!=""):
						self.hand[cardsSet]=node.getAttribute('card')[0].upper()+node.getAttribute('card')[1]
						cardsSet += 1
				self.setHandClass()
			self.setPot(dom.getElementsByTagName('pot'))

	def getHandStrength(self):
		evaluator = Evaluator()
		score = evaluator.evaluate([Card.new(str(self.hand[0])),Card.new(str(self.hand[1]))], [Card.new('Td'), Card.new('4c'), Card.new('9s')])
		rank = evaluator.get_rank_class(score)
		print "Score:" , score , "Percentile:" , round(1-float(score)/float(7254), 2) , "Class:" , evaluator.class_to_string(rank)