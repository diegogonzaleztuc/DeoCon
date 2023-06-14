from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Deontology(Page):
    form_model = 'player'
    form_fields = ['Frage_1']

    def before_next_page(self):
        self.player.set_payoffs()


class Check(Page):
    form_model = 'player'
    form_fields = ['s_society', 's_club']

    def is_displayed(self):
        return self.player.round_number == 1


class Results(Page):
    pass


page_sequence = [Deontology, Results]
#page_sequence = [Deontology, Check, Results]
