from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "API running on Render Free Plan!"})

@app.route("/info")
def info():
    return jsonify({"owner": "Baharul", "status": "ok"})

if __name__ == "__main__":
    app.run()
