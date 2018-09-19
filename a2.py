#!/usr/bin/env python3
"""
Assignment 2 - UNO++
CSSE1001/7030
Semester 2, 2018
"""

import random

__author__ = "Your name & student number here"

# Write your classes here


class Player:
    def __init__(self, name):
        self.name = name
        self.deck = Deck()

    def get_name(self):
        return self.name

    def get_deck(self):
        return self.deck

    def is_playable(self):
        # 判断玩家和机器的标志，是玩家则返回True，否则则返回False
        raise NotImplementedError("is_playable to be implemented by subclasses")

    def has_won(self):
        # 是否获胜，deck为空则为获胜
        cards = self.deck.get_cards()

        if len(cards) == 0:
            return True
        else:
            return False

    def pick_card(self, putdown_pile):
        """ 出牌 """
        raise NotImplementedError("pick_card to be implemented by subclasses")


class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def is_playable(self):
        """ 是玩家，返回True，否则返回False """
        return True

    def pick_card(self, putdown_pile):
        """ 人出牌则返回None """
        return None


class ComputerPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def is_playable(self):
        """ 是玩家，返回True，否则返回False """
        return False

    def pick_card(self, putdown_pile):
        # 电脑出牌根据出牌堆中的顶牌出牌，出牌必须和顶牌花色或者数字相同或者黑色特别牌
        match_card = None
        top_card = putdown_pile.top()
        if top_card:
            current_cards = self.deck.get_cards()
            for card in current_cards:
                if card.matches(top_card):
                    match_card = card
                    self.deck.get_cards().remove(match_card)
                    break

        return match_card


class Deck:
    def __init__(self, cards=None):
        if cards is None:
            self.cards = []
        else:
            self.cards = cards

    def get_cards(self):
        return self.cards

    def get_amount(self):
        return len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def pick(self, amount=1):
        """ 从出牌堆挑选几张牌,将挑选的牌返回 """

        pick_cards = []
        for _ in range(amount):
            pick_cards.append(self.cards.pop())

        return pick_cards

    def add_cards(self, cards):
        if isinstance(cards, list):
            self.cards.extend(cards)
        else:
            self.cards.append(cards)

    def top(self):
        if len(self.cards) > 0:
            return self.cards[-1]
        else:
            return None


class Card:
    def __init__(self, number, colour):
        self.number = number
        self.colour = colour

    def get_number(self):
        return self.number

    def get_colour(self):
        return self.colour

    def set_number(self, number: int):
        self.number = number

    def set_colour(self, colour):
        self.colour = colour

    def get_pickup_amount(self):
        return 1

    def matches(self, card):
        print(self, card)
        if card:
            if self.__class__ == Pickup4Card:
                return True

            if card.__class__ == Card and self.__class__ == Card:
                if card.colour == self.colour or card.number == self.number:
                    return True
            else:
                if card.colour == self.colour or card.__class__ == self.__class__:
                    return True

        return False

    def play(self, player, game):
        pass

    def __str__(self):
        msg = 'Card(%d, %s)' % (self.number, self.colour)
        return msg

    def __repr__(self):
        return self.__str__()


class SkipCard(Card):
    def __init__(self, number, colour):
        super().__init__(number, colour)

    def play(self, player, game):
        game.skip()

    def __str__(self):
        msg = 'SkipCard(%d, %s)' % (self.number, self.colour)
        return msg

    def __repr__(self):
        return self.__str__()


class ReverseCard(Card):
    def __init__(self, number, colour):
        super().__init__(number, colour)

    def play(self, player, game):
        game.reverse()

    def __str__(self):
        msg = 'ReverseCard(%d, %s)' % (self.number, self.colour)
        return msg

    def __repr__(self):
        return self.__str__()


class Pickup2Card(Card):
    def __init__(self, number, colour):
        super().__init__(number, colour)

    def get_pickup_amount(self):
        return 2

    def play(self, player, game):
        pick_number = self.get_pickup_amount()
        game.next_player().get_deck().add_cards(game.pickup_pile.pick(pick_number))

    def __str__(self):
        msg = 'Pickup2Card(%d, %s)' % (self.number, self.colour)
        return msg

    def __repr__(self):
        return self.__str__()


class Pickup4Card(Card):
    def __init__(self, number, colour):
        super().__init__(number, colour)

    def get_pickup_amount(self):
        return 4

    def play(self, player, game):
        pick_number = self.get_pickup_amount()
        game.next_player().get_deck().add_cards(game.pickup_pile.pick(pick_number))

    def __str__(self):
        msg = 'Pickup4Card(%d, %s)' % (self.number, self.colour)
        return msg

    def __repr__(self):
        return self.__str__()


def main():
    print("Please run gui.py instead")


if __name__ == "__main__":
    main()
