#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: 1277_submatrix
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

from typing import List

from icecream import ic


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # we have to create a dp
        res = 0

        # Matrix would act as out dp value i guess here
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        res += 1
                    else:
                        # Remember we have to replace this value here
                        # as we use it to compare the next two vlaues before
                        # hand
                        matrix[i][j] = (
                            min(
                                matrix[i - 1][j - 1], matrix[i][j - 1], matrix[i - 1][j]
                            )
                            + matrix[i][j]
                        )
                        res += matrix[i][j]

        return res


def main() -> None:
    ic(Solution().countSquares([[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]]))
    Solution().countSquares([[1, 0, 1], [1, 1, 0], [1, 1, 0]])


if __name__ == "__main__":
    main()
