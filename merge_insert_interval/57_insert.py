#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: 57_insert
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"


from typing import List

import pyinspect as pi


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        res = []

        for indx, (v1, v2) in enumerate(intervals):

            # Check if first index of new interval is > the second index
            if v2 < newInterval[0]:
                res.append([v1, v2])

            # Check if the second index of newInterval is < v1
            elif v1 > newInterval[1]:
                res.append(newInterval)
                return res + intervals[indx:]

            else:
                # we have to then replace the values
                newInterval[0] = min(newInterval[0], v1)
                newInterval[1] = max(newInterval[1], v2)

        res.append(newInterval)
        return res

    # def insert_my_verison(
    #     self, intervals: List[List[int]], newInterval: List[int]
    # ) -> List[List[int]]:

    #     res = []
    #     for i in range(len(intervals)):

    #         if newInterval[1] < intervals[i][0]:
    #             res.append(newInterval)
    #             return res + intervals[i:]

    #         elif newInterval[0] > intervals[i][1]:
    #             res.append(intervals[i])

    #         else:
    #             newInterval = [
    #                 min(newInterval[0], intervals[i][0]),
    #                 max(newInterval[1], intervals[i][1]),
    #             ]

    #     res.append(newInterval)
    #     return res


def main() -> None:
    print(
        Solution().insert(
            intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8]
        )
    )

    # print(
    #     Solution().insert_my_verison(
    #         intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8]
    #     )
    # )

    # print(
    #     Solution().insert(
    #         intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[-5, -3]
    #     )
    # )


if __name__ == "__main__":
    pi.install_traceback()
    main()
