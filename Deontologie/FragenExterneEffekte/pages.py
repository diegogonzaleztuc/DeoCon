from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class a_Käufer(Page):
    form_model = "player"
    form_fields = ["Frage_1"]

    def before_next_page(self):
        # den Wert des Sliders mit dem Namen "slider" finden
        slider_value = self.request.POST.get('Frage_1', '')
        # slider_value enthält jetzt den Wert des Sliders
        # verwenden Sie den Wert für mathematische Berechnungen oder speichern Sie ihn in einer Variablen


class b_Dritte_Partei(Page):
    form_model = "player"
    form_fields = ["Frage_2"]



class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [a_Käufer, b_Dritte_Partei, Results]
