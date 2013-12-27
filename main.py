import copy
import distribution
import numpy
from config import *

# Optimize for minimal number time in expectation
class Optimizer(object):
    def __init__(self, n, desired):
        n -= 2
        self.n = n
        self.INF = 10000
        self.calculator = distribution.Calculator()
        self.distribution = {}
        for slot in range(10):
            self.distribution[slot] = {}
            for t in range(n):
                self.distribution[slot][t] = self.calculator.distribution(slot, t)
        self.costs = [self.INF] * 10
        self.desired = desired
        for x in self.desired:
            self.costs[x] = 0

        self.p_encounter = ENCOUNTER_RATE / 256.0
        self.base_distribution = [(ENCOUNTER_SLOTS[i+1] - ENCOUNTER_SLOTS[i]) / 256.0 for i in range(10)]

    def eval(self, strats):
        costs = []
        coefficients = []
        p_encounter = self.p_encounter
        if len(strats) != 10:
            raise Exception("Need to provide strats for all 10 encounter slots")
        for i in range(10):
            x = [0] * 10

            cost = 1 / p_encounter
            for j in range(10):
                if j in self.desired:
                    continue
                cost += self.base_distribution[j] * ENCOUNTER_TIME
                x[j] += self.base_distribution[j]

            strat = strats[i]
            n = len(strat)
            if n > self.n:
                raise Exception("Strat %d with %d elements is too long, preprocessing only goes up to %d." % (i, n, self.n))
            for k in reversed(range(n)):
                if strat[k] == 0:
                    cost += 1
                    continue
                dist = self.distribution[i][k]
                s = sum(ENCOUNTER_TIME * dist[j] for j in range(10) if j not in self.desired)
                cost = 1 + p_encounter * s + (1 - p_encounter) * cost
                for j in range(10):
                    if j in self.desired:
                        continue
                    x[j] = p_encounter * dist[j] + (1 - p_encounter) * x[j]
            costs.append(cost)
            coefficients.append(x)

        x = numpy.linalg.inv(numpy.identity(10) - numpy.matrix(coefficients))
        out = [sum(x.item((i, j)) * costs[j] for j in range(10)) for i in range(10)]
        return out

    # Expected cost of an encounter from given distribution
    def expected_cost(self, dist):
        costs = self.costs
        x = sum(dist[i] * (costs[i] + ENCOUNTER_TIME) for i in range(10) if i not in self.desired)
        return x

    def optimize_once(self, slot):
        expected_costs = [self.expected_cost(self.distribution[slot][k]) for k in range(self.n)]

        p_encounter = self.p_encounter
        failure_cost = 1 / self.p_encounter + self.expected_cost(self.base_distribution)

        strat = []
        for k in reversed(range(self.n)):
            no_encounter_cost = 1 + failure_cost
            encounter_cost = 1 + p_encounter * expected_costs[k]  + (1 - p_encounter) * failure_cost
            failure_cost = min(no_encounter_cost, encounter_cost)
            strat.append(int(encounter_cost < no_encounter_cost))
        strat.reverse()
        return strat, failure_cost

    def optimize(self, n_iterations = 200):
        strats, costs = [], []
        for i in range(n_iterations):
            strats, costs = [], []
            last_costs = self.costs
            for slot in range(10):
                strat, cost = self.optimize_once(slot)
                strats.append(strat)
                costs.append(cost)
            self.costs = copy.copy(costs)
            for slot in self.desired:
                self.costs[slot] = 0
            dcosts = sum([(last_costs[i] - self.costs[i]) ** 2 for i in range(len(costs))])
            if dcosts < 1e-6:
                break
        return strats, costs

# Optimize for maximum probability within a time threshold
class Maximizer(object):
    def __init__(self, n, desired):
        n -= 2
        self.n = n
        self.calculator = distribution.Calculator()
        self.distribution = {}
        for slot in range(10):
            self.distribution[slot] = {}
            for t in range(n):
                self.distribution[slot][t] = self.calculator.distribution(slot, t)
        self.desired = desired

        self.p_encounter = ENCOUNTER_RATE / 256.0
        self.probabilities = {}
        self.base_distribution = [(ENCOUNTER_SLOTS[i+1] - ENCOUNTER_SLOTS[i]) / 256.0 for i in range(10)]

    def probability(self, dist, steps_left):
        if steps_left >= 0:
            x = sum(dist[i] * (1 if i in self.desired else self.probabilities[steps_left][i]) for i in range(10))
        else:
            x = sum(dist[i] for i in self.desired)
        return x

    def maximize(self, steps_left):
        n = self.n
        p_encounter = self.p_encounter
        out = []
        p_desired = sum([ENCOUNTER_SLOTS[i+1] - ENCOUNTER_SLOTS[i] for i in self.desired]) / 256.0

        boundary_p = 0
        for s in range(steps_left + 1):
            # Assume that after n steps, we know nothing about distribution and take every step in the grass
            if s > n:
                boundary_p = p_encounter * self.probability(self.base_distribution, s - n - 1 - ENCOUNTER_TIME) + (1 - p_encounter) * boundary_p
            self.probabilities[s] = [0] * 10
            strats = []
            for i in range(10):
                p = boundary_p
                strat = []
                for k in reversed(range(n)):
                    if k >= s:
                        strat.append(0)
                        continue
                    t = p_encounter * self.probability(self.distribution[i][k], s - k - 1 - ENCOUNTER_TIME) + (1 - p_encounter) * p
                    strat.append(int(t > p))
                    p = max(t, p)
                self.probabilities[s][i] = p
                strat.reverse()
                strats.append(strat)
            out.append(strats)
        return out, self.probabilities[steps_left]

def print_array(arr):
    def collapse(arr):
        arr.append(-1)
        first = None
        last = None
        out = []
        s = 0
        for x in arr:
            if x != last:
                if last is not None:
                    out.append(s)
                if last is None:
                    s = 3
                    first = x
                else:
                    s = 1
                last = x
            else:
                s += 1

        return (out, first)
    arr, p = collapse(arr)
    s = []
    from termcolor import colored
    for i in range(len(arr)):
        if i % 2 == p:
            s.append(colored(arr[i], 'blue', attrs=['bold']))
        else:
            s.append(colored(arr[i], 'red', attrs=['bold']))
    s = ', '.join(s)
    print '[%s]' % s

def test(steps):
    steps -= 2
    maximizer = Maximizer(100, DESIRED_SLOTS)
    strats, p = maximizer.maximize(steps)
    strats = strats[-1]
    for i in range(10):
        print ENCOUNTER_NAMES[i]
        print_array(strats[i])
        print ''

def main():
    optimizer = Optimizer(100, DESIRED_SLOTS)
    strats, costs = optimizer.optimize()
    for i in range(10):
        print ENCOUNTER_NAMES[i]
        print_array(strats[i])
        print ''

if __name__ == '__main__':
    import sys
    import colorama
    colorama.init()

    if len(sys.argv) > 1:
        test(int(sys.argv[1]))
    else:
        main()
