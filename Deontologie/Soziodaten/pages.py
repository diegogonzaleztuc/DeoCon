from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Survey (Page):
    form_model = "player"
    form_fields = ["age", "gender", "education", "income", "nationality", "religion", "party_preferences"]


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [Survey, ResultsWaitPage, Results]
