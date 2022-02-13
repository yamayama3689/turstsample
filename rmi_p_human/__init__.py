from otree.api import *
from otree.api import Currency as c, currency_range
import random


doc = """
rmi_over_0 human trust game
"""

#Models
class Constants(BaseConstants):
    name_in_url = 'rmi_p_human'
    players_per_group = None
    num_rounds = 10

    endowment = c(1000)
    multiplier = 3

    instructions_template = 'rmi_p_human/instructions.html'


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    #currency_rangeの形式のフォームだと、タイムアウトになった時、sent_amountに何も値が入らない（エラー吐く）ので、初期値を設定しています。
    sent_amount = models.CurrencyField(
        choices=currency_range(c(0), Constants.endowment, c(50)),
        doc="""Amount sent by P1""",
        label="相手にいくら送りますか?",
        initial=c(0)
    )

    thanks = models.IntegerField(
        choices=[1,2,3,4,5,6,7],
        label='取引した結果、現在相手に対してどの程度「感謝」の気持ちを抱いていますか？',
        widget=widgets.RadioSelect,
    )

    anger = models.IntegerField(
        choices=[1,2,3,4,5,6,7],
        label='取引した結果、現在相手に対してどの程度「怒り」の気持ちを抱いていますか？',
        widget=widgets.RadioSelect,
    )

#Pages
class Send(Page):

    form_model = 'player'
    form_fields = ['sent_amount']

    timeout_seconds = 60

    def vars_for_template(player: Player):
        round = player.round_number
        return dict(round = round)

    #送金額~送金額の3倍の中から50円刻みで返金額を決定
    @staticmethod
    def  before_next_page(player: Player, timeout_happened):
            tripled_amount = player.sent_amount * Constants.multiplier + c(1)
            sent_back_amount = random.randrange(player.sent_amount, tripled_amount, c(50))
            player.payoff = Constants.endowment - player.sent_amount + sent_back_amount

class Results(Page):
    timeout_seconds = 60
    def vars_for_template(player: Player):
        return dict(sent_back_amount = player.payoff + player.sent_amount - Constants.endowment)

class Survey(Page):
    timeout_seconds = 60

    form_model = 'player'
    form_fields = ['thanks', 'anger']


page_sequence = [Send, Results, Survey]

    
    