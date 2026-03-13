from flask import Flask, request, jsonify
from main import handle_signal

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():

    raw_signal = request.data.decode("utf-8").strip()

    print("ALERT RECEIVED:", raw_signal)

    if raw_signal:
        handle_signal(raw_signal)

    return jsonify({"status": "ok"})