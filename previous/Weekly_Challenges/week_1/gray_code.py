#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: gray_code
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

from typing import List

import pyinspect as pi


class Solution:
    def grayCode(self, n: int) -> List[int]:

        return [i ^ (i >> 1) for i in range(0, 1 << n)]


def main() -> None:

    x = Solution()
    print(x.grayCode(1))


if __name__ == "__main__":
    pi.install_traceback()
    main()
