from .units import *
import math


class Teleconvert(object):
    @classmethod
    def to_self(cls, value: TelecomUnit) -> TelecomUnit:
        return value

    @classmethod
    def db_to_dbm(cls, db: DB) -> DBM:
        return DBM(db.value + 30)

    @classmethod
    def db_to_bell(cls, db: DB) -> Bell:
        return Bell(db.value / 10)

    @classmethod
    def bell_to_db(cls, bell: Bell) -> DB:
        return DB(bell.value * 10)

    @classmethod
    def dbm_to_db(cls, dbm: DBM) -> DB:
        return DB(dbm.value - 30)

    @classmethod
    def dbm_to_watt(cls, dbm: DBM) -> Watt:
        return Watt(10 ** (dbm.value / 10 - 3))

    @classmethod
    def dbm_to_dbw(cls, dbm: DBM) -> DBW:
        return DBW(dbm.value - 30)

    @classmethod
    def dbw_to_dbm(cls, dbw: DBW) -> DBM:
        return DBM(dbw.value + 30)

    @classmethod
    def dbw_to_watt(cls, dbw: DBW) -> Watt:
        return Watt(10 ** (dbw.value / 10))

    @classmethod
    def watt_to_kilowatt(cls, watt: Watt) -> KiloWatt:
        return KiloWatt(watt.value / 1000)

    @classmethod
    def watt_to_miliwatt(cls, watt: Watt) -> MiliWatt:
        return MiliWatt(watt.value * 1000)

    @classmethod
    def watt_to_dbw(cls, watt: Watt) -> DBW:
        return DBW(10 * math.log10(watt.value))

    @classmethod
    def miliwatt_to_watt(cls, miliwatt: MiliWatt) -> Watt:
        return Watt(miliwatt.value / 1000)

    @classmethod
    def kilowatt_to_watt(cls, kilowatt: KiloWatt) -> Watt:
        return Watt(kilowatt.value * 1000)

    @classmethod
    def watt_to_dbm(cls, watt: Watt) -> DBM:
        return cls.dbw_to_dbm(cls.watt_to_dbw(watt))

    @classmethod
    def dbm_to_bell(cls, dbm: DBM) -> Bell:
        return cls.db_to_bell(cls.dbm_to_db(dbm))

    @classmethod
    def dbm_to_miliwatt(cls, dbm: DBM) -> MiliWatt:
        return cls.watt_to_miliwatt(cls.dbm_to_watt(dbm))

    @classmethod
    def dbm_to_kilowatt(cls, dbm: DBM) -> KiloWatt:
        return cls.watt_to_kilowatt(cls.dbm_to_watt(dbm))

    @classmethod
    def dbw_to_kilowatt(cls, dbw: DBW) -> KiloWatt:
        return cls.watt_to_kilowatt(cls.dbw_to_watt(dbw))

    @classmethod
    def dbw_to_miliwatt(cls, dbw: DBW) -> KiloWatt:
        return cls.watt_to_miliwatt(cls.dbw_to_watt(dbw))

    @classmethod
    def bell_to_dbm(cls, bell: Bell) -> DBM:
        return cls.db_to_dbm(cls.bell_to_db(bell))


CONVERTION_MAPPER: dict[str, dict[str, any]] = {
    constants.DB_SYMBOL: {
        constants.DB_SYMBOL: Teleconvert.to_self,
        constants.DBM_SYMBOL: Teleconvert.db_to_dbm,
        constants.BELL_SYMBOL: Teleconvert.db_to_bell,
    },
    constants.DBM_SYMBOL: {
        constants.DBM_SYMBOL: Teleconvert.to_self,
        constants.DB_SYMBOL: Teleconvert.dbm_to_db,
        constants.DBW_SYMBOL: Teleconvert.dbm_to_dbw,
        constants.BELL_SYMBOL: Teleconvert.dbm_to_bell,
        constants.MILIWATT_SYMBOL: Teleconvert.dbm_to_miliwatt,
        constants.KILOWATT_SYMBOL: Teleconvert.dbm_to_kilowatt,
        constants.WATT_SYMBOL: Teleconvert.dbm_to_watt,
    },
    constants.DBW_SYMBOL: {
        constants.DBW_SYMBOL: Teleconvert.to_self,
        constants.DBM_SYMBOL: Teleconvert.dbw_to_dbm,
        constants.MILIWATT_SYMBOL: Teleconvert.dbw_to_miliwatt,
        constants.KILOWATT_SYMBOL: Teleconvert.dbw_to_kilowatt,
        constants.WATT_SYMBOL: Teleconvert.dbw_to_watt,
    },
    constants.BELL_SYMBOL: {
        constants.BELL_SYMBOL: Teleconvert.to_self,
        constants.DB_SYMBOL: Teleconvert.bell_to_db,
        constants.DBM_SYMBOL: Teleconvert.bell_to_dbm,
    },
    constants.WATT_SYMBOL: {
        constants.WATT_SYMBOL: Teleconvert.to_self,
        constants.KILOWATT_SYMBOL: Teleconvert.watt_to_kilowatt,
        constants.MILIWATT_SYMBOL: Teleconvert.watt_to_miliwatt,
        constants.DBM_SYMBOL: Teleconvert.watt_to_dbm,
        constants.DBW_SYMBOL: Teleconvert.watt_to_dbw,
    },
    # TODO: finish KiloWatt, MiliWatt, Volt, MiliVolt, KiloVolt, DBR, DBU, etc.
}
