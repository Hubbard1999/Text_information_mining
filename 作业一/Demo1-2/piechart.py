import matplotlib.pyplot as plt
import csv
import numpy as np
np.set_printoptions(suppress=True)

# 图六：对比不同关键词（会计、审计）下（国企、民营、合资、外资、创业、上市公司等）的百分比（饼状图）
nameList = ["创业公司","非营利组织","国企","合资","民营公司","上市公司","事业单位","外企","其他"]
with open('./huizong/hebing2.csv', 'r') as f:
    reader = csv.reader(f)
    result = list(reader)


count = np.ones((8, 2)) * 0

for item in result:
    if item[4] == '创业公司':
        if '会计' in item[0]:
            count[0][0] += 1
        elif '审计' in item[0]:
            count[0][1] += 1
    elif item[4] == '非营利组织':
        if '会计' in item[0]:
            count[1][0] += 1
        elif '审计' in item[0]:
            count[1][1] += 1
    elif item[4] == '国企':
        if '会计' in item[0]:
            count[2][0] += 1
        elif '审计' in item[0]:
            count[2][1] += 1
    elif item[4] == '合资':
        if '会计' in item[0]:
            count[3][0] += 1
        elif '审计' in item[0]:
            count[3][1] += 1
    elif item[4] == '民营公司':
        if '会计' in item[0]:
            count[4][0] += 1
        elif '审计' in item[0]:
            count[4][1] += 1
    elif item[4] == '上市公司':
        if '会计' in item[0]:
            count[5][0] += 1
        elif '审计' in item[0]:
            count[5][1] += 1
    elif item[4] == '事业单位':
        if '会计' in item[0]:
            count[6][0] += 1
        elif '审计' in item[0]:
            count[6][1] += 1
    elif item[4] == '':
        continue
    else:
        if '会计' in item[0]:
            count[7][0] += 1
        elif '审计' in item[0]:
            count[7][1] += 1

kuai = [i[0] for i in count]
shen = [i[1] for i in count]
print(count)
print(kuai)
print(shen)

plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
plt.rcParams['axes.unicode_minus'] = False
labels = ["创业公司","非营利组织","国企","合资","民营公司","上市公司","事业单位","外企"]
fraces = kuai
plt.axes(aspect=1)
plt.pie(x=fraces,autopct='%.2f%%',labels= labels,pctdistance=1,explode=(0,0.3,0,0,0,0,0,0))
plt.legend()
plt.savefig('./pictures/会计饼状图.png')
plt.show()

fraces = shen
plt.axes(aspect=1)
plt.pie(x=fraces,autopct='%.2f%%',labels= labels,pctdistance=1,explode=(0,0.6,0,0,0,0,0,0))
plt.legend()
plt.savefig('./pictures/审计饼状图.png')
plt.show()