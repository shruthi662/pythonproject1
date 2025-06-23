import random

def roll_die():
    """Simulates a roll of a single die from the dice cup."""
    # Green: 3 brains, 2 footsteps, 1 shotgun
    # Yellow: 2 brains, 2 footsteps, 2 shotguns
    # Red: 1 brain, 2 footsteps, 3 shotguns

    color = random.choice(['green', 'yellow', 'red'])
    if color == 'green':
        return random.choice(['brain', 'brain', 'brain', 'footsteps', 'footsteps', 'shotgun'])
    elif color == 'yellow':
        return random.choice(['brain', 'brain', 'footsteps', 'footsteps', 'shotgun', 'shotgun'])
    else:
        return random.choice(['brain', 'footsteps', 'footsteps', 'shotgun', 'shotgun', 'shotgun'])

def simple_zombie_bot():
    brains = 0
    shotguns = 0

    while True:
        roll_results = [roll_die() for _ in range(3)]
        print(f"Rolled: {roll_results}")

        for result in roll_results:
            if result == 'brain':
                brains += 1
            elif result == 'shotgun':
                shotguns += 1

        print(f"Brains: {brains}, Shotguns: {shotguns}")

        # Stop if too risky
        if shotguns >= 2:
            print("Too risky! Stopping turn.")
            break

    print(f"Turn ends with {brains} brains.\n")

# Run bot simulation
simple_zombie_bot()
