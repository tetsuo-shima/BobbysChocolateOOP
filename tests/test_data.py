import unittest
from data import load_orders, _cast_integers, _read_csv
from orderdata import OrderData

filename = 'test_resources/test_orders.csv'


class TestData(unittest.TestCase):
    def test_load_orders(self):
        actual = load_orders(filename)
        expected = [
            OrderData(type='milk', cash=12, price=2, ratio=5),
            OrderData(type='violet', cash=13, price=4, ratio=1),
            OrderData(type='espresso', cash=6, price=2, ratio=2)
        ]
        self.assertEqual(actual, expected)

    def test_cast_integers(self):
        actual = _cast_integers([{'one': '1', 'two': '2.0', 'three': 3.0,
                                  'four': 'four'}])
        expected = [{'one': 1, 'two': '2.0', 'three': 3, 'four': 'four'}]
        self.assertEqual(actual, expected)

    def test_read_csv(self):
        actual = _read_csv(filename)
        expected = [
            {'type': 'milk', 'cash': '12', 'price': '2', 'ratio': '5'},
            {'type': 'violet', 'cash': '13', 'price': '4', 'ratio': '1'},
            {'type': 'espresso', 'cash': '6', 'price': '2', 'ratio': '2'}
        ]
        self.assertEqual(actual, expected)

