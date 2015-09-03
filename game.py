#imports
import random

#global variables
deck = []
playerHands = []
playerBank = []
numPlayers = 0
numComputers = 0
potSize = 0

#functions
def initialize(): #does all of the setup required for a new game
	global numPlayers
	global numComputers
	global playerHands
	global playerBank
	shuffleDeck()
	print "Welcome to 7Up"
	numPlayers = input("How many players total? ") #ask to see how many players there should be total
	while(type(numPlayers) is not int or numPlayers < 2 or numPlayers > 8): #verify that it's a valid number of players
		print "There must be between 2 and 8 players." #print out an error message if it's not
		numPlayers = input("How many players total? ") #reask the question
	numComputers = input("How many computers players? ") #ask to see how many computer players there should be total
	while(type(numComputers) is not int or numComputers < 0 or numComputers > numPlayers): #verify that it's a valid number of computers
		print "The number of computer players must be less than or equal to the number of players total." #print out an error message if it's not
		numComputers = input("How many computers players? ") #reask the question
	startingChips = input("How chips should each player start with? ") #ask to see how many chips each player should start with
	while(type(startingChips) is not int or startingChips < 0): #verify that it's a valid number of starting chips
		print "Each player must have at least 1 chip to start." #print out an error message if it's not
		startingChips = input("How chips should each player start with? ") #reask the question
	playerHands = [[] for i in range(numPlayers)] #create the list that holds the player hands in it
	playerBank = [[] for i in range(numPlayers)] #create the list that holds the player's number of chips
	for i in range(numPlayers): #loops though the number of players
		playerBank[i] = startingChips #gives them their starting number of chips
	dealDeck()

def shuffleDeck(): #shuffles all of the cards and then puts them into the global deck
	global deck
	deck = []
	cards = ["AH","2H","3H","4H","5H","6H","7H","8H","9H","10H","JH","QH","KH","AD","2D","3D","4D","5D","6D","7D","8D","9D","10D","JD","QD","KD","AC","2C","3C","4C","5C","6C","7C","8C","9C","10C","JC","QC","KC","AS","2S","3S","4S","5S","6S","7S","8S","9S","10S","JS","QS","KS"]
	while len(cards) > 0:
		deck.append(cards.pop(random.randrange(0,len(cards))))

def dealDeck(): #takes the global deck and deals out the cards to the players
	global deck
	global playerHands
	global numPlayers
	for i in range(52):
		playerHands[i%numPlayers].append(deck.pop(0))
	
def printDeck(): #prints out all of the cards in the deck (utility function)
	for card in deck:
		print card
		
def payPot(playerNum, amount=1): #takes money out of the player's bank and puts it into the pot, defaults to 1
	global playerBank
	global potSize
	while(amount > 0): #removes the chips 1 at a time to handle not having enough
		if(playerBank[playerNum] > 0): #checks to make sure the player has chips remaining
			playerBank[playerNum] = playerBank[playerNum] - 1 #removes one of the player's chips
			potSize = potSize + 1 #and adds it to the pot
		else:
			amount = amount - 1 #reduce the amount owed to the pot since the player can't afford it anyway

def collectPot(playerNum): #gives all of the chips in the pot to the player
	global playerBank
	global potSize
	playerBank[playerNum] = playerBank[playerNum] + potSize #adds the pot to the player
	potSize = 0 #resets the pot down to 0 chips

#startup code
initialize()
