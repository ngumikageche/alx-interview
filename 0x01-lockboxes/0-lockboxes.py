#!/usr/bin/python3

def canUnlockAll(boxes):
    """ func that that determines if all the boxes can be opened."""
    """ Initialize a list to keep track of visited boxes"""
    visited = [False] * len(boxes)
    """Mark the first box as visited."""
    visited[0] = True
    """ Initialize a list of unopened boxes with
    the keys from the first box."""
    unopened_boxes = list(boxes[0])
    while unopened_boxes:
        box = unopened_boxes.pop()
        """ If this box has not been visited yet, mark it as
        visited and add its keys to unopened_boxes."""
        if not visited[box]:
            visited[box] = True
            unopened_boxes.extend(boxes[box])
    return all(visited)
