################################################################################
#
#  Permission is hereby granted, free of charge, to any person obtaining a
#  copy of this software and associated documentation files (the "Software"),
#  to deal in the Software without restriction, including without limitation
#  the rights to use, copy, modify, merge, publish, distribute, sublicense,
#  and/or sell copies of the Software, and to permit persons to whom the
#  Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

import json
import random
import urllib.request
import time  # Import the time module for sleep function

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server requests
N = 500


def getDataPoint(quote):
    """ Produce all the needed values to generate a datapoint """
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = (bid_price + ask_price) / 2
    return stock, bid_price, ask_price, price


def getRatio(price_a, price_b):
    """ Get ratio of price_a to price_b """
    if price_b == 0:
        return None  # Handle division by zero
    else:
        return price_a / price_b


# Initialize N and QUERY here
N = 10
BASE_QUERY = "http://localhost:8080/query?id={}"

# Main
if __name__ == "__main__":
    # Query the price once every N seconds.
    for _ in range(N):
        # Generate a random ID for the query
        random_id = random.random()
        query = BASE_QUERY.format(random_id)

        quotes = json.loads(urllib.request.urlopen(query).read())

        # Initialize prices dictionary
        prices = {}

        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            print("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))

            # Update prices dictionary with stock and corresponding price
            prices[stock] = price

        # Calculate and print the ratio for each stock
        for stock, price in prices.items():
            ratio = getRatio(price, prices[stock])  # Use the correct prices for price_a and price_b
            print("Ratio for %s: %s" % (stock, ratio))

        # Sleep for a few seconds before the next iteration
        time.sleep(5)  # Adjust the sleep duration
