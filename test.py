import pandas as pd
import torch
from deepctr_torch.inputs import SparseFeat, get_feature_names
from deepctr_torch.models import NFM
from sklearn.preprocessing import LabelEncoder


def input_course_num(num: int):
    df = pd.read_csv("data/choose_course_num.csv")
    data = pd.read_csv("data/ndf107sparse_feat.csv")
    data = data.iloc[num:num + 1, :]
    df = df.append(data)
    df = df.reset_index(drop=True)
    df.to_csv("data/choose_course_num.csv", index=False, encoding="utf_8_sig")


def rs_nfm():
    data = pd.read_csv("data/ndf107T.csv")
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
    test = pd.read_csv("data/choose_course_num.csv")

    test_model_input = {name: test[name] for name in feature_names}

    model = NFM(linear_feature_columns, dnn_feature_columns, task='regression', device="cuda")
    model.load_state_dict(torch.load("NFM500.h5"))
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
    data = pd.read_csv("data/ndf107T.csv")
    sparse_features = ['C' + str(i) for i in range(0, 346)]
    sparse_features[0] = 'course'
    data.columns = sparse_features
    for i in round_rs_num:
        ndf = data.iloc[i:i+1,:]
        print(ndf['course'])

if __name__ == "__main__":
    a = rs_nfm()
    # b = input_course_num(200)
    c = round_rs_num(a)
    d = print_rs_course(c)
