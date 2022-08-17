### High or low card game script

# Libraries
import random
import pandas as pd
from openpyxl import load_workbook
## Game setup 
print('Prendo le carte...')
# Creating Deck
deck = []

# Generating 10 cards for each seed
for i in range(1, 11, 1):
    spade = f'{i} di spade'
    deck.append(spade)
    bastoni = f'{i} di bastoni'
    deck.append(bastoni)
    denari = f'{i} di denari'
    deck.append(denari)
    coppe = f'{i} di coppe'
    deck.append(coppe)

#Creating point pools
    #Giocatore
P1 = 0
    #Mazziere
P2 = 0

# Deck of used cards
carte_uscite = []

# List of used conditions
highs = []
lows = []
choices = []
choices_recap = f'Scelte alte: {len(highs)}, scelte basse: {len(lows)}'

## Game mechanics
print('Cominciamo!')
#Iterate deck
while len(deck) > 0:
    #Generate card and extrapolate num as int
    card = random.choice(deck)
    card_num = int(card[0:2])
    #Ask for condition
    condition = input('La carta è? (A per alta / B per bassa): ')

    #Error if condition is invalid
    if condition.lower() != 'a' and condition.lower() != 'b':
        print('Inserire una condizione valida! Le conditioni valide sono: "a" e "b"')
    
    #Turn if condition is valid
    else:
        #Show card to players
        print(f'La carta è il {card}.')
        
        #When alta
        if condition.lower() == 'a':
            highs.append(condition)
            if card_num > 5:
                P1=P1+1
            else:
                P2=P2+1

        #When bassa
        if condition.lower() == 'b':
            lows.append(condition)
            if card_num < 5:
                P1=P1+1
            else:
                P2=P2+1

        #Remove card from deck
        deck.remove(card)
        carte_uscite.append(card)
        choices.append(condition)

    #Game info at the end of turn
    print(f'Punti giocatore: {P1}, Punti mazziere: {P2}')
    print(f'Carte rimanenti: {len(deck)}')

# print(carte_uscite)

## Game End

#Print result
if P1>P2:
    print(f'Il giocatore vince per {P1} a {P2}!')
elif P1==P2:
    print(f'È un pareggio! {P1} a {P2}.')
elif P2>P1:
    print(f'Il mazziere vince per {P2} a {P1}!')
#Data
print(f'Le scelte sono state: {len(highs)} alte, {len(lows)} basse.')
print('Exporting data...')
old_df = pd.read_csv(r'/Users/dario/Documents/VSCode/gioco_di_carte/choices.txt')
new_df = pd.DataFrame(choices, columns=['choice'])
complete_df = pd.concat([old_df, new_df], axis=0)
complete_df.to_csv(path_or_buf=r'/Users/dario/Documents/VSCode/gioco_di_carte/choices.txt', sep=',', mode='w', index=False)
print('All done!')