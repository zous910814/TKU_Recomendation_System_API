from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('app.setting')  # 模块下的setting文件名，不用加py后缀
app.config.from_envvar('FLASKR_SETTINGS')  # 環境變亮，指向配置文件setting的路径

# db = SQLAlchemy(app)
