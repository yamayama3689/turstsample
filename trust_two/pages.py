from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Send(Page):

    form_model = 'group'
    form_fields = ['sent_amountP1']

    def is_displayed(self):
        return self.player.id_in_group == 1


class WaitForP1(WaitPage):
    pass


class SendBack(Page):

    form_model = 'group'
    form_fields = ['sent_back_amountP1']

    def is_displayed(self):
        return self.player.id_in_group == 2

    """ def vars_for_template(self):
        return dict(twice_amountP1=self.group.sent_amountP1 * Constants.multiplier) """

class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'

class Results(Page):
    def vars_for_template(self):
        return dict(
            revenuP1 =self.group.sent_back_amountP1,
            first_fundsP1 =Constants.endowment - self.group.sent_amountP1,
            first_payoffP1 =Constants.endowment - self.group.sent_amountP1 + self.group.sent_back_amountP1,
            revenuP2 =self.group.sent_amountP1 - self.group.sent_back_amountP1/Constants.multiplier,
            first_payoffP2 =self.group.sent_amountP1 - self.group.sent_back_amountP1/Constants.multiplier + Constants.endowment
            )
        

    

class SendP2(Page):
    form_model = 'group'
    form_fields = ['sent_amountP2']

    def is_displayed(self):
        return self.player.id_in_group == 2

class WaitForP2(WaitPage):
    pass

class SendBackP2(Page):

    form_model = 'group'
    form_fields = ['sent_back_amountP2']

    def is_displayed(self):
        return self.player.id_in_group == 1

    """ def vars_for_template(self):
        return dict(twice_amountP2=self.group.sent_amountP2 * Constants.multiplier) """

class ResultsWaitPageAgain(WaitPage):
    after_all_players_arrive = 'set_payoffs_again'

class ResultsAgain(Page):
    def vars_for_template(self):
        return dict(
            second_revenuP2 =self.group.sent_back_amountP2,
            second_payoffP2 =Constants.endowment - self.group.sent_amountP2 + self.group.sent_back_amountP2 + self.group.sent_amountP1 - self.group.sent_back_amountP1/Constants.multiplier,
            second_revenuP1 =self.group.sent_amountP2 - self.group.sent_back_amountP2/Constants.multiplier,
            second_payoffP1 =Constants.endowment - self.group.sent_amountP1 + self.group.sent_back_amountP1 + self.group.sent_amountP2 - self.group.sent_back_amountP2/Constants.multiplier
            )



page_sequence = [Send, WaitForP1, SendBack, ResultsWaitPage, Results, SendP2, WaitForP2,
SendBackP2, ResultsWaitPageAgain, ResultsAgain]