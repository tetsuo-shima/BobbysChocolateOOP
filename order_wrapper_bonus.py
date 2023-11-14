from abc import abstractmethod, ABC
from chocolate_type import ChocolateType
from order_wrapper import OrderWrapper


class OrderWrapperBonus(OrderWrapper, ABC):

    @abstractmethod
    def _process_bonus(self) -> int:
        pass



class OrderWrapperBonusMilk(OrderWrapperBonus):

    def __init__(self, order, flavors=ChocolateType):
        self.order = order
        self.flavors = flavors

    def _process_bonus(self) -> int:
        return self._calculate_quantity(self.order) // self.order.ratio

    def process_order(self):
        report = self._create_blank_report()

        for key in report.keys():
            if key == self.order.type:
                report[key] = (self._calculate_quantity(self.order) +
                               self._process_bonus())

        return report


class OrderWrapperBonusViolet(OrderWrapperBonus):

    def __init__(self, order, flavors=ChocolateType):
        self.order = order
        self.flavors = flavors

    def _process_bonus(self) -> int:
        return (self._calculate_quantity(self.order) // self.order.ratio) * 2

    def process_order(self):
        report = self._create_blank_report()

        for key in report.keys():
            if key == self.order.type:
                report[key] = (self._calculate_quantity(self.order) +
                               self._process_bonus())

        return report


class OrderWrapperBonusEspresso(OrderWrapperBonus):
    def __init__(self, order, flavors=ChocolateType):
        self.order = order
        self.flavors = flavors

    def _process_bonus(self) -> int:
        return self._calculate_quantity(self.order) // self.order.ratio

    def process_order(self):
        report = self._create_blank_report()
        bonus = report[self.flavors.milk.name] = self._process_bonus()

        for key in report.keys():
            if key == self.order.type:
                report[key] = self._calculate_quantity(self.order) + bonus

        return report


class OrderWrapperBonusRuby(OrderWrapperBonus):
    def __init__(self, order, flavors=ChocolateType):
        self.order = order
        self.flavors = flavors

    def _process_bonus(self) -> int:
        return self._calculate_quantity(self.order) // self.order.ratio

    def process_order(self):
        report = self._create_blank_report()
        bonus = self._process_bonus()

        for key in report.keys():
            report[key] = bonus
            if key == self.order.type:
                report[key] += self._calculate_quantity(self.order)

        return report
