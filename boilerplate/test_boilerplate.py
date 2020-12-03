#!usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import boilerplate

number_sets = [
    (1, '1'),
    (3, 'Fizz'),
    (5, 'Buzz'),
    (15, 'FizzBuzz')
]


@pytest.mark.parametrize('number, expect', number_sets)
def test_boilerplate_call(number, expect):
    ret = boilerplate.execute(number)
    assert ret == expect
