
#!usr/bin/env python
#-*- coding: utf-8 -*-

from boilerplate.factory import Factory
from boilerplate.fizz import FizzGenerator
from boilerplate.buzz import BuzzGenerator
from boilerplate.just import JustGenerator

def call(num: int) -> str:
    factory: Factory[int, str] = Factory(
        generators=[FizzGenerator(), BuzzGenerator()], 
        fallback=JustGenerator(),
        reducer=lambda x: "".join(x))
    return factory.create(num)
