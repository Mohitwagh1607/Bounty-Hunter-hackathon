print("--- Bounty Hunter Registration ---")
name = input("Enter your Hunter Name: ")
bounties_collected = input("How many bounties have you collected? ")

try:
    # This tries to convert their answer into a math number
    bounties_num = int(bounties_collected)
    
    if bounties_num >= 10:
        print(f"Status: Elite Hunter {name}! You are ready for the hackathon.")
    else:
        print(f"Status: Rookie Hunter {name}. Time to collect more bounties!")
        
except ValueError:
    # If they type words instead of numbers, this stops the program from crashing
    print("System Error: Please restart and enter a valid number.")