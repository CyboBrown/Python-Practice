import random

def play():
    user = input("Rock[R], Paper[P], or Scissors[S]: ")
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        return 'It\'s a tie.'
    if is_win(user, computer):
        return 'The user won.'
    return 'The computer won.'

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    else:
        return False

print(play())