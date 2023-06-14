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


class Constants(BaseConstants):
    name_in_url = 'Deontologie_Game'
    players_per_group = None
    num_rounds = 1

class Group(BaseGroup):
    pass

class Subsession(BaseSubsession):
    pass

class Player(BasePlayer):

    Frage_1 = models.IntegerField(
        label="Bis welcher Schadenswahrscheinlichkeit π in Prozent ist aus ihrer Sicht akzeptabel?",
        min=0,
        max=100,
        initial=50,
        widget=widgets.SliderInput(attrs={'step': '10'})
    )

    s_society = models.IntegerField(
        label="Wie schätzen Sie Ihren Beitrag zum Öffentlichen Recyclingsystem ein?",
        choices=[
            (1, "Eigener Beitrag ist höher als der durchschnittliche Beitrag."),
            (2, "Eigener Beitrag ist niedriger als der durchschnittliche Beitrag."),
            (3, "Eigener Beitrag entspricht ungefähr dem durchschnittlichen Beitrag.")],
        widget=widgets.RadioSelect()
    )

    s_club = models.IntegerField(
        label="Wie schätzen Sie Ihren Beitrag zum Recyclingsystem Ihres Klubs ein?",
        choices=[
            (1, "Eigener Beitrag ist höher als der durchschnittliche Beitrag."),
            (2, "Eigener Beitrag ist niedriger als der durchschnittliche Beitrag."),
            (3, "Eigener Beitrag entspricht ungefähr dem durchschnittlichen Beitrag.")],
        widget=widgets.RadioSelect()
    )

    payoff_1 = models.FloatField()
    payoff_2 = models.FloatField()

    def role(self):
        if self.id_in_group == 1:
            return 'Käufer'
        elif self.id_in_group == 2:
            return 'Unbeteiligter Beobachter'

    def exponential(self, Frage_1):
        return 1 - (1 - Frage_1 / 100) ** 3

    def set_payoffs(self):
        c = 1.5 - 1.5 * self.exponential(self.Frage_1)
        if self.role() == 'Käufer':
            self.payoff_1 = round(100 - (80 - (c * 40)), 2)
        elif self.role() == 'Unbeteiligter Beobachter':
            self.payoff_2 = round((self.Frage_1 / 100) * 40, 2)

    def before_session_starts(self):
        self.set_payoffs()