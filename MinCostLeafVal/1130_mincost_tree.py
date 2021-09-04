#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: 1130_mincost_tree
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

from typing import List

import pyinspect as pi


# I think with this , the question was rather hard for me to understand , and
# i was not sure where to start
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        """Checking to see base case"""
        res = 0
        while len(arr) > 1:
            min_index = arr.index(min(arr))
            if 0 < min_index < len(arr) - 1:
                res += min(arr[min_index - 1], arr[min_index + 1]) * arr[min_index]

            elif min_index == 0:
                res += arr[1] * arr[min_index]

            else:
                res += arr[min_index - 1] * arr[min_index]

            arr.pop(min_index)

        return res


def main() -> None:
    print(Solution().mctFromLeafValues([6, 2, 4]))
    print(Solution()._1mctFromLeafValues([6, 2, 4]))


if __name__ == "__main__":
    pi.install_traceback()
    main()

# Notes on this
"""
0 or 2 nodes as childreren
in order transversal 
value of each non lead node is equal to th eproduct of the largest leaf
Input: arr = [6,2,4]
Output: 32
Explanation:
There are two possible trees.  The first has non-leaf node sum 36, and the second has non-leaf node sum 32.

    24            24
   /  \          /  \
  12   4        6    8
 /  \               / \
6    2             2   4

# so we have to add the smalelst min , value from those two points
# when you are building upwards , but you would have to make sure that the first
# point of the tree would be the same


return the smallest possible sum of the values of each non lead nodes 
"""
