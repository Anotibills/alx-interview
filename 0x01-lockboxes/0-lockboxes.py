#!/usr/bin/python3
"""
Function that determines all boxes are opened
"""
def canUnlockAll(boxes):
    if not isinstance(boxes, list):
        return False

    if len(boxes) == 0:
        return False

    keys = [0]
    for box_id in keys:
        for key in boxes[box_id]:
            if key not in keys and key != box_id and 0 < key < len(boxes):
                keys.append(key)

    return len(keys) == len(boxes)
