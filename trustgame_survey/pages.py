from otree.api import Currency as c, currency_range
from ._builtin import Page
from .models import Constants


class Questions(Page):
    form_model = 'player'
    form_fields = ['num', 'age']

class Thanks(Page):
    pass

page_sequence = [Questions, Thanks]