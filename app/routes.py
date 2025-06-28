from app import app
from flask import render_template, request, jsonify
from app.utils import get_animal_choices, random_button, outcome, get_combo_animals, combo_outcome

@app.route('/')
def index():
    return render_template('rock_paper_scissors.html')

@app.route('/animal_click', methods = ['POST'])
def animal_click():
    data = request.get_json()
    player_action, computer_action = get_animal_choices(data)
    print(f"It's {player_action} vs {computer_action}!!")
    return jsonify ({"player": player_action, "computer": computer_action})

@app.route('/random_button', methods = ['POST'])
def get_random_button():
    button_dialogue = random_button()
    print(button_dialogue)
    return jsonify ({"random_button": button_dialogue})

@app.route('/outcome', methods = ['POST'])
def get_outcome():
    data = request.get_json()
    player_action = data.get("player_action")
    computer_action = data.get("computer_action") 
    
    description, result = outcome(player_action, computer_action)

    print(description, result)
    return jsonify ({
        "description": description,
        "result": result
    }) 

@app.route("/get_combos", methods = ["POST"])
def get_combos():
    data = request.get_json()
    player_combo, computer_combo, element, computer_element = get_combo_animals(data)
    
    description, result = combo_outcome(data) 
    
    print(f"You chose {element} and the opponent chose {computer_element}.")
    print(f"It's {player_combo} vs {computer_combo}!!")
    print("Data received:", data)
    print("Combo results:", player_combo, computer_combo)

    return jsonify ({
        "player_combo": player_combo, 
        "computer_combo": computer_combo, 
        "computer_element": computer_element,
        "element": element,
        "description": description,
        "result": result})
