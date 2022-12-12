#!/usr/bin/env python3.9.5
# -*- coding:utf-8 -*-

'''
@author：gladlys
@date：2022/12/12 12:02
@filename: test_response.py
@software: PyCharm
@version: Python 3.9.5
'''
from app.src.utils.response_result import get_result_ok, get_result_failure


def test():
    print()
    print(get_result_ok(msg='test get_result_ok no data').__dict__)
    print(get_result_failure('test get_result_failure no data', 401).__dict__)
    print(get_result_failure('test get_result_failure no data no code').__dict__)
    print(get_result_ok(msg='test get_result_ok', data={'detail': 'succeed'}).__dict__)
    print(get_result_failure(msg='test get_result_failure', code=401, data={'detail': 'not authorized'}).__dict__)
