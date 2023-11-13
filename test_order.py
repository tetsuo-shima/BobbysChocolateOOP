import unittest

from orderdata import OrderData

order = {'type': 'milk', 'cash': 12, 'price': 2, 'ratio': 5}

class TestOrder(unittest.TestCase):
    def test_declaration(self):
        data = OrderData(**order)
        self.assertEqual(data.type, 'milk')
        self.assertEqual(data.price, 2)
        self.assertEqual(data.cash, 12)
        self.assertEqual(data.ratio, 5)
