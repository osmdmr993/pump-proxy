from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/trending")
def trending():
    url = "https://api.dexscreener.com/latest/dex/trending"
    data = requests.get(url).json()
    return jsonify(data)

if __name__ == "__main__":
    os.environ.get("PORT", 10000)
