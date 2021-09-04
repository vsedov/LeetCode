#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: FindMedianDataStream
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

import bisect

import pyinspect as pi
from icecream import ic


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []

    def addNum(self, num: int) -> None:

        bisect.insort(self.arr, num)

    def findMedian(self) -> float:
        length = len(self.arr)
        if length % 2 == 1:
            return self.arr[length // 2]

        return (self.arr[length // 2] + self.arr[length // 2 - 1]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
#
def main() -> None:
    sol = MedianFinder()

    sol.addNum(6)
    sol.addNum(10)
    sol.addNum(2)
    sol.addNum(6)
    sol.addNum(5)
    sol.addNum(0)

    ic(sorted(sol.arr))
    ic(sol.findMedian())


if __name__ == "__main__":
    pi.install_traceback()
    main()
