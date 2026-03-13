from flask import Flask, request
import os
from delta_rest_client import DeltaRestClient, OrderType

app = Flask(__name__)

API_KEY = os.environ.get("DELTA_API_KEY")
API_SECRET = os.environ.get("DELTA_API_SECRET")

delta_client = DeltaRestClient(
    base_url="https://demo-api.india.delta.exchange",
    api_key=API_KEY,
    api_secret=API_SECRET
)

PRODUCT_ID = 27
ORDER_SIZE = 1

current_position = None


@app.route("/")
def home():
    return "Trading bot running"


@app.route("/webhook", methods=["POST"])
def webhook():

    data = request.data.decode("utf-8")
    print("Webhook received:", data)

    handle_signal(data)

    return "ok", 200


def buy():
    global current_position

    print("Executing BUY")

    response = delta_client.place_order(
        product_id=PRODUCT_ID,
        size=ORDER_SIZE,
        side="buy",
        order_type=OrderType.MARKET
    )

    print("Delta response:", response)

    current_position = "LONG"


def sell():
    global current_position

    print("Executing SELL")

    response = delta_client.place_order(
        product_id=PRODUCT_ID,
        size=ORDER_SIZE,
        side="sell",
        order_type=OrderType.MARKET
    )

    print("Delta response:", response)

    current_position = "SHORT"


def handle_signal(signal):

    signal = signal.upper()

    print("Signal received:", signal)

    if "BUY" in signal:
        buy()

    elif "SELL" in signal:
        sell()