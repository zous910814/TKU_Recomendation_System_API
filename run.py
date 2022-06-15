from app import app
from flask import request
from app.model import rs_model, rs_nfm



@app.route('/')
def index():
    return 'Welcome To TKU Recommendation System API'


@app.route('/course',methods=['GET'])
def course():
    if request.method == 'GET':
        return rs_nfm.all_course()
    else:
        return "NOT FOUND 405"

@app.route('/course',methods=['POST'])
def rscourse():
    if request.is_json:
        d = request.get_json()
        user_id = rs_model.get_user_id(d)
        rs_num = rs_model.get_rs_num(user_id)
        return rs_model.rs_course(rs_num)
    else:
        result = 'Not JSON Data'
    return result

# @app.route('/rs', methods=['POST'])
# def rs():
#     if request.is_json:
#         d = request.get_json()
#         user_id = rs_model.get_user_id(d)
#         rs_num = rs_model.get_rs_num(user_id)
#         return rs_model.rs_course(rs_num)
#     else:
#         result = 'Not JSON Data'
#     return result



if __name__ == '__main__':
    app.run(debug=True)
