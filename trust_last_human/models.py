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
trust two
"""


class Constants(BaseConstants):
    name_in_url = 'trust_last_human'
    players_per_group = 2
    num_rounds = 1

    endowment = c(30)
    multiplier = 2

    instructions_template = 'trust_last_human/instructions.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    sent_amountP1 = models.CurrencyField(
        doc="Amount sent by P1",
        label="参加者Bにいくら送金しますか？半角数字で入力してください。",
    )

    def sent_amountP1_choices(self):
        """ choices = [c(0), self.participant.payoff, c(10)]
        return choices """
        p1 = self.get_player_by_id(1)
        return currency_range(c(0), p1.participant.payoff, c(10))
    pass

    sent_amountP2 = models.CurrencyField(
        doc="Amount sent by P2",
        label="参加者Aにいくら送金しますか？半角数字で入力してください。",
    )

    def sent_amountP2_choices(self):
        """ choices = [c(0), self.participant.payoff, c(10)]
        return choices """
        p2 = self.get_player_by_id(2)
        return currency_range(c(0), p2.participant.payoff, c(10))

    REPAYMENT = (
            (True, "返金する"),
            (False, '返金しない'),
        )

    sent_back_amountP1 = models.BooleanField(
        choices=REPAYMENT,
        doc="Amount sent back by P2", label="参加者Bからもらったお金を参加者Bに返金しますか、それともしませんか?"
    )  

    sent_back_amountP2 = models.BooleanField(
        choices=REPAYMENT,
        doc="Amount sent back by P2", label="参加者Aからもらったお金を参加者Aに返金しますか、それともしませんか?"
    ) 

    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)

        if self.sent_back_amountP2 == True:
            p1.payoff = p1.participant.payoff - self.sent_amountP1 + self.sent_amountP1 * Constants.multiplier
        elif self.sent_back_amountP1 == False:
            p1.payoff = p1.participant.payoff - self.sent_amountP1 + self.sent_amountP2 + self.sent_amountP1 * Constants.multiplier

        if self.sent_back_amountP1 == True and self.sent_back_amountP2 == True:
            last_fundsp1 = self.sent_amountP1 * Constants.multiplier - self.sent_amountP1
            last_fundsp2 = self.sent_amountP2 * Constants.multiplier - self.sent_amountP2
        elif self.sent_back_amountP1 == True and self.sent_back_amountP2 == False:
            last_fundsp1 = self.sent_amountP1 * (-1)
            last_fundsp2 = self.sent_amountP1 + self.sent_amountP2 * Constants.multiplier - self.sent_amountP2
        elif self.sent_back_amountP1 == False and self.sent_back_amountP2 == True:
            last_fundsp1 = self.sent_amountP2 + self.sent_amountP1 * Constants.multiplier - self.sent_amountP1
            last_fundsp2 = self.sent_amountP2 * (-1)
        elif self.sent_back_amountP1 == True and self.sent_back_amountP2 == True:
            last_fundsp1 = self.sent_amountP2
            last_fundsp2 = self.sent_amountP1

        if self.sent_amountP1 == 0:
            p1.payoff = p1.participant.payoff + last_fundsp1
        else:
            p1.payoff = p1.participant.payoff + last_fundsp1 -100
        if self.sent_amountP1 == 0:
            p2.payoff = p2.participant.payoff + last_fundsp2
        else:
            p2.payoff = p2.participant.payoff + last_fundsp2 -100
        

        """ p1.payoff = p1.participant.payoff - self.sent_amountP1 + self.sent_amountP2 + self.sent_amountP1 * Constants.multiplier
        p2.payoff = p2.participant.payoff - self.sent_amountP2 + self.sent_amountP1 + self.sent_amountP2 * Constants.multiplier """

    
    



class Player(BasePlayer):
   
    pass