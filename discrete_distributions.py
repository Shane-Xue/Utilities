from random import random
import numpy as np


def bernoulli(successProb):
    return 1 if random() < successProb else 0


def binomial(trials, successProb):
    """returns the times of trials that are successful in 'trials' trials"""
    return sum([bernoulli(successProb) for a in range(trials)])


def negBinomial(fails_expect, successProb):
    fails = 0
    times = 0
    while fails != fails_expect:
        if bernoulli(successProb) == 0:
            fails += 1
        times += 1
    return times


def main():
    print(np.mean([bernoulli(0.63)
                  for a in range(10000)]))  # sth around 0.63
    print(np.mean([binomial(100, 0.63)
                  for a in range(10000)]))  # sth around 63
    print(np.mean([negBinomial(37, 0.63)
                  for a in range(10000)]))   # sth around 100


def test_bernoulli():
    for a in range(10000):
        rand = random()
        assert abs(np.mean([bernoulli(rand)
                   for a in range(10000)]) - rand) < 0.1


if __name__ == "__main__":
    main()
