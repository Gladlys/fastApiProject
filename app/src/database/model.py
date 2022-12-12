#!/usr/bin/env python3.9.5
# -*- coding:utf-8 -*-

"""
@author：gladlys
@date：2022/11/21 15:05
@filename: model.py
@software: PyCharm
@version: Python 3.9.5
"""

from datetime import datetime

from sqlalchemy import Column, Integer, VARCHAR, CHAR, DateTime, Boolean
from sqlalchemy import ForeignKey

from app.src.database.db import Base

"""
t_user表
"""


class User(Base):
    __tablename__ = "t_user"
    uid = Column(Integer, primary_key=True, autoincrement=True)
    account = Column(VARCHAR(20), nullable=False, unique=True, comment="用户名")
    username = Column(VARCHAR(20), nullable=False, comment="姓名")
    gender = Column(Integer, nullable=False, comment="0为未知，1为男，2为女")
    pwd = Column(VARCHAR(255), nullable=False, comment="密码")
    email = Column(VARCHAR(50), nullable=False, unique=True)
    mobile = Column(CHAR(11), nullable=False, unique=True)
    is_active = Column(Boolean, default=False)
    is_banned = Column(Boolean, default=False)
    is_deleted = Column(Boolean, default=False)
    create_time = Column(DateTime(), nullable=True, default=datetime.now())
    update_time = Column(DateTime(), nullable=True, default=datetime.now(), onupdate=datetime.now())

    def __repr__(self):
        return f"{self.__dict__}\n"


"""
t_role表
"""


class Role(Base):
    __tablename__ = "t_role"
    role_id = Column(Integer, primary_key=True, autoincrement=True)
    role_name = Column(VARCHAR(50), nullable=False, unique=True, comment="角色名")
    parent_id = Column(Integer, nullable=True, comment="父角色id")
    role_comment = Column(VARCHAR(255), nullable=True, comment="角色描述")
    create_time = Column(DateTime(), nullable=False, default=datetime.now())
    update_time = Column(DateTime(), nullable=False, default=datetime.now(), onupdate=datetime.now())

    def __repr__(self):
        return f"{self.__dict__}\n"


"""
t_permission表
"""


class Permission(Base):
    __tablename__ = "t_permission"
    permission_id = Column(Integer, primary_key=True, autoincrement=True)
    permission_name = Column(VARCHAR(50), primary_key=True, comment="权限名")
    permission_parent_id = Column(Integer, nullable=True, comment="父权限id")
    permission_comment = Column(VARCHAR(255), nullable=True, comment="权限描述")
    create_time = Column(DateTime(), nullable=False, default=datetime.now())
    update_time = Column(DateTime(), nullable=False, default=datetime.now(), onupdate=datetime.now())

    def __repr__(self):
        return f"{self.__dict__}\n"


"""
t_user_role表
"""


class UserRole(Base):
    __tablename__ = "t_user_role"

    ur_id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(Integer, ForeignKey("t_user.uid"), nullable=False)
    role_id = Column(Integer, ForeignKey("t_role.role_id"), nullable=False)
    role_name = Column(VARCHAR(25), ForeignKey("t_role.role_name"), nullable=False, comment="角色名")

    def __repr__(self):
        return f"{self.__dict__}\n"


"""
t_role_permission表
"""


class RolePermission(Base):
    __tablename__ = "t_role_permission"

    rp_id = Column(Integer, primary_key=True, autoincrement=True)
    role_id = Column(Integer, ForeignKey("t_role.role_id"), nullable=False)
    role_name = Column(VARCHAR(25), ForeignKey("t_role.role_name"), nullable=False, comment="角色名")
    permission_id = Column(Integer, ForeignKey("t_permission.permission_id"), nullable=False)
    permission_name = Column(VARCHAR(50), ForeignKey("t_permission.permission_name"), nullable=False, comment="权限名")

    def __repr__(self):
        return f"{self.__dict__}\n"


"""
t_diagnose表
"""


class Diagnose(Base):
    __tablename__ = "t_diagnose"
    diagnose_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    did = Column(Integer, ForeignKey("t_user.uid"), nullable=False, comment="医生id")
    pid = Column(Integer, ForeignKey("t_user.uid"), nullable=False, comment="病人id")
    diagnose_result = Column(VARCHAR(1024), nullable=False, comment="医生诊断结果")
    ai_diagnose_result = Column(VARCHAR(1024), nullable=False, comment="AI诊断结果")
    diagnose_time = Column(DateTime(), default=datetime.now(), nullable=False)

    def __repr__(self):
        return f"{self.__dict__}\n"


"""
t_feedback
"""


class Feedback(Base):
    __tablename__ = "t_feedback"
    feedback_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    uid = Column(Integer, ForeignKey("t_user.uid"), nullable=False, comment="用户")
    feedback_header = Column(VARCHAR(255), nullable=False, comment="反馈标题")
    feedback_content = Column(VARCHAR(1024), nullable=False, comment="反馈内容")
    feedback_time = Column(DateTime(), default=datetime.now(), nullable=False)
    status = Column(Integer, nullable=False, comment="标记反馈的状态")
    handler_id = Column(Integer, ForeignKey("t_user.uid"), nullable=False, comment="处理反馈的用户")
    handler_time = Column(DateTime(), ForeignKey("t_user.uid"), default=None, onupdate=datetime.now(),
                          nullable=True, comment="处理时间")

    def __repr__(self):
        return f"{self.__dict__}\n"


"""
t_avatar
"""


class Avatar(Base):
    __tablename__ = "t_avatar"
    avatar_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    uid = Column(Integer, ForeignKey("t_user.uid"), nullable=False, comment="用户id")
    avatar_upload_time = Column(DateTime(), default=datetime.now(), nullable=False)
    avatar_url = Column(VARCHAR(1024), nullable=False, comment="头像路径")

    def __repr__(self):
        return f"{self.__dict__}\n"


"""
t_login_log
"""


class LoginLog(Base):
    __tablename__ = "t_login_log"
    log_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    uid = Column(Integer, ForeignKey("t_user.uid"), nullable=False, comment="用户id")
    login_device = Column(VARCHAR(1024), nullable=False, comment="登录设备")
    login_location = Column(VARCHAR(1024), nullable=False, comment="登录地点")
    login_time = Column(DateTime(), default=datetime.now(), nullable=False, comment="登录时间")

    def __repr__(self):
        return f"{self.__dict__}\n"


"""
t_upload_log
"""


class UploadLog(Base):
    __tablename__ = "t_upload_log"
    upload_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    uploader_id = Column(Integer, ForeignKey("t_user.uid"), nullable=False, comment="上传用户的id")
    diagnose_id = Column(Integer, ForeignKey("t_diagnose.diagnose_id"), nullable=False, comment="相关的诊断记录id")
    file_url = Column(VARCHAR(1024), nullable=False, comment="文件路径")
    upload_time = Column(DateTime(), default=datetime.now(), nullable=False)

    def __repr__(self):
        return f"{self.__dict__}\n"
