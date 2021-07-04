from wordcloud import WordCloud
import matplotlib.pyplot as plt
import csv
import numpy as np
np.set_printoptions(suppress=True)

nameList = ["创业公司", "非营利组织", "国企", "合资", "民营公司", "上市公司", "事业单位", "外企", "其他"]
typeList = []


# 统计各职位词频
def calculate_number():
    with open('./huizong/hebing2.csv', 'r') as f:
        reader = csv.reader(f)
        result = list(reader)
    temp_li = []
    for item in result:
        if '(' in item[0]:
            temp_li.append(item[0][0:item[0].index('(')])
        elif '（' in item[0]:
            temp_li.append(item[0][0:item[0].index('（')])
        elif '/' in item[0]:
            temp_li.append(item[0][0:item[0].index('/')])
        elif '\\' in item[0]:
            temp_li.append(item[0][0:item[0].index('\\')])
        else:
            temp_li.append(item[0])
    temp_li = list(set(temp_li))
    print(temp_li)

    # for i in range(0,len(temp_li)):
    #     with open('./huizong/{}.csv'.format('temp_li'), mode='a', encoding='utf-8') as f:
    #         f.write('{}\n'.format(temp_li[i]))
    global typeList
    typeList = temp_li

    count = np.zeros(len(typeList))

    for item in result:
        for i in range(0, len(typeList)):
            if typeList[i] in item[0]:
                # print(typeList[i])
                # print(item[0])
                count[i] += 1
    return count


# 生成词云
def create_word_cloud():
    result = calculate_number()

    frequencies = {}
    for j in range(0,len(typeList)):
        frequencies[typeList[j]] = float(result[j])

    wc = WordCloud(
        font_path="./SimHei.ttf",
        background_color="white",
        max_words=100,
        width=2000,
        height=1200,
    )
    word_cloud = wc.generate_from_frequencies(frequencies)
    # 写词云图片
    word_cloud.to_file("./pictures/{}.jpg".format('图4'))
    # 显示词云文件
    plt.imshow(word_cloud)
    plt.axis("off")
    plt.show()

    # 支持中文, SimHei.ttf可从以下地址下载：https://github.com/cystanford/word_cloud


# 根据词频生成词云
create_word_cloud()
