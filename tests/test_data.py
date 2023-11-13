import unittest
from data import load_orders
from orderdata import OrderData

filename = 'test_resources/test_orders.csv'


class TestData(unittest.TestCase):
    def test_read_file(self):
        orders = load_orders(filename)
        first = OrderData(type='milk', cash=12, price=2, ratio=5)
        second = OrderData(type='violet', cash=13, price=4, ratio=1)
        third = OrderData(type='espresso', cash=6, price=2, ratio=2)
        self.assertEqual(orders, [first, second, third])
