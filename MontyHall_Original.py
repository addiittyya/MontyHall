import random
from colorama import Fore, Style

def monty_hall_simulation():
    # Get the number of iterations from the user
    iterations = int(input("Enter the number of iterations you want to run: "))
    wins = 0
    
    for i in range(iterations):
        # Randomly place the car behind one of the doors
        doors = ['goat', 'goat', 'car']
        random.shuffle(doors)
        
        # Randomly select a door for the user
        user_choice = random.randint(0, 2)
        
        # Host opens a door that has a goat and is not the user's choice
        possible_doors = [i for i in range(3) if i != user_choice and doors[i] == 'goat']
        host_choice = random.choice(possible_doors)
        
        # Automatically switch to the remaining door
        new_choice = [i for i in range(3) if i != user_choice and i != host_choice][0]
        
        # Display the results of this iteration
        print(f"\nIteration {i + 1}:")
        print(f"Doors: {doors}")
        print(f"User initially selected door {user_choice + 1}")
        print(f"Host opened door {host_choice + 1} which has a goat.")
        print(f"User switched to door {new_choice + 1}.")
        
        # Check if the user's final choice has the car
        if doors[new_choice] == 'car':
            print("Result: User won the car!")
            wins += 1
        else:
            print("Result: User won a goat.")
    
    # Print the result
    print(f"\n{Style.BRIGHT}Number of games: {Fore.BLUE}{iterations}")
    print(f"{Style.RESET_ALL}{Style.BRIGHT}Number of times you won the Car: {Fore.GREEN}{wins}")
    
    # Calculate Win Percentage
    per=float(wins)*(100.0/iterations)
    per=round(per,2)
    print(f"{Style.RESET_ALL}{Style.BRIGHT}Win Percentage: {Fore.GREEN}{per} %{Style.RESET_ALL}")

if __name__ == "__main__":
    monty_hall_simulation()
