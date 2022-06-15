import json
import pandas as pd
import numpy as np

# with open('database/ndf107course.json', 'r', encoding="utf-8") as f:
#     datac = json.load(f)
#
# with open('database/ndf107course.json', 'r', encoding="utf-8") as f:
#     data = json.load(f)
#
# def get_user_id(course):
#     # course = {"course":"數位藝術與人機互動"}
#     for i in range(len(datac['data'])):
#         if datac['data'][i] == course:
#             return i
#
# def get_rs_num(user_id, num=6):
#     user_course_matrix = pd.read_json("database/ndf107cs.json")
#     user_vec = user_course_matrix.loc[user_id].values
#     sorted_index = np.argsort(user_vec)[:num]
#     return list(user_course_matrix.columns[sorted_index])[1:]
#
#
# def rs_course(rs_num):
#     cl={}
#     for i in rs_num:
#         cl.update({'course{0}'.format(i): data['data'][i]['course']})
#     return cl

# a = get_rs_num(200)
# print(ndf.iloc[200])
# print(ndf.iloc[a[1:]])
# if __name__=="__main__":
# a = get_user_id(course = {"course":"中國藝術史"})
# b = get_rs_num(a)
# c = rs_course(b)
# print(a)
# print(b)
# print(c)