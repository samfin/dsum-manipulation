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

def distribution_constant():
    y = numpy.zeros(256)
    for i in range(ENCOUNTER_RATE):
        y[i] = 1.0 / ENCOUNTER_RATE

    z = numpy.zeros(256)
    MAX_DEV = int(6 * DSUM_STDEV)
    for i in range(-MAX_DEV, MAX_DEV + 1):
        a = (i + 256) % 256
        z[a] += norm.cdf((i + 0.5) / DSUM_STDEV) - norm.cdf((i - 0.5) / DSUM_STDEV)
    distribution_normalize(z)

    w = numpy.zeros(256)
    for i in range(ENCOUNTER_RATE):
        w[(256 - i) % 256] = 1.0 / ENCOUNTER_RATE

    return reduce(distribution_add, [y, z, w])

distribution_constant = distribution_constant()

def distribution_base(n_steps):
    if n_steps in distribution_base.data:
        return distribution_base.data[n_steps]

    x = numpy.zeros(256)
    t = (DSUM_PER_STEP * n_steps + DSUM_DIFF) % 256
    if t < 0:
        t += 256
    u = int(t)
    x[u] = 1 - (t - u)
    x[(u+1) % 256] = t - u

    y = numpy.zeros(256)
    stdev = math.sqrt(n_steps) * DSUM_PER_STEP_STDEV
    if stdev < 1e-4:
        y[0] = 1
    else:
        MAX_DEV = int(4 * stdev)
        for i in range(-MAX_DEV, MAX_DEV + 1):
            a = (i + 256) % 256
            y[a] += norm.cdf((i + 0.5) / stdev) - norm.cdf((i - 0.5) / stdev)
        distribution_normalize(y)

    dist = reduce(distribution_add, [x, y, distribution_constant])
    distribution_base.data[n_steps] = dist
    return dist

distribution_base.data = {}

def distribution(ind, time):
    x = distribution_base(time)

    y = numpy.zeros(256)
    n = (ENCOUNTER_SLOTS[ind+1] - ENCOUNTER_SLOTS[ind])
    for i in range(ENCOUNTER_SLOTS[ind] + 1, ENCOUNTER_SLOTS[ind+1] + 1):
        y[i] = 1.0 / n

    dist = distribution_add(x, y)

    out = [0] * 10
    for i in range(10):
        out[i] = sum(dist[ENCOUNTER_SLOTS[i] + 1 : ENCOUNTER_SLOTS[i+1] + 1])

    return out
