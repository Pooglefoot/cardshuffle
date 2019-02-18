from random import shuffle
import os

#####################
#--- Create Deck ---#
#####################

#Simple function making use of list comprehension to make a list of cards.
#Ordered from aces to kings, but in separate suits.
def create_deck():
    deck = []
    suits = ['H','S','C','D']
    special = ['a','j','q','k']

    for j in range(len(suits)):
        k = []
        for i in range(len(special)):
            a = [special[i], suits[j]]
            if i == 0:
                deck.append(''.join(a))
            else:
                k.append(''.join(a))
        for i in range(2,11):
            a = [str(i), suits[j]]
            deck.append(''.join(a))
        deck.extend(k)

    return deck



########################
#--- Riffle Shuffle ---#
########################

#Riffle shuffle function with no random elements.
#Split decklist in two and append one element from each list per while step until size of new list is size of old (no lost cards).
def riffle(decklist):
    a = decklist[:len(decklist)//2] #Floor division just in case.
    b = decklist[len(decklist)//2:]
    c = []
    i = 0
   

    #Starts by appending from list b because of aforementioned floor division.
    while len(c) != len(decklist):
        c.append(b[i])

        #Exception handling in case deck size is odd (pesky Jokers).
        #TODO: Create modulo check before while to save comparisons in case deck size is even.
        if i > len(a):
            i = i+1
            continue
        c.append(a[i])
        i = i+1
    
    return c



#########################
#--- Mongean Shuffle ---#
#########################

#Mongean shuffle - take cards from unshuffled deck and swap between putting them on top and at the bottom of new deck.
def mongean(decklist):
    c = []
    i = 0

    while len(c) != len(decklist):
        if i%2 == 0:
            c.append(decklist[i])
        else:
            c.insert(0,decklist[i])
        i = i+1
    return c



######################
#--- Pile Shuffle ---#
######################

#A regular pile shuffle. Cards are taken from the unshuffled deck and placed in one of three piles.
#Not one after another, as is using modulo operators and defaulting to three, then 2, so with every cycle the modulo 2 and non-modulo conditions will swap turns.
def pile(decklist):
    a = []
    b = []
    c = []
    d = []
    i = 0

    while i != len(decklist):
        if (i+1)%3 == 0:
            a.append(decklist[i])
        elif (i+1)%2 == 0:
            b.append(decklist[i])
        else:
            c.append(decklist[i])
        i = i+1
    d.extend(b)
    d.extend(c)
    d.extend(a)

    return d


#######################
#--- Corgi Shuffle ---#
#######################

#The Corgi Shuffle is supposed to simulate spreading cards out on a table and gathering them up.
#Caved (for now) and used randomiser functions.
def corgi(decklist):
    shuffle(decklist)
    return decklist

#################################################
#--- Formerly Filthy but now Mon-Global Code ---#
#################################################

def dealer():
    os.system("clear")
    menu = True
    deck = []
    while menu == True:
        print("\nHi, I'm your dealer.")
        if len(deck) == 0:
            print("\nIt seems like you don't have a deck. One is being generated for you.\n")
            deck = create_deck()
            print(deck)
        print("\nPlease enter a command.")
        print("\nEnter 1 to see your current deck.")
        print("Enter 2 to get a new, unshuffled deck.")
        print("Enter 3 for a Riffle Shuffle.")
        print("Enter 4 for a Mongean Shuffle.")
        print("Enter 5 for a Pile Shuffle.")
        print("Enter 6 for a Corgi Shuffle.")
        print("Enter 7 to clear console.")
        print("Enter 8 to quit.\n")

        inp = input("What would you like to do? ")
        if inp.isdigit():
            inp = int(inp)
        else:
            print("\nThat is not a number.")
            continue
    
        if inp < 1 or inp > 8:
            print("\nUnrecognised command, please try again.")
        elif inp == 8:
            menu = False
            break
        else:
            if inp == 1:
                print("\nThis is your current deck.")
                print(deck)
            elif inp == 2:
                deck = create_deck()
                print("\nHere's your new deck.\n")
                print(deck)
            elif inp == 3:
                deck = riffle(deck)
                print("\nRiffle Shuffle coming up.\n")
                print(deck)
            elif inp == 4:
                deck = mongean(deck)
                print("\nMongean Shuffle, exciting!\n")
                print(deck)
            elif inp == 5:
                deck = pile(deck)
                print("\nStructural and ordered, here you go.\n")
                print(deck)
            elif inp == 6:
                deck = corgi(deck)
                print("\nEasy and effective, here you go!\n")
                print(deck)
            elif inp == 7:
                os.system("clear")
            del inp

dealer()
