#!usr/bin/env python
# -*- coding: utf-8 -*-

from .generator import Generator


class FizzGenerator(Generator[int, str]):

    def name(self) -> str:
        return 'FizzGenerator'

    def enabled(self, input) -> bool:
        return input % 3 == 0

    def generate(self, input: int) -> str:
        return 'Fizz'
