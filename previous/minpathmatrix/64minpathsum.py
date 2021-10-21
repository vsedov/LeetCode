#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: 64minpathsum
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

from typing import List

import pyinspect as pi


class Solution:
    # def minPathSum(self, grid: List[List[int]]) -> int:
    #     # we have to create a dp
    #     for i in range(len(grid)):
    #         for j in range(len(grid[0])):

    #             if i > 0 and j > 0:

    #                 grid[i][j] += min(grid[i][j - 1], grid[i - 1][j])

    #             elif i > 0:

    #                 grid[i][j] += grid[i - 1][j]

    #             elif j > 0:

    #                 grid[i][j] += grid[i][j - 1]

    #     return grid[-1][-1]

    def minPathSum(self, grid: List[List[int]]) -> int:
        # O(N*M)
        rows, col = len(grid), len(grid[0])

        # Save everything into memory
        dp = [[float("inf")] * (col + 1) for _ in range(rows + 1)]

        dp[rows - 1][col] = 0
        for i in range(rows - 1, -1, -1):
            for j in range(col - 1, -1, -1):

                dp[i][j] = grid[i][j] + min(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]


def main() -> None:

    print(Solution().minPathSum([[1, 2, 3], [4, 5, 6]]), 12)

    # print(Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]), 7)

    # print(Solution().minPathSum([[1, 2], [1, 1]]), 3)


if __name__ == "__main__":
    pi.install_traceback()
    main()
