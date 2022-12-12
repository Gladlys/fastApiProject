#!/usr/bin/env python3.9.5
# -*- coding:utf-8 -*-

"""
@author：gladlys
@date：2022/11/21 15:05
@filename: db.py
@software: PyCharm
@version: Python 3.9.5
"""

import json

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.util.compat import contextmanager

Base = declarative_base()

config: {
    "": ""
}

with open('D:/MyCode/Python/fastApiProject/app/src/database/config.json', 'r') as json_file:
    config = json.load(json_file)
    # print(json.dumps(config, indent=4))

pools = "pools"
pool = "ecg"
db_type = config[pools][pool]["db_type"]
db_con = config[pools][pool]["db_con"]
user = config[pools][pool]["user"]
password = config[pools][pool]["password"]
server = config[pools][pool]["server"]
database = config[pools][pool]["database"]
db_url = f"{db_type}+{db_con}://{user}:{password}@{server}/{database}"

engine = create_engine(db_url, echo=True)

Session = sessionmaker(autocommit=True, autoflush=True, bind=engine)
session = Session()


# session.close()


# dependency,依赖

@contextmanager
def get_db(session_maker: sessionmaker):
    db_session = session_maker()
    try:
        yield db_session  # 使用yield实现orm的异步操作
        db_session.commit()
    except Exception as e:
        print(e)
        raise e
    finally:
        db_session.close()


if __name__ == "__main__":
    print(get_db(Session))
