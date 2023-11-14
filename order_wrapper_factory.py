from constants import BONUS_PROMOTION_ACTIVATED
from name_not_found_exception import NameNotFoundException
from order_wrapper_bonus import (OrderWrapperBonus,
                                 OrderWrapperBonusMilk,
                                 OrderWrapperBonusViolet,
                                 OrderWrapperBonusEspresso,
                                 OrderWrapperBonusRuby)
from order_wrapper import OrderWrapperRegular, OrderWrapper
from chocolate_type import ChocolateType


# TODO: Write tests
class OrderWrapperFactory:
    def __init__(self, flavors=ChocolateType):
        self.flavors = flavors
        self.types = [chocolate.name for chocolate in flavors]
        self.promotion_wrappers_dict = {
            flavors.milk.name: OrderWrapperBonusMilk,
            flavors.violet.name: OrderWrapperBonusViolet,
            flavors.espresso.name: OrderWrapperBonusEspresso,
            flavors.ruby.name: OrderWrapperBonusRuby
        }

    def _get_promotion_wrapper(self, order_type) -> OrderWrapperBonus:
        return self.promotion_wrappers_dict[order_type]

    def wrap_order(self, order) -> OrderWrapper:
        if (BONUS_PROMOTION_ACTIVATED and
                order.type in self.promotion_wrappers_dict.keys()):
            return self._get_promotion_wrapper(order.type)(order)
        elif order.type in self.types:
            return OrderWrapperRegular(order)
        else:
            raise NameNotFoundException(order.type)
