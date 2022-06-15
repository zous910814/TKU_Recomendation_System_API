import pandas as pd
import torch
from deepctr_torch.inputs import SparseFeat, get_feature_names
from deepctr_torch.models import NFM
from sklearn.preprocessing import LabelEncoder
import sqlite3

con = sqlite3.connect('database/database.sqlite', check_same_thread=False)
cur = con.cursor()


def input_course_num(num: int):
    df = pd.read_sql("SELECT * FROM choose_course_num", con)
    data = pd.read_sql("SELECT * FROM ndf107sparsefeat", con)
    data = data.iloc[num:num + 1, :]
    df = df.append(data)
    df = df.reset_index(drop=True)
    df.to_sql("choose_course_num", con, if_exists='replace', index=False)


def rs_nfm():
    data = pd.read_sql("SELECT * FROM ndf107T", con)
    sparse_features = ['C' + str(i) for i in range(0, 346)]
    sparse_features[0] = 'course'
    target = ['course']
    data.columns = sparse_features

    for feat in sparse_features:
        lbe = LabelEncoder()
        data[feat] = lbe.fit_transform(data[feat])
    fixlen_feature_columns = [SparseFeat(feat, data[feat].nunique())
                              for feat in sparse_features]

    linear_feature_columns = fixlen_feature_columns
    dnn_feature_columns = fixlen_feature_columns
    feature_names = get_feature_names(linear_feature_columns + dnn_feature_columns)
    test = pd.read_sql("SELECT * FROM choose_course_num", con)

    test_model_input = {name: test[name] for name in feature_names}

    model = NFM(linear_feature_columns, dnn_feature_columns, task='regression', device="cuda")
    model.load_state_dict(torch.load("../../database/NFM/NFM500.h5"))
    model.eval()

    pred_ans = model.predict(test_model_input, batch_size=256)
    pred_ans = str(pred_ans).replace('[', "")
    pred_ans = str(pred_ans).replace(']', '')
    pred_ans = str(pred_ans).replace('\n', ' ')
    pred_ans_list = pred_ans.split()

    return pred_ans_list


def round_rs_num(rs_nfm):
    int_rs_num_list = []
    for i in range(len(rs_nfm)):
        int_rs_num_list.append(round(float(rs_nfm[i])))
    return int_rs_num_list


def print_rs_course(round_rs_num):
    data = pd.read_sql("SELECT * FROM ndf107T", con)
    sparse_features = ['C' + str(i) for i in range(0, 346)]
    sparse_features[0] = 'course'
    data.columns = sparse_features
    for i in round_rs_num:
        ndf = data.iloc[i:i + 1, :]
        print(ndf['course'])


def all_course():
    cl = cur.execute("SELECT * FROM ndf107course").fetchall()

    cl = str(cl).replace("(", "")
    cl = str(cl).replace(")", "")
    cl = str(cl).replace(",", "")
    cl = str(cl).replace("'", "")
    cl = str(cl).replace("[", "")
    cl = str(cl).replace("]", "")
    cl_list = cl.split()

    cs = {}
    for i, j in enumerate(cl_list):
        cs.update({'course{0}'.format(i): j})
    return cs


if __name__ == "__main__":
    # a = rs_nfm()
    # b = input_course_num(78)
    # c = round_rs_num(a)
    # d = print_rs_course(c)
    e = all_course()
    print(e)
