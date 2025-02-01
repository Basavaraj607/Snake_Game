from flask import Flask, render_template
import threading
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start_game', methods=['POST'])
def start_game():
    threading.Thread(target=run_game).start()
    return '', 204

def run_game():
    subprocess.run(['python', 'snake_game.py'])

if __name__ == '__main__':
    app.run(debug=True)
