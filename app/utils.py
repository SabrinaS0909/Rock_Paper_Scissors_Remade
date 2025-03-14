#for reusable logic and functions; define them here

import random

def get_animal_choices(data):
    player_action = data["animal"]
    possible_actions = ["bee", "bun", "corvid", "cat", "wolf", "human"]
    computer_action = random.choice(possible_actions)
    return player_action, computer_action