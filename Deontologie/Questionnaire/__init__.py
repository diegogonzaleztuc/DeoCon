from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'Questionnaire'
    INSTRUCTIONS_TEMPLATE = 'Questionnaire/instructions.html'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    Quantity_max = 100
    Price_max = 300
    ENDOWMENT = 300
    FAKE_COST = 35


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    age = models.IntegerField(min=1960, max=2003, doc="age in years")
    gender = models.IntegerField(choices=[[1, 'männlich'],
                                          [2, 'weiblich'],
                                          [3, 'divers']],
                                 widget=widgets.RadioSelectHorizontal)
    studies = models.IntegerField(choices=[[1, 'Rechtswissenschaften'],
                                           [2, 'Volkswirtschaft'],
                                           [3, 'Sozialwissenschaft'],
                                           [4, 'Betriebswirtschaft'],
                                           [5, 'Medizin'],
                                           [6, 'Erziehungswissenschaft'],
                                           [7, 'Geisteswissenschaft'],
                                           [8, 'Informatik'],
                                           [9, 'Mathematik'],
                                           [10, 'Naturwissenschaft'],
                                           [11, 'Psychologie'],
                                           [12, 'Bewegungswissenschaften'],
                                           [13, 'Sonstiges']],
                                  doc="field of studies")
    semester = models.IntegerField(min=0, max=35, doc="semester")

    work = models.IntegerField(choices=[[1, 'Ja'], [2,'Nein']])
    bafog = models.IntegerField(choices=[[1, 'Ja'], [2,'Nein']])
    opinion = models.IntegerField(choices=[[1, 'Nicht wichtig'], [2,'Eher nicht wichtig'], [3, 'Weder wichtig, noch unwichtig'],
                                           [4, 'Eher wichtig'], [5, 'Sehr wichtig']])

    onlineshopping = models.IntegerField(choices=[[1, 'Täglich'], [2,'Mehrmals pro Woche'], [3, 'Mehrmals pro Monat'],
                                           [4, 'Einmal im Monat'], [5, 'Seltener']])

    bewertungssystem = models.IntegerField(choices=[[1, 'Sehr wichtig'], [2,'Wichtig'], [3, 'Teils wichtig, teils nicht wichtig'],
                                           [4, 'Weniger wichtig'], [5, 'Gar nicht wichtig']])

    car_km = models.IntegerField()
    car_justified = models.IntegerField(choices=[[1, 'Voll und ganz gerechtfertigt'], [2,'Eher gerechtfertigt'], [3, 'Weder/Noch'],
                                           [4, 'Weniger gerechtfertigt'], [5, 'Gar nicht gerechtfertigt']])

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

# FUNCTIONS



# PAGES
class Introduction(Page):
    pass

class WaitAll(WaitPage):
    body_text = "Bitte warten Sie auf die anderen Teilnehmer."


class Soziodemographie(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'studies', 'semester', 'work', 'bafog']



class Reasons(Page):
    pass
    #form_model = 'player'
    #form_fields = ['opinion', 'car_justified', 'car_km', 'onlineshopping', 'bewertungssystem']



class OUS_Scale(Page):
    form_model = 'player'
    form_fields = ['scale1', 'scale2', 'scale3', 'scale4', 'scale5', 'scale6', 'scale7', 'scale8', 'scale9']


class ResultsWaitPage(WaitPage):
    wait_for_all_players = True
    body_text = "Bitte warten Sie auf die anderen Teilnehmer."



class Results(Page):
    pass


page_sequence = [Introduction,
                 WaitAll,
                 Soziodemographie,
                 OUS_Scale,
                 Reasons,
                 ResultsWaitPage,
                 Results]
