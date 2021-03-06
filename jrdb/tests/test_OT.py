import os

from django.forms import model_to_dict

from jrdb.models import Program, Race
from jrdb.tests.base import JRDBTestCase, SAMPLES_DIR
from jrdb.templates import OT


class OTTestCase(JRDBTestCase):
    fixtures = ["racetrack"]

    @classmethod
    def setUpTestData(cls):
        template_path = os.path.join(SAMPLES_DIR, "OT020908.txt")
        t = OT(template_path).extract()

        # only import the first row to make
        # test record easy to identify
        t.df = t.df.iloc[0].to_frame().T
        t.load()

        cls.program = Program.objects.first()
        cls.race = Race.objects.first()

    def test_load_program(self):
        act = model_to_dict(self.program)
        exp = {"racetrack": 1, "yr": 2, "round": 2, "day": "2"}
        self.assertSubDict(exp, act)

    def test_load_race(self):
        act = model_to_dict(self.race)
        exp = {"num": 1, "contender_count": 13}
        self.assertSubDict(exp, act)

        self.assertEqual(len(self.race.odds_trio), 816)
        self.assertEqual(self.race.odds_trio[0], 232.5)
        self.assertEqual(self.race.odds_trio[408], 182.3)
        self.assertEqual(self.race.odds_trio[815], None)
