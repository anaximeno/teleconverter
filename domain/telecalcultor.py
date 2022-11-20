import math
from .units import *


class Telecalculator(object):
    def __init__(self) -> None:
        pass

    def db(self, p0: Watt, p1: Watt) -> DB:
        return DB(10 * math.log10(p1.value / p0.value))

    def dbm(self, p: Watt) -> DBM:
        return DBM(30 + self.db(MiliWatt(1), p))

    def dbw(self, p: Watt) -> DBW:
        return DBW(self.db(Watt(1), p))

    def dbu(self, v0: Volt, v1: Volt) -> DBU:
        """Returns the value in dBu, under the same resistance."""
        return DBU(20 * math.log10(v1.value / v0.value))

    def dbr(self, v: Volt) -> DBR:
        return self.dbu(Volt(0.775), v)