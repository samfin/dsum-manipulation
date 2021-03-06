import math
import numpy
from scipy.stats import norm
from config import *

def distribution_add(x, y):
    z = numpy.convolve(x, y)
    for i in range(256, len(z)):
        z[i-256] += z[i]
    return z[0:256]

def distribution_multiply(x, n):
    out = numpy.zeros(256)
    out[0] = 1

    while n > 0:
        if n % 2:
            out = distribution_add(out, x)
        x = distribution_add(x, x)
        n /= 2

    return out

def distribution_normalize(x):
    s = sum(x)
    for i in range(len(x)):
        x[i] /= s

# Convert dictionary of probabilities to numpy distribution
def distirbution_convert(d):
    dist = numpy.zeros(256)
    for x in d:
        a = x
        if a < 0:
            a += 256
        dist[a] = d[x]
    return dist

def distribution_gaussian(mean, stdev):
    x = numpy.zeros(256)
    mean = ((mean % 256) + 256) % 256
    MAX_DEV = int(6 * stdev + 1)
    for i in range(-MAX_DEV + int(mean), MAX_DEV + int(mean)):
        a = (i + 256) % 256
        x[a] += norm.cdf((i + 0.5 - mean) / stdev) - norm.cdf((i - 0.5 - mean) / stdev)
    distribution_normalize(x)
    return x

class Calculator(object):
    def __init__(self, prior = None):
        if prior is None:
            prior = numpy.ones(256)
        self.prior = prior
        self.dsum_data = {}
        self.encounter_data = {}
        self.data = {}
        self.step_data = {}

        # Distribution to convert dsum distribution to encounter distribution
        self.conversion_factor = numpy.zeros(256)
        for i in range(ENCOUNTER_RATE):
            self.conversion_factor[(256 - i) % 256] = 1.0 / ENCOUNTER_RATE

        # Get per-step distribution
        if isinstance(DSUM_PER_STEP, dict):
            self.step_data[1] = distirbution_convert(DSUM_PER_STEP)
        else:
            self.step_data[1] = distribution_gaussian(DSUM_PER_STEP, DSUM_PER_STEP_STDEV)

        # Get battle distribution
        self.battle_constant = []
        for i in range(10):
            x = numpy.zeros(256)
            name = ENCOUNTER_NAMES[i].split(' ')[0]
            if name in BATTLE_DIFFS:
                mean, stdev = BATTLE_DIFFS[name]
            else:
                mean, stdev = DSUM_DIFF, DSUM_STDEV
            x = distribution_gaussian(mean, stdev)
            self.battle_constant.append(x)

    def reset_memoized_data(self):
        self.encounter_data = {}
        self.dsum_data = {}
        self.data = {}

    def update_prior(self, encounter, n_steps):
        self.prior = self.dsum_distribution(encounter, n_steps)
        self.reset_memoized_data()

    def encounter_term(self, encounter):
        # Get initial dsum distribution based on encounter slot
        if encounter in self.encounter_data:
            return self.encounter_data[encounter]

        # First get dsum distribution immediately before the encounter
        x = numpy.zeros(256)
        for i in range(ENCOUNTER_RATE):
            x[i] = 1.0 / ENCOUNTER_RATE

        y = numpy.zeros(256)
        for i in range(ENCOUNTER_SLOTS[encounter] + 1, ENCOUNTER_SLOTS[encounter+1] + 1):
            y[i] = 1

        z = distribution_add(x, y)
        # z[k] = probability of given encounter slot given that dsum is k
        # Use Bayes rule to get probability that dsum is k given encounter slot
        out = z * self.prior
        distribution_normalize(out)


        # Add in the cost of running from the encounter
        out = distribution_add(out, self.battle_constant[encounter])

        self.encounter_data[encounter] = out
        return out

    def step_term(self, n_steps):
        # Get dsum change distribution from taking n_steps steps
        if n_steps in self.step_data:
            return self.step_data[n_steps]

        if n_steps - 1 in self.step_data:
            out = distribution_add(self.step_data[n_steps - 1], self.step_data[1])
        else:
            out = distribution_multiply(self.step_data[1], n_steps)

        self.step_data[n_steps] = out
        return out

    def dsum_distribution(self, encounter, n_steps):
        args = (encounter, n_steps)
        if args in self.dsum_data:
            return self.dsum_data[args]

        out = distribution_add(self.encounter_term(encounter), self.step_term(n_steps))

        self.dsum_data[args] = out
        return out

    def distribution(self, encounter, n_steps):
        args = (encounter, n_steps)
        if args in self.data:
            return self.data[args]

        dist = distribution_add(self.dsum_distribution(encounter, n_steps), self.conversion_factor)

        # Convert distribution on encounter byte to distribution on encounter slots
        out = [0] * 10
        for i in range(10):
            out[i] = sum(dist[ENCOUNTER_SLOTS[i] + 1 : ENCOUNTER_SLOTS[i+1] + 1])

        self.data[args] = out
        return out
