from typing import TypeVar

Self = TypeVar('Self')


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
        T = type(self)
        if isinstance(other, T):
            return T(self._value + other._value)
        raise ValueError()

    def __sub__(self, other: Self) -> Self:
        T = type(self)
        if isinstance(other, T):
            return Watt(self._value - other._value)
        raise ValueError()

    def __truediv__(self, other: Self) -> Self:
        T = type(self)
        if isinstance(other, T):
            return T(self._value / other._value)
        raise ValueError()

    def __mul__(self, other: Self) -> Self:
        T = type(self)
        if isinstance(other, T):
            return T(self._value * other._value)
        raise ValueError()

    def __lt__(self, other: Self) -> bool:
        T = type(self)
        if isinstance(other, T):
            return self._value < other._value
        raise ValueError()

    def __le__(self, other: Self) -> bool:
        T = type(self)
        if isinstance(other, T):
            return self._value <= other._value
        raise ValueError()

    def __gt__(self, other: Self) -> bool:
        T = type(self)
        if isinstance(other, T):
            return self._value > other._value
        raise ValueError()

    def __ge__(self, other: Self) -> bool:
        T = type(self)
        if isinstance(other, T):
            return self._value >= other._value
        raise ValueError()


class DB(TelecomUnit):
    def __init__(self, value: float) -> None:
        super().__init__(value, "dB")


class Bell(DB):
    def __init__(self, value: float) -> None:
        super().__init__(value * 10)
        self._symbol = "B"

    @property
    def value(self) -> float:
        return super().value / 10


class DBM(DB):
    def __init__(self, value: float) -> None:
        super().__init__(value - 30)
        self._symbol = f'{self._symbol}M'

    @property
    def value(self) -> float:
        return super().value + 30


class DBW(TelecomUnit):
    def __init__(self, value: float) -> None:
        super().__init__(value, "dBW")


class DBU(TelecomUnit):
    def __init__(self, value: float) -> None:
        super().__init__(value, "dBU")


class DBR(TelecomUnit):
    def __init__(self, value: float) -> None:
        super().__init__(value, "dBR")


class Linear(TelecomUnit):
    def __init__(self, value: float) -> None:
        super().__init__(value, "")


class Volt(TelecomUnit):
    def __init__(self, value: float) -> None:
        super().__init__(value, "V")


class MiliVolt(TelecomUnit):
    def __init__(self, value: float, symbol: str) -> None:
        super().__init__(value, symbol)


class Watt(TelecomUnit):

    def __init__(self, value: float) -> None:
        super().__init__(value, "W")


class MiliWatt(Watt):
    def __init__(self, value: float) -> None:
        super().__init__(value / 1000)
        self._symbol = f'm{self._symbol}'

    @property
    def value(self) -> float:
        return super().value * 1000


class KiloWatt(Watt):
    def __init__(self, value: float) -> None:
        super().__init__(value * 1000)
        self._symbol = f'k{self._symbol}'

    @property
    def value(self) -> float:
        return super().value / 1000
