#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: jewlsandstone
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"


import collections

import pyinspect as pi


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        stone_ammount = collections.defaultdict(int)
        for i in stones:
            stone_ammount[i] += 1
        return sum(stone_ammount[i] for i in jewels)

        # # --------------------Another method

        # x = set(jewels)

        # counter = 0
        # for i in stones:
        #     if i in x:
        #         counter += 1

        # return counter

        # return sum(i in jewels for i in stones)


def main() -> None:
    print(
        Solution().numJewelsInStones(
            jewels="aA",
            stones="aAAbbbb",
        )
    )
    pass


if __name__ == "__main__":
    pi.install_traceback()
    main()
