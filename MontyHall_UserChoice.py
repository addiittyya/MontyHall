import random

def setup_doors():
    # Randomly assign car and goats to doors
    doors = ['goat', 'goat', 'car']
    random.shuffle(doors)
    return doors

def play_game():
    wins = 0

    for i in range(10):
        print(f"\nRound {i+1}:")
        doors = setup_doors()
        
        # User selects a door
        user_choice = int(input("Select a door (1, 2, or 3): ")) - 1

        # Host opens a door that has a goat and isn't the user's choice
        available_doors = [i for i in range(3) if i != user_choice and doors[i] == 'goat']
        opened_door = random.choice(available_doors)
        print(f"Host opens door {opened_door + 1} which has a goat.")

        # User chooses whether to switch or stay
        switch = input("Do you want to switch doors? (yes/no): ").lower()

        if switch == 'yes':
            user_choice = [i for i in range(3) if i != user_choice and i != opened_door][0]

        # Reveal if the user won a car or goat
        if doors[user_choice] == 'car':
            print("Congratulations! You won a car!")
            wins += 1
        else:
            print("You won a goat. Better luck next time!")

    print(f"\nGame Over! You won the car {wins} out of 10 times.")

if __name__ == "__main__":
    play_game()
