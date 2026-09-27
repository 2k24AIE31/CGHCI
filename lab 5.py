"""
Week 02 Lab  Problem 5

Name: Syed Muzammil Hussain
Roll number: 2k24AIE65
Course: CGHCI
"""

# ## Problem 5: Find an Edge with Sobel (1 mark)
#
# Use a Sobel filter to find how strong an edge is in the middle of a `3 x 3` block.
#
# ### Step 1: Inputs and output
# Input: a `3 x 3` grayscale block. Output: `gx`, `gy`, and edge strength.
#
# ### Step 2: Rule
# Multiply the block by each kernel below, add the 9 results to get `gx` and `gy`:
#
# ```text
# Gx =       Gy =
# -1  0  1   -1 -2 -1
# -2  0  2    0  0  0
# -1  0  1    1  2  1
# ```
#
# Then `strength = sqrt(gx * gx + gy * gy)`.
#
# ### Step 3: Small example
# ```text
# 20  20 200
# 20  20 200
# 20  20 200
# ```
# `gx = 720`, `gy = 0`, so `strength = 720`.
#
# ### Step 4: Python
# Fill in the 2 `TODO` items.

import numpy as np

# TODO 1: Write the two kernels, multiply them with the block, and add the results to get gx and gy.
def sobel_response(block: np.ndarray) -> tuple[float, float, float]:
    """Return gx, gy, and edge strength."""
    Gx = np.array([[-1, 0, 1],
                   [-2, 0, 2],
                   [-1, 0, 1]], dtype=np.float32)
    Gy = np.array([[-1, -2, -1],
                   [ 0,  0,  0],
                   [ 1,  2,  1]], dtype=np.float32)
    gx = float(np.sum(block * Gx))
    gy = float(np.sum(block * Gy))
    strength = float(np.sqrt(gx * gx + gy * gy))
    return gx, gy, strength

problem_5_input = np.array([[20, 20, 200], [20, 20, 200], [20, 20, 200]], dtype=np.float32)

# TODO 2: Remove the # symbols and run the given test.
gx, gy, strength = sobel_response(problem_5_input)
assert gx == 720.0 and gy == 0.0
print("Problem 5 passed")