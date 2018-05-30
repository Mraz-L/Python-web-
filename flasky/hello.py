# -*- coding: UTF-8 -*-
#初始化
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_script import Manager
app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)

#路由和视图函数,渲染
@app.route('/')
def index():
    return render_template('index.html')

#增加动态路由,渲染
@app.route('/user/<name>')
def user(name):
	return render_template('user.html', name=name)

#自定义错误页面
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404
@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500

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
