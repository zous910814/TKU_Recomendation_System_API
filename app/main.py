from app import app
from flask import request
from app.model import rs_nfm

@app.route('/')
def index():
    return 'Welcome To TKU Recommendation System API'

@app.route('/course', methods = ['GET'])
def course():
    if request.method == 'GET':
        return rs_nfm.all_course()
    else:
        return "NOT FOUND 405"

@app.route('/rscourse', methods = ['POST'])
def rscourse():
    if request.is_json:
        d = request.get_json()
        course_id = rs_nfm.get_course_id(d)
        rs_nfm.input_course_id(course_id)
        rsnfm = rs_nfm.rs_nfm()
        rrn = rs_nfm.round_rs_num(rsnfm)
        prc = rs_nfm.print_rs_course(rrn)
        return prc
    else:
        result = 'Not JSON data'
        return result
