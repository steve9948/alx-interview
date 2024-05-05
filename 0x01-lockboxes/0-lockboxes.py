#!/usr/bin/env python3

from collections import deque


"""lock_boxes."""
def can_unlock_all(boxes):
    """ Set to keep track of visited boxes"""
    visited = set()
    visited.add(0)  # Start with the first box unlocked

    # Queue to manage boxes whose keys have been found but not yet explored
    queue = deque([0])

    # BFS to explore all reachable boxes
    while queue:
        current_box = queue.popleft()

        # Explore keys in the current box
        for key in boxes[current_box]:
            if key < len(boxes) and key not in visited:
                visited.add(key)
                queue.append(key)

    # Check if all boxes have been visited
    return len(visited) == len(boxes)