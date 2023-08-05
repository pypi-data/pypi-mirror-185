# Copyright 2023 by Leonard Becker
# All rights reserved.
# This file is part of the matrops python package,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

import unittest

from tests.matrix.test_matrix import TestMatrix
from tests.vector.test_vector import TestVector

def main(): 
    matrix = TestMatrix()
    vector = TestVector()
    unittest.main()

if __name__ == "__main__":
    main()