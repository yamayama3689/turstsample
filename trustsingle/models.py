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
trust single
"""

class Constants(BaseConstants):
    name_in_url = 'trustsingle'
    players_per_group = None
    num_rounds = 1

    endowment = c(30)
    multiplier = 2

    instructions_template = 'trustsingle/instructions.html'

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass
    

class Player(BasePlayer):
    sent_amount = models.CurrencyField(
        min=c(0),
        max=Constants.endowment,
        doc="""Amount sent by P1""",
        label="How much do you want to send to participant robot?",
    )

    """ sent_back_amount = models.CurrencyField(
        doc=Amount sent back by P2, label="How much do you want to send back?"
    )
 """
    def sent_back_amount_choices(self):
        return currency_range(c(0), self.sent_amount * Constants.multiplier, c(1))

    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        #p2 = self.get_player_by_id(2)
        p1.payoff = Constants.endowment - self.sent_amount + self.sent_back_amount
        #p2.payoff = self.sent_amount * Constants.multiplier - self.sent_back_amount
