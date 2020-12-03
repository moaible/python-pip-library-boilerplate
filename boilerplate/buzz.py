#!usr/bin/env python
# -*- coding: utf-8 -*-

from .generator import Generator


class BuzzGenerator(Generator[int, str]):

    def name(self) -> str:
        return 'BuzzGenerator'

    def enabled(self, input) -> bool:
        return input % 5 == 0

    def generate(self, input: int) -> str:
        return 'Buzz'
