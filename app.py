from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow frontend requests

@app.route("/")
def home():
    return "<h1>Backend is working!</h1>"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)
