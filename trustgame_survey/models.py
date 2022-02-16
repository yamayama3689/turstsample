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
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    idnum = models.IntegerField(label='''実験者IDを入力してください(半角数字)''' )
    age = models.IntegerField(label='''年齢を入力してください（半角数字）''')
    gender = models.IntegerField(
        choices=[
            [1, '女性'],
            [2, '男性'],
            [3, 'その他']
        ],
        label='''性別を選択してください（半角数字）''')
    date = models.IntegerField(
        choices=[
            [1, '2月17日14:00~'],
            [2, '2月18日14:00~'],
            [3, '2月18日20:00~'],
            [4, '2月21日14:00~'],
            [5, '2月21日20:00~'],
            [6, '2月22日14:00~']],
        label='実験に参加した日時を選択してください',
        widget=widgets.RadioSelect,
    )
