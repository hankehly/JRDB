import datetime
import os

from django.forms import model_to_dict

from jrdb.models import choices, Trainer
from jrdb.tests.base import JRDBTestCase, SAMPLES_DIR
from jrdb.templates import CZA


class CYBTestCase(JRDBTestCase):
    fixtures = ["racetrack"]

    def setUp(self) -> None:
        template_path = os.path.join(SAMPLES_DIR, "CSA020907.txt")
        t = CZA(template_path).extract()

        # only import the first row to make
        # test record easy to identify
        t.df = t.df.iloc[0].to_frame().T
        t.load()

        self.trainer = Trainer.objects.first()

    def test_load_trainer(self):
        act = model_to_dict(self.trainer)

        exp = {
            "code": "10085",
            "retired_on": None,
            "name": "成宮明光",
            "name_kana": "ナルミヤ アキミツ",
            "name_abbr": "成 宮",
            "area": choices.AREA.KANTOU,
            "training_center_name": "美浦",
            "birthday": datetime.date(1935, 11, 2),
            "lic_acquired_yr": 1964,
            "jrdb_comment": "人気薄でも厩舎指数がプラスなら複勝圏内。",
            "jrdb_comment_date": datetime.date(2002, 8, 15),
            "cur_yr_leading": 61,
            "cur_yr_flat_r": [6, 8, 7, 134],
            "cur_yr_obst_r": [1, 3, 1, 5],
            "cur_yr_sp_wins": 0,
            "cur_yr_hs_wins": 0,
            "prev_yr_leading": 54,
            "prev_yr_flat_r": [13, 14, 14, 195],
            "prev_yr_obst_r": [0, 0, 0, 8],
            "prev_yr_sp_wins": 0,
            "prev_yr_hs_wins": 0,
            "sum_flat_r": [675, 659, 688, 5560],
            "sum_obst_r": [30, 27, 24, 177],
            "jrdb_saved_on": datetime.date(2002, 9, 7),
        }
        self.assertSubDict(exp, act)

    def test_load_trainer_do_nothing_where_past_results(self):
        template_path = os.path.join(SAMPLES_DIR, "CSA010907.txt")
        t = CZA(template_path).extract()
        t.df = t.df.iloc[0].to_frame().T
        t.load()

        exp = self.trainer.jrdb_saved_on
        act = Trainer.objects.first().jrdb_saved_on

        self.assertEqual(exp, act)
