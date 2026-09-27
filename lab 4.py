"""
Week 02 Lab  Problem 4

Name: Syed Muzammil Hussain
Roll number: 2k24AIE65
Course: CGHCI
"""

# ## Problem 4: Change Image Contrast (1 mark)
#
# Change numbers from one range to another range.
#
# ### Step 1: Inputs and output
# Input: an array and two ranges (old and new). Output: an array with the new values.
#
# ### Step 2: Rule
# `new = (value - old_min) / (old_max - old_min) * (new_max - new_min) + new_min`
#
# ### Step 3: Small example
# Change `[50, 100, 150]` from range `[50, 150]` to `[0, 255]`:
# `50 -> 0`, `100 -> 127.5`, `150 -> 255`.
#
# ### Step 4: Python
# Fill in the 2 `TODO` items.

import numpy as np

# TODO 1: Use the formula from the problem description, then np.clip to stay in [out_min, out_max].
def contrast_stretch(
    image: np.ndarray,
    in_min: float,
    in_max: float,
    out_min: float = 0.0,
    out_max: float = 255.0,
) -> np.ndarray:
    """Change image values from one range to another."""
    scaled = (image - in_min) / (in_max - in_min) * (out_max - out_min) + out_min
    return np.clip(scaled, out_min, out_max)

problem_4_input = np.array([50, 100, 150], dtype=np.float32)

# TODO 2: Remove the # symbols and run the given test.
expected = np.array([0.0, 127.5, 255.0], dtype=np.float32)
np.testing.assert_allclose(contrast_stretch(problem_4_input, 50, 150), expected)
print("Problem 4 passed")