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


doc = """
Simple trust game
"""


class Constants(BaseConstants):
    name_in_url = 'trust_simple'
    players_per_group = 2
    num_rounds = 10

    endowment = c(10)
    multiplier = 3

    instructions_template = 'trust_simple/instructions.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    sent_amount = models.CurrencyField(
        min=c(0),
        max=Constants.endowment,
        doc="""Amount sent by P1""",
        label="参加者Bにいくら送りますか?",
    )

    sent_back_amount = models.CurrencyField(
        doc="""Amount sent back by P2""", label="いくら送り返しますか?"
    )

    thanks = models.IntegerField(
        choices=[1,2,3,4,5,6,7],
        label='取引相手に対してどの程度「感謝」の気持ちを抱いていますか？',
        widget=widgets.RadioSelect,
    )

    anger = models.IntegerField(
        choices=[1,2,3,4,5,6,7],
        label='取引相手に対してどの程度「怒り」の気持ちを抱いていますか？',
        widget=widgets.RadioSelect,
    )

    def sent_back_amount_choices(self):
        return currency_range(c(0), self.sent_amount * Constants.multiplier, c(1))

    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p1.payoff = Constants.endowment - self.sent_amount + self.sent_back_amount
        p2.payoff = self.sent_amount * Constants.multiplier - self.sent_back_amount


class Player(BasePlayer):
    pass