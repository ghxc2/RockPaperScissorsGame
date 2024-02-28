"""
Algorithm.py

Contains Algorithm Classes to select best move for Player in Rock Paper Scissors
Uses Abstract Class Algorithm as interface for implementation
"""
# Import necessary modules
import random
from abc import ABC, abstractmethod
from collections import Counter

# Import custom module
from BestMoveChooser import BestMoveChooser


class Algorithm(ABC):
    """
    Abstract Algorithm Class
    Contains choose_move() function for deciding best move to use
    for current turn in rock paper scissors
    """
    @staticmethod
    @abstractmethod
    def choose_move(past_moves, choices):
        """
        Method for Choosing next move
        :param past_moves: List of Opponent's previous moves
        :param choices: List of all available choices
        :return: Choice for Player
        """
        pass


class RandomAlgorithm(Algorithm):
    """
    RandomAlgorithm Algorithm Class

    Randomly chooses one of the available choices as the next move
    when choose_move() is called
    """
    @staticmethod
    def choose_move(past_moves, choices):
        """
        Selects random move for next turn
        Uses no logic, just Randomness
        :param past_moves: List of Opponent's previous moves
        :param choices: List of all available choices
        :return: Randomly Selected Choice
        """
        return random.choice(choices)


class PreviousCounterAlgorithm(Algorithm):
    """
    PreviousCounterAlgorithm Algorithm Class

    Looks at previous move from opponent when deciding next best turn for user to use
    when choose_move() is called
    """
    @staticmethod
    def choose_move(past_moves, choices):
        """
        Selects best move for next turn
        If opponent's past moves are empty, will use RandomAlgorithm algorithm
        Else will look to opponent's latest move and will attempt to counter it
        :param past_moves: List of Opponent's previous moves
        :param choices: List of all available choices
        :return: Best Counter to Opponent's Last Turn
        """
        # If no past moves, choose randomly
        if len(past_moves) == 0:
            return RandomAlgorithm.choose_move(past_moves, choices)
        # Otherwise, choose best move based on past move
        else:
            return BestMoveChooser.best_move(past_moves[-1])


class MostCommonCounterAlgorithm(Algorithm, BestMoveChooser):
    """
    MostCommonCounterAlgorithm Algorithm Class

    Looks all previous moves from opponent when deciding next best turn for use to use
    and then selects the most common outcome and attempts to counter
    when choose_move() is called
    """
    @staticmethod
    def choose_move(past_moves, choices):
        """
        Selects the best move for next turn
        If opponent's past moves are empty, will use RandomAlgorithm algorithm
        Else, will look at all of opponent's last moves, and will attempt to counter
        the most common result found
        :param past_moves: List of Opponent's Previous Moves
        :param choices: List of all available choices
        :return: Best Counter to Opponent's Most Common Choice
        """
        if len(past_moves) == 0:
            return RandomAlgorithm().choose_move(past_moves, choices)
        else:
            return BestMoveChooser().best_move(Counter(past_moves).most_common(1)[0][0])
