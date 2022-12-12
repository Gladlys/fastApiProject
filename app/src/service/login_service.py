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
from sqlalchemy.orm import Session

from app.src.database.crud import select_user_by_account_mobile_email
from app.src.database.db import session
from app.src.utils.hash_pwd import get_password_hashed, verify_password
from app.src.utils.response_result import get_result_ok, get_result_failure

login_service = APIRouter()


# TODO(gladlys) login security
# 用户登录
def login(account: str, pwd: str, db: Session):
    user = select_user_by_account_mobile_email(db, account)[0]
    print(user)

    password = user['pwd']
    print(password)

    if verify_password(pwd, password):
        user.pop('pwd')
        return get_result_ok('登录成功', user)
    else:
        return get_result_failure('登录失败，账号或密码错误！', 401)


if __name__ == '__main__':
    print(login('admin', '123456', session).__dict__)
