from xml.dom import minidom

class Table:
	pot = 0
	players = 0
	cardOne = ""
	cardTwo = ""
	handClass = ""
	dealer = 0
	
	def __init__(self):
		self.pot = 0

	def reset(self):
		print "reset"

	def getHandClass():
		if(cardOne[1]==cardTwo[1]):
			handClass = cardOne[0] , cardTwo[0] , "s"
		else:
			handClass = cardOne[0] , cardTwo[0] , "o"

	def out(self):
		print "pot: " , self.pot
		print "players: " , self.players
		print "hand: " , self.cardOne , " " , self.cardTwo

	def getPlayers():
		num = 0
		players = dom.getElementsByTagName('table')
		for char in players.getAttribute('states'):
			if char=='p':
				num += 1
		return num

	def parse(self, data):
		print data
		dom = minidom.parse("hands.txt")
		if "newhand" in data:
			self.reset()
			# get # players
			# get new hand
			if "pcard" in data:
				print "test"
				cards = dom.getElementsByTagName('pcard')
				self.cardOne = cards[0][0:1]
				self.cardTwo = cards[1][0:1]