from .item import ForeignKeyItem, IntegerItem, StringItem, ArrayItem
from .loader import ProgramRaceLoadMixin
from .template import Template


class SRB(Template, ProgramRaceLoadMixin):
    """
    http://www.jrdb.com/program/Srb/srb_doc.txt
    """
    name = 'JRDB成績レースデータ（SRB）'
    items = [
        ForeignKeyItem('場コード', 2, 0, 'jrdb.Program.racetrack', 'jrdb.Racetrack.code'),
        IntegerItem('年', 2, 2, 'jrdb.Program.yr'),
        IntegerItem('回', 1, 4, 'jrdb.Program.round'),
        StringItem('日', 1, 5, 'jrdb.Program.day'),
        IntegerItem('Ｒ', 2, 6, 'jrdb.Race.num'),

        # TODO:
        ArrayItem('ハロンタイム', 3 * 18, 8, 'jrdb.Race.furlong_times', size=18, mapper=lambda n: round(n * 0.1, 1)),
        # ArrayItem('１コーナー', 64, 62, 'jrdb.Race.c1pos', ),
        # ArrayItem('２コーナー', 64, 126, 'jrdb.Race.c2pos', ),
        # ArrayItem('３コーナー', 64, 190, 'jrdb.Race.c3pos', ),
        # ArrayItem('４コーナー', 64, 254, 'jrdb.Race.c4pos', ),
        # ArrayItem('ペースアップ位置', 2, 318, 'jrdb.Race.pace_up_pos', ),

        ArrayItem('トラックバイアス（１角）', 3, 320, 'jrdb.Race.c1_track_bias', 3),
        ArrayItem('トラックバイアス（２角）', 3, 323, 'jrdb.Race.c2_track_bias', 3),
        ArrayItem('トラックバイアス（向正）', 3, 326, 'jrdb.Race.bs_track_bias', 3),
        ArrayItem('トラックバイアス（３角）', 3, 329, 'jrdb.Race.c3_track_bias', 3),
        ArrayItem('トラックバイアス（４角）', 5, 332, 'jrdb.Race.c4_track_bias', 5),
        ArrayItem('トラックバイアス（直線）', 5, 337, 'jrdb.Race.hs_track_bias', 5),
        StringItem('レースコメント', 500, 342, 'jrdb.Race.comment'),
    ]
