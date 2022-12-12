#!/usr/bin/env python3.9.5
# -*- coding:utf-8 -*-

"""
@author：gladlys
@date：2022/11/22 10:33
@filename: login_service.py
@software: PyCharm
@version: Python 3.9.5
"""

from fastapi import APIRouter

from app.src.utils.response_result import get_result_ok, get_result_failure

login_service = APIRouter()


# TODO(gladlys) login security
def login(username: str, pwd: str):
    return get_result_ok(..., msg=username, data={'pwd': pwd})


if __name__ == '__main__':
    print(login('a', 'b').__dict__)
