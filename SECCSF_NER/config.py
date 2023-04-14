import os
import torch

data_dir = '/content/drive/MyDrive/CLUENER2020-main/DataSet/'
train_dir = data_dir + '/1.0/R_S_train_1.0.npz'
test_dir = data_dir + '/Test/R_S_test.npz'
files = ['train', 'test']
bert_model = 'pretrained_bert_models/bert-base-chinese/'
roberta_model = 'pretrained_bert_models/chinese_roberta_wwm_large_ext/'
model_dir = os.getcwd() + '/experiments/clue/'
log_dir = model_dir + 'train.log'
case_dir = os.getcwd() + '/case/R_S_1.0_bad_case.txt'
#additional
case_log_dir = os.getcwd() + '/case/R_S_1.0_record.csv'
max_vocab_size = 1000000

# 训练集、验证集划分比例
dev_split_size = 0.25

# 是否加载训练好的NER模型
load_before = False

# 是否对整个BERT进行fine tuning
full_fine_tuning = True

# hyper-parameter
learning_rate = 3e-5
weight_decay = 0.01
clip_grad = 5

#batch_size = 32
batch_size = 16
#epoch_num = 50
epoch_num = 20
min_epoch_num = 15
patience = 0.0002
patience_num = 10

gpu = '0'

if gpu != '':
    device = torch.device(f"cuda:{gpu}")
else:
    device = torch.device("cpu")
"""

labels = ['Case', 'Relationship', 'Job', 'Gender', 'Address',
          'Date', 'Time', 'Commute', 'Quarantine', 'Transportation', 'Age']

label2id = {
    "O": 0,
    "B-Case": 1,
    "B-Relationship": 2,
    "B-Job": 3,
    'B-Gender': 4,
    'B-Address': 5,
    'B-Date': 6,
    'B-Time': 7,
    'B-Commute': 8,
    'B-Quarantine': 9,
    'B-Transportation': 10,
    "B-Age": 11,
    "I-Case": 12,
    "I-Relationship": 13,
    'I-Job': 14,
    'I-Gender': 15,
    'I-Address': 16,
    'I-Date': 17,
    'I-Time': 18,
    'I-Commute': 19,
    'I-Quarantine': 20,
    "I-Transportation": 21,
    "I-Age": 22,
    "S-company": 23,
    'S-game': 24,
    'S-government': 25,
    'S-movie': 26,
    'S-name': 27,
    'S-organization': 28,
    'S-position': 29,
    'S-scene': 30
}
"""

labels = ['Case', 'Relationship', 'H_Address', 'W_Address', 'L_Address', 'Date', 'Time', 'Commute', 'Quarantine', 'Transportation' ]

label2id = {
    "O": 0,
    "B-Case": 1,
    "B-Relationship": 2,
    "B-H_Address": 3,
    'B-W_Address': 4,
    'B-L_Address': 5,
    'B-Date': 6,
    'B-Time': 7,
    'B-Commute': 8,
    'B-Quarantine': 9,
    'B-Transportation': 10,
    "B-Age": 11,
    "I-Case": 12,
    "I-Relationship": 13,
    'I-H_Address': 14,
    'I-W_Address': 15,
    'I-L_Address': 16,
    'I-Date': 17,
    'I-Time': 18,
    'I-Commute': 19,
    'I-Quarantine': 20,
    "I-Transportation": 21,
    "I-Age": 22,
    "S": 23,
    'S-game': 24,
    'S-government': 25,
    'S-movie': 26,
    'S-name': 27,
    'S-organization': 28,
    'S-position': 29,
    'S-scene': 30
}
id2label = {_id: _label for _label, _id in list(label2id.items())}
