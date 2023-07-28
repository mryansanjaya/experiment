from otree.api import *
import csv
import random


class C(BaseConstants):
    NAME_IN_URL = 'tax_compliance_practice3'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        for group in self.get_groups():
            group.set_group_bagipajak()


def creating_session(subsession: Subsession):
    subsession.group_randomly()

    prefilled_event = open(__name__ + '/parameter/prefilled_form.csv', encoding='utf-8-sig')
    audit_event = open(__name__ + '/parameter/audit_event.csv', encoding='utf-8-sig')
    returntax = open(__name__ + '/parameter/return_tax.csv', encoding='utf-8-sig')

    prefilledform = list(csv.DictReader(prefilled_event))
    audit = list(csv.DictReader(audit_event))
    returntax = list(csv.DictReader(returntax))
    random.shuffle(returntax)
    random.shuffle(audit)
    random.shuffle(prefilledform)

    groups = subsession.get_groups()
    for i in range(len(groups)):
        returntax_cols = returntax[i]
        player = groups[i]
        player.return_tax = float(returntax_cols['98'])

    players = subsession.get_players()
    for i in range(len(players)):
        prefilled_cols = prefilledform[i]
        audit_cols = audit[i]
        player = players[i]
        player.prefilled_form = float(prefilled_cols['112'])
        player.audit = bool(int(audit_cols['1']))


class Group(BaseGroup):
    return_tax = models.FloatField(min=0, max=0)
    lat_totalpajak = models.FloatField(min=0, max=1)
    lat_bagipajak = models.FloatField(min=0, max=1)

    def set_group_bagipajak(self):
        self.group_bagipajak = self.lat_bagipajak


class Player(BasePlayer):
    lat_pendapatanakhir = models.FloatField(min=0, max=1, initial=0)
    lat_laporpendapatan = models.FloatField(label="Masukkan Pendapatan Anda", initial=0)
    lat_estimasi_pendapatan = models.FloatField(min=0, max=1, initial=0)
    lat_bebanpajak = models.FloatField(min=0, max=1, initial=0)
    audit = models.BooleanField()
    prefilled_form = models.FloatField(min=0, max=0, initial=0)
    denda = models.FloatField(min=0, max=1, initial=0)


# FUNCTIONS
def set_jumlahpajak(group: Group):
    players = group.get_players()
    total_pajak = [p.lat_bebanpajak for p in players]
    if total_pajak == 0:
        total_pajak = 0.0000001
    group.lat_totalpajak = sum(total_pajak)
    for player in players:
        group.lat_bagipajak = (group.lat_totalpajak * (group.return_tax / 100)) / C.PLAYERS_PER_GROUP
        player.lat_estimasi_pendapatan = player.lat_pendapatanakhir * (player.prefilled_form / 100)


# PAGES
class WaitPlayer(WaitPage):
    wait_for_all_groups = True


class BeforeTaxPage(Page):
    timeout_seconds = 15

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        player.lat_pendapatanakhir = participant.total_payoff


class TaxPage(Page):
    timeout_seconds = 20

    form_model = 'player'
    form_fields = ['lat_laporpendapatan']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        laporpendapatanbersih = player.lat_laporpendapatan - 200
        laporpendapatanlebih = player.lat_laporpendapatan - player.lat_pendapatanakhir

        if laporpendapatanlebih > 500:
            player.lat_bebanpajak = 0
        elif 0 < laporpendapatanbersih <= 500:
            player.lat_bebanpajak = laporpendapatanbersih * 0.05
        elif 500 < laporpendapatanbersih <= 1000:
            player.lat_bebanpajak = (500 * 0.05) + ((laporpendapatanbersih - 500) * 0.15)
        elif laporpendapatanbersih > 1000:
            player.lat_bebanpajak = (500 * 0.05) + (500 * 0.15) + ((laporpendapatanbersih - 1000) * 0.25)
        elif laporpendapatanbersih <= 0:
            player.lat_bebanpajak = 0


class TotalPajak(WaitPage):
    after_all_players_arrive = set_jumlahpajak


class PooledTax(Page):
    timeout_seconds = 10

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        hasilbagipajak = player.group.lat_bagipajak
        pres_denda = (player.lat_pendapatanakhir - player.lat_laporpendapatan) * 0.5
        laporpendapatanlebih = player.lat_laporpendapatan - player.lat_pendapatanakhir

        if laporpendapatanlebih > 0 and player.audit == 1:
            player.denda = 0
            player.payoff = player.lat_pendapatanakhir - player.lat_bebanpajak + hasilbagipajak
        elif player.audit == 1:
            player.denda = pres_denda
            player.payoff = player.lat_pendapatanakhir - player.denda - player.lat_bebanpajak + hasilbagipajak
        elif laporpendapatanlebih > 0 and player.audit == 0:
            player.denda = 0
            player.payoff = player.lat_pendapatanakhir - player.lat_bebanpajak + hasilbagipajak
        elif player.audit == 0:
            player.payoff = player.lat_pendapatanakhir - player.lat_bebanpajak + hasilbagipajak


class FinalResults(Page):
    # timeout_seconds = 10

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        laporpendapatanlebih = player.lat_laporpendapatan - player.lat_pendapatanakhir
        participant.payment = player.payoff * 100
        participant.participant_fee = 10000
        participant.finalpayment = participant.payment + participant.participant_fee
        participant.laporlebih = laporpendapatanlebih


page_sequence = [WaitPlayer, BeforeTaxPage, TaxPage, TotalPajak, PooledTax, FinalResults]
