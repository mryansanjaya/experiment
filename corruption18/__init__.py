from otree.api import *
import csv
import random


class C(BaseConstants):
    NAME_IN_URL = 'corruption18'
    PLAYERS_PER_GROUP = 4
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        for group in self.get_groups():
            group.set_group_bagipajak()


def creating_session(subsession):
    subsession.group_randomly()

    corrupt_event = open(__name__ + '/parameter/ambiguous_corruption_event.csv', encoding='utf-8-sig')
    audit_event = open(__name__ + '/parameter/audit_event.csv', encoding='utf-8-sig')
    middle_return = open(__name__ + '/parameter/middle_return.csv', encoding='utf-8-sig')

    corrupt = list(csv.DictReader(corrupt_event))
    audit = list(csv.DictReader(audit_event))
    returntax = list(csv.DictReader(middle_return))
    random.shuffle(returntax)
    random.shuffle(audit)
    random.shuffle(corrupt)

    groups = subsession.get_groups()
    for i in range(len(groups)):
        corrupt_cols = corrupt[i]
        returntax_cols = returntax[i]
        player = groups[i]
        player.corrupt = float(corrupt_cols['77'])
        player.return_tax = float(returntax_cols['110'])

    players = subsession.get_players()
    for i in range(len(players)):
        audit_cols = audit[i]
        player = players[i]
        player.audit = bool(int(audit_cols['1']))


class Group(BaseGroup):
    corrupt = models.FloatField(min=0, max=1)
    return_tax = models.FloatField(min=0, max=1)
    totalpajak = models.FloatField(min=0, max=1)
    bagipajak = models.FloatField(min=0, max=1)

    def set_group_bagipajak(self):
        self.group_bagipajak = self.bagipajak


class Player(BasePlayer):
    pendapatanakhir = models.FloatField(min=0, max=1, initial=0)
    laporpendapatan = models.FloatField(label="Masukkan Pendapatan Anda", initial=0)
    bebanpajak = models.FloatField(min=0, max=1, initial=0)
    audit = models.BooleanField()
    hasil_korupsi = models.FloatField(min=0, max=1, initial=0)
    denda = models.FloatField(min=0, max=1, initial=0)


# FUNCTIONS
def set_jumlahpajak(group: Group):
    players = group.get_players()
    total_pajak = [p.bebanpajak for p in players]
    if total_pajak == 0:
        total_pajak = 0.0000001
    group.totalpajak = sum(total_pajak)
    for player in players:
        besar_korupsi = player.bebanpajak - (player.bebanpajak * (group.corrupt / 100))
        player.hasil_korupsi = besar_korupsi
        group.bagipajak = (group.totalpajak * (group.return_tax / 100) - player.hasil_korupsi) /\
                              C.PLAYERS_PER_GROUP


# PAGES
class WaitPlayer(WaitPage):
    wait_for_all_groups = True


class BeforeTaxPage(Page):
    timeout_seconds = 10

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        player.pendapatanakhir = participant.total_payoff


class TaxPage(Page):
    timeout_seconds = 20

    form_model = 'player'
    form_fields = ['laporpendapatan']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        laporpendapatanbersih = player.laporpendapatan - 200
        laporpendapatanlebih = player.laporpendapatan - player.pendapatanakhir

        if laporpendapatanlebih > 500:
            player.bebanpajak = 0
        elif 0 < laporpendapatanbersih <= 500:
            player.bebanpajak = laporpendapatanbersih * 0.05
        elif 500 < laporpendapatanbersih <= 1000:
            player.bebanpajak = (500 * 0.05) + ((laporpendapatanbersih - 500) * 0.15)
        elif laporpendapatanbersih > 1000:
            player.bebanpajak = (500 * 0.05) + (500 * 0.15) + ((laporpendapatanbersih - 1000) * 0.25)
        elif laporpendapatanbersih <= 0:
            player.bebanpajak = 0


class TotalPajak(WaitPage):
    after_all_players_arrive = set_jumlahpajak


class PooledTax(Page):
    timeout_seconds = 10

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        hasilbagipajak = player.group.bagipajak
        pres_denda = (player.pendapatanakhir - player.laporpendapatan) * 0.5
        laporpendapatanlebih = player.laporpendapatan - player.pendapatanakhir

        if laporpendapatanlebih > 0 and player.audit == 1:
            player.denda = 0
            player.payoff = player.pendapatanakhir - player.bebanpajak + hasilbagipajak
        elif player.audit == 1:
            player.denda = pres_denda
            player.payoff = player.pendapatanakhir - player.denda - player.bebanpajak + hasilbagipajak
        elif laporpendapatanlebih > 0 and player.audit == 0:
            player.denda = 0
            player.payoff = player.pendapatanakhir - player.bebanpajak + hasilbagipajak
        elif player.audit == 0:
            player.payoff = player.pendapatanakhir - player.bebanpajak + hasilbagipajak


class FinalResults(Page):
    timeout_seconds = 10

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        laporpendapatanlebih = player.laporpendapatan - player.pendapatanakhir
        participant.laporlebih = laporpendapatanlebih

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant

        if player.round_number == C.NUM_ROUNDS:
            random_round = random.randint(1, C.NUM_ROUNDS)
            participant.selected_round = random_round
            player_in_selected_round = player.in_round(random_round)
            participant.pay_treatment18 = player_in_selected_round.payoff


page_sequence = [WaitPlayer, BeforeTaxPage, TaxPage, TotalPajak, PooledTax, FinalResults]
