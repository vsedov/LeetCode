#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: Longest_SubString_Without_Repeat_3_0
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"


import pyinspect as pi


# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = ""
        length = 0
        # ic(s)
        # for i in s:
        #     if i not in unique:
        #         unique += i

        #     else:

        #         # Test arond this if you can
        #         unique = unique[unique.index(i) + 1 :] + i

        #     length = max(length, len(unique))

        for i in range(len(s)):
            s_val = s[i]
            if s_val not in unique:
                unique += s_val

            else:
                # Creates  formats the values
                unique = unique[unique.index(s_val) + 1 :] + s_val
            length = max(length, len(unique))

        return length


print(Solution().lengthOfLongestSubstring("abadbbdavaa"))


if __name__ == "__main__":
    pi.install_traceback()
"""
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.


Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
