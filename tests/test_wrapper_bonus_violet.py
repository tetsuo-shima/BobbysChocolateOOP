import unittest
from order_wrapper_bonus import OrderWrapperBonusViolet
from orderdata import OrderData

order = OrderData(**{'type': 'violet', 'cash': 13, 'price': 4, 'ratio': 1})
order_wrapper = OrderWrapperBonusViolet(order)


class TestOrderWrapperBonusViolet(unittest.TestCase):
    def test_instantiation(self):
        self.assertEqual(order_wrapper.order.type, 'violet')
        self.assertEqual(order_wrapper.order.cash, 13)
        self.assertEqual(order_wrapper.order.price, 4)
        self.assertEqual(order_wrapper.order.ratio, 1)

    def test_process_bonus(self):
        actual = order_wrapper.process_order()
        expected = {'milk': 0, 'violet': 9, 'espresso': 0}
        self.assertEqual(actual, expected)
