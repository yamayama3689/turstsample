from os import environ


SESSION_CONFIGS = [
    {
        "name": "RMI_p_human",
        "display_name": "RMI_p_human",
        "num_demo_participants": 1,
        "app_sequence": ["jsai_demo_round", "rmi_p_human", "trustgame_survey"],
    },
    {
        "name": "RMI_m_human",
        "display_name": "RMI_m_human",
        "num_demo_participants": 1,
        "app_sequence": ["jsai_demo_round", "rmi_m_human", "trustgame_survey"],
    },
    {
        "name": "RMI_p_robot",
        "display_name": "RMI_p_robot",
        "num_demo_participants": 1,
        "app_sequence": ["jsai_demo_round", "rmi_p_robot", "trustgame_survey"],
    },
    {
        "name": "RMI_m_robot",
        "display_name": "RMI_m_robot",
        "num_demo_participants": 1,
        "app_sequence": ["jsai_demo_round", "rmi_m_robot", "trustgame_survey"],
    },
    # {
    #     "name": "trustgame_aftersurvey",
    #     "display_name": "信頼ゲーム_事後質問",
    #     "num_demo_participants": 2,
    #     "app_sequence": ["trust_simple", "trustgame_survey"],
    # },
    # {
    #     "name": "trust_participant_train",
    #     "display_name": "参加者オブジェクトについて（信頼ゲーム）",
    #     "num_demo_participants": 2,
    #     "app_sequence": ["trust_participant_train", "trust_last_human"],
    # },
    # {
    #     "name": "trust_last_human",
    #     "display_name": "最終取引(人間) ",
    #     "num_demo_participants": 2,
    #     "app_sequence": ["trust_last_human"],
    # },
    # {
    #     "name": "trust_human",
    #     "display_name": "依存度選択囚人のジレンマ",
    #     "num_demo_participants": 2,
    #     "app_sequence": ["trust_two", "trust_last_human"],
    # },
    # dict(
    #     name='guess_two_thirds',
    #     display_name="Guess 2/3 of the Average",
    #     app_sequence=['guess_two_thirds', 'payment_info'],
    #     num_demo_participants=3,
    # ),
    # dict(
    #     name='survey', app_sequence=['survey', 'payment_info'], num_demo_participants=1
    # ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
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
        name='jsai02_17_1400',
        display_name='2月17日14:00枠',
        participant_label_file='_rooms/jsai02_17_1400.txt',
    ),
    dict(
        name='jsai02_18_1400ex1',
        display_name='2月18日14:00枠実験1',
        participant_label_file='_rooms/jsai02_18_1400.txt',
    ),
    dict(
        name='jsai02_18_1400ex2',
        display_name='2月18日14:00枠実験2',
        participant_label_file='_rooms/jsai02_18_1400.txt',
    ),
    dict(
        name='jsai02_18_2000ex1',
        display_name='2月18日20:00枠実験1',
        participant_label_file='_rooms/jsai02_18_2000.txt',
    ),
    dict(
        name='jsai02_18_2000ex2',
        display_name='2月18日20:00枠実験2',
        participant_label_file='_rooms/jsai02_18_2000.txt',
    ),
    dict(
        name='jsai02_21_1400ex1',
        display_name='2月21日14:00枠実験1',
        participant_label_file='_rooms/jsai02_21_1400.txt',
    ),
    dict(
        name='jsai02_21_1400ex2',
        display_name='2月21日14:00枠実験2',
        participant_label_file='_rooms/jsai02_21_1400.txt',
    ),
    dict(
        name='jsai02_21_2000ex1',
        display_name='2月21日20:00枠実験1',
        participant_label_file='_rooms/jsai02_21_2000.txt',
    ),
    dict(
        name='jsai02_21_2000ex2',
        display_name='2月21日20:00枠実験2',
        participant_label_file='_rooms/jsai02_21_2000.txt',
    ),
    dict(
        name='jsai02_22_1400ex1',
        display_name='2月22日14:00枠実験1',
        participant_label_file='_rooms/jsai02_22_1400.txt',
    ),
    dict(
        name='jsai02_22_1400ex2',
        display_name='2月22日14:00枠実験2',
        participant_label_file='_rooms/jsai02_22_1400.txt',
    ),
    # dict(
    #     name='econ101',
    #     display_name='Econ 101 class',
    #     participant_label_file='_rooms/econ101.txt',
    #     #use_secure_urls=True
    # ),
    #dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '3583200750768'

INSTALLED_APPS = ['otree']

