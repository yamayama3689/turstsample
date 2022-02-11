from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random

class Send(Page):

    form_model = 'player'
    form_fields = ['sent_amount']

    """ def is_displayed(self):
        return self.player.id_in_group == 1 """

    




class WaitForP1(WaitPage):
    pass


class SendBack(Page):

    #form_model = 'group'
    #form_fields = ['sent_back_amount']

    """ def vars_for_template(self):
        return dict(twice_amount=self.group.sent_amount * Constants.multiplier) """


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'


class Results(Page):
    def vars_for_template(self):
        num = random.randrange(1, 101)
        if num > 30:
            return dict(twice_amount = self.player.sent_amount * Constants.multiplier)
        else:
            return dict(twice_amount = 0)


page_sequence = [Send, Results]