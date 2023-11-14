import unittest

from order_wrapper_bonus import OrderWrapperBonusMilk
from order_wrapper_factory import OrderWrapperFactory
from orderdata import OrderData

factory = OrderWrapperFactory()
order = OrderData(**{'type': 'milk', 'cash': 12, 'price': 2, 'ratio': 5})


# TODO: Complete tests
class TestOrderWrapperFactory(unittest.TestCase):
    def test_wrap_order(self):
        actual = factory.wrap_order(order)
        self.assertEqual(actual.order, order)

