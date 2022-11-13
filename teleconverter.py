import math


class TelecomUnit(object):
    """Abstract class representing a Telecommunication Unit."""

    def __init__(self, value: float, symbol: str) -> None:
        super(TelecomUnit, self).__init__()
        self.value = value
        self.symbol = symbol

    def __str__(self) -> str:
        return f'{self.value} {self.symbol}'

    def __repr__(self) -> str:
        return str(self)

    def to_dbm(self) -> any:
        """Returns the value converted in dBm."""
        pass  # NOTE: should be implemented by subclasses


class DBM(TelecomUnit):
    def __init__(self, value: float) -> None:
        super().__init__(value, "dBm")

    def to_dbm(self) -> TelecomUnit:
        return self


class DB(TelecomUnit):
    def __init__(self, value: float) -> None:
        super().__init__(value, "dB")

    def to_dbm(self) -> DBM:
        return DBM(self.value + 30)


class DBU(TelecomUnit):
    def __init__(self, value: float) -> None:
        super().__init__(value, "dBu")

    def to_dbm(self) -> DBM:
        pass  # TODO


class DBW(TelecomUnit):
    def __init__(self, value: float) -> None:
        super().__init__(value, "dBW")

    def to_dbm(self) -> DBM:
        pass  # TODO


class Linear(TelecomUnit):
    def __init__(self, value: float) -> None:
        super().__init__(value, "")

    def to_dbm(self) -> DBM:
        pass  # TODO


class Watt(TelecomUnit):

    def __init__(self, value: float) -> None:
        super().__init__(value, "W")

    def to_dbm(self) -> DBM:
        return DBM(10 * math.log10(self.value / 1000))

    def to_miliwatts(self) -> TelecomUnit:
        return MiliWatt(self.value * 1000)

    def to_kilowatts(self) -> TelecomUnit:
        return KiloWatt(self.value / 1000)


class MiliWatt(TelecomUnit):
    def __init__(self, value: float) -> None:
        super().__init__(value, "mW")

    def to_dbm(self) -> DBM:
        return self.to_watts().to_dbm()

    def to_watts(self) -> Watt:
        return Watt(self.value / 1000)


class KiloWatt(TelecomUnit):
    def __init__(self, value: float) -> None:
        super().__init__(value, "kW")

    def to_dbm(self) -> DBM:
        return self.to_watts().to_dbm()

    def to_watts(self) -> Watt:
        return Watt(self.value * 1000)


class Teleconverter(object):
    def __init__(self, value: TelecomUnit) -> None:
        super(Teleconverter, self).__init__()
        self._dbm_real_value = value.to_dbm().value
        self._value = value

    @property
    def value(self) -> TelecomUnit:
        return self._value

    def db(self) -> DB:
        return DB(self._dbm_real_value - 30)

    def dbm(self) -> DBM:
        return self._dbm_real_value

    def watts(self) -> Watt:
        return Watt(1000 * (10 ** (self._dbm_real_value / 10)))

    def miliwatts(self) -> MiliWatt:
        return self.to_watts().to_miliwatts()

    def kilowatts(self) -> KiloWatt:
        return self.to_watts().to_kilowatts()

    def dbu(self) -> DBU:
        pass  # TODO

    def linear(self) -> Linear:
        pass  # TODO

    def dbw(self) -> DBW:
        pass  # TODO

    @classmethod
    def db_from_potency(cls, p0: Watt, p1: Watt) -> DB:
        """Retorna o valor em dB através da relação entre duas pontências,
        `p0` de entrada e `p1` de saída."""
        return DB(10 * math.log10(p1.value / p0.value))
