#!usr/bin/env python
# -*- coding: utf-8 -*-

from .generator import Generator


class JustGenerator(Generator[int, str]):

    def name(self) -> str:
        return 'JustGenerator'

    def enabled(self, input) -> bool:
        return True

    def generate(self, input: int) -> str:
        return str(input)
