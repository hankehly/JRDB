from django.core.validators import validate_comma_separated_integer_list
from django.db import models

from jrdb.models import BaseModel
from jrdb.models.choices import (
    PACE_CATEGORY,
    RACE_CATEGORY,
    RACE_HORSE_SEX_SYMBOL,
    RACE_HORSE_TYPE_SYMBOL,
    RACE_INTERLEAGUE_SYMBOL,
    IMPOST_CLASS,
    GRADE,
    TRACK_CONDITION,
    WEATHER
)


class Race(BaseModel):
    OTHER = 'OTHER'

    TURF = 'TURF'
    DIRT = 'DIRT'
    OBSTACLE = 'OBSTACLE'
    SURFACE_CHOICES = (
        (TURF, '芝'),
        (DIRT, 'ダート'),
        (OBSTACLE, '障害'),
    )

    RIGHT = 'RIGHT'
    LEFT = 'LEFT'
    STRAIGHT = 'STRAIGHT'
    DIRECTION_CHOICES = (
        (RIGHT, '右'),
        (LEFT, '左'),
        (STRAIGHT, '直'),
        (OTHER, '他'),
    )

    INSIDE = 'INSIDE'
    OUTSIDE = 'OUTSIDE'
    STRAIGHT_DIRT = 'STRAIGHT_DIRT'
    COURSE_INOUT_CHOICES = (
        (INSIDE, '通常(内)'),
        (OUTSIDE, '外'),
        (STRAIGHT_DIRT, '直ダ'),
        (OTHER, '他'),
    )

    A = 'A'
    A1 = 'A1'
    A2 = 'A2'
    B = 'B'
    C = 'C'
    D = 'D'
    COURSE_LABEL_CHOICES = (
        (A, 'A'),
        (A1, 'A1'),
        (A2, 'A2'),
        (B, 'B'),
        (C, 'C'),
        (D, 'D'),
    )

    # key related data
    racetrack = models.ForeignKey('jrdb.Racetrack', on_delete=models.CASCADE)
    yr = models.PositiveSmallIntegerField()
    round = models.PositiveSmallIntegerField()
    day = models.PositiveSmallIntegerField()
    num = models.PositiveSmallIntegerField()

    # codes
    category = models.CharField(max_length=255, choices=RACE_CATEGORY.CHOICES, null=True)
    cond = models.ForeignKey('jrdb.RaceConditionCode', on_delete=models.CASCADE, null=True)
    horse_sex_symbol = models.CharField(max_length=255, choices=RACE_HORSE_SEX_SYMBOL.CHOICES, null=True)
    horse_type_symbol = models.CharField(max_length=255, choices=RACE_HORSE_TYPE_SYMBOL.CHOICES, null=True)
    interleague_symbol = models.CharField(max_length=255, choices=RACE_INTERLEAGUE_SYMBOL.CHOICES,
                                          on_delete=models.CASCADE, null=True)
    impost_class = models.CharField(max_length=255, choices=IMPOST_CLASS.CHOICES, null=True)
    grade = models.CharField(max_length=255, choices=GRADE.CHOICES, null=True)
    track_cond = models.CharField(max_length=255, choices=TRACK_CONDITION.CHOICES, null=True)
    weather = models.CharField(max_length=255, choices=WEATHER.CHOICES, null=True)

    name = models.CharField(max_length=50, null=True)
    name_abbr = models.CharField(max_length=8, null=True)
    name_short = models.CharField(max_length=18, null=True)

    # composed of yr/month/date + hh/mm from separate files
    started_at = models.DateTimeField(null=True)

    distance = models.PositiveSmallIntegerField(null=True)
    surface = models.CharField(max_length=255, choices=SURFACE_CHOICES, null=True)
    direction = models.CharField(max_length=255, choices=DIRECTION_CHOICES, null=True)
    course_inout = models.CharField(max_length=255, choices=COURSE_INOUT_CHOICES, null=True)
    course_label = models.CharField(max_length=255, choices=COURSE_LABEL_CHOICES, null=True)
    comment = models.TextField(max_length=500)
    nth_occurrence = models.PositiveSmallIntegerField(null=True)

    # earnings
    p1_purse = models.PositiveSmallIntegerField(null=True)
    p2_purse = models.PositiveSmallIntegerField(null=True)
    p3_purse = models.PositiveSmallIntegerField(null=True)
    p4_purse = models.PositiveSmallIntegerField(null=True)
    p5_purse = models.PositiveSmallIntegerField(null=True)
    p1_prize = models.PositiveSmallIntegerField(null=True)
    p2_prize = models.PositiveSmallIntegerField(null=True)

    # track bias
    track_bias_1C = models.CharField(
        max_length=255,
        validators=[validate_comma_separated_integer_list],
        verbose_name='Corner 1 track bias',
        help_text='（内、中、外）',
        null=True
    )

    track_bias_2C = models.CharField(
        max_length=255,
        validators=[validate_comma_separated_integer_list],
        verbose_name='Corner 2 track bias',
        help_text='（内、中、外）',
        null=True
    )

    track_bias_3C = models.CharField(
        max_length=255,
        validators=[validate_comma_separated_integer_list],
        verbose_name='Corner 3 track bias',
        help_text='（内、中、外）',
        null=True
    )

    track_bias_4C = models.CharField(
        max_length=255,
        validators=[validate_comma_separated_integer_list],
        verbose_name='Corner 4 track bias',
        help_text='（最内、内、中、外、大外）',
        null=True
    )

    track_bias_bs = models.CharField(
        max_length=255,
        validators=[validate_comma_separated_integer_list],
        verbose_name='Backstretch track bias',
        help_text='（内、中、外）',
        null=True
    )

    track_bias_hs = models.CharField(
        max_length=255,
        validators=[validate_comma_separated_integer_list],
        verbose_name='Homestretch track bias',
        help_text='（最内、内、中、外、大外）',
        null=True
    )

    # betting ticket sales
    issued_bt_win = models.BooleanField(null=True)
    issued_bt_show = models.BooleanField(null=True)
    issued_bt_bracket_quinella = models.BooleanField(null=True)
    issued_bt_quinella = models.BooleanField(null=True)
    issued_bt_exacta = models.BooleanField(null=True)
    issued_bt_duet = models.BooleanField(null=True)
    issued_bt_trio = models.BooleanField(null=True)
    issued_bt_trifecta = models.BooleanField(null=True)

    track_speed_shift = models.SmallIntegerField(null=True)

    pace_cat = models.CharField(max_length=255, choices=PACE_CATEGORY.CHOICES)
    pace_index = models.FloatField(null=True, help_text='レースのペースを指数化したもの')
    pace_flow = models.ForeignKey('jrdb.PaceFlowCode', null=True, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('racetrack', 'yr', 'round', 'day', 'num')
