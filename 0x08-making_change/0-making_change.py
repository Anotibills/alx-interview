#!/usr/bin/python3
"""
This determine the fewest number of coins needed to meet a given amount total
"""


def makeChange(coins, total):
    """
    This calculates and returns the fewest numbers of coins
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    index, coin_count = 0, 0
    remaining_total = total
    num_coins = len(coins)

    while index < num_coins and remaining_total > 0:
        if (remaining_total - coins[index]) >= 0:
            remaining_total -= coins[index]
            coin_count += 1
        else:
            index += 1

    check = remaining_total > 0 and coin_count > 0
    return -1 if check or coin_count == 0 else coin_count
