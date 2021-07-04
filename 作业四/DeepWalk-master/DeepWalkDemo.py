from gensim.models import Word2Vec
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import warnings
warnings.filterwarnings('ignore')

import  time
t1 = time.time()
model = Word2Vec.load('gen/model')
t2 = time.time()
print(model)
print(".molde load time %.4f"%(t2-t1))
# find top n similar nodes
all_wordList=['genshin impact','animal crossing','the legend of zelda','nintendo switch','playstation 5']

similar_wordList=['genshin impact','animal crossing','the legend of zelda','nintendo switch','playstation 5']

for word in all_wordList:
    for tmp in model.similar_by_word(word,topn=10): #选最近的5个
        similar_wordList.append(tmp[0])


def plot_nodes(word_list):
    X = model[word_list]

    # reduce dimensions to 2
    pca = PCA(n_components=2)
    result = pca.fit_transform(X)

    plt.figure(figsize=(20, 20))
    # create a scatter plot of the projection
    plt.scatter(result[:, 0], result[:, 1])
    print(word_list)
    for i, word in enumerate(word_list):
        print(i, word)
        if i<5:
            ttext = word
        else:
            ttext = i
        plt.annotate(ttext, xy=(result[i, 0], result[i, 1]))
    plt.gca().set_aspect('equal', 'datalim')
    plt.ylim(-3, 4)

    plt.title('cosine measure')
    plt.savefig('./cosine measure.jpg')
    plt.show()

plot_nodes(similar_wordList)