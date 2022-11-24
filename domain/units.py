from typing import TypeVar
Self = TypeVar('Self')

from . import constants


class TelecomUnit(object):
    """Abstract class representing some unit in the area of telecommunication."""

    def __init__(self, value: float, symbol: str) -> None:
        super(TelecomUnit, self).__init__()
        self._value = value
        self._symbol = symbol

    @property
    def value(self) -> float:
        return self._value

    @property
    def symbol(self) -> str:
        return self._symbol

    def __str__(self) -> str:
        return f'{self.value} {self.symbol}'

    def __repr__(self) -> str:
        return str(self)

    def __add__(self, other: Self) -> Self:
        if isinstance(other, T := type(self)) or isinstance(self, T := type(other)):
            return T(self._value + other._value)
        raise ValueError()

    def __sub__(self, other: Self) -> Self:
        if isinstance(other, T := type(self)) or isinstance(self, T := type(other)):
            return T(self._value - other._value)
        raise ValueError()

    def __truediv__(self, other: Self) -> Self:
        if isinstance(other, T := type(self)) or isinstance(self, T := type(other)):
            return T(self._value / other._value)
        raise ValueError()

    def __mul__(self, other: Self) -> Self:
        if isinstance(other, T := type(self)) or isinstance(self, T := type(other)):
            return T(self._value * other._value)
        raise ValueError()

    def __lt__(self, other: Self) -> bool:
        if isinstance(other, type(self)) or isinstance(self, type(other)):
            return self._value < other._value
        raise ValueError()

    def __le__(self, other: Self) -> bool:
        if isinstance(other, type(self)) or isinstance(self, type(other)):
            return self._value <= other._value
        raise ValueError()

    def __gt__(self, other: Self) -> bool:
        if isinstance(other, type(self)) or isinstance(self, type(other)):
            return self._value > other._value
        raise ValueError()

    def __ge__(self, other: Self) -> bool:
        if isinstance(other, type(self)) or isinstance(self, type(other)):
            return self._value >= other._value
        raise ValueError()


class DBM(TelecomUnit):
    def __init__(self, value: float) -> None:
        super().__init__(value, constants.DBM_SYMBOL)


class Bell(DBM):
    def __init__(self, value: float) -> None:
        super().__init__(10 * value + 30)

    @property
    def symbol(self) -> str:
        return constants.BELL_SYMBOL

    @property
    def value(self) -> float:
        return (super().value - 30) / 10


class DB(DBM):
    def __init__(self, value: float) -> None:
        super().__init__(value + 30)

    @property
    def symbol(self) -> str:
        return constants.DB_SYMBOL

    @property
    def value(self) -> float:
        return super().value - 30


class DBW(TelecomUnit):
    def __init__(self, value: float) -> None:
        super().__init__(value, constants.DBW_SYMBOL)


class DBU(TelecomUnit):
    def __init__(self, value: float) -> None:
        super().__init__(value, constants.DBU_SYMBOL)


class DBR(TelecomUnit):
    def __init__(self, value: float) -> None:
        super().__init__(value, constants.DB_SYMBOL)


class Linear(TelecomUnit):
    def __init__(self, value: float) -> None:
        super().__init__(value, "")


class Volt(TelecomUnit):
    def __init__(self, value: float) -> None:
        super().__init__(value, constants.VOLT_SYMBOL)


class MiliVolt(Volt):
    def __init__(self, value: float) -> None:
        super().__init__(value / 1000)

    @property
    def symbol(self) -> str:
        return constants.MILIVOLT_SYMBOL

    @property
    def value(self) -> float:
        return super().value * 1000


class KiloVolt(Volt):
    def __init__(self, value: float) -> None:
        super().__init__(value * 1000)

    @property
    def symbol(self) -> str:
        return constants.KILOVOLT_SYMBOL

    @property
    def value(self) -> float:
        return super().value / 1000


class Watt(TelecomUnit):
    def __init__(self, value: float) -> None:
        super().__init__(value, constants.WATT_SYMBOL)


class MiliWatt(Watt):
    def __init__(self, value: float) -> None:
        super().__init__(value / 1000)

    @property
    def symbol(self) -> str:
        return constants.MILIWATT_SYMBOL

    @property
    def value(self) -> float:
        return super().value * 1000


class KiloWatt(Watt):
    def __init__(self, value: float) -> None:
        super().__init__(value * 1000)

    @property
    def symbol(self) -> str:
        return constants.KILOWATT_SYMBOL

    @property
    def value(self) -> float:
        return super().value / 1000


units_mapper: dict[str, TelecomUnit] = {
    constants.BELL_SYMBOL: Bell,
    constants.DB_SYMBOL: DB,
    constants.DBM_SYMBOL: DBM,
    constants.DBU_SYMBOL: DBU,
    constants.DBW_SYMBOL: DBW,
    constants.DBR_SYMBOL: DBR,
    constants.WATT_SYMBOL: Watt,
    constants.KILOWATT_SYMBOL: KiloWatt,
    constants.MILIWATT_SYMBOL: MiliWatt,
    constants.VOLT_SYMBOL: Volt,
    constants.KILOVOLT_SYMBOL: KiloVolt,
    constants.MILIVOLT_SYMBOL: MiliVolt,
}
