# /app.py

from flask import Flask, render_template, jsonify
import time
import threading

app = Flask(__name__)





def print_with_delay(message, delay):
    threading.Timer(delay, print, [message]).start()

print("hi1")
print("hi2")
print_with_delay("hi3 after 5 sec", 5)
print_with_delay("hi3 after 20 sec", 20)
print_with_delay("hi3 after 2 min", 120)



