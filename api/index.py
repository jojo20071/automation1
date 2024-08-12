from flask import Flask, send_file, jsonify,render_template, make_response
from flask import request
import json
import os
import time




app = Flask(__name__)




name = 1

@app.route('/homescreen', methods=['GET'])
def home():
    start_time = time.time()
    running = True
    while running:
        current_time = time.time()
        elapsed_time = current_time - start_time
        if elapsed_time >= 10:
            running = False
    return "10 seconds have passed"


@app.route('/1', methods=['GET'])
def d():
    name = 2
    return "set to 2"


