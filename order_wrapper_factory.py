from constants import BONUS_PROMOTION_ACTIVATED
from order_wrapper_bonus import (OrderWrapperBonusMilk,
                                 OrderWrapperBonusViolet,
                                 OrderWrapperBonusEspresso,
                                 OrderWrapperBonusRuby)
from order_wrapper import OrderWrapperRegular
from chocolate_type import ChocolateType


class OrderWrapperFactory:

    def _get_promotion_wrapper(self, order_type):
        promotion_wrappers = {
            ChocolateType.milk.name: OrderWrapperBonusMilk,
            ChocolateType.violet.name: OrderWrapperBonusViolet,
            ChocolateType.espresso.name: OrderWrapperBonusEspresso,
            ChocolateType.ruby.name: OrderWrapperBonusRuby
        }

        return promotion_wrappers[order_type]

    def wrap_order(self, order):
        if BONUS_PROMOTION_ACTIVATED:
            return self._get_promotion_wrapper(order.type)(order)
        else:
            return OrderWrapperRegular(order)
