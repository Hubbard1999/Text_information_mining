import matplotlib.pyplot as plt
import csv
import numpy as np
np.set_printoptions(suppress=True)

# 图三：分布情况5000以下 5000-8000 8000-11000 11000-14000 14000以上画柱状图
rangeList = ['<5000','5000-8000','8000-11000','11000-14000','>14000']
with open('./huizong/hebing2.csv', 'r') as f:
    reader = csv.reader(f)
    result = list(reader)

range_wage = np.ones((9, 5)) * 0

for item in result:
    if item[4] == '创业公司':
        if float(item[2]) < 5000:
            range_wage[0][0] += 1
        elif float(item[2]) < 8000:
            range_wage[0][1] += 1
        elif float(item[2]) < 11000:
            range_wage[0][2] += 1
        elif float(item[2]) < 14000:
            range_wage[0][3] += 1
        else:
            range_wage[0][4] += 1
    elif item[4] == '非营利组织':
        if float(item[2]) < 5000:
            range_wage[1][0] += 1
        elif float(item[2]) < 8000:
            range_wage[1][1] += 1
        elif float(item[2]) < 11000:
            range_wage[1][2] += 1
        elif float(item[2]) < 14000:
            range_wage[1][3] += 1
        else:
            range_wage[1][4] += 1
    elif item[4] == '国企':
        if float(item[2]) < 5000:
            range_wage[2][0] += 1
        elif float(item[2]) < 8000:
            range_wage[2][1] += 1
        elif float(item[2]) < 11000:
            range_wage[2][2] += 1
        elif float(item[2]) < 14000:
            range_wage[2][3] += 1
        else:
            range_wage[2][4] += 1
    elif item[4] == '合资':
        if float(item[2]) < 5000:
            range_wage[3][0] += 1
        elif float(item[2]) < 8000:
            range_wage[3][1] += 1
        elif float(item[2]) < 11000:
            range_wage[3][2] += 1
        elif float(item[2]) < 14000:
            range_wage[3][3] += 1
        else:
            range_wage[3][4] += 1
    elif item[4] == '民营公司':
        if float(item[2]) < 5000:
            range_wage[4][0] += 1
        elif float(item[2]) < 8000:
            range_wage[4][1] += 1
        elif float(item[2]) < 11000:
            range_wage[4][2] += 1
        elif float(item[2]) < 14000:
            range_wage[4][3] += 1
        else:
            range_wage[4][4] += 1
    elif item[4] == '上市公司':
        if float(item[2]) < 5000:
            range_wage[5][0] += 1
        elif float(item[2]) < 8000:
            range_wage[5][1] += 1
        elif float(item[2]) < 11000:
            range_wage[5][2] += 1
        elif float(item[2]) < 14000:
            range_wage[5][3] += 1
        else:
            range_wage[5][4] += 1
    elif item[4] == '事业单位':
        if float(item[2]) < 5000:
            range_wage[6][0] += 1
        elif float(item[2]) < 8000:
            range_wage[6][1] += 1
        elif float(item[2]) < 11000:
            range_wage[6][2] += 1
        elif float(item[2]) < 14000:
            range_wage[6][3] += 1
        else:
            range_wage[6][4] += 1
    elif item[4] == '':
        if float(item[2]) < 5000:
            range_wage[8][0] += 1
        elif float(item[2]) < 8000:
            range_wage[8][1] += 1
        elif float(item[2]) < 11000:
            range_wage[8][2] += 1
        elif float(item[2]) < 14000:
            range_wage[8][3] += 1
        else:
            range_wage[8][4] += 1
    else:
        if float(item[2]) < 5000:
            range_wage[7][0] += 1
        elif float(item[2]) < 8000:
            range_wage[7][1] += 1
        elif float(item[2]) < 11000:
            range_wage[7][2] += 1
        elif float(item[2]) < 14000:
            range_wage[7][3] += 1
        else:
            range_wage[7][4] += 1


# print(sum(sum(range_wage)))
nameList = ["创业公司","非营利组织","国企","合资","民营公司","上市公司","事业单位","外企","其他"]
for i in range(0,len(nameList)):
    plt.rcParams['font.sans-serif']=['SimHei'] #显示中文标签
    plt.rcParams['axes.unicode_minus']=False
    # 构建数据
    x_data = rangeList
    y_data = range_wage[i]

    # 绘图
    plt.bar(x=x_data, height=y_data, label='工资/月', color='indianred', alpha=0.8)

    # 在柱状图上显示具体数值, ha参数控制水平对齐方式, va控制垂直对齐方式
    for x, y in enumerate(y_data):
        plt.text(x, y + 100, '%s' % y, ha='center', va='bottom')

    # 设置标题
    plt.title("{}工资对比".format(nameList[i]))
    # 为两条坐标轴设置名称
    plt.xlabel("{}".format(nameList[i]))
    plt.ylabel("频数")
    # 显示图例
    plt.legend()
    plt.savefig('./pictures/{}工资对比.png'.format(nameList[i]))
    plt.show()
