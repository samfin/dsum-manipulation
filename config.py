IS_YELLOW = True
ODDISH_ROUTE = False
RAT_ROUTE = False

ENCOUNTER_RATE = 0x19
# Cost in steps of an encounter
ENCOUNTER_TIME = 44

# red
DSUM_SPEED = -0x50 / 500.19
STEP_SPEED = 59.7 / 16
DSUM_DIFF = 256 - 112.84
DSUM_STDEV = 8.655209591

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
    DSUM_SPEED = (0x4f - 0x0b) / 772.06
    DSUM_DIFF = 256 - 38.28571429
    DSUM_STDEV = 9.05724094
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

DSUM_PER_STEP = DSUM_SPEED / STEP_SPEED * 256
DSUM_PER_STEP_STDEV = abs(0.1 * DSUM_PER_STEP) # NOT ACTUALLY FROM A MEASUREMENT

ENCOUNTER_SLOTS = [-1,50,101,140,165,190,215,228,241,252,255]
