#!/usr/bin/env python3.9.5
# -*- coding:utf-8 -*-

'''
@author：gladlys
@date：2022/12/12 9:06
@filename: test_crud.py
@software: PyCharm
@version: Python 3.9.5
'''

from app.src.database.crud import *
from app.src.database.db import session
from app.src.database.schema import SelectUser


def test():
    print('\n\033[4;36m' + 'test select_all_user():' + '\033[0m')
    for user in select_all_user(session):
        print(SelectUser(user).__dict__)

    print('\n\033[4;36m' + 'test select_all_user_like_an():' + '\033[0m')
    for user in select_user_like_account_username(session, '角色'):
        print(SelectUser(user).__dict__)

    print('\n\033[4;36m' + 'test select_user_by_account_mobile_email():' + '\033[0m')
    for user in select_user_by_account_mobile_email(session, '15231260610'):
        print(user)
    print(datetime.now())
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    # print('\n\033[4;36mtest create_user():\033[0m')
    # # a=create_user(session,SelectUser())
    # a = create_user(session, SelectUser(
    #     {'account': 'test4', 'username': '角色为病人', 'gender': 0, 'pwd': '123456', 'email': '6@qq.com',
    #      'mobile': '15231260615', 'role_name': 'ROLE_PATIENT'}))
    # print(a)

    print('\n\033[4;36m' + 'test delete_user():' + '\033[0m')
    print(delete_user(session, 1))

    print('\n\033[4;36m' + 'test select_all_role():' + '\033[0m')
    print(select_all_role(session))

    print('\n\033[4;36m' + 'test select_all_permission():' + '\033[0m')
    print(select_all_permission(session))

    print('\n\033[4;36m' + 'test select_all_ur():' + '\033[0m')
    print(select_all_ur(session))

    print('\n\033[4;36m' + 'test select_all_rp():' + '\033[0m')
    print(select_all_rp(session))

    print('\n\033[4;36m' + 'test select_all_avatar():' + '\033[0m')
    print(select_all_avatar(session))

    print('\n\033[4;36m' + 'test select_all_diagnose():' + '\033[0m')
    print(select_all_diagnose(session))

    print('\n\033[4;36m' + 'test select_all_feedback():' + '\033[0m')
    print(select_all_feedback(session))

    print('\n\033[4;36m' + 'test select_all_login_log():' + '\033[0m')
    print(select_all_login_log(session))

    print('\n\033[4;36m' + 'test select_all_upload_log():' + '\033[0m')
    print(select_all_upload_log(session))
