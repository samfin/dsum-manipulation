IS_YELLOW = False
ODDISH_ROUTE = False
RAT_ROUTE = False
ABRA_ROUTE = False
ABRA_ROUTE_2 = False
RANDOMIZER = True

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

if RANDOMIZER:
    ENCOUNTER_TIME = 50
    DSUM_DIFF = -67
    DSUM_STDEV = 15
    BATTLE_DIFFS = {}
    DESIRED_SLOTS = [6,7,8,9]

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
    BATTLE_DIFFS = {
        'METAPOD':  (-80.9879781562, 10.7898602064),
        'CATERPIE': (-79.3087537818, 10.5088387177),
        'ODDISH':   (-87.7140276047, 14.0405994154),
        'ABRA':     (-75.8244204999, 14.1599552928),
        'KAKUNA':   (-84.5727629967, 13.15367056),
        'PIDGEY':   (-93.5994060867, 14.416049601),
        'WEEDLE':   (-85.3388622727, 12.9513812634),
    }
    DSUM_DIFF += 9
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

if ABRA_ROUTE_2:
    BATTLE_DIFFS = {
        'ODDISH':   (-83.8234050834, 11.444339233),
        'ABRA':     (-73.5804643175, 11.314334087),
        'KAKUNA':   (-80.0182788576, 10.0494974544),
        'PIDGEY':   (-91.103898243, 10.2958962562),
        'WEEDLE':   (-82.2996521266, 10.4410590273),
    }
    DSUM_DIFF += 9
    DESIRED_SLOTS = [5,8,9]
    ENCOUNTER_NAMES = [
        'WEEDLE 7',
        'KAKUNA 8',
        'PIDGEY 12',
        'ODDISH 12',
        'ODDISH 13',
        'ABRA   10',
        'ODDISH 14',
        'PIDGEY 13',
        'ABRA   8',
        'ABRA   12'
    ]

# yellow
if IS_YELLOW:
    DSUM_PER_STEP = 5.438174611
    DSUM_PER_STEP_STDEV = 1.47650834106
    DSUM_DIFF = -46
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

    if RANDOMIZER:
        ENCOUNTER_TIME = 55
        DSUM_DIFF = -40
        DSUM_STDEV = 15
        BATTLE_DIFFS = {}
        DESIRED_SLOTS = [6,7,8,9]

    if ABRA_ROUTE:
        ENCOUNTER_RATE = 0x0f
        DESIRED_SLOTS = [2]
        for x in BATTLE_DIFFS:
            a, b = BATTLE_DIFFS[x]
            BATTLE_DIFFS[x] = (a+20, b)
        DSUM_DIFF += 20
        ENCOUNTER_NAMES = [
            'PIDGEY  15',
            'RATTATA 14',
            'ABRA    7',
            'PIDGEY  16',
            'RATTATA 16',
            'PIDGEY  17',
            'PIDGEOTTO 17',
            'JIGGLYPUFF 3',
            'JIGGLYPUFF 5',
            'JIGGLYPUFF 7'
        ]

ENCOUNTER_SLOTS = [-1,50,101,140,165,190,215,228,241,252,255]
