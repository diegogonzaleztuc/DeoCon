from otree.api import *


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Deontologe'
    players_per_group = 2
    num_rounds = 1
    instructions_template = 'Deontologe/instructions.html'



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Frage_1 = models.IntegerField(
        label="Bis welcher Schadenswahrscheinlichkeit π in Prozent ist aus ihrer Sicht akzeptabel?",
        min=0,
        max=100,
        initial=50,
        #widget=widgets.SliderInput(attrs={'step': '10'})
    )

    def exponential(Player, Frage_1):
        return 1 - (1 - Frage_1 / 100) ** 3




#def set_payoffs(group: Group):
#    for p in group.get_players():
#        set_payoff(p)


# PAGES

class Matching(WaitPage):
    group_by_arrival_time = True

    title_text = "Bitte warten"
    body_text = "Nachdem alle Teilnehmer eine Entscheidung getroffen haben, geht es weiter."

class Start(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Introduction(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Comprehension_Intro(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Deontology(Page):
    form_model = 'player'
    form_fields = ['Frage_1']

class WaitHL(WaitPage):
    #after_all_players_arrive = set_payoffs

    title_text = "Bitte warten"
    body_text = "Nachdem alle Teilnehmer eine Entscheidung getroffen haben, geht es weiter."




page_sequence = [Matching,
                 Start,
                 Introduction,
                 Deontology,
                 ]
