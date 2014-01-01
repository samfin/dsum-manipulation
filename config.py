IS_YELLOW = False
ODDISH_ROUTE = False
RAT_ROUTE = False
ABRA_ROUTE = True

ENCOUNTER_RATE = 0x19
STEP_SPEED = 59.7 / 17

# red
ENCOUNTER_TIME = 60
DSUM_PER_STEP = -11.3961556406
DSUM_PER_STEP_STDEV = 1.56276899796
BATTLE_DIFFS = {
    'RATTATA':  (-85.7504069891, 11.0341694943),
    'NIDO_M':   (-82.3644472131, 11.677758745),
    'SPEAROW':  (-74.1037938989, 11.7238796452),
    'NIDO_F':   (-83.196335575, 9.56496516309),
    'PIDGEY':   (-87.233689757, 9.86946893711),
    'WEEDLE':   (-76.40608555, 8.41922306989),
}
DSUM_DIFF = -75
DSUM_STDEV = 12

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
    DSUM_PER_STEP = -11.5718242214
    DSUM_PER_STEP_STDEV = 1.39137230179
    DESIRED_SLOTS = [3, 7]
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

if ABRA_ROUTE:
    ENCOUNTER_RATE = 0x0f
    DESIRED_SLOTS = [5,7]
    ENCOUNTER_NAMES = [
        'WEEDLE 8',
        'KAKUNA 9',
        'PIDGEY 13',
        'ODDISH 12',
        'ODDISH 13',
        'ABRA   12',
        'ODDISH 14',
        'ABRA   10',
        'METAPOD 7',
        'CATERPIE 8'
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
