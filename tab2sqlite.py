import os
import os.path
from sqlalchemy import *

DB_FILE = 'data\\cj.db'
CJ_SRC_FILE = 'data\\all.txt'


def create_db():
    if os.path.isfile(DB_FILE):
        print("DB file exist.")
        os.remove(DB_FILE)
        print("DB file removed.")

    db = create_engine('sqlite:///data\\cj.db')

    db.echo = True  # True to see what happens

    metadata = MetaData(db)

    # table to store cangjie codes
    codes = Table('codes', metadata,
                  Column('id', Integer, primary_key=True, autoincrement=True),
                  Column('code', String(10)),
                  Column('word', String(10)),
                  )

    codes.create()

    infile = CJ_SRC_FILE
    i = codes.insert()

    try:
        file_cj_src = open(infile, 'r', encoding="UTF-8")
        lines = file_cj_src.readlines()

        objs = []
        for line in lines:

            tk = line.split()
            if len(tk) != 2:
                continue

            obj = {'code': tk[0], 'word': tk[1]}
            objs.append(obj)

            print(obj)

        # 一次執行插入
        i.execute(tuple(objs))

    except IOError:
        print("Could not read from", infile)
        raise SystemExit

    # 檢查是否有正確寫入
    s = codes.select()
    rs = s.execute()

    for row in rs:
        print(row.code, '==>', row.word)


create_db()
