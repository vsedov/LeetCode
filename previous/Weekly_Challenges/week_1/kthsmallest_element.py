#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: kthsmallest_element
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

from functools import lru_cache
from typing import List

import numpy as np


@lru_cache
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # m = np.array(matrix)
        # matrix = sorted(m.flatten())

        # j = 2 if k == 1 else k

        # x = matrix[:: j - 1]
        # if k > 1:
        #     x.pop(0)

        # return min(x)
        return sorted(np.array(matrix).flatten())[k - 1]


def main() -> None:
    # print(Solution().kthSmallest([[1, 2], [3, 3]], 1))
    # print(Solution().kthSmallest([[-5]], 1))

    print(Solution().kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))


if __name__ == "__main__":
    main()
