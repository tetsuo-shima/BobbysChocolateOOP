import copy
import csv
from constants import ORDER_FILE, BONUS_PROMOTION_ACTIVATED
from orderdata import OrderData


# TODO: add tests

def _read_csv(datafile=ORDER_FILE):
    with open(datafile, 'r') as file:
        csv_reader = csv.DictReader(file)
        orders = [order for order in csv_reader]

    return orders


def _cast_integers(orders: dict):
    new_orders = copy.deepcopy(orders)
    for order in new_orders:
        for key, value in order.items():
            try:
                order[key] = int(value)
            except ValueError:
                pass

    return new_orders


def load_orders(datafile=ORDER_FILE) -> list:
    orders = _read_csv(datafile)
    return [OrderData(**order) for order in _cast_integers(orders)]


# TODO: add test for this
def pair_processing(orders: list) -> list:
    processing_pairs = []
    for order in orders:
        if BONUS_PROMOTION_ACTIVATED:
            if order['type'] == 'ruby':
                pair = (order, ruby_bonus)
            elif order['type'] == 'milk':
                pair = (order, milk_bonus)
            elif order['type'] == 'violet':
                pair = (order, violet_bonus)
            elif order['type'] == 'espresso':
                pair = (order, espresso_bonus)
        else:
            pair = (order, process_regular_order)

        processing_pairs.append(pair)

    return processing_pairs
