import random
from collections import Counter

choices = ['r', 'p', 's']
wins = 0
draws = 0
losses = 0
past_moves = []
while True:
    choice = input("Rock Paper Scissor? q to Quit[r, p, s, q]")
    if choice not in choices and choice != 'q':
        continue

    if choice == 'q':
        break

    alg_choice = random.randint(1, 3)

    ai_choice = ""

    if alg_choice == 1:
        ai_choice = random.choice(choices)
    if alg_choice == 2:
        if len(past_moves) == 0:
            ai_choice = random.choice(choices)
        else:
            last_choice = past_moves[-1]
            if last_choice == 'r':
                ai_choice = 'p'
            if last_choice == 'p':
                ai_choice = 's'
            if last_choice == 's':
                ai_choice = 'r'
    if alg_choice == 3:
        if len(past_moves) == 0:
            ai_choice = random.choice(choices)
        else:
            most_common = Counter(past_moves).most_common(1)[0][0]
            if most_common == 'r':
                ai_choice = 'p'
            if most_common == 'p':
                ai_choice = 's'
            if most_common == 's':
                ai_choice = 'r'

    lose = tie = win = False
    if choice == 'r':
        if ai_choice == 'p':
            lose = True
        elif ai_choice == 'S':
            win = True
        else:
            tie = True

    if choice == 'p':
        if ai_choice == 's':
            lose = True
        elif ai_choice == 'r':
            win = True
        else:
            tie = True

    if choice == 's':
        if ai_choice == 'r':
            lose = True
        elif ai_choice == 'p':
            win = True
        else:
            tie = True

    past_moves.append(choice)

    if lose:
        print("You loose!")
        losses += 1
    elif win:
        print("You win!")
        wins += 1
    elif tie:
        print("Tie")
        draws += 1

print("Wins:", wins)
print("Losses:", losses)
print("Draws:", draws)
