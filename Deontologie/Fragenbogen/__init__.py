from otree.api import *


doc = """
Your app description
"""

class Constants(BaseConstants):
    name_in_url = 'Fragebogen'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    def rating_field():
        return models.IntegerField(
            choices=[
                [1, "1"],
                [2, "2"],
                [3, "3"],
                [4, "4"],
                [5, "5"],
                [6, "6"],
                [7, "7"],
            ],
            widget=widgets.RadioSelectHorizontal
        )

    scale1 = rating_field()
    scale2 = rating_field()
    scale3 = rating_field()
    scale4 = rating_field()
    scale5 = rating_field()
    scale6 = rating_field()
    scale7 = rating_field()
    scale8 = rating_field()
    scale9 = rating_field()

#Pages

class Instructions(Page):
    form_model = "player"


class Survey(Page):
    form_model = "player"
    form_fields = ["scale1", "scale2", "scale3", "scale4", "scale5", "scale6", "scale7", "scale8", "scale9"]


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [Instructions, Survey, Results]

#page_sequence = [Instructions, Survey, ResultsWaitPage, Results]