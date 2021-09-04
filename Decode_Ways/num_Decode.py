#
# /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: num_Decode
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

import pyinspect as pi


class Solution:
    def numDecodings(self, s: str) -> int:

        # Might as well code the map set

        # You want all possible combinations , of how something could be
        # decoded
        if s == "0":
            return 0

        dp = [0 for x in range(len(s) + 1)]

        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1

        for i in range(2, len(s) + 1):
            # I think i need to know where to start with stuff like this
            if 0 < int(s[i - 1 : i]) <= 9:
                dp[i] += dp[i - 1]

            if 10 <= int(s[i - 2 : i]) <= 26:
                dp[i] += dp[i - 2]

        return dp[len(s)]


def main() -> None:
    print(Solution().numDecodings("12302"))


if __name__ == "__main__":
    pi.install_traceback()
    main()
"""

11 10 6

    
only possible pair you can get
11,10,6
1,1,10,6
"""
