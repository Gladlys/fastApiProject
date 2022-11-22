#!/usr/bin/env python3.9.5
# -*- coding:utf-8 -*-

"""
@author：gladlys
@date：2022/11/21 15:05
@filename: crud.py
@software: PyCharm
@version: Python 3.9.5
"""
from datetime import datetime

from sqlalchemy.orm import Session
from sqlalchemy.sql import or_

from app.src.database.db import session
from app.src.database.model import User, UserRole

"""
t_user
"""


class tmp:
    uid: int
    account: str
    username: str
    gender: int
    pwd: str
    email: str
    mobile: str
    is_active: bool
    create_time: datetime
    update_time: datetime
    role_name: str

    def __init__(self,_obj):
        if _obj:
            self.__dict__.update(_obj)
    # def __init__(self, **entries):
    #     self.__dict__.update(**entries)





# 包含有角色名
def select_all_user(db: Session):
    res = db.query(User.uid, User.account, User.username, User.gender, User.pwd, User.email,
                   User.mobile, User.is_active, User.create_time, User.update_time, UserRole.role_name) \
        .outerjoin(UserRole, User.uid == UserRole.uid).filter().all()
    # print(tmp.__init__(res[0]))
    dict_res = [dict(zip(result.keys(), result)) for result in res]
    return dict_res


# 角色姓名、用户列表模糊查找
def select_all_user_like_an(db: Session, search_by: str):
    print('str:' + search_by)
    if search_by is None:
        return db.query(User.uid, User.account, User.username, User.gender, User.pwd, User.email,
                        User.mobile, User.is_active, User.create_time, User.update_time, UserRole.role_name) \
            .outerjoin(UserRole, User.uid == UserRole.uid).filter().all()

    elif search_by is not None:
        return db.query(User.uid, User.account, User.username, User.gender, User.pwd, User.email,
                        User.mobile, User.is_active, User.create_time, User.update_time, UserRole.role_name) \
            .outerjoin(UserRole, User.uid == UserRole.uid).filter(
            or_(User.account.like(f'%{search_by}%'), User.username.like(f'%{search_by}%'))).all()


# 角色邮件、手机号、用户名精确查找
def select_user_by_account_mobile_email(db: Session, search_by: str):
    return db.query(User.uid, User.account, User.username, User.gender, User.pwd, User.email,
                    User.mobile, User.is_active, User.create_time, User.update_time, UserRole.role_name) \
        .outerjoin(UserRole, User.uid == UserRole.uid).filter(or_(User.account.like(f'%{search_by}%'))).all()


"""
t_user
"""


if __name__ == "__main__":
    print('test select_all_user(): \n')
    for user in select_all_user(session):
        print(tmp(user))
    print('test select_all_user_like_an(): \n')
    for user in select_all_user_like_an(session, "a"):
        print(user)
