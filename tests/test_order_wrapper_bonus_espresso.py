import unittest
from order_wrapper_bonus import OrderWrapperBonusEspresso
from orderdata import OrderData

order = OrderData(**{'type': 'espresso', 'cash': 6, 'price': 2, 'ratio': 2})
order_wrapper = OrderWrapperBonusEspresso(order)


class TestOrderWrapperBonusViolet(unittest.TestCase):
    def test_instantiation(self):
        self.assertEqual(order_wrapper.order.type, 'espresso')
        self.assertEqual(order_wrapper.order.cash, 6)
        self.assertEqual(order_wrapper.order.price, 2)
        self.assertEqual(order_wrapper.order.ratio, 2)

    def test_process_bonus(self):
        actual = order_wrapper.process_order()
        expected = {'milk': 1, 'violet': 0, 'espresso': 4}
        self.assertEqual(actual, expected)
