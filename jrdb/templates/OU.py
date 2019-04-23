import logging

from .item import ForeignKeyItem, IntegerItem, StringItem, ArrayItem
from .template import Template, RacePersistMixin

logger = logging.getLogger(__name__)


class OU(Template, RacePersistMixin):
    """
    http://www.jrdb.com/program/Ou/Oudata_doc.txt
    """
    name = '馬単基準オッズデータ（OU）'
    items = [
        ForeignKeyItem('場コード', 2, 0, 'jrdb.Race.racetrack', 'jrdb.Racetrack.code'),
        IntegerItem('年', 2, 2, 'jrdb.Race.yr'),
        IntegerItem('回', 1, 4, 'jrdb.Race.round'),
        StringItem('日', 1, 5, 'jrdb.Race.day'),
        IntegerItem('Ｒ', 2, 6, 'jrdb.Race.num'),
        IntegerItem('登録頭数', 2, 8, 'jrdb.Race.contender_count'),
        ArrayItem('馬単オッズ', 6 * 306, 10, 'jrdb.Race.odds_exacta', 306),
    ]
