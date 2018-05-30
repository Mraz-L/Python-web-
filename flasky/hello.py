# -*- coding: UTF-8 -*-
#初始化,引入类
from flask import Flask, render_template#框架，渲染文件夹
from flask_bootstrap import Bootstrap#Twitter的前端框架
from flask_script import Manager#Flask Script扩展提供向Flask插入外部脚本的功能
from flask_moment import Moment#本地化时间戳
from datetime import datetime#获取日期时间
from flask_wtf import Form#初始化定义表单
from wtforms import StringField, SubmitField
from wtforms.validators import Required

#定义类的实例
app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'hard to guess string' #设置Flask-WTF,保护表单免受跨站请求伪造

#路由和视图函数,渲染
@app.route('/')
def index():
	name = None
	form = NameForm()
	if form.validate_on_submit():
		name = form.name.data
		form.name.data = ''
	return render_template('index.html', form=form, name=name, current_time=datetime.utcnow())

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

#简单的web表单
class NameForm(Form):
	name = StringField('wt is your name?', validators=[Required()])
	submit = SubmitField('Submit')

#启动web服务器：5000端口（默认）
if __name__ == '__main__':
    # app.run(host='0.0.0.0',port='5000',debug=True)
    manager.run()
