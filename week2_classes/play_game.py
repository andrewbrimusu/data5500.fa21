from DeckOfCards import DeckOfCards

deck = DeckOfCards()

deck.print_deck()

deck.shuffle_deck()

deck.print_deck()


# deal two cards to the user
card = deck.get_card()
card2 = deck.get_card()

score = 0
# calculate the user's hand score
score += card.val
score += card2.val
print("Your score is: ", score)


# ask user if they would like a "hit" (another card)
hit = input("would you like a hit? ")

if hit == 'y':
    card3 = deck.get_card()
    score += card3.val
    print("new score: ", score)
    
    
