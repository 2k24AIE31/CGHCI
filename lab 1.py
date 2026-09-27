"""
Week 02 Lab  Problem 1

Name: Syed Muzammil Hussain
Roll number: 2k24AIE65
Course: CGHCI
"""

# ## Problem 1: Thresholding (1 mark)
#
# Turn each grayscale value into black (`0`) or white (`255`).
#
# ### Step 1: Inputs and output
# Input: an image and a threshold number. Output: an image of only `0` and `255`.
#
# ### Step 2: Rule
# If `pixel >= threshold`, output `255`. Otherwise output `0`.
#
# ### Step 3: Small example
# For threshold `128`:
#
# ```text
# 20  128  200
# 100 150  250
# ```
#
# Answer: `0 255 255` / `0 255 255`.
#
# ### Step 4: Python
# Fill in the 2 `TODO` items in the next cell. Note: `128` counts as white.

import numpy as np

# TODO 1: Return 255 when a pixel is >= threshold; otherwise return 0.
def threshold_image(image: np.ndarray, threshold: int) -> np.ndarray:
    """Convert a grayscale image to black and white."""
    return np.where(image >= threshold, 255, 0).astype(np.uint8)

problem_1_input = np.array([[20, 128, 200], [100, 150, 250]], dtype=np.uint8)
problem_1_expected = np.array([[0, 255, 255], [0, 255, 255]], dtype=np.uint8)

# TODO 2: Remove the # symbols and run the test.
np.testing.assert_array_equal(threshold_image(problem_1_input, 128), problem_1_expected)
print("Problem 1 passed")