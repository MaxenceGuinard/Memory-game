## coding: utf8
import os
import random
# fonction pour clear la console windows
def clear(): return os.system('cls')
# linux: clear = lambda: os.system('clear')


cards32 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# constructeur pour créer les cartes


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

# fonction qui retroune le string contenu en position x dans le tableau


def cardIdentification(nbr):
    cards = ["A♠", "7♠", "8♠", "9♠", "10♠", "J♠", "Q♠", "K♠", "A♦", "7♦", "8♦", "9♦", "10♦", "J♦", "Q♦",
             "K♦", "A♣", "7♣", "8♣", "9♣", "10♣", "J♣", "Q♣", "K♣", "A♥", "7♥", "8♥", "9♥", "10♥", "♥J", "Q♥", "K♥"]
    return cards[nbr]

# fonction pour calculer la taille du repère où les cartes sont contenu. En sortie on obtient un tableau du type [3, 2] qui représente 3 x 2


def createBoard(nbr_card):
    final_size = []
    # on fait la racine carée du nombre de carte pour avoir une premièere référence
    size = nbr_card ** 0.5
    # ensuite on complexifie pour prendre un compte les cas où le nombre de carte n'est pas un carré parfait
    size_int = int(size)
    if size > size_int:
        size_int += 1
    final_size.append(size_int)
    if size_int * (size_int - 1) < nbr_card:
        final_size.append(size_int)
    else:
        final_size.append(size_int - 1)
    return final_size

# fonction  qui permet de créer les cartes


def createCards(nbr_card):
    board = createBoard(nbr_card)
    x = 0
    y = 0
    counter = 0
    creation = []
    occurrence = []
    cards = []
    # ici creation représente les valeurs des cartes créée
    for _ in range(0, nbr_card):
        creation.append(0)
    # ici occurence représente la création d'une double valeur à chaque fois. Pour 32 cartes on a 16 valeurs différentes donc 2 fois chaque 16 valeurs
    for _ in range(0, int(nbr_card / 2)):
        occurrence.append(0)

    # on affecte à chaque coordonnées une veleurs calculée de manière aléatoire
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
            # on place ensuite tout les objets cartes crées dans le tableau cards
            cards.append(card(x, y, value))
            counter += 1
            if counter == nbr_card:
                break
    #  on retroune le tableau cards qu contient toutes les cartes
    return cards


# fonction qui permet de change l'état de la carte 1 = carte visible 0 = carte retrounée fonctionne avec la fonction qui suit pour retrouner une carte
def turnCard(selection, cards):
    length = len(cards)
    for i in range(0, length):
        if cards[i].x == int(selection[1:]) - 1 and cards[i].y == int(ord(selection[0]) - 97):
            cards[i].state = 1
            card_ = i
    displayBoard(length, cards)
    # retourne la valeur de la carte pour ensuite pouvoir comparer si les veleurs sont égales
    return cards[card_].value


def reTurnCard(selection, cards):
    lenght = len(cards)
    for i in range(0, lenght):
        if cards[i].x == int(selection[1:]) - 1 and cards[i].y == int(ord(selection[0]) - 97):
            cards[i].state = 0
    displayBoard(lenght, cards)

# si les deux valeurs correspondent alors on passe la carte en found = 1 pour indiquée qu'elle a été trouvée


def cardFound(value, cards):
    length = len(cards)
    for i in range(0, length):
        if cards[i].value == value:
            cards[i].found = 1

#  permet de regarder si la partie est gagné à chaque tour


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

#  fonction qui permet d'afficher les les cartes avec le repère de manière à ce que toutes les valeurs s'affichent correctement


def displayBoard(nbr_card, cards):
    clear()
    counter = 0
    board = createBoard(nbr_card)
    line = []
    occurrence = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for _ in range(0, board[1] + 1):
        line.append("")

    line[0] += "   "
    # sert à créer la première ligne avec l'axe des abscisse
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

    # permet de créer le reste des lignes pour les afficher par la suite. Tout les cas sont spécifiés pour que l'affichage fonctionne correctement
    for i in range(1, board[1] + 1):
        line[i] += "  " + chr(96 + i)
        for _ in range(0, board[0]):
            if counter < nbr_card:
                #  cas où le nombre de carte > 99 pour avoir toutes les valeurs sur 3 caractères etc ..
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
                    if cards[counter].value > 9 or mode == 1:
                        if cards[counter].state == 1 or cards[counter].found == 1:
                            if mode == 1:
                                if occurrence[cards[counter].value - 1] == 0 and occurrence[cards[counter].value + 15] == 0:
                                    rand = random.randint(1, 2)
                                    if rand == 1:
                                        line[i] += " " + \
                                            cardIdentification(
                                                cards[counter].value - 1)
                                        occurrence[cards[counter].value - 1] = 1
                                    else:
                                        line[i] += " " + \
                                            cardIdentification(
                                                cards[counter].value + 15)
                                        occurrence[cards[counter].value + 15] = 1
                                else:
                                    if occurrence[cards[counter].value - 1] == 1:
                                        line[i] += " " + \
                                            cardIdentification(
                                                cards[counter].value + 15)
                                        occurrence[cards[counter].value + 15] = 1
                                    else:
                                        line[i] += " " + \
                                            cardIdentification(
                                                cards[counter].value - 1)
                                        occurrence[cards[counter].value - 1] = 1

                            else:
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
    # puis à la fin on affiche toutes les lignes
    for i in range(0, board[1] + 1):
        print(line[i])

# fonction pour kancer une partie


def play(nbr_card):
    # création des cartes
    cards = createCards(nbr_card)
    # statut de victoire
    win = 0
    # affichage de la planche de jeu une première fois
    displayBoard(nbr_card, cards)
    # compteur de coup pour gagner
    counter_game = 0
    while win == 0:
        # selection de la premier carte
        selection1 = str(
            input("Selectionner la carte à retourner: "))
        card1 = turnCard(selection1, cards)
        # selection de la deuxième carte
        selection2 = str(
            input("Selectionner la seconde carte à retourner: "))
        card2 = turnCard(selection2, cards)
        # vérification si les cartes font une paire
        if card1 == card2:
            cardFound(card1, cards)
            win = isGameWin(cards)
        # si non alors on retrourne les cartes et laisse le joueur les regarder pour pouvoir les mémoriser
        else:
            o = input("\n\nAppuyer sur entrée pour continuer... ")
            reTurnCard(selection1, cards)
            reTurnCard(selection2, cards)

        counter_game += 1

    end = input(
        "Félicitation, vous avez gagné en " + str(counter_game) + " coups.\n\nAppuyer sur entrée pour revenir au menu principal... ")


while True:
    clear()
    mode = int(input(
        "Memory par Maxence Guinard\n\n1. Classique 32 cartes\n2. Partie personnalisée\n3. Quitter\n\nSélectionner le mode de jeu: "))
    # mode à 32 cartes
    if mode == 1:
        clear()
        nbr_card = 32
        play(nbr_card)

    # mode à 2n cartes
    elif mode == 2:
        error = 1
        while error == 1:
            clear()
            nbr_card = int(
                input("Entrez le nombre de cartes compris entre 4 et 676: "))
            nbr_card_even = nbr_card % 2
            # ici on oblige le joueur à rentre un nombre pair compris entre 4 et 676
            if nbr_card < 4 or nbr_card_even == 1 or nbr_card > 676:
                error = 1
            else:
                error = 0

        play(nbr_card)

    # quitter le jeu
    elif mode == 3:
        clear()
        break
