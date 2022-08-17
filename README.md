# highorlow
 Python script running a famous italian card game

First thing first it creates a deck of neapolitan cards using a for loop (40 cards, 10 for each seed).
The player and the house start each game with 0 points.

Using random library a card gets drawn from the deck as if it was shuffled beforehand. 
Now the player has to input his guess if the card is either A (higher than 5) or B (lower than 6).
The guess is appended to the respective list (highs or lows) for later use.

If the guess is correct the player gets 1 point, otherwise the house gets 1. 
The card is now removed from the deck so that it can't be drawn again.

At the end of each turn points and remaining cards is shown.

At the end of the game the winner is announced and the choices (highs or lows) are stored in a csv file for later analysis.
