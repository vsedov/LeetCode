#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: FindPeek
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

from typing import List

import pyinspect as pi


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0

        length = len(nums)

        return next(
            (i for i in range(length - 1) if nums[i] > nums[i + 1]), length - 1
        )


def main() -> None:

    print(Solution().findPeakElement([3, 2, 1]))


if __name__ == "__main__":
    pi.install_traceback()
    main()
