import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

MINDSTUDIO_API_KEY = os.getenv('MINDSTUDIO_API_KEY')
AGENT_ID = os.getenv('MINDSTUDIO_AGENT_ID')

@app.route('/api/scan', methods=['POST'])
def scan_website():
    data = request.json
    website_url = data.get('websiteUrl', '')
    email = data.get('email', '')
    
    url = 'https://v1.mindstudio-api.com/developer/v2/agents/run'
    headers = {
        'Authorization': f'Bearer {MINDSTUDIO_API_KEY}',
        'Content-Type': 'application/json'
    }
    
    payload = {
        "agentId": AGENT_ID,
        "workflow": "Main",
        "variables": {
            "websiteContent": "",
            "websiteUrl": website_url,
            "email": email,
            "language": "nl"
        }
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
