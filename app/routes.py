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
    player_combo, computer_combo = get_combo_animals(data)
    print(f"It's {player_combo} vs {computer_combo}!!")
    print("Data received:", data)
    print("Combo results:", player_combo, computer_combo)
    return jsonify ({"player_combo": player_combo, "computer_combo": computer_combo})

@app.route('/element_outcome', methods = ['POST'])
def get_element_outcome():
    data = request.get_json()
    player_combo = data.get("player_combo")
    computer_combo = data.get("computer_combo")
    
    description, result = outcome(player_combo, computer_combo)

    print(description, result)
    return jsonify ({
        "description": description,
        "result": result
    })
