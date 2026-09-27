"""
Week 02 Lab  Problem 2

Name: Syed Muzammil Hussain
Roll number: 2k24AIE65
Course: CGHCI
"""

# ## Problem 2: Image Memory (1 mark)
#
# Calculate how many bytes an uncompressed image uses.
#
# ### Step 1: Inputs and output
# Inputs: width, height, and bits per pixel (`bpp`). Output: memory in bytes.
#
# ### Step 2: Rule
# `bytes = width * height * bpp / 8`
#
# ### Step 3: Small example
# For `1920 x 1080` and `24 bpp`: `1920 * 1080 * 24 / 8 = 6,220,800` bytes.
#
# ### Step 4: Python
# Fill in the 2 `TODO` items.

import numpy as np

# TODO 1: Multiply width, height, and bpp, then divide by 8.
def display_memory_bytes(width: int, height: int, bpp: int) -> int:
    """Return image memory in bytes."""
    return width * height * bpp // 8

# TODO 2: Remove the # symbols and run the given test.
expected_bytes = 1920 * 1080 * 24 // 8
assert display_memory_bytes(1920, 1080, 24) == expected_bytes
print("Problem 2 passed")