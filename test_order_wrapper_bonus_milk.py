import unittest
from order_wrapper_bonus import OrderWrapperBonusMilk
from orderdata import OrderData

order = OrderData(**{'type': 'milk', 'cash': 12, 'price': 2, 'ratio': 5})
order_wrapper = OrderWrapperBonusMilk(order)


class TestOrderWrapperBonusMilk(unittest.TestCase):
    def test_instantiation(self):
        self.assertEqual(order_wrapper.order.type, 'milk')
        self.assertEqual(order_wrapper.order.cash, 12)
        self.assertEqual(order_wrapper.order.price, 2)
        self.assertEqual(order_wrapper.order.ratio, 5)

    def test_process_bonus(self):
        actual = order_wrapper.process_order()
        expected = {'milk': 7, 'violet': 0, 'espresso': 0}
        self.assertEqual(actual, expected)
