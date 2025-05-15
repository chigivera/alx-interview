#!/usr/bin/python3
"""
Module to determine if all boxes can be opened.
"""

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    
    Parameters:
    boxes (list of lists): Each index represents a box and contains keys to other boxes.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    opened = set([0])  # Start with box 0 unlocked
    keys = set(boxes[0])  # Keys initially found in box 0

    while keys:
        key = keys.pop()
        if 0 <= key < n and key not in opened:
            opened.add(key)
            keys.update(boxes[key])

    return len(opened) == n
