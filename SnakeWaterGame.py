import random

def game_win(computer, player):
    if computer == player:
        return None
    elif computer == 's':
        if player == 'w':
            return False
        elif player == 'g':
            return True
    elif computer == 'w':
        if player == 'g':
            return False
        elif player == 's':
            return True
    elif computer == 'g':
        if player == 's':
            return False
        elif player == 'w':
            return True

print("Welcome to Snake-Water-Gun!")
print("Choices: Snake(s), Water(w), Gun(g)")
print("Let's play!")

random_number = random.randint(1, 3)
if random_number == 1:
    computer_choice = 's'
elif random_number == 2:
    computer_choice = 'w'
elif random_number == 3:
    computer_choice = 'g'

player_choice = input("Your Turn: ").lower()

if player_choice not in ['s', 'w', 'g']:
    print("Invalid input! Please select a valid option.")
else:
    result = game_win(computer_choice, player_choice)

    print(f"\nComputer chose: {computer_choice}")
    print(f"You chose: {player_choice}\n")

    if result is None:
        print("It's a tie!")
    elif result:
        print("Congratulations! You win!")
    else:
        print("Sorry, you lose!")
