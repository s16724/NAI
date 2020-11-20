# Link : https://pl.wikipedia.org/wiki/Oczko_(gra_karciana)
# Autorzy : Dominika Stryjewska , Jan Rygulski
from easyAI import TwoPlayersGame, Human_Player, AI_Player, Negamax
import random


class BlackJack(TwoPlayersGame):

    def __init__(self, players):
        self.players = players
        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'W', 'Q', 'K', 'A'] * 4
        self.nplayer =1  #random.randrange(1, 3)
        self.humanTotal = 0
        self.aiTotal = 0
        self.aiQuit = False
        self.humanQuit = False
        random.shuffle(self.deck)

    def take_card(self, total):
        card = self.deck[0]
        self.deck = self.deck[1:]
        if type(card) == int:
            total = card
        if card == 'W':
            total = 2
        if card == 'Q':
            total = 3
        if card == 'K':
            total = 4
        if card == 'A':
            total = 11
        return total

    def possible_moves(self):
        if self.nplayer == 2:
            if self.aiTotal >= 18:
                return ['s']
            elif self.aiTotal <= self.humanTotal:
                return ['h']
            else:
                return ['s']
        else:
            return ['h', 's']

    def make_move(self, move):

        if move == 's' and self.nplayer == 1:
            self.humanQuit = True
        if move == 's' and self.nplayer == 2:
            self.aiQuit = True
        if move == 'h' and self.nplayer == 1:
            self.humanTotal += self.take_card(self.humanTotal)
        if move == 'h' and self.nplayer == 2:
            self.aiTotal += self.take_card(self.aiTotal)

    def scoring(self):
        return 100 if self.win() else 0

    def is_over(self):
        if self.aiTotal >= 21 or self.humanTotal >= 21 or \
                self.aiQuit == True and self.humanQuit == True:
            return True

    def win(self):
        return self.humanTotal < self.aiTotal <= 21

    def scoring(self):
        return 100 if self.win() else 0  # For the AI

    def show(self):

        print("Press (h)it or (s)tay ")
        print("wynik dla ai = " + str(self.aiTotal))
        print("wynik dla human = " + str(self.humanTotal))


ai = Negamax(13)
game = BlackJack([Human_Player(), AI_Player(ai)])
history = game.play()
