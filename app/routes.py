from app import app
from flask import render_template, request, jsonify
from app.utils import get_animal_choices

@app.route('/')
def index():
    return render_template('rock_paper_scissors.html')

@app.route('/animal_click', methods = ['POST'])
def animal_click():
    data = request.get_json()
    player_action, computer_action = get_animal_choices(data)
    print(f"It's {player_action} vs {computer_action}!!")
    return jsonify ({"player": player_action, "computer": computer_action})

print("routes is working")