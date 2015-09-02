import random

deck = []


def shuffleDeck():
	global deck
	deck = []
	cards = ["AH","2H","3H","4H","5H","6H","7H","8H","9H","10H","JH","QH","KH","AD","2D","3D","4D","5D","6D","7D","8D","9D","10D","JD","QD","KD","AC","2C","3C","4C","5C","6C","7C","8C","9C","10C","JC","QC","KC","AS","2S","3S","4S","5S","6S","7S","8S","9S","10S","JS","QS","KS"]
	while len(cards) > 0:
		deck.append(cards.pop(random.randrange(0,len(cards))))
	
def printDeck():
	for card in deck:
		print card