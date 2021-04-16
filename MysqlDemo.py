#!/usr/bin/python3
import pymysql

# 打开数据库连接
db = pymysql.connect(host='localhost', user='root', password='123456', database='test', charset='utf8')
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()



# 使用 execute()  方法执行 SQL 查询 
cursor.execute("select * from test")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

# 批量插入
def insertData(cursor,conn):
    sql = "INSERT INTO test(bb, cc, dd) VALUES (%s, %s, %s);"
    username = "Alex"
    age = 18
    ages = 19
    try:
        # 执行SQL语句
        cursor.execute(sql, [username, age,ages])
        # 提交事务
        conn.commit()
    except Exception as e:
        # 有异常，回滚事务
        conn.rollback()
    cursor.close()
    conn.close()

# 批量插入
def insertDataBatch(cursor,conn):
    sql = "INSERT INTO test(bb, cc, dd) VALUES (%s, %s, %s);"
    data = [("a1", "a2","a3"), ("b1", "b2","b3"), ("c1", "c2","c3")]
    try:
        # 批量执行多条插入SQL语句
        cursor.executemany(sql, data)
        # 提交事务
        conn.commit()
    except Exception as e:
        # 有异常，回滚事务
        conn.rollback()
    cursor.close()
    conn.close()

# 单条查询
def selSig(cursor,conn):
    sql = "select * from test"
    # 执行SQL语句
    count=cursor.execute(sql)
    print('count:',count)
    # for i in range(count):
    #     # 获取查询的结果
    #     result = cursor.fetchone()
    #     print('result:',result)
    # 获取单条查询数据  cursor.fetchone()：将只取最上面的第一条结果，返回单个元组，然后多次使用cursor.fetchone()，依次取得下一条结果，直到为空。
    ret = cursor.fetchone()
    for dat1 in ret:
        print('dat1:',dat1)
    # 打印下查询结果
    for index, v in enumerate(ret):
        print('index:',index)
        print('v:',v)
    # 获取表结构
    desc = cursor.description
    for field in desc:
        print('field:',field[0])
    # print(ret)
    # print(ret[0])
    cursor.close()
    conn.close()

# 多条查询
def selManys(cursor,conn):
    # 导入pymysql模块
    # 查询数据的SQL语句
    sql = "select * from test"
    # 执行SQL语句
    cursor.execute(sql)
    # 获取多条查询数据
    ret = cursor.fetchall()
    for dat1 in ret:
        print("dat2:",dat1)
        for subData in dat1:
            print("subData：",subData)

    print("-------stat---")
    for index, v in enumerate(ret):
        print('index:',index)
        print('v:',v)
        for index,subV in enumerate(v):
            print('subV index:',index)
            print('subV:',subV)

    cursor.close()
    conn.close()
    # 打印下查询结果
    print(ret)

    # 可以获取指定数量的数据
    ret=cursor.fetchmany(2)
    # ret = cursor.fetchall()
    print("++++++++++++++++++++++++++++")
    # 光标按绝对位置移动1
    cursor.scroll(1, mode="absolute")
    # 光标按照相对位置(当前位置)移动1
    cursor.scroll(1, mode="relative")
# 删除
def delManys(cursor,conn):
    cursor = conn.cursor()
    sql = "DELETE FROM test WHERE aa=%s;"
    try:
        cursor.execute(sql, [4])
        # 提交事务
        conn.commit()
    except Exception as e:
        # 有异常，回滚事务
        conn.rollback()
    cursor.close()
    conn.close()

# 更新
def updateManys(cursor,conn):
    sql = "UPDATE test SET bb=%s WHERE cc=%s;"
    username = "c2"
    age = 80
    try:
        # 执行SQL语句
        cursor.execute(sql, [age, username])
        # 提交事务
        conn.commit()
    except Exception as e:
        # 有异常，回滚事务
        conn.rollback()
    cursor.close()
    conn.close()

# 批量插入
# insertData(cursor,db)
# 批量插入
# insertDataBatch(cursor,db)
# 单条查询
# selSig(cursor,db)
# 多条查询
# selManys(cursor,db)
# 删除
# delManys(cursor,db)
# 更新
updateManys(cursor,db)