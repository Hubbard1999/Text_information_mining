import csv
import numpy as np
np.set_printoptions(suppress=True)

nameList = ["创业公司","非营利组织","国企","合资","民营公司","上市公司","事业单位","外企","其他"]
typeList = []

with open('./huizong/hebing2.csv', 'r') as f:
    reader = csv.reader(f)
    result = list(reader)
temp_li = []
for item in result:
    if item[5] != '':
        # temp_li.extend(item[5].split(' '))
        # temp_li = list(set(temp_li))
        temp_li = list(set(temp_li+item[5].split(' ')))

typeList = temp_li

with open('./huizong/hebing2.csv', 'r') as f:
    reader = csv.reader(f)
    result = list(reader)

count = np.ones((9, len(typeList)))*0
sum = np.ones((1, 9))*0

for item in result:
    if item[4] == '创业公司':
        for i in range(0, len(typeList)):
            if typeList[i] in item[5]:
                count[0][i] += 1
    elif item[4] == '非营利组织':
        for i in range(0, len(typeList)):
            if typeList[i] in item[5]:
                count[1][i] += 1
    elif item[4] == '国企':
        for i in range(0, len(typeList)):
            if typeList[i] in item[5]:
                count[2][i] += 1
    elif item[4] == '合资':
        for i in range(0, len(typeList)):
            if typeList[i] in item[5]:
                count[3][i] += 1
    elif item[4] == '民营公司':
        for i in range(0, len(typeList)):
            if typeList[i] in item[5]:
                count[4][i] += 1
    elif item[4] == '上市公司':
        for i in range(0, len(typeList)):
            if typeList[i] in item[5]:
                count[5][i] += 1
    elif item[4] == '事业单位':
        for i in range(0, len(typeList)):
            if typeList[i] in item[5]:
                count[6][i] += 1
    elif item[4] == '':
        print(item[5])
        for i in range(0, len(typeList)):
            if typeList[i] in item[5]:
                print(typeList[i])
                count[8][i] += 1
    else:
        for i in range(0, len(typeList)):
            if typeList[i] in item[5]:
                count[7][i] += 1

for item in count:
    print(sum(item))