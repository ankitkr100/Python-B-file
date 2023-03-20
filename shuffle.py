# Import required modules
from random import shuffle
# Define a class to create
# all type of cards
class cards:
	global suites, values
	suites = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
	values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

	def __init__(self):
		pass

# Define a class to categorize each card
class Deck(Cards):
	def __init__(self):
		Card.__init__(self)
		self.mycardset = []
		for n in suits:
			for c in values:
				self.mycardset.append((c)+" "+"of"+" "+n)
# Method to remove a card from the deck
def popCard(self):
	if len(self.mycardset) == 0:
		return "No card can be popped further"
	else:
		cardpopped = self.mycardset.pop()
		print("card removed is", cardpopped)

# Define a class to shuffle the deck of cards 
class ShuffleCards(Deck):
	# Constructor
	def __init__(self):
		Deck.__init__(self)

# Method to shuffle cards
def shuffle(self):
	if len(self.mycardset) < 52:
            print("cannot shuffle the cards")
        else:
            shuffle(self.mycardset)
            return self.mycardset

