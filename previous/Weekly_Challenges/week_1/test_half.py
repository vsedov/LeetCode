#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: test_half
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"


import pytest
from termcolor import colored

from reduce_size_half import Solution


@pytest.fixture()
def resource() -> Solution:
    print(colored("Setup Outer Function Call", "magenta", "on_grey"))

    yield Solution()

    print(colored("Teardown Outer Function Call", "magenta", "on_grey"))


@pytest.mark.usefixtures("resource")
class TestArray:
    # @classmethod
    # def setup_class(cls) -> None:
    #     print(colored(f"Setup Class : Start : class -> {cls.__name__} execution,green"))

    # @classmethod
    # def teardown_class(cls) -> None:
    #     print(colored(f"Setup Class : Start : class -> {cls.__name__} execution,green"))

    def test_case_1(self, resource: resource) -> None:
        print(f"Testing : {resource}")
        sol = resource
        assert sol.minSetSize([7, 7, 7, 7, 7, 7]) == 1

    def test_case_2(self, resource: resource) -> None:
        print(f"Testing : {resource}")
        sol = resource

        assert sol.minSetSize([1, 9]) == 1

    def test_case_3(self, resource: resource) -> None:
        print(f"testing : {resource}")
        sol = resource

        assert sol.minSetSize([1000, 1000, 3, 7]) == 1

    def test_case_4(self, resource: resource) -> None:
        print(f"testing : {resource}")
        sol = resource

        assert (
            sol.minSetSize(
                [9, 77, 63, 22, 92, 9, 14, 54, 8, 38, 18, 19, 38, 68, 58, 19]
            )
            == 5
        )


if __name__ == "__main__":
    pytest.main()
