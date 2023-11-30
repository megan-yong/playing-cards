<h1>Playing Cards Project</h1>

<b>Date completed:</b> November 29, 2023

<h2>Description</h2>
A Python program using the object-oriented programming paradigm to create a reusable model of a deck of cards for building digital card game programs, such as Poker and Blackjack.
<br>
<br>
The program takes three classes: 'Card', 'Deck' and 'Hand'. 
<br>
<br>
<b>Card class</b>
<br>
The Card class represents the individual playing cards. It contains the property with a setter to ensure that the suit one of "Hearts", "Clubs", "Diamonds", or "Spades", as well as to ensure that the number is valid between 2 to 10, J, Q, K, and A. 
<br>
<br>
It also attributes the value of a card as an integer. Numbered cards are valued equivalent to their numbers and “picture cards” (J, K, Q) are worth as 10. Depending on the game, the ace may be high or low, and can be adjusted accordingly within the class variable. 
<br>
<br>
<b>Deck class</b>
<br>
The Deck class manages a deck of cards by populating it with instances of the Card class with 52 cards, one for each combination of suit and number. 
<br>
<br>
The Deck class also extends it's functionality with three additional methods. 
<br>
<br>
  - The cards can be shuffled to randomise the order of the cards in the deck using shuffle().
<br> <br>
  - Cards can be checked against the Card class whether a particular card is present in the deck or not. It returns True if the card is in the deck, otherwise False. 
<br> <br>
  - Cards are dealt from the deck to a specified number of players and a specified number of cards per player. It checks if there are enough cards in the deck for the specified deal; if not, it prints an error message and returns None. It then creates a list of hands, where each hand corresponds to a player, and each player receives a specified number of cards, returning the hands as a list of lists.
<br>
<br>
<b>Hand class</b>
<br>
The Hand class represents a player's hand, managing the cards held in a card game. It allows for the creation of a player's hand based on cards dealt in the Deck class, the addition of cards to the hand, and provides a display of the cards held in hand. 
<br>
<br>
"The Hand class represents a player's hand, managing the cards held in a card game. It facilitates the creation of a player's hand based on cards dealt in the Deck class, enables the addition of cards from the top of the deck into the hand, and provides a method to display the cards held in the hand."

<h2>Remarks</h2>
- 
