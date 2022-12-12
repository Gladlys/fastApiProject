#!/usr/bin/env python3.9.5
# -*- coding:utf-8 -*-

"""
@author：gladlys
@date：2022/11/21 15:05
@filename: schema.py
@software: PyCharm
@version: Python 3.9.5
"""
from datetime import datetime


class ReturnUser:
    uid: int
    account: str
    username: str
    gender: int
    email: str
    mobile: str
    is_active: bool
    is_banned: bool
    is_deleted: bool
    create_time: datetime
    update_time: datetime
    # datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    role_name: str

    def __init__(self, _obj):
        if _obj:
            self.__dict__.update(_obj)

    def __repr__(self):
        return f"{self.__dict__}\n"


class SelectUser(ReturnUser):
    pwd: str

    # 将字典转化为class
    def __init__(self, _obj=None):
        super().__init__(_obj)
        if _obj:
            self.__dict__.update(_obj)

    # def __init__(self, **entries):
    #     self.__dict__.update(**entries)
    def __repr__(self):
        return f"{self.__dict__}\n"
