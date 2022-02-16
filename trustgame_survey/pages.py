from socket import timeout
from ._builtin import Page
from .models import Constants


class Questions(Page):
    form_model = 'player'
    form_fields = ['idnum', 'age', 'gender', 'date']

    timeout_seconds = 120

class Thanks(Page):
    pass

page_sequence = [Questions, Thanks]