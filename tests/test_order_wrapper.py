import unittest
from order_wrapper import OrderWrapperRegular
from orderdata import OrderData
from test_resources.test_chocolate_type import ChocolateType as Ct

order = OrderData(**{'type': 'milk', 'cash': 12, 'price': 2, 'ratio': 5})
order_wrapper = OrderWrapperRegular(order, Ct)


class TestOrderWrapper(unittest.TestCase):

    def test_instantiate_order_wrapper(self):
        self.assertEqual(order_wrapper.order.type, 'milk')
        self.assertEqual(order_wrapper.order.cash, 12)
        self.assertEqual(order_wrapper.order.price, 2)
        self.assertEqual(order_wrapper.order.ratio, 5)

    def test_create_blank_report(self):
        blank_report = order_wrapper._create_blank_report()
        expected = {'milk': 0, 'violet': 0, 'espresso': 0}
        self.assertEqual(blank_report, expected)

    def test_calculate_quantity(self):
        actual = order_wrapper._calculate_quantity(order)
        expected = 6
        self.assertEqual(actual, expected)

    def test_process_order(self):
        actual = order_wrapper.process_order()
        expected = {'milk': 6, 'violet': 0, 'espresso': 0}
        self.assertEqual(actual, expected)
