#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: 119_pascals_triangle_2
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

from typing import List

import pyinspect as pi


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:  # noqa:ignore

        new_index = rowIndex + 1
        dp = [[1] * (i + 1) for i in range(new_index)]

        for i in range(2, new_index):
            for j in range(1, i):
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

        return dp[rowIndex]


def main() -> None:

    print(Solution().getRow(3))


if __name__ == "__main__":
    pi.install_traceback()
    main()
