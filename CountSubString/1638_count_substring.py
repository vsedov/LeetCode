#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: 1638_count_substring
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

import pyinspect as pi


class Solution:
    def countSubstrings(self, s: str, t: str) -> int:

        pass


def main() -> None:
    Solution().countSubstrings("aba", "baba")


if __name__ == "__main__":
    pi.install_traceback()

    main()
# First we would have to see where teh substring would be
# Get a list of common substrings , or the longest substring
# and then we compare them
#
