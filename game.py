#imports
import random

#global variables
deck = []
playerHands = []
numPlayers = 0
numComputers = 0

#functions
def initialize():
	global numPlayers
	global numComputers
	shuffleDeck()
	print "Welcome to 7Up"
	numPlayers = input("How many players total? ")
	while(type(numPlayers) is not int or numPlayers < 2 or numPlayers > 8):
		print "There must be between 2 and 8 players."
		numPlayers = input("How many players total? ")
	numComputers = input("How many computers players? ")
	while(type(numComputers) is not int or numComputers < 0 or numComputers > numPlayers):
		print "The number of computer players must be less than or equal to the number of players total."
		numComputers = input("How many computers players? ")
	dealDeck()

def shuffleDeck():
	global deck
	deck = []
	cards = ["AH","2H","3H","4H","5H","6H","7H","8H","9H","10H","JH","QH","KH","AD","2D","3D","4D","5D","6D","7D","8D","9D","10D","JD","QD","KD","AC","2C","3C","4C","5C","6C","7C","8C","9C","10C","JC","QC","KC","AS","2S","3S","4S","5S","6S","7S","8S","9S","10S","JS","QS","KS"]
	while len(cards) > 0:
		deck.append(cards.pop(random.randrange(0,len(cards))))

def dealDeck():
	global deck
	global playerHands
	global numPlayers
	nextDeal = 0
	playerHands = [[] for i in range(numPlayers)]
	print deck
	for j in range(52):
		playerHands[nextDeal%numPlayers].append(deck.pop(0))
		nextDeal = nextDeal + 1
	print playerHands
	
def printDeck():
	for card in deck:
		print card
		
#startup code
initialize()
