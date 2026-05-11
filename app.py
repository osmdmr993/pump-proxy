from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

@app.route("/trending")
def trending():
    url = "https://api.dexscreener.com/latest/dex/trending"
    data = requests.get(url).json()
    return jsonify(data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
    @app.route("/")
def root():
    return "ok", 200


