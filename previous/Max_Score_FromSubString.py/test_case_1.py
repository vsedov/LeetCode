#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: test_case_1
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"


import pytest
from termcolor import colored

from MaxScore import Solution


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

        x = sol.maximumGain("cdbcbbaaabab", 4, 5)
        assert x == 19

    def test_case_2(self, resource: resource) -> None:
        print(f"Testing : {resource}")
        sol = resource

        assert sol.maximumGain("cdbcbbaaabab", 4, 5) == 19


if __name__ == "__main__":
    pytest.main()
