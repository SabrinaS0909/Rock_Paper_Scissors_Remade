from app import app
from flask import render_template, request, jsonify
from app.utils import get_animal_choices, random_button, outcome

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
    
    outcome_dialogue = outcome(player_action, computer_action)
    
    #update the stuff below this to accept and process tuples 
    print(outcome_dialogue)
    return jsonify ({"outcome": outcome_dialogue})

print("routes is working") 
