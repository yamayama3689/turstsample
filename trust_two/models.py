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
trust two
"""


class Constants(BaseConstants):
    name_in_url = 'trust_two'
    players_per_group = 2
    num_rounds = 2

    endowment = c(30)
    multiplier = 2

    instructions_template = 'trust_two/instructions.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    sent_amountP1 = models.CurrencyField(
        min=c(0),
        max=Constants.endowment,
        doc="Amount sent by P1",
        label="参加者Bにいくら送金しますか？半角数字で入力してください。",
    )

    sent_back_amountP1 = models.CurrencyField(
        #choices=[0, sent_amount],
        #max=sent_amount * Constants.multiplier,
        doc="Amount sent back by P2", label="参加者Aからもらったお金を参加者Aに返金しますか、それともしませんか?（返金する場合、参加者Aが受け取る金額は、あなたが参加者Aからもらった金額の2倍になります。返金しない場合は、今あなたが持っている金額がそのままあなたの「収入」になります。また、初めに持っている「資金」30円は返金の原資にすることはできません。）"
    ) 

    def sent_back_amountP1_choices(self):
        #return currency_range(c(0), self.sent_amount * Constants.multiplier, c(1)) 
        choices = [c(0), self.sent_amountP1 * Constants.multiplier]
        return choices

    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p1.payoff = Constants.endowment - self.sent_amountP1 + self.sent_back_amountP1
        p2.payoff = self.sent_amountP1 * Constants.multiplier - self.sent_back_amountP1

    sent_amountP2 = models.CurrencyField(
        min=c(0),
        max=Constants.endowment,
        doc="Amount sent by P2",
        label="参加者Aにいくら送金しますか？半角数字で入力してください。",
    )

    sent_back_amountP2 = models.CurrencyField(
        #choices=[0, sent_amount],
        #max=sent_amount * Constants.multiplier,
        doc="Amount sent back by P2", label="参加者Bからもらったお金を参加者Bに返金しますか、それともしませんか?（返金する場合、参加者Bが受け取る金額は、あなたが参加者Bからもらった金額の2倍になります。返金しない場合は、今あなたが持っている金額がそのままあなたの「収入」になります。また、残っている「資金」や前半で獲得した「収入」は返金の原資にすることはできません。"
    ) 

    def sent_back_amountP2_choices(self):
        #return currency_range(c(0), self.sent_amount * Constants.multiplier, c(1)) 
        choices = [c(0), self.sent_amountP2 * Constants.multiplier]
        return choices
    
    def set_payoffs_again(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p2.payoff = Constants.endowment - self.sent_amountP2 + self.sent_back_amountP2 + self.sent_amountP1 - self.sent_back_amountP1/Constants.multiplier
        p1.payoff = Constants.endowment - self.sent_amountP1 + self.sent_back_amountP1 + self.sent_amountP2 - self.sent_back_amountP2/Constants.multiplier
        


class Player(BasePlayer):
   pass