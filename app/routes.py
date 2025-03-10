from app import app
from flask import render_template, request, jsonify

@app.route('/')
def index():
    return render_template('rock_paper_scissors.html')

@app.route('/animal_click', methods = ['POST'])
def animal_click():
    data = request.get_json()
    animal = data['animal']
    print(f"Server received: {animal}")
    return jsonify ({"message": "Animal click received"})
