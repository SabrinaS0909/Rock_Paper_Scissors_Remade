#for reusable logic and functions; define them here

import random

animal_outcomes_map = {
    ("bee", "bee"): ("Tie", "tie"),
    ("bee", "bun"): ("In a battle for territory, where the prize is a meadow full of flowers that are both great for buns to eat and hide from predators and for bees to siphon nectar, the bun calls in reinforcements. Soon, there are too many to drive off with stings and pheromones. The buns claim the meadow of flowers, eating too many for your colony to sustain. You lose!", "lose"),
    ("bee", "corvid"): ("The corvid eats you. You lose!", "lose"),
    ("bee", "cat"): ("Despite a well calculated swat, you outmaneuver the cat and manage to sting it right in the offending paw, sending the cat running. You win!", "win"),
    ("bee", "wolf"): ("You sting the wolf in the muzz and it looks silly the rest of the day. You win!", "win"),
    ("bee", "human"): [
        ("The human is allergic to your sting and is so terrified of being hospitalized that they cower in fear, showing you their bottle of Benedryl as if it were a cross and you were a demon. You win!", "win"),
        ("The human smacks you with a newspaper, crushing you immediately. You lose!", "lose")
    ],

    ("bun", "bee"): ("Your ears flick as the sound of buzzing fills their tunneling canals. You're able to pinpoint just where it's coming from, and just where it's going. With one impressive hop, and a well timed kick with your large fluffy feet, you kick the bee out of the air and send it spiraling back from whence it came. You win!", "win"),
    ("bun", "bun"): ("Tie", "tie"),
    ("bun", "corvid"): ("The corvid sees you outside of your den and alerts your presence to nearby wolves. You are hunted, and both wolf and corvid enjoy the meal. You lose!", "lose"),
    ("bun", "cat"): ("The cat, brought in as pest control, drives you and your family from the garden you've lived in from birth. You lose!", "lose"),
    ("bun", "wolf"): ("The wolf takes chase after you, but you're too fast and you make it back to the den before you can be claimed as dinner. The wolf must go hungry this time. You win!", "win"),
    ("bun", "human"): [
        ("The human unknowingly plants a garden of lettuce and tomatoes ontop of an underground bunny tunnel system, allowing you and your family easy access to the human's produce while being difficult to find and exterminate. You win!", "win"),
        ("The human lays traps that ensnare you and your kin. You lose!", "lose")
    ],

    ("corvid", "bee"): ("With your vast intelligence and tool-making abilities, you use a stick to pry bees and larvae from their hive for a quick snack while using your flight and agility to avoid their stings. You win!", "win"),
    ("corvid", "bun"): ("The bun, while trying to cross the street, is spooked when you swoop down at it, causing it to backtrack and get hit by a car. You can now feed on the roadkill. You win!", "win"),
    ("corvid", "corvid"): ("Tie", "tie"),
    ("corvid", "cat"): ("The cat stalks and kills you. You lose!", "lose"),
    ("corvid", "wolf"): ("The wolf, after making a kill, reacts aggressively to you when you come down to try and scavange with the pack. You become an appetizer to the meal. You lose!", "lose"),
    ("corvid", "human"): [
        ("The human enters the world of Alfred Hitchcock's *The Birds* and has their eyes pecked out by you, a crazed corvid. You win!", "win"),
        ("The human destroys your natural habitat and you're forced to live in the city. You lose!", "lose")
    ],

    ("cat", "bee"): ("Your nap is interrupted by the pesky buzzing of a bee. You don't remember that you're sleeping on the window sill of a seven story building until your leap towards the bee leaves you looking at the long drop below you. You land on your feet, but you're now a long ways from your home and the bee gets your napping spot. You lose!", "lose"),
    ("cat", "bun"): ("The bun tests its luck and explores a yard that is highly protected by you. You make simple work of the curious bun. You win!", "win"),
    ("cat", "corvid"): ("You decide to take a cat nap in a tree, and any corvid that even tries to stop and rest there knows immediately to turn around and go back. You win!", "win"),
    ("cat", "cat"): ("Tie", "tie"),
    ("cat", "wolf"): ("While overconfidently wandering the woods near you, woodlands that are known for wolf activity, you're stolen away for dinner. You lose!", "lose"),
    ("cat", "human"): [
        ("The human is infected with toxoplasmosis and becomes a slave to you. You win!", "win"),
        ("The human domesticates you and makes you wear silly hats and posts pictures of the embarrassing situation all over the internet. You lose!", "lose")
    ],

    ("wolf", "bee"): ("The bee flies into your ear and buzzes right against your eardrum. The sound is intensely loud due to your sensitive hearing and it sends you into a desperate frenzy of scratching to get it out. You lose!", "lose"),
    ("wolf", "bun"): ("The bun, while being chased by you, leads you directly into the pathway of hunters before disappearing beneath the ground. Now you have to outrun gunfire, as you are no longer protected by a status of being endangered. Thanks, gov'ment! You lose!", "lose"),
    ("wolf", "corvid"): ("You befriend the corvid and benefit from an additional aerial view when searching for food. You get many more meals than you would have otherwise due to it. You win!", "win"),
    ("wolf", "cat"): ("The cat, who has lived its entire life with nothing larger than a Chihuaha, is intimidated by your sheer size and immediately runs home. You win!", "win"),
    ("wolf", "wolf"): ("Tie", "tie"),
    ("wolf", "human"): [
        ("The human tests your, and a couple other wolves', boundaries with a Jackass™-style meat-suit and gets mauled. You win!", "win"),
        ("The human confuses coyotes killing their livestock for you and your pack, and goes on a mass hunting spree. You lose!", "lose")
    ],

    ("human", "bee"): [
                ("You make a movie about the bee that makes everyone assume it likes jazz. It hears 'Ya like jazz?' for the remainder of its life. You win!", "win"),
                ("The bee does a little dance that rallies the masses to attack you. You lose!", "lose")
            ],
    ("human", "bun"): [
                ("The bun foregoes its usual choice of lettuce, and other mediocre looking vegetables, for some unusually juicy and delicious looking tomatoes. Turns out the reason they looked so good was because of DDT. The bun is poisoned and no longer bothers any of your crops. You win!", "win"),
                ("The bun, and its family, enjoys a very large yard which, to your dismay, translates to thousands of burrows that destroy your grass and soil integrity. You lose!", "lose")
            ],
    ("human", "corvid"): [
                ("The corvid drops from the sky with it's buddies due to some human neonicotinoids you had been spraying. Well, at least the bugs are gone from the apples. You win!", "win"),
                ("The corvid waits for you to turn your head then attacks while you're not looking. You lose!", "lose")
            ],
    ("human", "cat"): [
                ("You adopt the cat and realize that putting forth effort for another individual is too much. The cat is dumped in the street. You win!", "win"),
                ("The cat, while being driven out of your home with a broom, turns and mauls your face with claws of fury. You lose!", "lose")
            ],
    ("human", "wolf"): [
                ("Your government retracts laws against indiscriminate hunting of wolves. Wolves go extinct and species that require a keystone species destroy the ecosystem. You win!", "win"),
                ("You attempt to hunt a wolf and instead meet the whole pack. You're out of ammo. You lose!", "lose")
            ],
    ("human", "human"): ("Tie", "tie"),
}

element_animals_map = {
    ("bee", "water"): ("a Baltic isopod"),
    ("bee", "fire"): ("a wasp"),
    ("bee", "earth"): ("a scorpion"),
    ("bee", "air"): ("a bumble bee"),

    ("bun", "water"): ("a sea bunny"),
    ("bun", "fire"): ("a desert jackrabbit"),
    ("bun", "earth"): ("a Flemish giant rabbit"),
    ("bun", "air"): ("a Netherland Dwarf rabbit"),

    ("corvid", "water"): ("a crow"),
    ("corvid", "fire"): ("a jay"),
    ("corvid", "earth"): ("a raven"),
    ("corvid", "air"): ("a magpie"),

    ("cat", "water"): ("a jaguar"),
    ("cat", "fire"): ("a tiger"),
    ("cat", "earth"): ("a lion"),
    ("cat", "air"): ("a snow leopard"),

    ("wolf", "water"): ("a coastal wolf"),
    ("wolf", "fire"): ("a Maine wolf"),
    ("wolf", "earth"): ("a grey wolf"),
    ("wolf", "air"): ("an arctic wolf"),

    ("human", "water"): ("a marine biologist"),
    ("human", "fire"): ("a firefighter"),
    ("human", "earth"): ("a geologist"),
    ("human", "air"): ("an aircraft pilot"),
}

def get_animal_choices(data):
    player_action = data["animal"]
    possible_actions = ["bee"] #, "bun", "corvid", "cat", "wolf", "human"
    computer_action = random.choice(possible_actions)
    return player_action, computer_action

def random_button():
    possible_buttons = ["Let's go!", "It's on!", "Cower before me!", "You're too weak!", "I'm scared!"]
    button_dialogue = random.choice(possible_buttons)
    return button_dialogue

def outcome(player_action, computer_action):
    print("outcome function is working")

    key = (player_action, computer_action)

    if key not in animal_outcomes_map:
       raise ValueError(f"Unexpected input: player = {player_action}, computer = {computer_action}")
    
    result = animal_outcomes_map[key]
       
    return random.choice(result) if isinstance(result, list) else result 

#I want to log what outcomes a player has already experienced, and prevent them from happening again until at least 3-5 turns later.

def get_random_element():
    return random.choice(["water", "fire", "earth", "air"])