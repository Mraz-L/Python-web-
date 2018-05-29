# -*- coding: UTF-8 -*-
#初始化
from flask import Flask
from flask_script import Manager
app = Flask(__name__)
manager = Manager(app)

#路由和视图函数
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

#增加动态路由
@app.route('/user/<name>')
def user(name):
	return '<h1>Hello, %s!</h1>' % name

#URL中动态参数id对应的用户不存在，返回状态码404
@app.route('/user/<id>')
def get_user(id):
	user = load_user(id)
	if not user:
		abort(404)
	return '<h1>Hello, %s</h1>' % user.name

#启动web服务器：5000端口（默认）
if __name__ == '__main__':
    # app.run(host='0.0.0.0',port='5000',debug=True)
    manager.run()
