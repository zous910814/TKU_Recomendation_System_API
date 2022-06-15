from flask import Flask



app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///./database/database.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# with open('database/ndf107.json', 'r', encoding="utf-8") as f:
#     data = json.load(f)
#
# with open('database/ndf107course.json', 'r', encoding="utf-8") as f:
#     datacourse = json.load(f)
app.config.from_object('app.setting')  # 模块下的setting文件名，不用加py后缀
# app.config.from_envvar('FLASKR_SETTINGS')  # 環境變亮，指向配置文件setting的路径
