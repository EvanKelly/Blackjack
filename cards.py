import random

class Card:
   def __init__(self, suit, value, card_value):
      self.suit = suits
      self.value = value
      self.card_value = card_value

suits = ["Spades", "Hearts", "Clubs", "Diamonds"]

cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
 
cards_values = {"A": 11, "Al": 1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}

numdecks = 1
shoe = []
i = numdecks
while i >= numdecks:
   for suit in suits:
      for card in cards:
         shoe.append(Card(suit, card, cards_values[card]))
   i = i-1

def checkBlackjack(card1, card2):
   if (card1 == 'A') and (cards_values[card2] == 10):
      return 1
   if (card2 == 'A') and (cards_values[card1] == 10):
      return 1
   else:
      return 0

def handScore(card1, card2):
   return cards_values[card1] + cards_values[card2]

def hand_simulator():
   global cards_values
   global cards

   handsWon = 0
   valueWon = 0
   handsPushed = 0
   handsLost = 0

   numSims = input("Enter number of times to run the hand :")
   betSize = input("Enter betsize :")
   dealerUp = input("Enter Dealer Up Card:")
   playerc1 = input("Enter Player Card 1:")
   playerc2 = input("Enter Player Card2:")

   numSims = int(numSims)
   betSize = int(betSize)

   def playDealerHand(card1, card2):
      #define Al as Ace Low for when both are aces
      if card1 == 'A' and card2 == 'A':
            card1 = 'Al'
      dealer_score = handScore(card1, card2)
      hand = [card1, card2]
      return (dealer_score, hand)

   def playPlayerHand(card1, card2):
      if card1 == 'A' and card2 == 'A':
            card1 = 'Al'
      hand = [card1, card2]
      player_score = handScore(card1, card2)
      while player_score <= 16:
         newCard = random.choice(cards)
         hand.append(newCard)
         player_score += cards_values[newCard]
         if player_score > 21:
            for card in hand:
               if card == 'A':
                  card = 'Al'
                  player_score -= 10
                  break
         if player_score > 21:
            return (player_score, hand)
      return (player_score, hand)
   def printHands(pScore, dScore, pHand, dHand):
      print("Dealer Hand: ")
      for c in dHand:
         print(c, end=' ')
      print ("\nDealer Score: " + str(dScore))
      print("Player Hand: ")
      for c in pHand:
         print(c, end=' ')
      print ("\nPlayer Score: " + str(pScore))

   while numSims >= 1:
      dealerDown = random.choice(cards)
      dealerBJ = checkBlackjack(str(dealerUp), dealerDown)
      playerBJ = checkBlackjack(playerc1, playerc2)
      if (dealerBJ == 1) and (playerBJ == 1):
         handsPushed += 1
         print ("BJ Push")
         numSims = numSims - 1
         continue
      if (playerBJ == 1):
         handsWon += 1
         valueWon += betSize * 1.5
         print ("Player BJ!!!!!!!!!")
         numSims = numSims - 1
         continue
      if (dealerBJ == 1):
         handsLost += 1
         valueWon -= betSize
         print ("Dealer BJ")
         numSims = numSims - 1
         continue

      pScore, pHand = playPlayerHand(playerc1, playerc2)
      if pScore > 21:
         handsLost += 1
         valueWon -= betSize
         numSims = numSims - 1
         printHands (pScore, handScore(dealerDown, str(dealerUp)), pHand, [str(dealerUp), dealerDown])
         continue
      dScore, dHand = playDealerHand(dealerDown, str(dealerUp))
      if pScore == dScore:
         handsPushed += 1
         printHands (pScore, dScore, pHand, dHand)
         numSims = numSims - 1
         continue
      if pScore > dScore:
         handsWon += 1
         valueWon += betSize
         printHands (pScore, dScore, pHand, dHand)
         numSims = numSims - 1
         continue
      if pScore < dScore:
         handsLost += 1
         valueWon -= betSize
         printHands (pScore, dScore, pHand, dHand)


      
      numSims = numSims - 1
   print("______TOTALS______")
   print("Hands Played: " + str(handsWon + handsPushed + handsLost))
   print("Hands Won: " + str(handsWon))
   print("Winnings: $" + str(valueWon))

hand_simulator()

