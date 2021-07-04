from wordcloud import WordCloud
import matplotlib.pyplot as plt
import csv
import numpy as np
np.set_printoptions(suppress=True)

typeList = ['无需经验', '在校生/应届生', '大专', '初中及以下', '博士', '中专','中技', '2年经验', '本科', '1年经验', '5-7年经验', '8-9年经验', '高中', '硕士', '10年以上经验', '3-4年经验']


# 图五：工作经验词云图
def calculate_number():
    with open('./huizong/hebing2.csv', 'r') as f:
        reader = csv.reader(f)
        result = list(reader)

    count = np.zeros(len(typeList))

    for item in result:
        for i in range(0, len(typeList)):
            if typeList[i] in item[6]:
                count[i] += 1
    return count


# 生成词云
def create_word_cloud():
    result = calculate_number()

    frequencies = {}
    for j in range(0, len(typeList)):
        frequencies[typeList[j]] = float(result[j])
    print(frequencies)
    wc = WordCloud(
        font_path="./SimHei.ttf",
        background_color="white",
        max_words=100,
        width=2000,
        height=1200,
    )
    word_cloud = wc.generate_from_frequencies(frequencies)
    # 写词云图片
    word_cloud.to_file("./pictures/{}.jpg".format('图5'))
    # 显示词云文件
    plt.imshow(word_cloud)
    plt.axis("off")
    plt.show()

    # 支持中文, SimHei.ttf可从以下地址下载：https://github.com/cystanford/word_cloud


# 根据词频生成词云
create_word_cloud()