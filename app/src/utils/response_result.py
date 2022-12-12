#!/usr/bin/env python3.9.5
# -*- coding:utf-8 -*-

'''
@author：gladlys
@date：2022/12/12 9:27
@filename: response_result.py
@software: PyCharm
@version: Python 3.9.5
'''


class ResponseResult:
    code: int
    msg: str

    def ok(self, msg: str):
        self.code = 200
        self.msg = msg
        return self

    def failure(self, code: int, msg: str):
        if code:
            self.code = code
        else:
            self.code = 201
        self.msg = msg
        return self


class ResponseResultData(ResponseResult):
    data: dict

    def data_ok(self, msg: str, data: dict):
        self.data = data
        super().ok(msg)
        return self

    def data_failure(self, code: int, msg: str, data: dict):
        self.data = data
        super().failure(code, msg)
        return self


def get_result_ok(msg: str, data: dict = None):
    if data:
        return ResponseResultData().data_ok(msg, data)
    else:
        return ResponseResult().ok(msg)


def get_result_failure(msg: str, code: int = None, data: dict = None):
    if data:
        return ResponseResultData().data_failure(code, msg, data)
    else:
        return ResponseResult().failure(code, msg)
