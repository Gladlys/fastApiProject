#!/usr/bin/env python3.9.5
# -*- coding:utf-8 -*-

'''
@author：gladlys
@date：2022/12/12 13:04
@filename: hash_pwd.py
@software: PyCharm
@version: Python 3.9.5
'''
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(password, hashed_password):  # 密码验证
    return pwd_context.verify(password, hashed_password)


def get_password_hashed(password):  # 密码加密
    return pwd_context.hash(password)
