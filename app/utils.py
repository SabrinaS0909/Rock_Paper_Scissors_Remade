#for reusable logic and functions; define them here

import random

def get_animal_choices(data):
    player_action = data["animal"]
    possible_actions = ["bee", "bun", "corvid", "cat", "wolf", "human"]
    computer_action = random.choice(possible_actions)
    return player_action, computer_action

def random_button():
    possible_buttons = ["Let's go!", "It's on!", "Cower before me!", "You're too weak!", "I'm scared!"]
    button_dialogue = random.choice(possible_buttons)
    return button_dialogue

def outcome():
    outcome = "Outcome"
    return outcome

"""
def outcome_possibilities(player_action, computer_action):
    print("outcome function is working")
    if player_action == "bee":
        if computer_action == "bee":
            outcome_dialogue = "Tie"
        elif computer_action == "bun":
            outcome_dialogue = "In a battle for territory where the prize is land full of flowers which are great for hiding from predators, as wells as siphoning nectar, the bun calls in reinforcements and quickly there are too many to drive off with stings and pheramones. The buns claim the meadow of flowers. You lose!\n"
        elif computer_action == "corvid":
            outcome_dialogue = "Corvid eats the bee. You lose!\n"
        elif computer_action == "cat":
            outcome_dialogue = "Despite a well calculated swat, the bee outmanuervers the cat and manages to sting it right in the offending paw, sending the cat running. You win!\n"
        elif computer_action == "wolf":
            outcome_dialogue = "The wolf gets stung in the muzz and looks silly the rest of the day. You win!\n"
        else:
            outcome_dialogue = "wild card"
    elif player_action == "bun":
        if computer_action == "bee":
            outcome_dialogue = "In a battle for territory where the prize is land full of flowers which are great for hiding from predators, as wells as siphoning nectar, the bun calls in reinforcements and quickly there are too many to drive off with stings and pheramones. The buns claim the meadow of flowers. You lose!\n"
        elif computer_action == "bun":
            outcome_dialogue = "Tie"
        elif computer_action == "corvid":
            outcome_dialogue = "Corvid eats the bee. You lose!\n"
        elif computer_action == "cat":
            outcome_dialogue = "Despite a well calculated swat, the bee outmanuervers the cat and manages to sting it right in the offending paw, sending the cat running. You win!\n"
        elif computer_action == "wolf":
            outcome_dialogue = "The wolf gets stung in the muzz and looks silly the rest of the day. You win!\n"
        else:
            outcome_dialogue = "wild card"
    elif player_action == "corvid":
        if computer_action == "bee":
            outcome_dialogue = "In a battle for territory where the prize is land full of flowers which are great for hiding from predators, as wells as siphoning nectar, the bun calls in reinforcements and quickly there are too many to drive off with stings and pheramones. The buns claim the meadow of flowers. You lose!\n"
        elif computer_action == "bun":
            outcome_dialogue = "Corvid eats the bee. You lose!\n"
        elif computer_action == "corvid":
            outcome_dialogue = "Tie"
        elif computer_action == "cat":
            outcome_dialogue = "Despite a well calculated swat, the bee outmanuervers the cat and manages to sting it right in the offending paw, sending the cat running. You win!\n"
        elif computer_action == "wolf":
            outcome_dialogue = "The wolf gets stung in the muzz and looks silly the rest of the day. You win!\n"
        else:
            outcome_dialogue = "wild card"
    elif player_action == "cat":
        if computer_action == "bee":
            outcome_dialogue = "In a battle for territory where the prize is land full of flowers which are great for hiding from predators, as wells as siphoning nectar, the bun calls in reinforcements and quickly there are too many to drive off with stings and pheramones. The buns claim the meadow of flowers. You lose!\n"
        elif computer_action == "bun":
            outcome_dialogue = "Corvid eats the bee. You lose!\n"
        elif computer_action == "corvid":
            outcome_dialogue = "Despite a well calculated swat, the bee outmanuervers the cat and manages to sting it right in the offending paw, sending the cat running. You win!\n"
        elif computer_action == "cat":
            outcome_dialogue = "Tie"
        elif computer_action == "wolf":
            outcome_dialogue = "The wolf gets stung in the muzz and looks silly the rest of the day. You win!\n"
        else:
            outcome_dialogue = "wild card"
    elif player_action == "wolf":
        if computer_action == "bee":
            outcome_dialogue = "In a battle for territory where the prize is land full of flowers which are great for hiding from predators, as wells as siphoning nectar, the bun calls in reinforcements and quickly there are too many to drive off with stings and pheramones. The buns claim the meadow of flowers. You lose!\n"
        elif computer_action == "bun":
            outcome_dialogue = "Corvid eats the bee. You lose!\n"
        elif computer_action == "corvid":
            outcome_dialogue = "The wolf gets stung in the muzz and looks silly the rest of the day. You win!\n"
        elif computer_action == "cat":
            outcome_dialogue = "Despite a well calculated swat, the bee outmanuervers the cat and manages to sting it right in the offending paw, sending the cat running. You win!\n"
        elif computer_action == "wolf":
            outcome_dialogue = "Tie"
        else:
            outcome_dialogue = "wild card"
    elif player_action == "human":
        if computer_action == "bee":
            outcome_dialogue = "Bee Wild Card"
        elif computer_action == "bun":
            outcome_dialogue = "Bun Wild Card"
        elif computer_action == "corvid":
            outcome_dialogue = "Corvid Wild Card"
        elif computer_action == "cat":
            outcome_dialogue = "Cat Wild Card"
        elif computer_action == "wolf":
            outcome_dialogue = "Wolf Wild Card"
        else:
            outcome_dialogue = "Human Tie"
    else:
        raise ValueError(f"Unexpected input: player={player_action}, computer={computer_action}")
    
    return outcome_dialogue
"""