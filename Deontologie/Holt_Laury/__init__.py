from otree.api import *


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Holt_Laury'
    players_per_group = 2
    num_rounds = 1
    instructions_template_sicher = 'Holt_Laury/instructions_sicher.html'
    instructions_template_Lotterie = 'Holt_Laury/instructions_Lotterie.html'



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Holt1 = models.StringField(
        choices=[['A', 'A'], ['B', 'B']],
        doc="""This player's decision""",
        widget=widgets.RadioSelect,
    )
    Holt2 = models.StringField(
        choices=[['A', 'A'], ['B', 'B']],
        doc="""This player's decision""",
        widget=widgets.RadioSelect,
    )
    Holt3 = models.StringField(
        choices=[['A', 'A'], ['B', 'B']],
        doc="""This player's decision""",
        widget=widgets.RadioSelect,
    )
    Holt4 = models.StringField(
        choices=[['A', 'A'], ['B', 'B']],
        doc="""This player's decision""",
        widget=widgets.RadioSelect,
    )
    Holt5 = models.StringField(
        choices=[['A', 'A'], ['B', 'B']],
        doc="""This player's decision""",
        widget=widgets.RadioSelect,
    )
    Holt6 = models.StringField(
        choices=[['A', 'A'], ['B', 'B']],
        doc="""This player's decision""",
        widget=widgets.RadioSelect,
    )
    Holt7 = models.StringField(
        choices=[['A', 'A'], ['B', 'B']],
        doc="""This player's decision""",
        widget=widgets.RadioSelect,
    )
    Holt8 = models.StringField(
        choices=[['A', 'A'], ['B', 'B']],
        doc="""This player's decision""",
        widget=widgets.RadioSelect,
    )
    Holt9 = models.StringField(
        choices=[['A', 'A'], ['B', 'B']],
        doc="""This player's decision""",
        widget=widgets.RadioSelect,
    )
    Holt10 = models.StringField(
        choices=[['A', 'A'], ['B', 'B']],
        doc="""This player's decision""",
        widget=widgets.RadioSelect,
    )



def set_payoffs(group: Group):
    for p in group.get_players():
        set_payoff(p)


def set_payoff(player: Player):
    import random
    initial = random.randint(1, 100)
    if player.Holt3 == 'A':
        player.payoff = cu(0.75)
    elif player.Holt3 == 'B' and initial < 50:
        player.payoff = cu(2.50)
    elif player.Holt3 == 'B' and initial >= 50:
        player.payoff = cu(0)
    else:
        pass


# PAGES

class Matching(WaitPage):
    group_by_arrival_time = True

    title_text = "Bitte warten"
    body_text = "Nachdem alle Teilnehmer eine Entscheidung getroffen haben, geht es weiter."


class Introduction(Page):
    pass


class HL_Introduction(Page):
    pass


class Holt_Laury1(Page):
    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 1

    form_model = 'player'
    form_fields = ['Holt1', 'Holt2', 'Holt3', 'Holt4', 'Holt5', 'Holt6', 'Holt7', 'Holt8', 'Holt9', 'Holt10']

class Holt_Laury2(Page):
    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 2

    form_model = 'player'
    form_fields = ['Holt1', 'Holt2', 'Holt3', 'Holt4', 'Holt5', 'Holt6', 'Holt7', 'Holt8', 'Holt9', 'Holt10']



class WaitHL(WaitPage):
    after_all_players_arrive = set_payoffs

    title_text = "Bitte warten"
    body_text = "Nachdem alle Teilnehmer eine Entscheidung getroffen haben, geht es weiter."


class Part2(Page):
    pass


page_sequence = [Matching,
                 Introduction,
                 HL_Introduction,
                 Holt_Laury1,
                 Holt_Laury2,
                 WaitHL,
                 Part2
                 ]
