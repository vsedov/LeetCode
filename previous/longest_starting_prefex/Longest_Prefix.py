#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: Solution
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # Has to be a better method to this , THINK YOU STUPID FUCK

        unique = ""

        for i, *main_string in map(set, zip(*strs)):
            if main_string:
                return unique

            unique += i
        return unique


def main() -> None:
    # print(Solution().longestCommonPrefix(["flower", "flow", "flowerpot"]))
    print(Solution().another_version(["dog", "dogecar", "docar"]))
    # print(Solution().longestCommonPrefix(["a"]))


if __name__ == "__main__":
    main()
