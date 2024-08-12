from flask import Flask, request, jsonify
import threading
import time

app = Flask(__name__)

def run_periodically(n, interval, task_func):
    def task_runner():
        for _ in range(n):
            task_func()
            time.sleep(interval)
    
    thread = threading.Thread(target=task_runner)
    thread.start()

def example_task():
    print("Task executed")

@app.route('/start_task', methods=['POST'])
def start_task():
    data = request.get_json()
    n = data.get('n', 5)  # Default to running 5 times if not specified
    interval = 10  # Run every 10 seconds

    run_periodically(n, interval, example_task)
    
    return jsonify({"status": "Task started", "n": n, "interval": interval})

if __name__ == '__main__':
    app.run(debug=True)