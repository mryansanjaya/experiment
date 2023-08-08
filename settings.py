from os import environ
import sys

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
SESSION_CONFIGS = [
    dict(
        name="tax_ctpf1",
        display_name="CTPF1",
        num_demo_participants=8,
        app_sequence=["instruction_experiment4", "task_math_practice", "tax_compliance_practice4", "BeforeExperiment",
                      "task_math1", "prefilled_corruption1", "task_math2", "prefilled_corruption2", "task_math3",
                      "prefilled_corruption3", "task_math4", "prefilled_corruption4", "task_math5",
                      "prefilled_corruption5", "task_math6", "prefilled_corruption6", "task_math7",
                      "prefilled_corruption7", "task_math8", "prefilled_corruption8", "task_math9",
                      "prefilled_corruption9", "task_math10", "prefilled_corruption10", "task_math11",
                      "prefilled_corruption11", "task_math12", "prefilled_corruption12", "task_math13",
                      "prefilled_corruption13", "task_math14", "prefilled_corruption14", "task_math15",
                      "prefilled_corruption15", "task_math16", "prefilled_corruption16", "task_math17",
                      "prefilled_corruption17", "task_math18", "prefilled_corruption18", "task_math19",
                      "prefilled_corruption19", "task_math20", "prefilled_corruption20", "task_math21",
                      "prefilled_corruption21", "task_math22", "prefilled_corruption22", "task_math23",
                      "prefilled_corruption23", "task_math24", "prefilled_corruption24", "task_math25",
                      "prefilled_corruption25", "task_math26", "prefilled_corruption26", "task_math27",
                      "prefilled_corruption27", "task_math28", "prefilled_corruption28", "task_math29",
                      "prefilled_corruption29", "task_math30", "prefilled_corruption30",
                      "pay_random_apps4", "questionnaire", "payment_info"]
    ),
    dict(
        name="tax_ctpf2",
        display_name="CTPF2",
        num_demo_participants=8,
        app_sequence=["instruction_experiment4", "task_math_practice", "tax_compliance_practice4", "BeforeExperiment",
                      "task_math1", "prefilled_corruption1", "task_math2", "prefilled_corruption2", "task_math3",
                      "prefilled_corruption3", "task_math4", "prefilled_corruption4", "task_math5",
                      "prefilled_corruption5", "task_math6", "prefilled_corruption6", "task_math7",
                      "prefilled_corruption7", "task_math8", "prefilled_corruption8", "task_math9",
                      "prefilled_corruption9", "task_math10", "prefilled_corruption10", "task_math11",
                      "prefilled_corruption11", "task_math12", "prefilled_corruption12", "task_math13",
                      "prefilled_corruption13", "task_math14", "prefilled_corruption14", "task_math15",
                      "prefilled_corruption15", "task_math16", "prefilled_corruption16", "task_math17",
                      "prefilled_corruption17", "task_math18", "prefilled_corruption18", "task_math19",
                      "prefilled_corruption19", "task_math20", "prefilled_corruption20", "task_math21",
                      "prefilled_corruption21", "task_math22", "prefilled_corruption22", "task_math23",
                      "prefilled_corruption23", "task_math24", "prefilled_corruption24", "task_math25",
                      "prefilled_corruption25", "task_math26", "prefilled_corruption26", "task_math27",
                      "prefilled_corruption27", "task_math28", "prefilled_corruption28", "task_math29",
                      "prefilled_corruption29", "task_math30", "prefilled_corruption30",
                      "pay_random_apps4", "questionnaire", "payment_info"]
    ),
    dict(
        name="tax_ctpf3",
        display_name="CTPF3",
        num_demo_participants=8,
        app_sequence=["instruction_experiment4", "task_math_practice", "tax_compliance_practice4", "BeforeExperiment",
                      "task_math1", "prefilled_corruption1", "task_math2", "prefilled_corruption2", "task_math3",
                      "prefilled_corruption3", "task_math4", "prefilled_corruption4", "task_math5",
                      "prefilled_corruption5", "task_math6", "prefilled_corruption6", "task_math7",
                      "prefilled_corruption7", "task_math8", "prefilled_corruption8", "task_math9",
                      "prefilled_corruption9", "task_math10", "prefilled_corruption10", "task_math11",
                      "prefilled_corruption11", "task_math12", "prefilled_corruption12", "task_math13",
                      "prefilled_corruption13", "task_math14", "prefilled_corruption14", "task_math15",
                      "prefilled_corruption15", "task_math16", "prefilled_corruption16", "task_math17",
                      "prefilled_corruption17", "task_math18", "prefilled_corruption18", "task_math19",
                      "prefilled_corruption19", "task_math20", "prefilled_corruption20", "task_math21",
                      "prefilled_corruption21", "task_math22", "prefilled_corruption22", "task_math23",
                      "prefilled_corruption23", "task_math24", "prefilled_corruption24", "task_math25",
                      "prefilled_corruption25", "task_math26", "prefilled_corruption26", "task_math27",
                      "prefilled_corruption27", "task_math28", "prefilled_corruption28", "task_math29",
                      "prefilled_corruption29", "task_math30", "prefilled_corruption30",
                      "pay_random_apps4", "questionnaire", "payment_info"]
    ),
    dict(
        name="tax_ctpf4",
        display_name="CTPF4",
        num_demo_participants=8,
        app_sequence=["instruction_experiment4", "task_math_practice", "tax_compliance_practice4", "BeforeExperiment",
                      "task_math1", "prefilled_corruption1", "task_math2", "prefilled_corruption2", "task_math3",
                      "prefilled_corruption3", "task_math4", "prefilled_corruption4", "task_math5",
                      "prefilled_corruption5", "task_math6", "prefilled_corruption6", "task_math7",
                      "prefilled_corruption7", "task_math8", "prefilled_corruption8", "task_math9",
                      "prefilled_corruption9", "task_math10", "prefilled_corruption10", "task_math11",
                      "prefilled_corruption11", "task_math12", "prefilled_corruption12", "task_math13",
                      "prefilled_corruption13", "task_math14", "prefilled_corruption14", "task_math15",
                      "prefilled_corruption15", "task_math16", "prefilled_corruption16", "task_math17",
                      "prefilled_corruption17", "task_math18", "prefilled_corruption18", "task_math19",
                      "prefilled_corruption19", "task_math20", "prefilled_corruption20", "task_math21",
                      "prefilled_corruption21", "task_math22", "prefilled_corruption22", "task_math23",
                      "prefilled_corruption23", "task_math24", "prefilled_corruption24", "task_math25",
                      "prefilled_corruption25", "task_math26", "prefilled_corruption26", "task_math27",
                      "prefilled_corruption27", "task_math28", "prefilled_corruption28", "task_math29",
                      "prefilled_corruption29", "task_math30", "prefilled_corruption30",
                      "pay_random_apps4", "questionnaire", "payment_info"]
    )
]
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1, participation_fee=1.00, doc=""
)

PARTICIPANT_FIELDS = [
    'is_dropout',
    'total_payoff',
    'laporlebih',
    'selected_round',
    'pay_treatment1',
    'pay_treatment2',
    'pay_treatment3',
    'pay_treatment4',
    'pay_treatment5',
    'pay_treatment6',
    'pay_treatment7',
    'pay_treatment8',
    'pay_treatment9',
    'pay_treatment10',
    'pay_treatment11',
    'pay_treatment12',
    'pay_treatment13',
    'pay_treatment14',
    'pay_treatment15',
    'pay_treatment16',
    'pay_treatment17',
    'pay_treatment18',
    'pay_treatment19',
    'pay_treatment20',
    'pay_treatment21',
    'pay_treatment22',
    'pay_treatment23',
    'pay_treatment24',
    'pay_treatment25',
    'pay_treatment26',
    'pay_treatment27',
    'pay_treatment28',
    'pay_treatment29',
    'pay_treatment30',
]

SESSION_FIELDS = [
    'params'
]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = "en"

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = ""
USE_POINTS = True

ROOMS = [
    dict(
        name="tax_ctpf1",
        display_name="Eksperimen Perilaku Perpajakan Sesi 4 - Prefilled Form + Corruption Treatment",
        participant_label_file='_rooms/participant_labels.txt',
    ),
        dict(
        name="tax_ctpf2",
        display_name="Eksperimen Perilaku Perpajakan Sesi 4 - Prefilled Form + Corruption Treatment",
        participant_label_file='_rooms/participant_labels.txt',
    ),
    dict(
        name="tax_ctpf3",
        display_name="Eksperimen Perilaku Perpajakan Sesi 4 - Prefilled Form + Corruption Treatment",
        participant_label_file='_rooms/participant_labels.txt',
    ),
    dict(
        name="tax_ctpf4",
        display_name="Eksperimen Perilaku Perpajakan Sesi 4 - Prefilled Form + Corruption Treatment",
        participant_label_file='_rooms/participant_labels.txt',
    )

]

ADMIN_USERNAME = "admin"
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get("OTREE_ADMIN_PASSWORD")
DEBUG = False
AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

DEMO_PAGE_TITLE = "Eksperimen Perilaku Perpajakan"
DEMO_PAGE_INTRO_HTML = """
Selamat Datang di Eksperimen kami. Eksperimen ini diperuntukan penelitian tentang Perilaku Perpajakan.
"""

SECRET_KEY = "2015765205890"

# adjustments for testing
# generating session configs for all varieties of features
if sys.argv[1] == 'test':
    MAX_ITERATIONS = 5
    FREEZE_TIME = 0.1
    TRIAL_PAUSE = 0.2
    TRIAL_TIMEOUT = 0.3

    for task in ['task_math1']:
        SESSION_CONFIGS.extend(
            [
                dict(
                    name=f"testing_{task}_defaults",
                    num_demo_participants=1,
                    app_sequence=['task_math1'],
                    puzzle_delay=TRIAL_PAUSE,
                    retry_delay=FREEZE_TIME,
                ),
                dict(
                    name=f"testing_{task}_retrying",
                    num_demo_participants=1,
                    app_sequence=['task_math1'],
                    puzzle_delay=TRIAL_PAUSE,
                    retry_delay=FREEZE_TIME,
                    attempts_per_puzzle=5,
                ),
                dict(
                    name=f"testing_{task}_limited",
                    num_demo_participants=1,
                    app_sequence=['task_math1'],
                    puzzle_delay=TRIAL_PAUSE,
                    retry_delay=FREEZE_TIME,
                    max_iterations=MAX_ITERATIONS,
                )
            ]
        )
