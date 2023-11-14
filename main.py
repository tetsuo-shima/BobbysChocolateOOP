from data import load_orders
from order_wrapper_factory import OrderWrapperFactory


def main():
    factory = OrderWrapperFactory()
    wrapped_orders = [factory.wrap_order(order) for order in load_orders()]

    reports = [wrapped_order.process_order() for wrapped_order
               in wrapped_orders]

    for report in reports:
        results = [f'{key} {value}, ' for key, value in report.items()]
        print(''.join(results)[:-2])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
