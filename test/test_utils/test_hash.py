#!/usr/bin/env python3.9.5
# -*- coding:utf-8 -*-

'''
@author：gladlys
@date：2022/12/12 13:04
@filename: test_hash.py
@software: PyCharm
@version: Python 3.9.5
'''
from app.src.utils.hash_pwd import get_password_hashed, verify_password


def test():
    print()
    print(get_password_hashed('123456'))
    print(verify_password('123456', '$2b$12$WIIoct.0kzqRUtwWqxfweuM61qJJS5IxQA6Gj4dAfmHyN.0UcRBIq'))
