from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"message": "Hello, world!"})


@app.route("/webinar")
def webinar():
    return jsonify({"message": "Welcome to the webinar!"})

if __name__ == "__main__":
    # Listen on all interfaces so the container (or server) can access it
    app.run(host="0.0.0.0", port=5000)
