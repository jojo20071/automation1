# /app.py

from flask import Flask, render_template, jsonify
import time

app = Flask(__name__)

# Global variables to manage loop state
loop_running = False
last_run_time = None

# Function to run
def run_task():
    print("Function is running...")

print("hi1")
print("hi2")
time.sleep(5)
print("hi3 after 5 sec")
time.sleep(20)
print("hi3 after 20 sec")
time.sleep(120)
print("hi3 after 2 min")


# Route to serve the HTML page
@app.route('/')
def index():
    return render_template('index.html', loop_running=loop_running)

