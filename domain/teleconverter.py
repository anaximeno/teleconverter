import math
from .units import *


class Teleconvert(object):

    @classmethod
    def db_to_dbm(cls, db: DB) -> DBM:
        return DBM(db.value + 30)

    @classmethod
    def dbm_to_db(cls, dbm: DBM) -> DB:
        return DB(dbm.value - 30)

    # TODO: add more convertions
