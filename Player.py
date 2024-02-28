"""
Player.py

Contains Player Classes to control players during a game of Rock Paper Scissors
Uses Abstract Class Player as interface for implementation
"""
import random
from abc import ABC, abstractmethod

import Algorithm


class Player(ABC):
    """
    Abstract Player Class
    Contains make_move() function for retrieving the next move for the player to take
    Contains __init__() intended for setting class variable self.past_moves = []
    """
    @abstractmethod
    def __init__(self):
        """
        Intended for setting self.past_moves = []
        """
        pass

    @abstractmethod
    def make_move(self, opponent_past_moves, choices):
        """
        Retrieves next move for the player
        :param opponent_past_moves: List of Opponent's previous moves
        :param choices: List of all available choices
        :return: Player move Choice
        """
        pass


class HumanPlayer(Player):
    """
    HumanPlayer Player Class

    Actual User CLI Based Player
    """
    def __init__(self):
        self.past_moves = []

    def make_move(self, opponent_past_moves, choices):
        """
        Asks for player's move in command line, looping until valid response found
        Once found, returns move
        :param opponent_past_moves: List of Opponent's previous moves
        :param choices: List of all available choices
        :return: Player move Choice
        """
        while True:
            choice = input("Rock Paper Scissor? q to Quit[r, p, s, q]")
            if choice not in choices and choice != 'q':
                continue
            else:
                return choice


class AIPlayer(Player):
    """
    AIPlayer Player Class

    Computer Player class that is Algorithm based
    """
    def __init__(self):
        self.past_moves = []

    def make_move(self, opponenet_past_moves, choices):
        """
        Selects random Algorithm available, then uses algorithm to determine best move
        :param opponenet_past_moves: List of Opponent's previous moves
        :param choices: List of all available choices
        :return: Player move Choice
        """
        algorithm = random.choice([Algorithm.RandomAlgorithm, Algorithm.PreviousCounterAlgorithm,
                                   Algorithm.MostCommonCounterAlgorithm])
        return algorithm.choose_move(opponenet_past_moves, choices)
