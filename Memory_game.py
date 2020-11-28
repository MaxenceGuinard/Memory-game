# ♠♦♣♥

# linux: clear = lambda: os.system('clear')

import os
import random
def clear(): return os.system('cls')


class card:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        self.state = 0
        self.found = 0


class classicCard(card):
    def __init__(self, x, y, value):
        card.__init__(self, x, y, value)

    def cardIdentification(self, tab_id):
        cards = ["A♠", "7♠", "8♠", "9♠", "10♠", "J♠", "Q♠", "K♠", "A♦", "7♦", "8♦", "9♦", "10♦", "J♦", "Q♦",
                 "K♦", "A♣", "7♣", "8♣", "9♣", "10♣", "J♣", "Q♣", "K♣", "A♥", "7♥", "8♥", "9♥", "10♥", "♥J", "Q♥", "K♥"]
        return cards


def createBoard(nbr_card):
    final_size = []
    size = nbr_card ** 0.5
    size_int = int(size)
    if size > size_int:
        size_int += 1
    final_size.append(size_int)
    if size_int * (size_int - 1) < nbr_card:
        final_size.append(size_int)
    else:
        final_size.append(size_int - 1)
    return final_size


def createCards(nbr_card):
    board = createBoard(nbr_card)
    # print("board size", board[0], "x", board[1])
    x = 0
    y = 0
    counter = 0
    creation = []
    occurrence = []
    cards = []
    for _ in range(0, nbr_card):
        creation.append(0)
    for _ in range(0, int(nbr_card / 2)):
        occurrence.append(0)

    for y in range(0, board[1]):
        for x in range(0, board[0]):
            flag = 1
            while flag == 1:
                value = random.randint(1, nbr_card / 2)
                flag2 = 1
                for _ in range(0, len(creation)):
                    if occurrence[value - 1] < 2 and flag2 == 1:
                        occurrence[value - 1] += 1
                        flag2 = 0
                        flag = 0

            creation[counter] = value
            cards.append(card(x, y, value))
            counter += 1
            if counter == nbr_card:
                break
    return cards


def turnCard(selection, cards):
    length = len(cards)
    for i in range(0, length):
        if cards[i].x == int(selection[1]) - 1 and cards[i].y == int(ord(selection[0]) - 97):
            cards[i].state = 1
            card_ = i
    displayBoard(length, cards)
    print(cards[card_].value)
    return cards[card_].value

def reTurnCard(selection, cards):
    lenght = len(cards)
    for i in range(0, lenght):
        if cards[i].x == int(selection[1]) - 1 and cards[i].y == int(ord(selection[0]) - 97):
            cards[i].state = 0
    displayBoard(lenght, cards)
        

def cardFound(value, cards):
    length = len(cards)
    for i in range(0, length):
        if cards[i].value == value:
            cards[i].found = 1

def isGameWin(cards):
    length = len(cards)
    counter = 0
    for i in range(0, length):
        if cards[i].found == 1:
            counter += 1
    if counter == length:
        return 1
    else:
        return 0


def displayBoard(nbr_card, cards):
    clear()
    counter = 0
    board = createBoard(nbr_card)
    line = []
    for _ in range(0, board[1] + 1):
        line.append("")

    line[0] += "   "
    for i in range(1, board[0] + 1):
        if nbr_card > 199:
            if i > 9:
                line[0] += "  " + str(i)
            else:
                line[0] += "   " + str(i)

        elif nbr_card > 19:
            if i > 9:
                line[0] += " " + str(i)
            else:
                line[0] += "  " + str(i)
        else:
            line[0] += " " + str(i)

    for i in range(1, board[1] + 1):
        line[i] += "  " + chr(96 + i)
        for _ in range(0, board[0]):
            if counter < nbr_card:
                if nbr_card > 199:
                    if cards[counter].value > 99:
                        if cards[counter].state == 1 or cards[counter].found == 1:
                            line[i] += " " + str(cards[counter].value)
                        else:
                            line[i] += "   #"
                    elif cards[counter].value > 9:
                        if cards[counter].state == 1 or cards[counter].found == 1:
                            line[i] += "  " + str(cards[counter].value)
                        else:
                            line[i] += "   #"
                    else:
                        if cards[counter].state == 1 or cards[counter].found == 1:
                            line[i] += "   " + str(cards[counter].value)
                        else:
                            line[i] += "   #"

                elif nbr_card > 19:
                    if cards[counter].value > 9:
                        if cards[counter].state == 1 or cards[counter].found == 1:
                            line[i] += " " + str(cards[counter].value)
                        else:
                            line[i] += "  #"
                    else:
                        if cards[counter].state == 1 or cards[counter].found == 1:
                            line[i] += "  " + str(cards[counter].value)
                        else:
                            line[i] += "  #"
                else:
                    if cards[counter].state == 1 or cards[counter].found == 1:
                        line[i] += " " + str(cards[counter].value)
                    else:
                        line[i] += " #"
            counter += 1
    for i in range(0, board[1] + 1):
        print(line[i])


while True:
    clear()
    mode = int(input(
        "Memory par Maxence Guinard\n\n1. Classique 32 cartes\n2. Partie personnalisée\n3. Quitter\n\nSélectionner le mode de jeu: "))
    # mode à 32 cartes
    if mode == 1:
        print("Test")

        end = input(
            "Félicitation, vous avez gagné en x coups.\nEntrez une valeur pour revenir au menu principal: ")
    # mode à 2n cartes
    elif mode == 2:
        error = 1
        while error == 1:
            clear()
            nbr_card = int(
                input("Entrez le nombre de cartes compris entre 4 et 676: "))
            nbr_card_even = nbr_card % 2
            if nbr_card < 4 or nbr_card_even == 1 or nbr_card > 676:
                error = 1
            else:
                error = 0

        cards = createCards(nbr_card)
        win = 0
        displayBoard(nbr_card, cards)
        entry = 0
        counter_game = 0
        while win == 0:
            selection1 = str(
                input("Selectionner la carte à retourner: "))
            card1 = turnCard(selection1, cards)
            selection2 = str(
                input("Selectionner la seconde carte à retourner: "))
            card2 = turnCard(selection2, cards)
            if card1 == card2:
                cardFound(card1, cards)
                win = isGameWin(cards)
            else:
                o = input("\n\nAppuyer sur entrée pour continuer... ")
                reTurnCard(selection1, cards)
                reTurnCard(selection2, cards)
                
            counter_game += 1

        end = input(
            "Félicitation, vous avez gagné en " + str(counter_game) + " coups.\n\nAppuyer sur entrée pour revenir au menu principal... ")

    # quitter le jeu
    elif mode == 3:
        clear()
        break
