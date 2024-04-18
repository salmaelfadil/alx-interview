#!/usr/bin/python3
"""Prime Game Module"""


def isWinner(x, nums):
    """finds the winner"""
    winner_counter = {'Maria': 0, 'Ben': 0}

    for i in range(x):
        round_winner = determine_round_winner(nums[i], x)
        if round_winner is not None:
            winner_counter[round_winner] += 1

    if winner_counter['Maria'] > winner_counter['Ben']:
        return 'Maria'
    elif winner_counter['Ben'] > winner_counter['Maria']:
        return 'Ben'
    else:
        return None


def determine_round_winner(n, x):
    """returns the winner of a single round"""
    num_list = list(range(1, n + 1))
    players = ['Maria', 'Ben']

    for i in range(n):
        current_player = players[i % 2]
        selected_idxs = []
        prime = -1
        for idx, num in enumerate(num_list):
            if prime != -1:
                if num % prime == 0:
                    selected_idxs.append(idx)
            else:
                if is_prime(num):
                    selected_idxs.append(idx)
                    prime = num
        if prime == -1:
            if current_player == players[0]:
                return players[1]
            else:
                return players[0]
        else:
            for idx, val in enumerate(selected_idxs):
                del num_list[val - idx]
    return None


def is_prime(n):
    """determines if a number is prime"""
    if n < 2 or (n > 2 and n % 2 == 0):
        return False
    else:
        for i in range(3, int(n**(1/2)) + 1, 2):
            if n % i == 0:
                return False
        return True
