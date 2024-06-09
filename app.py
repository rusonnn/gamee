from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)
number_to_guess = random.randint(1, 100)
guess_count = 0

@app.route('/')
def index():
    global guess_count, number_to_guess
    guess_count = 0  # Reset guess count each time the page is loaded
    number_to_guess = random.randint(1, 100)  # Reset the number each time the page is loaded
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    global guess_count, number_to_guess
    guess = int(request.form['guess'])
    guess_count += 1

    if guess < number_to_guess:
        response = "Too low!"
    elif guess > number_to_guess:
        response = "Too high!"
    else:
        response = f"Congratulations! You guessed it in {guess_count} tries."
        number_to_guess = random.randint(1, 100)  # Reset the number
        guess_count = 0  # Reset guess count
    return jsonify(response=response)

if __name__ == '__main__':
    app.run(debug=True)
