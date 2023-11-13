import unittest
from enum import Enum

from order_wrapper_bonus import OrderWrapperBonusRuby
from orderdata import OrderData


class ChocolateType(Enum):
    milk = 1
    violet = 2
    espresso = 3
    ruby = 4


order = OrderData(**{'type': 'ruby', 'cash': 21, 'price': 2, 'ratio': 4})
order_wrapper = OrderWrapperBonusRuby(order, ChocolateType)


class TestOrderWrapperBonusRuby(unittest.TestCase):
    def test_instantiation(self):
        self.assertEqual(order_wrapper.order.type, 'ruby')
        self.assertEqual(order_wrapper.order.cash, 21)
        self.assertEqual(order_wrapper.order.price, 2)
        self.assertEqual(order_wrapper.order.ratio, 4)

    def test_process_bonus(self):
        actual = order_wrapper.process_order()
        expected = {'milk': 2, 'violet': 2, 'espresso': 2, 'ruby': 12}
        self.assertEqual(actual, expected)
