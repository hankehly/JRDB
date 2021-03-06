from .item import ForeignKeyItem, IntegerItem, StringItem, ArrayItem
from ..loaders import ProgramRaceLoadMixin
from .template import Template


class OU(Template, ProgramRaceLoadMixin):
    """
    http://www.jrdb.com/program/Ou/Oudata_doc.txt
    """

    description = "馬単基準オッズデータ（OU）"
    items = [
        ForeignKeyItem("場コード", 2, 0, "jrdb.Program.racetrack", "jrdb.Racetrack.code"),
        IntegerItem("年", 2, 2, "jrdb.Program.yr"),
        IntegerItem("回", 1, 4, "jrdb.Program.round"),
        StringItem("日", 1, 5, "jrdb.Program.day"),
        IntegerItem("Ｒ", 2, 6, "jrdb.Race.num"),
        IntegerItem("登録頭数", 2, 8, "jrdb.Race.contender_count"),
        ArrayItem("馬単オッズ", 6 * 306, 10, "jrdb.Race.odds_exacta", 306),
    ]

    def load(self) -> None:
        return self.load_programs_races()
