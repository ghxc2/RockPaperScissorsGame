class BestMoveChooser:
    """
    Class for determining the best counter for a given choice in rock paper scissors
    """
    @staticmethod
    def best_move(choice):
        """
        Determines the best choice to counter a move in Rock Paper Scissors
        :param choice: Opponent Selected Choice
        :return: Best Counter Choice
        """
        if choice == 'r':
            return 'p'
        if choice == 'p':
            return 's'
        if choice == 's':
            return 'r'
