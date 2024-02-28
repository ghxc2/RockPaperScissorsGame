"""
RockPaperScissorsGame.py

Contains Main game for RockPaperScissors
If ran, will initiate a game of TicTacToe
"""
import Player


class RockPaperScissorsGame:
    """
    RockPaperScissorsGame Class

    Handler class for running a game of TicTacToe
    Contains all necessary functions to play a game successfully
    Assumes one HumanPlayer followed by one AIPlayer
    """
    def __init__(self):
        """
        Initiates wins, losses, and draws statistics to 0
        Initiates possible game choices
        Initiates game Players
        Initiates possible winning operations
        """
        self._wins = 0
        self._losses = 0
        self._draws = 0
        self._choices = ['r', 'p', 's']
        self._players = [Player.HumanPlayer(), Player.AIPlayer()]
        self._winning_combinations = {
            ('r', 's'): 1,
            ('s', 'p'): 1,
            ('p', 'r'): 1,
            ('s', 'r'): 2,
            ('p', 's'): 2,
            ('r', 'p'): 2
        }

    def choose(self, player):
        """
        Retrieves selected player's move
        :param player: Player to retrieve move for
        :return: Player's choice
        """
        # Finds other Player
        other_player = (player + 1) % 2

        # Determines other player
        # using other player's passed moves and game choices
        return self._players[player].make_move(self._players[other_player].past_moves, self._choices)

    def determine_win(self, first_choice, second_choice):
        """
        Determines Winner based on possible winning combinations initialized at start
        If both players have chosen the same, will return 0 indicating a tie
        :param first_choice: First Player's Choice
        :param second_choice: Second Player's Choice
        :return: 0 if Tie, 1 If Player 1 Wins, 2 if Player 2 Wins
        """
        if first_choice == second_choice:
            return 0
        return self._winning_combinations[(first_choice, second_choice)]

    def play(self):
        """
        Runs a single turn of Rock Paper Scissors
        Determines First Player's move, then Second Player's
        Once both moves are determined, checks to see who wins
        If 'q' is selected as a move for the first player, the game will return -1
        This is used to know the player wishes to end the game
        :return: -1 if Game is Ending, 0 if Game is continuing
        """

        # Determine's first user's choice
        first_choice = self.choose(0)

        # Determines if first player wishes to quit
        if first_choice == 'q':
            return -1

        # Determine's second user's choice
        second_choice = self.choose(1)

        # Determine Winner
        winner = self.determine_win(first_choice, second_choice)

        # Prints Both Player's Choices
        print("Player 1: ", first_choice, " Player 2: ", second_choice)

        # Prints Result based on Player 1
        if winner == 0:
            self._draws += 1
            print("Draw!")
        elif winner == 1:
            self._wins += 1
            print("Win!")
        else:
            self._losses += 1
            print("Loss!")

        return 0

    def print_results(self):
        """
        Prints Game Results
        Wins, Losses, Draws
        """
        print("Wins:", self._wins)
        print("Losses:", self._losses)
        print("Draws:", self._draws)


if __name__ == "__main__":
    game = RockPaperScissorsGame()
    while True:
        result = game.play()
        if result == -1:
            break

    game.print_results()
