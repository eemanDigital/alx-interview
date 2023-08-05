#!/usr/bin/python3

"""
This module contains a function to determine if all the boxes can be opened.
"""

def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.

    Args:
        boxes (list): A list of lists. Each inner list represents a box and contains keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    visited = [False] * n
    stack = [0]

    while stack:
        current_box = stack.pop()
        visited[current_box] = True
        keys = boxes[current_box]

        for key in keys:
            if not visited[key]:
                stack.append(key)

    return all(visited)
