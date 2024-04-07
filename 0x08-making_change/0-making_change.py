#!/usr/bin/python3
"""Coin Change Problem"""


def makeChange(coins, total):
    """provide change"""
    num_coins = 0
    if not coins:
        return -1
    if total == 0:
        return num_coins
    while (total) and coins != []:
        big = max(coins)
        num_coins = num_coins + (total // big)
        total = total % big
        coins.remove(big)
    return num_coins if total == 0 else -1
