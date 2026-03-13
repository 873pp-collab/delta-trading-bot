import os
from delta_rest_client import DeltaRestClient, OrderType

API_KEY = os.environ.get("DELTA_API_KEY")
API_SECRET = os.environ.get("DELTA_API_SECRET")

delta_client = DeltaRestClient(
    base_url='https://demo-api.india.delta.exchange',
    api_key=API_KEY,
    api_secret=API_SECRET
)

PRODUCT_ID = 84
ORDER_SIZE = 1

current_position = None


def buy():
    global current_position

    if current_position == "LONG":
        print("Already in BUY")
        return

    if current_position == "SHORT":
        close_position()

    delta_client.place_order(
        product_id=PRODUCT_ID,
        size=ORDER_SIZE,
        side='buy',
        order_type=OrderType.MARKET
    )

    current_position = "LONG"


def sell():
    global current_position

    if current_position == "SHORT":
        print("Already in SELL")
        return

    if current_position == "LONG":
        close_position()

    delta_client.place_order(
        product_id=PRODUCT_ID,
        size=ORDER_SIZE,
        side='sell',
        order_type=OrderType.MARKET
    )

    current_position = "SHORT"


def close_position():
    global current_position

    if current_position is None:
        return

    side = 'sell' if current_position == "LONG" else 'buy'

    delta_client.place_order(
        product_id=PRODUCT_ID,
        size=ORDER_SIZE,
        side=side,
        order_type=OrderType.MARKET
    )

    current_position = None


def handle_signal(signal):
    signal = signal.upper()

    if "BUY" in signal:
        buy()

    elif "SELL" in signal:
        sell()