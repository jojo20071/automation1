from flask import Flask, send_file, jsonify,render_template, make_response
from flask import request
import json
import os




app = Flask(__name__)




name = 1

@app.route('/homescreen', methods=['GET'])
def home():
    return str(name)

@app.route('/1', methods=['GET'])
def d():
    name = 2
    return "set to 2"


