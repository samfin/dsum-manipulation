IS_YELLOW = False
ODDISH_ROUTE = False
RAT_ROUTE = False

ENCOUNTER_RATE = 0x19
STEP_SPEED = 59.7 / 17

# red
ENCOUNTER_TIME = 60
DSUM_PER_STEP = -11.4591695436
DSUM_PER_STEP_STDEV = 1.52559982827
BATTLE_DIFFS = {
    'RATTATA':  (-85.4315373942, 10.6719762185),
    'NIDO_M':   (-81.2629732485, 11.859172285),
    'SPEAROW':  (-73.7095633338, 12.1061073504),
    'NIDO_F':   (-82.3748960147, 10.1722152243),
}
DSUM_DIFF = -68
DSUM_STDEV = 9


DESIRED_SLOTS = [1,3]
ENCOUNTER_NAMES = [
    'RATTATA 3',
    'NIDO_M  3',
    'RATTATA 4',
    'NIDO M  4',
    'RATTATA 2',
    'NIDO_M  2',
    'SPEAROW 3',
    'SPEAROW 5',
    'NIDO_F  3',
    'NIDO_F  4'
]

if RAT_ROUTE:
    DESIRED_SLOTS = [7]
    ENCOUNTER_NAMES = [
        'RATTATA 3',
        'PIDGEY  3',
        'PIDGEY  4',
        'RATTATA 4',
        'PIDGEY  5',
        'WEEDLE  3',
        'RATTATA 2',
        'RATTATA 5',
        'WEEDLE  4',
        'WEEDLE  5'
    ]

if ODDISH_ROUTE:
    ENCOUNTER_RATE = 0x0f
    DESIRED_SLOTS = [0,5,6]
    ENCOUNTER_NAMES = [
        'ODDISH 13',
        'PIDGEY 13',
        'PIDGEY 15',
        'MANKEY 10',
        'MANKEY 12',
        'ODDISH 15',
        'ODDISH 16',
        'PIDGEY 16',
        'MANKEY 14',
        'MANKEY 16'
    ]

# yellow
if IS_YELLOW:
    DSUM_PER_STEP = 5.438174611
    DSUM_PER_STEP_STDEV = 1.47650834106
    DSUM_DIFF = -50
    ENCOUNTER_TIME = 60
    DSUM_STDEV = 11
    BATTLE_DIFFS = {
        'RATTATA':  (-51.9659, 10.56725),
        'NIDO_M':   (-46.1942, 9.433774),
        'NIDO_F':   (-46.8695, 9.775967),
        'PIDGEY':   (-54.9492, 10.56564)
    }
    DESIRED_SLOTS = [6]
    ENCOUNTER_NAMES = [
        'RATTATA 3',
        'PIDGEY  3',
        'RATTATA 4',
        'NIDO_M  4',
        'NIDO_F  4',
        'PIDGEY  5',
        'NIDO_M  6',
        'NIDO_F  6',
        'PIDGEY  7',
        'PIDGEY  7'
    ]


ENCOUNTER_SLOTS = [-1,50,101,140,165,190,215,228,241,252,255]
