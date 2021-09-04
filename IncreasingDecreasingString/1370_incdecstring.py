#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: 1370_incdecstring
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"


import collections

import pyinspect as pi


class Solution:
    def sortString(self, s: str) -> str:
        d = sorted([c, n] for c, n in collections.Counter(s).items())


def main() -> None:
    print(Solution().sortString("aaaabbbbcccc"))
    print("abccbaabccba")


if __name__ == "__main__":
    pi.install_traceback()
    main()
