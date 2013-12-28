IS_YELLOW = True
ODDISH_ROUTE = False
RAT_ROUTE = False

ENCOUNTER_RATE = 0x19
# Cost in steps of an encounter
ENCOUNTER_TIME = 45

# red
STEP_SPEED = 59.7 / 16
DSUM_DIFF = -68
DSUM_STDEV = 9
DSUM_PER_STEP = {
    -18: 0.0002131590166264033,
    -17: 0.0006394770498792099,
    -16: 0.0036947562881909906,
    -15: 0.01520534318601677,
    -14: 0.05442660224527498,
    -13: 0.1561745061816115,
    -12: 0.2773909336364928,
    -11: 0.28712519539576525,
    -10: 0.15574818814835867,
    -9: 0.04440812846383402,
    -8: 0.004405286343612335,
    -7: 0.0005684240443370755
}
BATTLE_DIFFS = {
    'RATTATA':  (-70.6554, 8.212372),
    'NIDO_M':   (-67.6164, 8.287307),
    'SPEAROW':  (-58.6786, 7.902431),
    'NIDO_F':   (-65.6667, 6.604785),
    'PIDGEY':   (-71.7398, 7.007904),
    'WEEDLE':   (-63.2421, 6.225949)
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
