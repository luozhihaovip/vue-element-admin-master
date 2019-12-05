#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import pymysql, logging
dict={
    "host":"10.55.9.155",
    "port":3306,
    "user":"root",
    "password":"Qatest2019!",
    "database":"start_data",
    "charset":"utf8"
    }

#日志模块
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# 定义一个类
class MysqlOperate:
# 连接MySQL
    def connect_local_db():

        return pymysql.connect(host=dict['host'], port=3306, user='root', password='Qatest2019!', database='start_data',
                               charset='utf8')

# 查询模块
def query_country_name(sql_str):
    logger.info(sql_str)
    con = MysqlOperate.connect_local_db()
    cur = con.cursor()
    try:
        cur.execute(sql_str)
        rows = cur.fetchmany(5)
        return rows
    except:
        logger.error("error!")
        raise
    finally:
        cur.close()
        con.close()


if __name__ == '__main__':
    dictm={
    "code":20000,
    "data":{
        "total":100,
        "items":[]
    }}
    list=[]

    result = query_country_name('call test01')
    for row in result:
        list.append(row)
    dictm["data"]["items"]=list
    print(json.dumps(dictm))