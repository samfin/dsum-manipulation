IS_YELLOW = True
ODDISH_ROUTE = False
RAT_ROUTE = False

ENCOUNTER_RATE = 0x19
# Cost in steps of an encounter
ENCOUNTER_TIME = 45

# red
STEP_SPEED = 59.7 / 16
DSUM_DIFF = 256 - 82.488
DSUM_STDEV = 7.417
DSUM_PER_STEP = {
    -16: 0.0014282313734825041,
    -15: 0.0049988098071887645,
    -14: 0.03761009283503928,
    -13: 0.15305879552487503,
    -12: 0.2751725779576291,
    -11: 0.2932635086884075,
    -10: 0.17686265174958343,
    -9: 0.050940252320875984,
    -8: 0.006427041180671268,
    -7: 0.00023803856224708403
}
BATTLE_DIFFS = {
    'RATTATA':  (-70.6554, 8.212372),
    'NIDO_M':   (-67.6164, 8.287307),
    'SPEAROW':  (-58.6786, 7.902431),
    'NIDO_F':   (-65.6667, 6.604785)
}

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
    BATTLE_DIFFS = {
        'PIDGEY': (49.723, ),

    }
    DSUM_PER_STEP = {
        0: 0.00014974094815968376,
        1: 0.001756960458406956,
        2: 0.015283559442165055,
        3: 0.06867119882603097,
        4: 0.18226468209996705,
        5: 0.29292324278997334,
        6: 0.2638635161171174,
        7: 0.1349565252113843,
        8: 0.036407015862557776,
        9: 0.0036636618649735957,
        10: 5.98963792638735e-05
    }
    print sum(x * DSUM_PER_STEP[x] for x in DSUM_PER_STEP)
    DSUM_DIFF = 256 - 54.02
    DSUM_STDEV = 8.5929
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
