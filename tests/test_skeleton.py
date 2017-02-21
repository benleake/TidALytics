#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from tidalytics.skeleton import fib

__author__ = "csdavenport6"
__copyright__ = "csdavenport6"
__license__ = "none"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
