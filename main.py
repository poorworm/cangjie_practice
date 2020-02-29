import random

from sqlalchemy import create_engine

db = create_engine('sqlite:///data\\cj.db')
db.echo = False  # True to see what happens

while True:
    codes = db.execute('SELECT * FROM codes')
    cnt = db.execute('SELECT COUNT(*) FROM codes').scalar()

    r = random.randint(1, cnt)

    chk_code = ''
    chk_word = ''

    # 查找
    idx = 0
    for _r in codes:
        if idx == r:
            chk_code = _r['code']
            chk_word = _r['word']
            print(_r['code'])
            print(_r['word'])
        idx += 1

    txt = None
    while txt != chk_code:

        if txt == 'zzzz':
            break

        txt = input("輸入【" + chk_word + "】:")
        print(chk_code)
        print('========================')
