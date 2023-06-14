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


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'FragenExterneEffekte'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Frage_1 = models.IntegerField(
        label="Bis welcher Schadenswahrscheinlichkeit π in Prozent ist aus ihrer Sicht als Käufer des Produkts akzeptabel?",
        min=0,
        max=100,
        initial=50,
        widget=widgets.SliderInput(attrs={'step': '10'})
    )
    Frage_2 = models.IntegerField(
        label="Bis welcher Schadenswahrscheinlichkeit π in Prozent ist aus ihrer Sicht als eine betroffene Person akzeptabel?",
        min=0,
        max=100,
        initial=50,
        widget=widgets.SliderInput(attrs={'step': '10'})
    )
