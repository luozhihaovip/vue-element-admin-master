from flask import Flask
from flask import request
import datetime
import json
import connectMysql #引用ConnectMysql文件
conn = connectMysql
app = Flask(__name__)


@app.route('/article/list')
def hello_world():
    dictm = {
        "code": 20000,
        "data": {
            "total": 100,
            "items": []
        }}
    list = []

    result = conn.query_country_name('call test01')
    for row in result:
        list.append(row)
    dictm["data"]["items"] = list
    dictm=json.dumps(dictm)
    return dictm
@app.route('/sockjs-node/info')
def info():

    return {"websocket":"true","origins":["*:*"],"cookie_needed":"false","entropy":3869736809}

@app.route('/user/info?token=admin-token')
def infoi():

    return {"code":20000,"data":{"roles":["admin"],"introduction":"I am a super administrator","avatar":"https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif","name":"Super Admin"}}

@app.route('/user/login', methods=['POST'])
def hello():


    re = request.json
    print(re)

    return {"code":20000,"data":{"token":"admin-token"}}
@app.route('/user/login', methods=['POST'])
def helllo():
    re = request.json
    print(re)

    return {"code":20000,"data":{"token":"admin-token"}}


@app.route('/time',methods=['post','get'])
def get_time():
    now=str(datetime.datetime.now())#把当前时间转换成字符串
    return "当前的时间是：%s"%now



if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

