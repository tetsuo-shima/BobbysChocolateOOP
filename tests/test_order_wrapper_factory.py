import unittest

from name_not_found_exception import NameNotFoundException
from order_wrapper_bonus import OrderWrapperBonusMilk, OrderWrapperBonusViolet, \
    OrderWrapperBonusEspresso, OrderWrapperBonusRuby
from order_wrapper_factory import OrderWrapperFactory
from orderdata import OrderData

factory = OrderWrapperFactory()


class TestOrderWrapperFactory(unittest.TestCase):
    def test_wrap_order_milk(self):
        order = OrderData(
            **{'type': 'milk', 'cash': 12, 'price': 2, 'ratio': 5}
        )
        actual = factory.wrap_order(order)
        self.assertEqual(actual.order, order)
        self.assertIsInstance(actual, OrderWrapperBonusMilk)

    def test_wrap_order_violet(self):
        order = OrderData(
            **{'type': 'violet', 'cash': '13', 'price': '4', 'ratio': '1'}
        )
        actual = factory.wrap_order(order)
        self.assertEqual(actual.order, order)
        self.assertIsInstance(actual, OrderWrapperBonusViolet)

    def test_wrap_order_espresso(self):
        order = OrderData(
            **{'type': 'espresso', 'cash': '6', 'price': '2', 'ratio': '2'}
        )
        actual = factory.wrap_order(order)
        self.assertEqual(actual.order, order)
        self.assertIsInstance(actual, OrderWrapperBonusEspresso)

    def test_wrap_order_ruby(self):
        order = OrderData(
            **{'type': 'ruby', 'cash': 21, 'price': 2, 'ratio': 4}
        )
        actual = factory.wrap_order(order)
        self.assertEqual(actual.order, order)
        self.assertIsInstance(actual, OrderWrapperBonusRuby)

    def test_wrap_order_not_in_enum(self):
        order = OrderData(
            **{'type': 'dummy', 'cash': 21, 'price': 2, 'ratio': 4}
        )
        with self.assertRaises(NameNotFoundException):
            factory.wrap_order(order)

