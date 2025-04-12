import random, sys

class Card:
   def __init__(self, suit, value, card_value):
      self.suit = suit
      self.value = value
      self.card_value = card_value

class Shoe:
   def __init__(self, num_decks):
      self.num_decks = num_decks
      self.cards = []
      for i in range(num_decks):
         for suit in suits:
            for card in cards:
               self.cards.append(Card(suit, card, card_values[card]))

   def shuffle(self):
      random.shuffle(self.cards)

   def draw_card(self):
      return self.cards.pop()

suits = ["Spades", "Hearts", "Clubs", "Diamonds"]

cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
 
card_values = {"A": 14, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":11, "Q":12, "K":13}

fourcount = 0
threecount = 0
twocount = 0
paircount = 0
full_house_count = 0
flushcount = 0
straightcount = 0
sfcount = 0
rfcount = 0
hccount = 0
numHands = 100000000
for x in range(numHands):
    myShoe = Shoe(1)
    myShoe.shuffle()

    def dealPokerHand():
        player_hand = []
        for i in range(5):
            card = myShoe.draw_card()
            player_hand.append(card)
        return player_hand

    myHand = dealPokerHand()
    def printHand():
        for card in myHand:
            print(f"{card.value} of {card.suit}")
    #printHand()

    def checkPokerHand():
        # Check for poker hand combinations
        hand_values = [card.card_value for card in myHand]
        hand_values.sort()
        
        # Check for flush
        flush = all(card.suit == myHand[0].suit for card in myHand)
        
        # Check for straight
        
        straight = all(hand_values[i] + 1 == hand_values[i + 1] for i in range(4))
        if(14 in hand_values and 2 in hand_values):
            # Special case for Ace-2-3-4-5 straight
            straight = straight or (hand_values == [2, 3, 4, 5, 14])
            
        # Check for pairs, three of a kind, four of a kind
        value_counts = {value: hand_values.count(value) for value in set(hand_values)}
        pairs = sum(1 for count in value_counts.values() if count == 2)
        three_of_a_kind = sum(1 for count in value_counts.values() if count == 3)
        four_of_a_kind = sum(1 for count in value_counts.values() if count == 4)
        full_house = pairs == 1 and three_of_a_kind == 1
        two_pair = pairs == 2
            # Determine hand rank
        if four_of_a_kind:
            #print("Four of a Kind")
            return "Four of a Kind"
        elif full_house:
            #print("Full House")
            return "Full House"
        elif three_of_a_kind:
            #print("Three of a Kind")
            return "Three of a Kind"
        elif two_pair:
            #print("Two Pair")   
            return "Two Pair"
        elif pairs == 1:
            #print("One Pair")     
            return "One Pair"
        elif flush and not straight:
            #print("Flush")     
            return "Flush"
        elif straight and not flush:
            #print("Straight")    
            return "Straight"
        elif straight and flush:
            # Check for straight flush
            if hand_values == [10, 11, 12, 13, 14]:
                return "Royal Flush"
            else:  
                #print("Straight Flush")
                return "Straight Flush"
        else:
            #print("High Card")
            return "High Card"
    
    result = checkPokerHand()

    if result == "High Card":
        hccount += 1
    elif result == "One Pair":
        paircount += 1
    elif result == "Two Pair":
        twocount += 1
    elif result == "Three of a Kind":
        threecount += 1
    elif result == "Straight":
        straightcount += 1
    elif result == "Flush":
        flushcount += 1
    elif result == "Full House":
        full_house_count += 1
    elif result == "Four of a Kind":
        fourcount += 1
    elif result == "Straight Flush":
        sfcount += 1
    elif result == "Royal Flush":
        rfcount += 1
    
print(f"Four of a Kind: {fourcount}")
print(f"Full House: {full_house_count}")
print(f"Flush: {flushcount}")
print(f"Straight: {straightcount}")
print(f"Straight Flush: {sfcount}")
print(f"Royal Flush: {rfcount}")
print(f"Three of a Kind: {threecount}")
print(f"Two Pair: {twocount}")
print(f"One Pair: {paircount}")
print(f"High Card: {hccount}")
print(f"Total Hands: {numHands}")