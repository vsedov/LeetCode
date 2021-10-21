#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: test_a
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"


import pytest
from termcolor import colored

from Longest_Prefix import Solution


@pytest.fixture()
def resource() -> Solution:
    print(colored("Setup Outer Function Call", "magenta", "on_grey"))

    yield Solution()

    print(colored("Teardown Outer Function Call", "magenta", "on_grey"))


@pytest.mark.usefixtures("resource")
class TestCase:
    # @classmethod
    # def setup_class(cls) -> None:
    #     print(colored(f"Setup Class : Start : class -> {cls.__name__} execution,green"))

    # @classmethod
    # def teardown_class(cls) -> None:
    #     print(colored(f"Setup Class : Start : class -> {cls.__name__} execution,green"))

    def test_case_1(self, resource: resource) -> None:
        print(f"Testing : {resource}")
        sol = resource
        assert sol.longestCommonPrefix(["flower", "flo", "flappy"]) == "fl"

    def test_case_2(self, resource: resource) -> None:
        print(f"Testing : {resource}")
        sol = resource
        assert sol.longestCommonPrefix(["a"]) == "a"

    def test_case_3(self, resource: resource) -> None:
        print(f"Testing : {resource}")
        sol = resource
        assert sol.longestCommonPrefix(["dog", "racecar", "car"]) == ""


if __name__ == "__main__":
    pytest.main()
