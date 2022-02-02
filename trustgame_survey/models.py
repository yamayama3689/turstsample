from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

from settings import PARTICIPANT_FIELDS


doc = """
trust survey
"""


class Constants(BaseConstants):
    name_in_url = 'trustgame_survey'
    players_per_group = 2
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    num = models.StringField(label='''実験者IDを入力してください(半角英数字)''' )
    age = models.StringField(label='''年齢を入力してください（半角英数字）''')
    thanks = models.IntegerField(
        choices=[1,2,3,4,5,6,7],
        label='取引相手に対してどの程度感謝を抱いていますか？',
        widget=widgets.RadioSelect,
    )
