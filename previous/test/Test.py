#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: Test
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

import pyinspect as pi
from icecream import ic


def main() -> None:
    x = [1, 2, 3, 4, 5, 6]

    for i in range(2, len(x) + 1):
        ic(x[i - 1 : i], x[i - 2 : i])



    # What a fuck way of doing something , but ah well it works in this case
    print(int(''.join( list(reversed(list(str(32)))))))
    

if __name__ == "__main__":
    pi.install_traceback()
    main()
