# 0x01. Lockboxes

This project is part of the **ALX Interview Preparation Curriculum**. It explores graph traversal concepts in the context of a simple problem: determining whether all boxes in a sequence can be unlocked given their keys.

## Problem Description

You have `n` number of locked boxes in front of you. Each box is numbered sequentially from `0` to `n - 1` and each box may contain keys to the other boxes.

- The first box (`boxes[0]`) is unlocked.
- Each key is represented by an integer corresponding to a box number.
- Some keys may not have corresponding boxes.
- The goal is to determine if **all** the boxes can be opened using the keys found.

## Function Prototype

```python
def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    """
