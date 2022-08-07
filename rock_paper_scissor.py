

# Import section
import random

print('***** Welcome to Rock Paper Scissor game *****\n')

def play():
    print('For rock, press r below')
    print('For paper, press p below')
    print('For scissor, press s below')
    user = input('User = ').lower()
    computer = random.choice(['r', 'p', 's'])
    print(f'Computer = {computer}')

    if user == computer:
        return 'Match tie'

    if win_check(user, computer):
        return 'You won!'

    return 'You lost!'

def win_check(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


print(play())