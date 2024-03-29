#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov


from typing import List

from icecream import ic


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        sorted_arr = sorted(arr, key=lambda num: abs(x - num))
        # Ah so this sortes it the other way
        print(sorted_arr)

        result = [sorted_arr[i] for i in range(k)]
        return sorted(result)


def main() -> None:

    x = Solution()
    arr = [1, 1, 1, 10, 10, 10]
    point = x.findClosestElements(arr, 1, 9)
    ic(point)


if __name__ == "__main__":
    main()
