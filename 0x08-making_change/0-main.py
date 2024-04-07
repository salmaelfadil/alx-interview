#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))
print(makeChange([1, 2, 5], 7))  # Output: 2 (using two coins of value 2)
print(makeChange([1, 3, 4], 6))  # Output: 2 (using two coins of value 3)
print(makeChange([1, 3, 4], 7))  # Output: 2 (using one coin of value 3 and one coin of value 4)
print(makeChange([1, 5, 10, 20, 50, 100, 200], 121))  # Output: 3 (using two coins of value 50 and one coin of value 20)
print(makeChange([1, 5, 10, 25], 30))  # Output: 2 (using one coin of value 25 and one coin of value 5)

