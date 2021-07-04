from wordcloud import WordCloud
import matplotlib.pyplot as plt
import csv
import numpy as np
np.set_printoptions(suppress=True)

nameList = ["创业公司", "非营利组织", "国企", "合资", "民营公司", "上市公司", "事业单位", "外企", "其他"]
typeList = []


# 生成9个关键词的词频
def calculate_number():
    with open('./huizong/hebing2.csv', 'r') as f:
        reader = csv.reader(f)
        result = list(reader)
    temp_li = []
    for item in result:
        if item[5] != '':
            # temp_li.extend(item[5].split(' '))
            # temp_li = list(set(temp_li))
            temp_li = list(set(temp_li + item[5].split(' ')))

    global typeList
    typeList = temp_li

    with open('./huizong/hebing2.csv', 'r') as f:
        reader = csv.reader(f)
        result = list(reader)

    count = np.ones((9, len(typeList))) * 0

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
            for i in range(0, len(typeList)):
                if typeList[i] in item[5]:
                    count[8][i] += 1
        else:
            for i in range(0, len(typeList)):
                if typeList[i] in item[5]:
                    count[7][i] += 1
    return count


# 生成9个关键词的词云图（图1xxx）
def create_word_cloud():
    result = calculate_number()

    for i in range(0,9):
        frequencies = {}
        for j in range(0,len(typeList)):

            frequencies[typeList[j]] = float(result[i][j])

        wc = WordCloud(
            font_path="./SimHei.ttf",
            background_color="white",
            max_words=100,
            width=2000,
            height=1200,
        )
        word_cloud = wc.generate_from_frequencies(frequencies)
        # 写词云图片
        word_cloud.to_file("./pictures/{}.jpg".format(nameList[i]))
        # 显示词云文件
        plt.imshow(word_cloud)
        plt.axis("off")
        plt.show()

    # 支持中文, SimHei.ttf可从以下地址下载：https://github.com/cystanford/word_cloud


# 根据词频生成词云
create_word_cloud()