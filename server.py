from flask import Flask, jsonify
import json, os

app = Flask(__name__)
counter_file = "counter.json"

def load_count():
    if os.path.exists(counter_file):
        with open(counter_file, "r") as f:
            return json.load(f).get("visits", 0)
    return 0

def save_count(count):
    with open(counter_file, "w") as f:
        json.dump({"visits": count}, f)

@app.route("/")
def home():
    return "Besøksteller kjører – bruk /count for å hente data."

@app.route("/count")
def count():
    count = load_count() + 1
    save_count(count)
    return jsonify({"visits": count})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
