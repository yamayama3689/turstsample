from os import environ


SESSION_CONFIGS = [
    {
        "name": "common_value_auction",
        "display_name": "common_value_auction",
        "num_demo_participants": 1,
        "app_sequence": ["common_value_auction"],
    },
    {
        "name": "RMI_p_human",
        "display_name": "RMI_p_human",
        "num_demo_participants": 1,
        "app_sequence": ["rmi_p_human"],
    },
    {
        "name": "trustgame_aftersurvey",
        "display_name": "信頼ゲーム_事後質問",
        "num_demo_participants": 2,
        "app_sequence": ["trust_simple", "trustgame_survey"],
    },
    {
        "name": "trust_participant_train",
        "display_name": "参加者オブジェクトについて（信頼ゲーム）",
        "num_demo_participants": 2,
        "app_sequence": ["trust_participant_train", "trust_last_human"],
    },
    {
        "name": "trust_last_human",
        "display_name": "最終取引(人間) ",
        "num_demo_participants": 2,
        "app_sequence": ["trust_last_human"],
    },
    {
        "name": "trust_human",
        "display_name": "依存度選択囚人のジレンマ",
        "num_demo_participants": 2,
        "app_sequence": ["trust_two", "trust_last_human"],
    },
    {
        "name": "trust_trust",
        "display_name": "相互信頼ゲーム",
        "num_demo_participants": 2,
        "app_sequence": ["trust_trust"],
    },
    {
        "name": "trustsingle",
        "display_name": "一人信頼ゲーム",
        "num_demo_participants": 1,
        "app_sequence": ["trustsingle"],
    },
    {
        "name": "sequential_prisoner_dilemma",
        "display_name": "繰り返し囚人のジレンマデモ",
        "num_demo_participants": 2,
        "app_sequence": ["sequential_prisoner_dilemma"],
    },
    {
        "name": "trust_simple",
        "display_name": "信頼ゲームだよ",
        "num_demo_participants": 2,
        "app_sequence": ["trust_simple"],
    },
    dict(
        name='guess_two_thirds',
        display_name="Guess 2/3 of the Average",
        app_sequence=['guess_two_thirds', 'payment_info'],
        num_demo_participants=3,
    ),
    dict(
        name='survey', app_sequence=['survey', 'payment_info'], num_demo_participants=1
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=2.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'ja'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'JPY'
USE_POINTS = False

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
        #use_secure_urls=True
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '3583200750768'

INSTALLED_APPS = ['otree']

