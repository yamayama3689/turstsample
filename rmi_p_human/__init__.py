from otree.api import *
from otree.api import Currency as c
import random



doc = """
rmi_over_0 human trust game
"""

#Models
class Constants(BaseConstants):
    name_in_url = 'rmi_p_human'
    players_per_group = None
    num_rounds = 1

    endowment = c(1000)
    multiplier = 3

    instructions_template = 'rmi_p_human/instructions.html'


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    sent_amount = models.CurrencyField(
        min=c(0),
        max=Constants.endowment,
        doc="""Amount sent by P1""",
        label="参加者Bにいくら送りますか?",
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

#Functions
def set_player(group: Group):
    players = group.get_players()
    for p in players:
      set_payoffs(p)

def set_payoffs(player: Player):
    tripled_amount = player.sent_amount * Constants.multiplier + 1
    sent_back_amount = random.randrange(player.sent_amount, tripled_amount, 50)
    player.payoff = Constants.endowment - player.sent_amount + sent_back_amount

#Pages
class Send(Page):

    form_model = 'player'
    form_fields = ['sent_amount']

    timeout_seconds = 60

class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_player'
    #after_all_players_arriveはGroupを引数にとる関数しか設定できないっぽい

class Results(Page):
    timeout_seconds = 60
    def vars_for_template(player: Player):
        return dict(sent_back_amount = player.payoff + player.sent_amount - Constants.endowment)

class Survey(Page):
    timeout_seconds = 60

    form_model = 'player'
    form_fields = ['thanks', 'anger']


page_sequence = [Send, ResultsWaitPage, Results,  Survey]

    








    