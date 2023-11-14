import unittest

from orderdata import OrderData


class TestOrder(unittest.TestCase):
    def test_declaration(self):
        order = {'type': 'milk', 'cash': 12, 'price': 2, 'ratio': 5}
        data = OrderData(**order)
        self.assertEqual(data.type, order['type'])
        self.assertEqual(data.price, order['price'])
        self.assertEqual(data.cash, order['cash'])
        self.assertEqual(data.ratio, order['ratio'])
