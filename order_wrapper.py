from abc import abstractmethod, ABC

from chocolate_type import ChocolateType
from orderdata import OrderData


# TODO: Write tests for this file
class OrderWrapper(ABC):

    def _create_blank_report(self) -> dict:
        return {flavor.name: 0 for flavor in self.flavors}

    def _calculate_quantity(self, order) -> int:
        return order.cash // order.price

    @abstractmethod
    def process_order(self):
        pass


class OrderWrapperRegular(OrderWrapper):
    def __init__(self, order, flavors=ChocolateType):
        self.order = order
        self.flavors = flavors

    def process_order(self):
        report = self._create_blank_report()

        for key in report.keys():
            if key == self.order.type:
                report[key] = self._calculate_quantity(self.order)

        return report
