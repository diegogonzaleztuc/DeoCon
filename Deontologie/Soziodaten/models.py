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


author = 'Diego Gonzalez'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Soziodaten'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(label="Wie alt sind Sie?", min=18, max=100)
    gender = models.StringField(label="Welches Geschlecht haben Sie?", choices=["Weiblich", "Männlich", "Divers"])
    education = models.StringField(label="Wie hoch ist Ihr Bildungsabschluss?",
                                   choices=["kein Abschluss", "Hauptschulabschluss", "Realschulabschluss", "Abitur", "Bachelor-Abschluss", "Master-Abschluss", "Promotion"])
    income = models.StringField(label="Wie hoch ist Ihr monatliches Nettoeinkommen?",
                                choices=["weniger als 1.000 Euro", "1.000 - 2.000 Euro", "2.000 - 3.000 Euro", "3.000 - 4.000 Euro", "mehr als 4.000 Euro"])
    nationality = models.StringField(label="Welcher Nationalität fühlen Sie sich zugehörig?", blank=True)
    religion = models.StringField(label="Welche Religion fühlen Sie sich zugehörig?", blank=True)
    party_preferences = models.StringField(label="Welche Partei entspricht am ehesten Ihren Präferenzen?",
                                   choices=["SPD", "Grüne", "FDP", "CDU","AfD", "Linke", "Keine Angabe"])

