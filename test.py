import json

with open('./database/ndf107.json', 'r', encoding="utf-8") as f:
    data = json.load(f)

with open('./database/ndf107course.json', 'r', encoding="utf-8") as f:
    datac = json.load(f)


print(datac['data'][0] =={"course":"數位藝術與人機互動"})
print(len(datac['data']))
print(data['data'][0]['course'] == '數位檔案管理')
