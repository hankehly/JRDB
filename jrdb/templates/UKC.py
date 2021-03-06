from ..models import choices
from .item import (
    IntegerItem,
    StringItem,
    ChoiceItem,
    DateItem,
    ForeignKeyItem,
    BooleanItem,
)
from .template import Template, startswith


def where(stmt):
    return (stmt.table.c.jrdb_saved_on == None) | (  # noqa: E711
        stmt.excluded.jrdb_saved_on >= stmt.table.c.jrdb_saved_on
    )


class UKC(Template):
    """
    http://www.jrdb.com/program/Ukc/ukc_doc.txt
    """

    description = "JRDB馬基本データ（UKC）"
    items = [
        StringItem("血統登録番号", 8, 0, "jrdb.Horse.pedigree_reg_num"),
        StringItem("馬名", 36, 8, "jrdb.Horse.name"),
        ChoiceItem("性別コード", 1, 44, "jrdb.Horse.sex", choices.SEX.options()),
        ChoiceItem(
            "毛色コード", 2, 45, "jrdb.Horse.hair_color", choices.HAIR_COLOR.options()
        ),
        ChoiceItem(
            "馬記号コード", 2, 47, "jrdb.Horse.symbol", choices.HORSE_SYMBOL.options()
        ),
        StringItem("父馬名", 36, 49, "jrdb.Horse.sire_name"),
        StringItem("母馬名", 36, 85, "jrdb.Horse.dam_name"),
        StringItem("母父馬名", 36, 121, "jrdb.Horse.damsire_name"),
        DateItem("生年月日", 8, 157, "jrdb.Horse.birthday"),
        IntegerItem("父馬生年", 4, 165, "jrdb.Horse.sire_birth_yr"),
        IntegerItem("母馬生年", 4, 169, "jrdb.Horse.dam_birth_yr"),
        IntegerItem("母父馬生年", 4, 173, "jrdb.Horse.damsire_birth_yr"),
        StringItem("馬主名", 40, 177, "jrdb.Horse.owner_name"),
        ForeignKeyItem(
            "馬主会コード", 2, 217, "jrdb.Horse.owner_racetrack", "jrdb.Racetrack.code"
        ),
        StringItem("生産者名", 40, 219, "jrdb.Horse.breeder_name"),
        StringItem("産地名", 8, 259, "jrdb.Horse.breeding_loc_name"),
        BooleanItem("登録抹消フラグ", 1, 267, "jrdb.Horse.is_retired"),
        DateItem("データ年月日", 8, 268, "jrdb.Horse.jrdb_saved_on"),
        ForeignKeyItem(
            "父系統コード", 4, 276, "jrdb.Horse.pedigree_sire", "jrdb.Pedigree.key"
        ),
        ForeignKeyItem(
            "母父系統コード", 4, 280, "jrdb.Horse.pedigree_damsire", "jrdb.Pedigree.key"
        ),
    ]

    def load(self):
        df = self.transform.pipe(startswith, "horse__", rename=True)
        self.loader_cls(df, "jrdb.Horse").load(where=where)
