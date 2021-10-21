#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: test_case_a
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"


import pytest
from termcolor import colored

from int_to_roman import Solution


@pytest.fixture()
def resource() -> Solution:
    print(colored("Setup Outer Function Call", "magenta", "on_grey"))

    yield Solution()

    print(colored("Teardown Outer Function Call", "magenta", "on_grey"))


@pytest.mark.usefixtures("resource")
class TestCase1:
    def test_case_1(self, resource: resource) -> None:
        sol = resource
        assert sol.intToRoman(3) == "III"

    def test_case_2(self, resource: resource) -> None:
        sol = resource
        assert sol.intToRoman(3) == "IV"

    def test_case_3(self, resource: resource) -> None:
        sol = resource
        assert sol.intToRoman(3) == "XXVII"


if __name__ == "__main__":
    pytest.main()
