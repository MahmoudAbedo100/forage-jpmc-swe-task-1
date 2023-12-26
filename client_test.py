import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        # Calculate the expected result manually based on the provided data
        expected_result = ('ABC', 120.48, 121.2, 120.48)

        # Use assert to check if the result matches the expected values
        self.assertEqual(getDataPoint(quotes[0]), expected_result)

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        # Calculate the expected result manually based on the provided data
        expected_result = ('ABC', 120.48, 119.2, 120.48)

        # Use assert to check if the result matches the expected values
        self.assertEqual(getDataPoint(quotes[0]), expected_result)

    def test_getDataPoint_calculatePriceForDifferentStock(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'XYZ'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'PQR'}
        ]

        # Calculate the expected result manually based on the provided data
        expected_result = ('XYZ', 120.48, 119.2, 120.48)

        # Use assert to check if the result matches the expected values
        self.assertEqual(getDataPoint(quotes[0]), expected_result)

    def test_getDataPoint_calculatePriceWithZeroBidPrice(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 0}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        # Calculate the expected result manually based on the provided data
        expected_result = ('ABC', 0, 119.2, 0)

        # Use assert to check if the result matches the expected values
        self.assertEqual(getDataPoint(quotes[0]), expected_result)

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()

