#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: 56_merge_interval
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

from typing import List

import pyinspect as pi


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # They need to be sorted before the loop has started
        # intervals = sorted(intervals)

        res = []
        for i in range(len(intervals) - 1):

            if intervals[i][1] < intervals[i + 1][0]:
                res.append(intervals[i])

            elif intervals[i][0] > intervals[i + 1][1]:
                res.append(intervals[i + 1])

            else:

                intervals[i + 1][0] = min(intervals[i + 1][0], intervals[i][0])
                intervals[i + 1][1] = max(intervals[i + 1][1], intervals[i][1])

        res.append(intervals[-1])


def main() -> None:
    print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))


if __name__ == "__main__":
    pi.install_traceback()
    main()
