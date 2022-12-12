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
from app.src.database.model import User, UserRole, Role, Permission, RolePermission
from app.src.database.model import Avatar, Feedback, UploadLog, LoginLog, Diagnose
from app.src.database.schema import SelectUser


def select_all(db: Session, clazz: any):
    # 查找全部信息的可复用方法
    res = {'code': 200, 'msg': '查找成功', 'data': None}
    dict_res: list = []
    try:
        results = db.query(clazz).all()
        for result in results:
            t = result.__dict__
            t.pop('_sa_instance_state')
            dict_res.append(t)
        res['data'] = dict_res
    except Exception as e:
        db.rollback()
        res = {'code': 202, 'msg': '查找失败', 'data': e}
        print(e)
        raise e
    finally:
        return res


"""
------------------------------------------------------------------------------------------------------------------------
t_user
------------------------------------------------------------------------------------------------------------------------
"""


# 包含有角色名
def select_all_user(db: Session):
    res = db.query(User.uid, User.account, User.username, User.gender, User.pwd, User.email,
                   User.mobile, User.is_active, User.is_banned, User.is_deleted, User.create_time, User.update_time,
                   UserRole.role_name) \
        .outerjoin(UserRole, User.uid == UserRole.uid).filter().all()

    # 将从数据库中自定义查询出的结果，从元组tuple转换成字典。
    dict_res = [dict(zip(result.keys(), result)) for result in res]
    return dict_res


def select_user_like_account_username(db: Session, search_by: str):
    # 角色姓名、用户列表模糊查找
    # print('str:' + search_by)
    if search_by is None:
        return select_all_user(db)

    elif search_by:
        res = db.query(User.uid, User.account, User.username, User.gender, User.pwd, User.email,
                       User.mobile, User.is_active, User.create_time, User.update_time, UserRole.role_name) \
            .outerjoin(UserRole, User.uid == UserRole.uid) \
            .filter(or_(User.account.like(f'%{search_by}%'), User.username.like(f'%{search_by}%'))).all()
        # 将从数据库中自定义查询出的结果，从元组tuple转换成字典。
        dict_res = [dict(zip(result.keys(), result)) for result in res]
        return dict_res


def select_user_by_account_mobile_email(db: Session, search_by: str):
    # 角色邮件、手机号、用户名精确查找
    res = db.query(User.uid, User.account, User.username, User.gender, User.pwd, User.email,
                   User.mobile, User.is_active, User.create_time, User.update_time, UserRole.role_name) \
        .outerjoin(UserRole, User.uid == UserRole.uid) \
        .filter(or_(User.account == search_by, User.mobile == search_by, User.email == search_by)).all()
    # 将从数据库中自定义查询出的结果，从元组tuple转换成字典。
    dict_res = [dict(zip(result.keys(), result)) for result in res]
    return dict_res


def create_user(db: Session, new_user: SelectUser):
    # 创建用户
    if new_user:
        res = {'code': 200, 'msg': 'succeed', 'data': None}
        try:
            temp = User(account=new_user.account, username=new_user.username, gender=new_user.gender, pwd=new_user.pwd,
                        email=new_user.email, mobile=new_user.mobile)
            print(temp)
            db.add(temp)
            db.flush()
            # 此时数据插入数据库中

            role = db.query(Role).filter(Role.role_name == new_user.role_name).first()
            db.add(UserRole(role_id=role.role_id, role_name=role.role_name, uid=temp.uid))
            db.flush()
            # 此时数据插入数据库中

            res['data'] = {'uid': temp.uid}
            return res
        except Exception as e:
            db.rollback()
            res = {'code': 202, 'msg': 'failure', 'data': e}
            print(e)
            raise e
        finally:
            return res
    else:
        return {'code': 201, 'msg': '空对象', 'data': None}


def delete_user(db: Session, uid: int):
    # 根据uid删除用户
    if uid:
        res = {'code': 200, 'msg': '删除成功', 'data': None}
        try:
            temp = db.query(User.is_deleted).filter(User.uid == uid).first()
            if temp[0]:
                res = {'code': 201, 'msg': '已经被删除', 'data': None}
                return res
            print("----------------")
            res["data"] = db.query(User).filter(User.uid == uid).update({"is_deleted": True})

        except Exception as e:
            db.rollback()
            res = {'code': 202, 'msg': '删除失败', 'data': e}
            print(e)
            raise e
        finally:
            return res


"""
------------------------------------------------------------------------------------------------------------------------
t_role
------------------------------------------------------------------------------------------------------------------------
"""


def select_all_role(db: Session):
    # 查找全部角色
    return select_all(db, Role)


"""
------------------------------------------------------------------------------------------------------------------------
t_permission
------------------------------------------------------------------------------------------------------------------------
"""


def select_all_permission(db: Session):
    # 查找全部权限信息
    return select_all(db, Permission)


"""
------------------------------------------------------------------------------------------------------------------------
t_user_role
------------------------------------------------------------------------------------------------------------------------
"""


def select_all_ur(db: Session):
    # 查找全部用户的角色信息
    return select_all(db, UserRole)


"""
------------------------------------------------------------------------------------------------------------------------
t_role_permission
------------------------------------------------------------------------------------------------------------------------
"""


def select_all_rp(db: Session):
    # 查找全部角色的权限信息
    return select_all(db, RolePermission)


"""
------------------------------------------------------------------------------------------------------------------------
t_avatar
------------------------------------------------------------------------------------------------------------------------
"""


def select_all_avatar(db: Session):
    # 查找全部角色的头像信息
    return select_all(db, Avatar)


"""
------------------------------------------------------------------------------------------------------------------------
t_diagnose
------------------------------------------------------------------------------------------------------------------------
"""


def select_all_diagnose(db: Session):
    # 查找全部诊断信息
    return select_all(db, Diagnose)


"""
------------------------------------------------------------------------------------------------------------------------
t_feedback
------------------------------------------------------------------------------------------------------------------------
"""


def select_all_feedback(db: Session):
    # 查找全部反馈信息
    return select_all(db, Feedback)


"""
------------------------------------------------------------------------------------------------------------------------
t_login_log
------------------------------------------------------------------------------------------------------------------------
"""


def select_all_login_log(db: Session):
    # 查找全部角色的权限信息
    return select_all(db, LoginLog)


"""
------------------------------------------------------------------------------------------------------------------------
t_upload_log
------------------------------------------------------------------------------------------------------------------------
"""


def select_all_upload_log(db: Session):
    # 查找全部xml上传记录
    return select_all(db, UploadLog)


"""
------------------------------------------------------------------------------------------------------------------------
main
------------------------------------------------------------------------------------------------------------------------
"""
if __name__ == "__main__":
    print('crud')
