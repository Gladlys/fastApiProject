#!/usr/bin/env python3.9.5
# -*- coding:utf-8 -*-

"""
@author：gladlys
@date：2022/11/21 15:05
@filename: crud.py
@software: PyCharm
@version: Python 3.9.5
"""

from sqlalchemy.orm import Session

from app.src.database.db import session
from app.src.database.model import User

"""
t_user
"""


def select_all_from_user(db: Session):
    return db.query(User).all()


if __name__ == "__main__":
    print(select_all_from_user(session))
