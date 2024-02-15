#!/usr/bin/python3
"""Lockbox module"""


def canUnlockAll(boxes):
    """checks if boxes can be unlocked using keys inside
    each box"""
    n = len(boxes)
    unlocked_boxes = set([0])
    new_boxes = set(boxes[0])

    while new_boxes:
        current_box = new_boxes.pop()

        if current_box < 0 or current_box >= n or current_box in unlocked_boxes:
            continue

        unlocked_boxes.add(current_box)
        new_boxes.update(boxes[current_box])

    return len(unlocked_boxes) == n
