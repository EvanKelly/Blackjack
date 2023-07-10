import random, sys

class Card:
   def __init__(self, suit, value, card_value):
      self.suit = suits
      self.value = value
      self.card_value = card_value

suits = ["Spades", "Hearts", "Clubs", "Diamonds"]

cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
 
cards_values = {"A": 11, "Al": 1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}

if '-P' in sys.argv:
   PRINTARG = True
else:
   PRINTARG = False
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

   handsWonHit = 0
   valueWonHit = 0
   handsWonStand = 0
   valueWonStand = 0
   handsPushedHit = 0
   handsPushedStand = 0
   handsLostHit = 0
   handsLostStand = 0

   numSims = input("Enter number of times to run the hand :")
   betSize = input("Enter betsize :")
   dealerUp = input("Enter Dealer Up Card:")
   playerc1 = input("Enter Player Card 1:")
   playerc2 = input("Enter Player Card 2:")

   numSims = int(numSims)
   #keep original value of sims
   totalSims = int(numSims)
   betSize = int(betSize)

   def playDealerHand(card1, card2):
      #define Al as Ace Low for when both are aces
      hitSoft17 = True
      if card1 == 'A' and card2 == 'A':
            card1 = 'Al'
      dealer_score = handScore(card1, card2)
      hand = [card1, card2]
      while dealer_score <= 17:
         foundAce = 0
         #stand on hard 17
         if( (dealer_score == 17) and ('A' not in hand)):
            break
         #stand on soft 17
         if( (dealer_score == 17 and (not hitSoft17))):
            break
         newCard = random.choice(cards)
         hand.append(newCard)
         dealer_score += cards_values[newCard]
         if dealer_score > 21:
            #first check if there's an Ah that we can lower to Al
            for card in hand:
               if foundAce == 1:
                  break
               if card == 'A':
                  hand.remove('A')
                  hand.append('Al')
                  dealer_score -= 10
                  foundAce = 1
                  break
         if dealer_score > 21:
            return (dealer_score, hand)
      return (dealer_score, hand)

   def playPlayerHand(card1, card2):
      if card1 == 'A' and card2 == 'A':
            card1 = 'Al'
      hand = [card1, card2]
      player_score = handScore(card1, card2)
      hit_score = player_score
      stand_hand = hand.copy()
      #Optional Strategy for First Play
      #hit
      hitHand = hand
      newCard = random.choice(cards)
      hitHand.append(newCard)
      hit_score += cards_values[newCard]
      if hit_score > 21:
         if 'A' in hitHand:
            hitHand.remove('A')
            hitHand.append('Al')
            hit_score -= 10
      #stand
      stand_score = player_score 
      #play normal after
      while player_score <= 16:
         newCard = random.choice(cards)
         hitHand.append(newCard)
         hit_score += cards_values[newCard]
         if hit_score > 21:
            if 'A' in hitHand:
               hitHand.remove('A')
               hitHand.append('Al')
               hit_score -= 10
            if player_score > 21:
               return (stand_score, stand_hand, hit_score, hitHand)
      return (stand_score, stand_hand, hit_score, hitHand)
   def printHands(pScore, dScore, pHand, dHand, sScore, sHand):
      print("Dealer Hand: ", end='')
      for c in dHand:
         print(c, end=' ')
      print ("\nDealer Score: " + str(dScore))
      print("Player Hit Hand: ", end='')
      for c in pHand:
         print(c, end=' ')
      print ("\nPlayer Hit Score: " + str(pScore))
      print("Player Stand Hand: ", end='')
      for c in sHand:
         print(c, end=' ')
      print ("\nPlayer Stand Score: " + str(sScore))

   dealerBJCount = 0
   while numSims >= 1:
      dealerDown = random.choice(cards)
      dealerBJ = checkBlackjack(str(dealerUp), dealerDown)
      playerBJ = checkBlackjack(playerc1, playerc2)
      if (dealerBJ == 1) and (playerBJ == 1):
         handsPushedHit += 1
         handsPushedStand += 1
         print ("BJ Push")
         numSims = numSims - 1
         continue
      if (playerBJ == 1):
         handsWonHit += 1
         valueWonHit += betSize * 1.5
         handsWonStand += 1
         valueWonStand += betSize * 1.5
         #print ("Player BJ!!!!!!!!!")
         numSims = numSims - 1
         continue
      if (dealerBJ == 1):
         #handsLostStand += 1
         #valueWonStand -= betSize
         #handsLostHit += 1
         #valueWonHit -= betSize
         dealerBJCount += 1
         if (PRINTARG):
            print ("Dealer BJ")
         #numSims = numSims - 1
         continue

      sScore, sHand, pScore, pHand = playPlayerHand(playerc1, playerc2)
      dScore, dHand = playDealerHand(str(dealerUp), dealerDown)
      if (PRINTARG):
         printHands(pScore, dScore, pHand, dHand, sScore, sHand)
      if pScore > 21:
         handsLostHit += 1
         valueWonHit -= betSize
      if dScore > 21:
         handsWonStand += 1
         valueWonStand += betSize
      if (pScore <= 21) and (pScore == dScore):
         handsPushedHit += 1
      if (sScore == dScore):
         handsPushedStand += 1
      if (sScore < dScore) and (dScore <= 21):
         handsLostStand += 1
         valueWonStand -= betSize
      if (sScore > dScore):
         handsWonStand += 1
         valueWonStand += betSize
      if ((pScore <= 21) and (pScore < dScore)):
         handsLostHit += 1
         valueWonHit -= betSize
      if ((pScore <= 21) and (pScore > dScore)):
         handsWonHit += 1
         valueWonHit += betSize
      
      numSims = numSims - 1
   eWinSurr = -1 *(betSize/2 * (totalSims - dealerBJCount)) - (dealerBJCount * betSize)
   print("______TOTALS______")
   print("Dealer BJs:" + str(dealerBJCount))
   print("Hands Played: " + str(totalSims))
   print("Hands Won Stand:" + str(handsWonStand))
   print("Hands Lost Stand:" + str(handsLostStand))
   print("Hands Pushed Stand:" + str(handsPushedStand))
   print("Hands Won Stand Percentage: " + str(handsWonStand/(totalSims) * 100) + '%')
   print("Expected Winnings Stand: $" + str(valueWonStand / (totalSims)))
   print("Hands Won Hit Percentage: " + str(handsWonHit/(totalSims) * 100) + '%')
   print("Expected Winnings Hit: $" + str(valueWonHit / (totalSims)))
   print("Expected Winnings Surrender: $" + str(eWinSurr/(totalSims)))

hand_simulator()

