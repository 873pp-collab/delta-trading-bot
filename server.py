from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.data.decode("utf-8")
    print("Webhook received:", data)

    if data == "BUY":
        print("BUY signal received")

    elif data == "SELL":
        print("SELL signal received")

    return "ok", 200