import random

num_of_choices = 5
chances_used = 0
human = 0
computer = 0
lst = ['r', 'p', 's']
print('Welcome to the Rock, Paper, Scissors Simulator\n')
print(' Rock = r\n Paper = p\n Scissors = s\n quit = quit\n\n')

while num_of_choices > chances_used:
    _input = input('Rock,Paper,Scissors:')
    _random = random.choice(lst)

    if _input == _random:
        print('Wow!! It is a Tie \n')
        print(f'Human guessed - {_input}')
        print(f'Computer guessed - {_random}')
        chances_used = chances_used + 1
        print(f'{chances_used} are done out of{num_of_choices}\n')

    elif _input == 'r' and _random == 'p':
        computer = computer + 1
        human = human
        print('Oops.. Computer got away with a point \n')
        print(f'Human guessed - {_input}')
        print(f'Computer guessed - {_random}')
        print(f'Human points are - {human}')
        print(f'Computer points are - {computer}')
        chances_used = chances_used + 1
        print(f'{chances_used} are done out of  {num_of_choices}\n')

    elif _input == 'r' and _random == 's':
        computer = computer
        human = human + 1
        print('Yay.. Human got a point \n')
        print(f'Human guessed - {_input}')
        print(f'Computer guessed - {_random}')
        print(f'Human points are - {human}')
        print(f'Computer points are - {computer}')
        chances_used = chances_used + 1
        print(f'{chances_used} are done out of  {num_of_choices}\n')
        
    elif _input == 'p' and _random == 'r':
        computer = computer
        human = human + 1
        print('Yay.. Human got a point \n')
        print(f'Human guessed - {_input}')
        print(f'Computer guessed - {_random}')
        print(f'Human points are - {human}')
        print(f'Computer points are - {computer}')
        chances_used = chances_used + 1
        print(f'{chances_used} are done out of  {num_of_choices}\n')

    elif _input == 'p' and _random == 's':
        computer = computer + 1
        human = human
        print('Oops.. Computer got away with a point \n')
        print(f'Human guessed - {_input}')
        print(f'Computer guessed - {_random}')
        print(f'Human points are - {human}')
        print(f'Computer points are - {computer}')
        chances_used = chances_used + 1
        print(f'{chances_used} are done out of  {num_of_choices}\n')

    elif _input == 's' and _random == 'r':
        computer = computer + 1
        human = human
        print('Oops.. Computer got away with a point \n')
        print(f'Human guessed - {_input}')
        print(f'Computer guessed - {_random}')
        print(f'Human points are - {human}')
        print(f'Computer points are - {computer}')
        chances_used = chances_used + 1
        print(f'{chances_used} are done out of  {num_of_choices}\n')

    elif _input == 's' and _random == 'p':
        computer = computer
        human = human + 1
        print('Yay.. Human got a point \n')
        print(f'Human guessed - {_input}')
        print(f'Computer guessed - {_random}')
        print(f'Human points are - {human}')
        print(f'Computer points are - {computer}')
        chances_used = chances_used + 1
        print(f'{chances_used} are done out of  {num_of_choices}\n')

    elif _input == 'quit':
        break

    else:
        print('Error:: Enter properly again')

if computer > human:
    print('Oops.. Computer has won\n')
    print(f'Human points are - {human}')
    print(f'Computer points are - {computer}')

elif human < computer:
    print('Yay! You have won\n')
    print(f'Human points are - {human}')
    print(f'Computer points are - {computer}')
