from otree.api import Currency as c, currency_range
from otree.models import player

from settings import PARTICIPANT_FIELDS
from ._builtin import Page, WaitPage
from .models import Constants


class SendP1(Page):

    form_model = 'group'
    form_fields = ['sent_amountP1']
    
    def is_displayed(self):
        return self.player.id_in_group == 1

    def vars_for_template(self):
        return dict(sumpayment = float(self.player.participant.payoff))
        #payoffs = [p.payoff for p in self.player.in_previous_rounds()]
        """  payoffs = player.payoff
        sumpayoff = sum(payoffs) """
        

        #return dict(sumpayoff = sumpayoff)
        

class SendP2(Page):

    form_model = 'group'
    form_fields = ['sent_amountP2']
    

    def is_displayed(self):
        return self.player.id_in_group == 2

    def vars_for_template(self):
        return dict(sumpayment = float(self.player.participant.payoff))

    


class SendBackP1(Page):

    form_model = 'group'
    form_fields = ['sent_back_amountP1']

    def is_displayed(self):
        return self.player.id_in_group == 1

    

    """ def vars_for_template(self):
        return dict(twice_amountP1=self.group.sent_amountP1 * Constants.multiplier) """

class SendBackP2(Page):

    form_model = 'group'
    form_fields = ['sent_back_amountP2']

    def is_displayed(self):
        return self.player.id_in_group == 2

    """ def vars_for_template(self):
        return dict(twice_amountP2=self.group.sent_amountP2 * Constants.multiplier) """

class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'

class ResultsP1(Page):
    def is_displayed(self):
        return self.player.id_in_group == 1
    """ def vars_for_template(self):
        return dict(
            revenuP1 =self.group.sent_back_amountP1,
            first_fundsP1 =Constants.endowment - self.group.sent_amountP1,
            first_payoffP1 =Constants.endowment - self.group.sent_amountP1 + self.group.sent_back_amountP1,
            revenuP2 =self.group.sent_amountP1 - self.group.sent_back_amountP1/Constants.multiplier,
            first_payoffP2 =self.group.sent_amountP1 - self.group.sent_back_amountP1/Constants.multiplier + Constants.endowment
            ) """
    def vars_for_template(self):
        if self.group.sent_back_amountP2 == True:
            return dict(repaymentP1 = self.group.sent_amountP2 * Constants.multiplier)
        elif self.group.sent_back_amountP2 == False:
            return dict(repaymentP1 = self.group.sent_amountP2 * 0)

class ResultsP2(Page):
    def is_displayed(self):
        return self.player.id_in_group == 2
    
    def vars_for_template(self):
        if self.group.sent_back_amountP1 == True:
            return dict(repaymentP2 = self.group.sent_amountP1 * Constants.multiplier)
        elif self.group.sent_back_amountP1 == False:
            return dict(repaymentP2 = self.group.sent_amountP1 * 0)

class Thanks(Page):
    pass




page_sequence = [SendP1, SendP2, SendBackP1, SendBackP2, ResultsWaitPage, ResultsP1, ResultsP2, Thanks]