#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: reduce_size_half
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

from collections import Counter
from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        target = len(arr) // 2
        sorted_counted_list = sorted((Counter(arr)).values(), reverse=True)
        #  need to get in the habbit of thinking in this way of how sorted
        #  values would work
        print(sorted_counted_list)
        control_count = 0
        for i, v in enumerate(sorted_counted_list):

            control_count += v

            if control_count >= target:

                return i + 1

        return 0


def main() -> None:

    x = Solution().minSetSize([3, 3, 3, 3, 5, 5, 5, 2, 2, 7])

    print(x)


if __name__ == "__main__":
    main()
