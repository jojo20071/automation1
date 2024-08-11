from flask import Flask, send_file, jsonify,render_template, make_response
from flask import request
import json
import os
from supabase import create_client, Client
from arcadeApi import ArcadeApi

api = ArcadeApi(user_id="U07B1MK6MAQ", save=True, debug=False)


app = Flask(__name__)






@app.route('/homescreen', methods=['GET'])
def home():
    api.start_session("My Arcade Session")
    return("Homescreen :) startet")






  

@app.route('/r', methods=['GET'])
def red():
    # HTML with embedded JavaScript to change local storage variable "color" and redirect after 1 second
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Change Color</title>
    </head>
    <body>
        
        <script>
            // JavaScript to change the local storage variable "color"
            localStorage.setItem('color', [0,"r"]); // Change 'newColorValue' as needed
            document.body.innerHTML += '<p>Color changed in local storage. Redirecting in 1 second...</p>';
            
            // Wait for 1 second before redirecting
            setTimeout(function() {
                window.location.href = 'https://color-wars-game.vercel.app/';
            }, 1000); // 1000 milliseconds = 1 second
        </script>
    </body>
    </html>
    """
    response = make_response(html_content)
    response.headers['Content-Type'] = 'text/html'
    return response


