#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: Understanding_index
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

import pyinspect as pi


def main() -> None:
    x = "acbdbab"

    unique = "abc"

    # Ah this gets you thie index
    for i in x:
        print(x.index(i), i)


if __name__ == "__main__":
    pi.install_traceback()
    main()
