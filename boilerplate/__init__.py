#!usr/bin/env python
# -*- coding: utf-8 -*-

from .factory import Factory
from .fizz import FizzGenerator
from .buzz import BuzzGenerator
from .just import JustGenerator


def execute(num: int) -> str:
    factory: Factory[int, str] = Factory(
        generators=[FizzGenerator(), BuzzGenerator()],
        fallback=JustGenerator(),
        reducer=lambda x: ''.join(x))
    return factory.create(num)
