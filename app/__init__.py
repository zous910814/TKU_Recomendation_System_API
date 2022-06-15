from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config.from_object('app.setting')  # 模块下的setting文件名，不用加py后缀
