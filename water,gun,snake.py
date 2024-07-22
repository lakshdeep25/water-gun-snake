import random

def get_computer_choice():
    return random.choice(['Water','Gun','Snake'])

def get_user_choice():
    choices = ['Water','Gun','Snake']
    user_choice = input("Enter your choice(Water/Gun/Snake): ").capitalize()
    while user_choice  not in choices:
        print("Invalid choice. Please Choice Water/Gun/Snake.")
        user_choice = input("Enter your choice Water/Gun/Snake.").capitalize()
        return user_choice

def determine_winner(user_choice,computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    
    elif (user_choice == 'Water' and computer_choice == 'Gun') or \
         (user_choice == 'Gun' and computer_choice == 'Snake') or \
         (user_choice == 'Snake' and computer_choice == 'Water'):
        return "you win!"
    else:
        return "Computer wins!"
    
def play_game():
    print("Welcome to 'Water','Gun','Snake'!")
    while True:
            user_choice = get_user_choice()
            computer_choice = get_computer_choice()
            print(f"\nComputer chose: {computer_choice}")
            print(determine_winner(user_choice,computer_choice))
            result = determine_winner(user_choice,computer_choice)
            print(f"\n{result}\n")

            play_again = input ("do you want play again? (yes/no): ").lower()
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    play_game()





