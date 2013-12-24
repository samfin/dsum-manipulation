import math
import numpy
from scipy.stats import norm
from config import *

def distribution_add(x, y):
    z = numpy.convolve(x, y)
    for i in range(256, len(z)):
        z[i-256] += z[i]
    return z[0:256]

def distribution_normalize(x):
    s = sum(x)
    for i in range(len(x)):
        x[i] /= s

class Calculator(object):
    def __init__(self, prior = None):
        if prior is None:
            prior = numpy.ones(256)
        self.prior = prior
        self.dsum_data = {}
        self.encounter_data = {}
        self.step_data = {}
        self.data = {}

        # Distribution to convert dsum distribution to encounter distribution
        self.conversion_factor = numpy.zeros(256)
        for i in range(ENCOUNTER_RATE):
            self.conversion_factor[(256 - i) % 256] = 1.0 / ENCOUNTER_RATE

    def reset_memoized_data(self):
        self.dsum_data = {}
        self.encounter_data = {}
        self.step_data = {}
        self.data = {}

    def update_prior(self, encounter, n_steps):
        self.prior = self.dsum_distribution(encounter, n_steps)
        self.reset_memoized_data()

    def encounter_term(self, encounter):
        # Get initial dsum distribution based on encounter slot
        if encounter in self.encounter_data:
            return self.encounter_data[encounter]

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

        self.encounter_data[encounter] = out
        return out

    def step_term(self, n_steps):
        # Get dsum change distribution from running away from encounter and taking n_steps steps
        if n_steps in self.step_data:
            return self.step_data[n_steps]

        stdev = math.sqrt(n_steps * DSUM_PER_STEP_STDEV * DSUM_PER_STEP_STDEV + DSUM_STDEV * DSUM_STDEV)
        mean = ((DSUM_PER_STEP * n_steps + DSUM_DIFF) % 256 + 256) % 256
        out = numpy.zeros(256)
        MAX_DEV = int(6 * stdev + 1)
        for i in range(-MAX_DEV + int(mean), MAX_DEV + int(mean)):
            a = (i + 256) % 256
            out[a] += norm.cdf((i + 0.5 - mean) / stdev) - norm.cdf((i - 0.5 - mean) / stdev)
        distribution_normalize(out)

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
