from DeckOfCards import *

deck1 = DeckOfCards()
deck1.shuffle_deck()
deck1.print_deck()

user_card = deck1.deck[deck1.get_card()]
print(user_card)

user2_card = deck1.deck[deck1.get_card()]
print(user2_card)

# add logic to see which card value is higher