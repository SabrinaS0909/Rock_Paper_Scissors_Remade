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

def outcome(player_action, computer_action):
    print("outcome function is working")

    if player_action == "bee":
        if computer_action == "bee":
            outcome = "Tie"
        elif computer_action == "bun":
            outcome = "In a battle for territory, where the prize is a meadow full of flowers that are both great for buns to eat and hide from predators and for bees to siphon nectar, the bun calls in reinforcements. Soon, there are too many to drive off with stings and pheramones. The buns claim the meadow of flowers, eating too many for your colony to sustain. You lose!\n"
        elif computer_action == "corvid":
            outcome = "The corvid eats you. You lose!\n"
        elif computer_action == "cat":
            outcome = "Despite a well calculated swat, you outmanuerver the cat and manage to sting it right in the offending paw, sending the cat running. You win!\n"
        elif computer_action == "wolf":
            outcome = "The wolf gets stung in the muzz and looks silly the rest of the day. You win!\n"
        else:
            humanandbee_win_or_lose_actions = [
                ("The human is allergic to your sting and is hospitalized. You win!\n", "win")
                ("The human smacks you with a newspaper, crushing you immediately. You lose!\n", "lose")
            ]
            computer_action_bee_vs_human = random.choice(humanandbee_win_or_lose_actions)
            outcome = computer_action_bee_vs_human
    elif player_action == "bun":
        if computer_action == "bee":
            outcome = "Your ears flick as the sound of buzzing fills their tunneling canals. You're able to pinpoint just where it's coming from, and just where it's going. With one impressive hop, and a well timed kick with your large fluffy feet, you kick the bee out of the air and send it spiraling back from whence it came. You win!\n"
        elif computer_action == "bun":
            outcome = "Tie"
        elif computer_action == "corvid":
            outcome = "The corvid sees you outside of your den and alerts your presence to nearby wolves. You are hunted, and both wolf and corvid enjoy the meal. You lose!\n"
        elif computer_action == "cat":
            outcome = "The cat, brought in as pest control, drives you and your family from the garden you've lived in from birth. You lose!\n"
        elif computer_action == "wolf":
            outcome = "The wolf takes chase after you, but you're too fast and you make it back to the den before you can be claimed as dinner. The wolf must go hungry this time. You win!\n"
        else:
            humanandbun_win_or_lose_actions = [
                ("The human unknowingly plants a garden of lettuce and tomatoes ontop of an underground bunny tunnel system, allowing you and your family easy access to the human's produce while being difficult to find and exterminate. You win!\n", "win")
                ("The human lays traps that ensnare you and your kin. You lose!\n", "lose")
            ]
            computer_action_bun_vs_human = random.choice(humanandbun_win_or_lose_actions)
            outcome = computer_action_bun_vs_human
    elif player_action == "corvid":
        if computer_action == "bee":
            outcome = "With your vast intelligence and tool-making abilities, you use a stick to pry bees and larvae from their hive for a quick snack while using your flight and agility to avoid their stings. You win!\n"
        elif computer_action == "bun":
            outcome = "The bun, while trying to cross the street, is spooked when you swoop down at it, causing it to backtrack and get hit by a car. You can now feed on the roadkill. You win!\n"
        elif computer_action == "corvid":
            outcome = "Tie"
        elif computer_action == "cat":
            outcome = "Cat stalks and kills the corvid. You lose!\n"
        elif computer_action == "wolf":
            outcome = "The wolf, after making a kill, reacts aggressively to you when you come down to try and scavange with the pack. You become an appetizer to the meal. You lose!\n"
        else:
            humanandcorvid_win_or_lose_actions = [
                ("The human destroys your natural habitat and you're forced to live in the city. You lose!\n", "lose") 
                ("The human enters the world of Alfred Hitchcock's *The Birds* and has their eyes pecked out by you, a crazed corvid. You win!\n", "win")
            ]
            computer_action_corvid_vs_human = random.choice(humanandcorvid_win_or_lose_actions)
            outcome = computer_action_corvid_vs_human
    elif player_action == "cat":
        if computer_action == "bee":
            outcome = "The bee becomes aggitated when you decide to climb a tree that inhabits their home. When you step on the hive to aid your ascent, the bee sends out the pheramones necessary to protect the hive. You quickly flee. You lose!\n"
        elif computer_action == "bun":
            outcome = "The bun tests its luck and explores a yard that is highly protected by you. You make simple work of the curious bun. You win!\n"
        elif computer_action == "corvid":
            outcome = "You decide to take a cat nap in a tree, and any corvid that even tries to stop and rest there knows immediately to turn around and go back. You win!\n"
        elif computer_action == "cat":
            outcome = "Tie"
        elif computer_action == "wolf":
            outcome = "While overconfidently wandering the woods near you, woodlands that are known for wolf activity, you're stolen away for dinner. You lose!\n"
        else:
            humanandcat_win_or_lose_actions = [
                ("Human domesticates the cat and makes it wear silly hats and posts pictures of the embarassing situation all over the internet. You lose!\n", "lose") 
                ("Human is infected with toxoplasmosis and becomes a slave to the cat. You win!\n", "win")
            ]
            computer_action_cat_vs_human = random.choice(humanandcat_win_or_lose_actions)
            outcome = computer_action_cat_vs_human
    elif player_action == "wolf":
        if computer_action == "bee":
            outcome = "The bee flies into your ear and buzzes right against your eardrum. The sound is intensely loud due to your sensitive hearing and it sends you into a desperate frenzy of scratching to get it out. You lose!\n"
        elif computer_action == "bun":
            outcome = "The bun, while being chased by you, leads you directly into the pathway of hunters before disappearing beneath the ground. Now you have to outrun gunfire, as you are no longer protected by a status of being endangered. Thanks, gov'ment! You lose!\n"
        elif computer_action == "corvid":
            outcome = "You befriend the corvid and benefit from an additional aerial view when searching for food. You get many more meals than you would have otherwise due to it. You win!\n"
        elif computer_action == "cat":
            outcome = "The cat, who has lived its entire life with nothing larger than a Chihuaha, is intimidated by your sheer size and immediately runs home. You win!\n"
        elif computer_action == "wolf":
            outcome = "Tie"
        else:
            humanandwolf_win_or_lose_actions = [
                ("The human tests the your, and a couple other wolves', boundaries with a Jackass™-style meat-suit and gets mauled. You win!\n", "win")
                ("The human confuses coyotes killing their livestock for you and your pack, and goes on a mass hunting spree. You lose!\n", "lose")
            ]
            computer_action_wolf_vs_human = random.choice(humanandwolf_win_or_lose_actions)
            outcome = computer_action_wolf_vs_human
    elif player_action == "human":
        if computer_action == "bee":
            bee_win_or_lose_actions = [
                ("Bee does a little dance that rallies the masses to attack you. You lose!\n", "lose")
                ("You make a movie about the bee that makes everyone assume it likes Jazz. It hears 'Ya like jazz?' for the remainder of its life. You win!\n", "win")
            ]
            computer_action_human_vs_bee = random.choice(bee_win_or_lose_actions)
            outcome = computer_action_human_vs_bee
        elif computer_action == "bun":
            bun_win_or_lose_actions = [
                ("Bun, and its family, enjoys a very large meal which, to your dismay, turns out to be your crop yeild for the season. You lose!\n", "lose")
                ("Bun foregoes it's usual choice of lettuce, and other mediocre looking vegetables, for some unusually juicy and delicious looking tomatoes. Turns out the reason they looked so good was because of DDT. The bun is poisoned and no longer bothers any of the crops. You win!\n", "win")
            ]
            computer_action_human_vs_bun = random.choice(bun_win_or_lose_actions)
            outcome = computer_action_human_vs_bun
        elif computer_action == "corvid":
            corvid_win_or_lose_actions = [
                ("The corvid drops from the sky with it's buddies due to some human neonicotinoids you had been spraying. Well, at least the bugs are gone from the apples. You win!\n", "win")
                ("The corvid waits for you to turn your head then attacks while you're not looking. You lose!\n", "lose")
            ]
            computer_action_human_vs_corvid = random.choice(corvid_win_or_lose_actions)
            outcome = computer_action_human_vs_corvid
        elif computer_action == "cat":
            cat_win_or_lose_actions = [
                ("You adopt the cat and realize that putting forth effort for another individual is too much. The cat is dumped in the street. You win!\n", "win")
                ("Cat, while being driven out of its home by someone who can no longer provide for it, turns and mauls the human with claws of fury before finding a better home elsewhere. You lose!\n", "lose")
            ]
            computer_action_human_vs_cat = random.choice(cat_win_or_lose_actions)
            outcome = computer_action_human_vs_cat
        elif computer_action == "wolf":
            wolf_win_or_lose_actions = [
                ("Human retracts laws against indiscriminatory hunting of wolves. Wolves go extinct and species that require a keystone species destroy the ecosystem. You win!\n", "win")
                ("Human attempts to hunt a wolf and instead meets the whole pack. The human is out of ammo. You lose!\n", "lose")
            ]
            computer_action_human_vs_wolf = random.choice(wolf_win_or_lose_actions)
            outcome = computer_action_human_vs_wolf
        else:
            outcome = "This is human vs human which are both wild cards, this will be substantially different from the function we've made."
    else:
        raise ValueError(f"Unexpected input: player={player_action}, computer={computer_action}")
    
    return outcome