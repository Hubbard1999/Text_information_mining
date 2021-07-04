import pandas as pd
import glob

outputfile = './huizong/hebing.csv'

csv_list = glob.glob('./huizong/*.csv')
print(u'共发现%s个CSV文件' % len(csv_list))
print(csv_list)
print(u'正在处理............')


# 用于将6个表格合并
def hebing():
    for inputfile in csv_list:
        f = open(inputfile, encoding="utf-8")
        data = pd.read_csv(f, error_bad_lines=False)
        data.to_csv(outputfile, mode='a', index=False, header=None)
    print('完成合并')


# 用于将合并的表格去重
def quchong(file):
    df = pd.read_csv(file, header=0, encoding="utf-8")
    datalist = df.drop_duplicates()
    datalist.to_csv(file)
    print('完成去重')


if __name__ == '__main__':
    hebing()
    quchong(outputfile)