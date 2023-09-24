#!/usr/bin/python3
"""making change.
"""


def makeChange(coins, total):
    """making change
    """
    if total <= 0:
        return 0
    tot = total
    count = 0
    idx = 0
    s_coins = sorted(coins, reverse=True)
    n = len(coins)
    while tot > 0:
        if idx >= n:
            return -1
        if tot - s_coins[idx] >= 0:
            tot -= s_coins[idx]
            count += 1
        else:
            idx += 1
    return count
