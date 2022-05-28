import pandas as pd
import torch
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from deepctr_torch.inputs import SparseFeat, get_feature_names
from deepctr_torch.models import NFM

if __name__ == "__main__":
    data = pd.read_csv("data/ndf107T.csv")

    sparse_features = ['C' + str(i) for i in range(0, 346)]
    sparse_features[0] = 'course'
    # print(len(sparse_features))
    target = ['course']
    data.columns = sparse_features
    # 1.Label Encoding for sparse features,and do simple Transformation for dense features
    for feat in sparse_features:
        lbe = LabelEncoder()
        data[feat] = lbe.fit_transform(data[feat])
    # 2.count #unique features for each sparse field
    fixlen_feature_columns = [SparseFeat(feat, data[feat].nunique())
                              for feat in sparse_features]
    # print(data)
    linear_feature_columns = fixlen_feature_columns
    dnn_feature_columns = fixlen_feature_columns
    feature_names = get_feature_names(linear_feature_columns + dnn_feature_columns)

    # 3.generate input data for model
    train, test = train_test_split(data, test_size=0.2)
    train_model_input = {name: train[name] for name in feature_names}
    test_model_input = {name: test[name] for name in feature_names}
    # print(train_model_input)
    # 4.Define Model,train,predict and evaluate

    if torch.cuda.is_available():
        print('cuda ready...')
        device = 'cuda:0'

    model = NFM(linear_feature_columns, dnn_feature_columns, task='regression', device=device)
    model.compile("adam", "mse", metrics=['mse'], )

    history = model.fit(train_model_input, train[target].values, batch_size=256, epochs=700, verbose=2,
                        validation_split=0.2)
    pred_ans = model.predict(test_model_input, batch_size=256)
    print("test MSE", round(mean_squared_error(
        test[target].values, pred_ans), 4))
    torch.save(model.state_dict(), 'NFM700.h5')
    # print(test[target].values[:5])
    # print(pred_ans[:5])
    # model.load_state_dict(torch.load('NFM_weights.h5'))
