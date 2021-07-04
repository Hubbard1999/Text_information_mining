import matplotlib.pyplot as plt
import csv
import numpy as np
np.set_printoptions(suppress=True)

# 图二：按照不同的公司类型画平均工资的柱状图
nameList = ["创业公司","非营利组织","国企","合资","民营公司","上市公司","事业单位","外企","其他"]
with open('./huizong/hebing2.csv', 'r') as f:
    reader = csv.reader(f)
    result = list(reader)

print(len(result))
all_sum = np.zeros(9)
total_wage = np.zeros(9)
average_wage = np.zeros(9)
print(all_sum)
for item in result:
    if item[4] == '创业公司':
        all_sum[0] += 1
        total_wage[0] += float(item[2])
    elif item[4] == '非营利组织':
        all_sum[1] += 1
        total_wage[1] += float(item[2])
    elif item[4] == '国企':
        all_sum[2] += 1
        total_wage[2] += float(item[2])
    elif item[4] == '合资':
        all_sum[3] += 1
        total_wage[3] += float(item[2])
    elif item[4] == '民营公司':
        all_sum[4] += 1
        total_wage[4] += float(item[2])
    elif item[4] == '上市公司':
        all_sum[5] += 1
        total_wage[5] += float(item[2])
    elif item[4] == '事业单位':
        all_sum[6] += 1
        total_wage[6] += float(item[2])
    elif item[4] == '':
        all_sum[8] += 1
        total_wage[8] += float(item[2])
    else:
        all_sum[7] += 1
        total_wage[7] += float(item[2])

# 计算平均工资
for i in range(0,9):
    average_wage[i] = round(total_wage[i]/all_sum[i], 2)

print(all_sum)
print(average_wage)
print(sum(all_sum))
plt.rcParams['font.sans-serif']=['SimHei'] #显示中文标签
plt.rcParams['axes.unicode_minus']=False
# 构建数据
x_data = nameList
y_data = average_wage

# 绘图
plt.bar(x=x_data, height=y_data, label='工资/月', color='indianred', alpha=0.8)

# 在柱状图上显示具体数值, ha参数控制水平对齐方式, va控制垂直对齐方式
for x, y in enumerate(y_data):
    plt.text(x, y + 100, '%s' % y, ha='center', va='bottom')

# 设置标题
plt.title("各公司类型月工资对比")
# 为两条坐标轴设置名称
plt.xlabel("公司类型")
plt.ylabel("频数")
# 显示图例
plt.legend()
plt.savefig('./pictures/各公司类型月工资对比.png')
plt.show()
