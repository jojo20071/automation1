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

# Before request hook to check and run the loop function
@app.before_request
def check_loop():
    global last_run_time
    if loop_running:
        current_time = time.time()
        # If it's the first run or 1 hour has passed, run the function
        if last_run_time is None or (current_time - last_run_time) >= 30:
            run_task()
            last_run_time = current_time

# Route to serve the HTML page
@app.route('/')
def index():
    return render_template('index.html', loop_running=loop_running)

# Start loop endpoint
@app.route('/start-loop', methods=['POST'])
def start_loop():
    global loop_running, last_run_time
    if not loop_running:
        loop_running = True
        last_run_time = None  # Reset to force an immediate run
    return jsonify({"status": "Loop started"}), 200

# Stop loop endpoint
@app.route('/stop-loop', methods=['POST'])
def stop_loop():
    global loop_running
    if loop_running:
        loop_running = False
    return jsonify({"status": "Loop stopped"}), 200

# Run the app
if __name__ == '__main__':
    app.run()