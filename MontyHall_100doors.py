import random
from colorama import Fore, Style

def monty_hall_simulation_switch_always(num_doors=100, iterations=25000):
    switch_wins = 0
    
    for _ in range(iterations):
        # Randomly place the car behind one door
        car_door = random.randint(0, num_doors - 1)
        
        # Player randomly picks one door
        player_choice = random.randint(0, num_doors - 1)
        
        # Host opens all other doors except one goat door and the player's choice
        remaining_doors = list(range(num_doors))
        remaining_doors.remove(player_choice)
        
        # Host can't open the car door, so remove all but one goat door
        if player_choice != car_door:
            remaining_doors.remove(car_door)  # Host doesn't open the car door
        
        # Player always switches to the only remaining unopened door
        # The new choice is now the car door if they initially picked a goat door
        if player_choice != car_door:
            switch_wins += 1  # Player wins by switching
    
    # Calculate the switch win percentage
    switch_win_percentage = (switch_wins / iterations) * 100
    
    # Display results
    print("\n")
    print(f"{Style.BRIGHT}After {Fore.BLUE}{iterations}{Style.RESET_ALL}{Style.BRIGHT} iterations with {Fore.GREEN}{num_doors}{Style.RESET_ALL}{Style.BRIGHT} doors:")
    print(f"Switch Wins: {Fore.GREEN}{switch_wins} ({switch_win_percentage:.2f}%){Style.RESET_ALL}")
    print("\n")

# Run the simulation with 100 doors and always switching
monty_hall_simulation_switch_always(num_doors=100, iterations=25000)
