#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: Odd_even_jump
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

from typing import List

# Hard question 1015:303


class Solution:
    def __init__(self, arr: List[int] = None) -> int:
        self.arr = None
        if arr is not None:

            self.arr: List[int] = arr
            self.legnth: int = len(self.arr)
        # You can start at the end index , which is a good index
        self.jump_counter: int = 1

    def __repr__(self):
        return f"{self.arr}"

    def oddEvenJumps(self, arr: List[int] = None) -> int:

        if self.arr is None:
            self.arr: List[int] = arr

            self.legnth: int = len(self.arr)

        arr = [[v, i] for i, v in enumerate(self.arr)]

        arr.sort()
        nxt_min = [None] * self.legnth
        nxt_max = [None] * self.legnth
        st = []

        for value, index in arr:  # get the index of the next larger value
            while st and st[-1] < index:
                nxt_max[st.pop()] = index
            st.append(index)

        st = []

        arr.sort(key=lambda x: [-x[0], x[1]])

        for value, index in arr:  # get the index of the next smaller value
            while st and st[-1] < index:
                nxt_min[st.pop()] = index
            st.append(index)

        dp = [[False, False] for i in range(self.legnth)]
        dp[-1] = [True, True]

        for index in range(self.legnth - 2, -1, -1):
            if nxt_max[index] and dp[nxt_max[index]][1]:
                dp[index][0] = True
            if nxt_min[index] and dp[nxt_min[index]][0]:
                dp[index][1] = True
            if dp[index][0]:
                self.jump_counter += 1
        return self.jump_counter


"""
odd => jump to the (smallest element >= current to the right)
even => jump to the largest (element <= current to the right)

when ties of smallest/largest, take the first element (smallest index)
    
brute force:
try all start indexes
for each start
	do all legal jumps (deterministic)
	if reaches the end -- good start
Time O(n^2)
-------------------
a better method:
try all start indexes from right to left, do both odd and even jumps
store whether a start index can eventually reaches the end
for each element to the left
	do only one jump, then re-use the result of the jump-to location

However, the one jump still requires O(n) due to finding the smallest/largest element >=/<= current. so overall O(n^2)
"""
# if self.arr is None:
#             self.arr: List[int] = arr

#             self.legnth: int = len(self.arr)

#         odd = [False] * self.legnth
#         even = [False] * self.legnth

#         odd[self.legnth - 1], even[self.legnth - 1] = True, True
#         # make one jump, use the solution of the jump-to location
#         for index in range(self.legnth - 2, -1, -1):  # n-2...1,0

#             # odd
#             largest = None
#             smallest = None
#             for j in range(index + 1, self.legnth):
#                 if self.arr[j] >= self.arr[index]:

#                     if smallest is None or self.arr[j] < self.arr[smallest]:
#                         smallest = j

#                 if smallest is not None:
#                     odd[index] = even[smallest]

#                 # even
#                 if self.arr[j] <= self.arr[index]:
#                     if largest is None or self.arr[j] > self.arr[largest]:
#                         largest = j

#                 if largest is not None:
#                     even[index] = odd[largest]

#             if odd[index]:
#                 self.jump_counter += 1

#         return self.jump_counter
