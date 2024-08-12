from flask import Flask, send_file, jsonify,render_template, make_response
from flask import request
import json
import os
import threading
import time




app = Flask(__name__)






# Global variables to manage loop state
loop_running = False
loop_thread = None

# Function that runs every hour
def run_task():
    print("Function is running...")

# Background loop function
def loop_function():
    global loop_running
    while loop_running:
        run_task()
        time.sleep(3600)  # Sleep for 1 hour (3600 seconds)

# Route to serve the HTML page
@app.route('/')
def index():
    return render_template('index.html', loop_running=loop_running)

# Start loop endpoint
@app.route('/start-loop', methods=['POST'])
def start_loop():
    global loop_running, loop_thread
    if not loop_running:
        loop_running = True
        loop_thread = threading.Thread(target=loop_function)
        loop_thread.start()
    return jsonify({"status": "Loop started"}), 200

# Stop loop endpoint
@app.route('/stop-loop', methods=['POST'])
def stop_loop():
    global loop_running
    if loop_running:
        loop_running = False
        if loop_thread is not None:
            loop_thread.join()  # Ensure the thread has fully stopped
    return jsonify({"status": "Loop stopped"}), 200

# Run the app
if __name__ == '__main__':
    app.run()