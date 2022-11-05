import math

class TelecomMetric(object):
    """Abstract class representing a Telecommunication Metric."""

    def __init__(self, value: float, symbol: str) -> None:
        super(TelecomMetric, self).__init__()
        self.value = value
        self.symbol = symbol

    def __str__(self) -> str:
        return f'{self.value} {self.symbol}'

    def __repr__(self) -> str:
        return str(self)

    def db_value(self) -> float:
        """Returns the value converted in db."""
        pass

class DB(TelecomMetric):
    def __init__(self, value: float) -> None:
        super().__init__(value, "dB")

    def db_value(self) -> float:
        return self.value

class DBM(TelecomMetric):
    def __init__(self, value: float) -> None:
        super().__init__(value, "dBm")

    def db_value(self) -> float:
        return self.value - 30

class DBU(TelecomMetric):
    def __init__(self, value: float) -> None:
        super().__init__(value, "dBu")

    def db_value(self) -> float:
        pass #TODO

class DBA(TelecomMetric):
    def __init__(self, value: float) -> None:
        super().__init__(value, "dBa")

    def db_value(self) -> float:
        pass #TODO

class DBR(TelecomMetric):
    def __init__(self, value: float) -> None:
        super().__init__(value, "dBr")

    def db_value(self) -> float:
        pass #TODO

class Watt(TelecomMetric):
    def __init__(self, value: float) -> None:
        super().__init__(value, "W")

    def db_value(self) -> float:
        pass #TODO

class MiliWatt(TelecomMetric):
    def __init__(self, value: float) -> None:
        super().__init__(value, "mW")

    def db_value(self) -> float:
        pass #TODO

class Telecalculator(object):
    @classmethod
    def db_from_potency(cls, p0: Watt, p1: Watt) -> DB:
        """Retorna o valor em dB através da relação entre duas pontências,
        `p0` de entrada e `p1` de saída."""
        return DB(10 * math.log10(p1.value / p0.value))

class Teleconverter(object):
    def __init__(self, value: TelecomMetric) -> None:
        super(Teleconverter, self).__init__()
        self.value = value

    def to_db(self) -> DB:
        return DB(self.value.db_value())

    def to_dbm(self) -> DBM:
        return DBM(self.value.db_value() + 30)

    def to_dbu(self) -> DBU:
        pass # TODO

    def to_dbr(self) -> DBR:
        pass # TODO

    def to_dba(self) -> DBR:
        pass # TODO