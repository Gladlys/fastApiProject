#!/usr/bin/env python3.9.5
# -*- coding:utf-8 -*-

'''
@author：gladlys
@date：2022/12/12 13:04
@filename: test_hash.py
@software: PyCharm
@version: Python 3.9.5
'''
from app.src.utils.hash_pwd import get_password_hashed


def test():
    print()
    print(get_password_hashed('123456'))
