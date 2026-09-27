"""
Week 02 Lab  Problem 3

Name: Syed Muzammil Hussain
Roll number: 2k24AIE65
Course: CGHCI
"""

# ## Problem 3: Average 9 Pixels (1 mark)
#
# Find the average of a small `3 x 3` image block.
#
# ### Step 1: Inputs and output
# Input: nine pixel values in a `3 x 3` array. Output: one rounded number.
#
# ### Step 2: Rule
# `average = sum of all 9 values / 9`
#
# ### Step 3: Small example
# ```text
# 10 20 10
# 30 50 30
# 10 20 10
# ```
# Sum = 190, so `190 / 9 = 21` (rounded).
#
# ### Step 4: Python
# Fill in the 2 `TODO` items.

import numpy as np

# TODO 1: Add all 9 values, divide by 9, and round the answer.
def mean_filter_3x3(neighborhood: np.ndarray) -> int:
    """Return the rounded average of 9 pixels."""
    return int(round(float(np.sum(neighborhood)) / 9))

problem_3_input = np.array([[10, 20, 10], [30, 50, 30], [10, 20, 10]], dtype=np.uint8)

# TODO 2: Remove the # symbols and run the given test.
assert mean_filter_3x3(problem_3_input) == 21
print("Problem 3 passed")