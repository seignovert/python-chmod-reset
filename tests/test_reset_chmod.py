# -*- coding: utf-8 -*-
import pytest

from reset_chmod import scan

def test_scan_err():
    with pytest.raises(ValueError):
        scan('wrong')
