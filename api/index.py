from flask import Flask
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

@app.route('/')
def home():
    return "The task is running in the background!"

if __name__ == '__main__':
    n = 5  # Number of times to run the task
    interval = 10  # Interval of 10 seconds

    run_periodically(n, interval, example_task)
    
    app.run(debug=True)