#%%
from gensim.corpora import Dictionary
from gensim.models import ldamodel
from gensim.models import CoherenceModel, LdaModel
from gensim import models
from gensim import corpora, models, similarities
from pprint import pprint
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
import umap

def GenDictandCorpus(documents):
    texts = [[word for word in document.lower().split()]
             for document in documents]
    dictionary = corpora.Dictionary(texts)

    corpus = [dictionary.doc2bow(text) for text in texts]
    # print(dictionary)
    # print(corpus)
    return dictionary, corpus

def TFIDF(corpus):

    # initialize a model
    tfidf = models.TfidfModel(corpus)


    corpus_tfidf = tfidf[corpus]
    # for doc in corpus_tfidf:
        # print(doc)

    return corpus_tfidf

def LDA(dictionary, corpus, corpus_tfidf, num_topics):
    ldamodel = models.LdaModel(corpus, id2word=dictionary, num_topics=num_topics)

    ldamodel.print_topics()
    pprint(ldamodel.print_topics())
    # lda_vis(dictionary, corpus, ldamodel)
    return ldamodel

def LSI(dictionary, corpus_tfidf, num_topics):
    lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=num_topics)
    # print(lsi)

def RP(corpus_tfidf, num_topics):

    rp = models.RpModel(corpus_tfidf, num_topics=num_topics)
    # print(rp)
def gensim_demo(documents,classify_num=6):
    dictionary, corpus = GenDictandCorpus(documents)

    tfidf = TFIDF(corpus)

    # print(tfidf)

    return LDA(dictionary, corpus, tfidf, classify_num)

    # LSI(dictionary, tfidf, 2)

    # RP(tfidf, 2)
def visualize_embeddings(target, embeddings, title):
    plt.scatter(embeddings[:, 0], embeddings[:, 1],c=target, cmap='Spectral', s=5)
    plt.gca().set_aspect('equal', 'datalim')
    plt.colorbar(boundaries=np.arange(6)-0.5).set_ticks(np.arange(5))
    plt.title(title)
    plt.savefig('./test2.jpg')
    plt.show()


import gensim
from gensim import models
import pyLDAvis.gensim_models


def lda_vis(dictionary,corpus,lda):
    vis = pyLDAvis.gensim_models.prepare(lda, corpus, dictionary)
    pyLDAvis.display(vis)

if __name__=='__main__':
    # data_list = open('fenci2_deleteStop.txt', encoding='utf-8').readlines()
    data_list = open('fenci2_deleteStop.txt', encoding='utf-8').readlines()
    documents = [line.strip("\n") for line in data_list]

    ## 只能过滤空字符和None
    documents = list(filter(None, documents))
    lda = gensim_demo(documents,classify_num=5)
    lda_word2id = lda.id2word.token2id
    # lda_id2word = lda.id2word
    lda_score = lda.expElogbeta

    ##获取分类标签
    sum = [[0] * lda.num_topics for row in range(len(documents))]
    testData = documents[:]
    for index, testW in tqdm(enumerate(testData)):
        sentence2wordList = testW.split()
        wordList2idList = []

        for word in sentence2wordList:
            try:
                if word in lda_word2id.keys():
                    wordList2idList.append(lda_word2id[word])
            except:
                print(word)

        for i in range(lda.num_topics):
            for id in wordList2idList:
                sum[index][i] += lda_score[i, id]

    classify = []
    for max_index in sum:
        classify.append(max_index.index(max(max_index)))
    print(len(classify))

    data_stop_path = "baidu_stopwords.txt"
    data_stop_list = open(data_stop_path, encoding='utf-8').readlines()
    data_stop_list = [line.strip("\n") for line in data_stop_list]
    vectorizer = CountVectorizer(stop_words=data_stop_list) #min_df=5, stop_words='english'

    word_doc_matrix = vectorizer.fit_transform(documents)
    embeddings = umap.UMAP(random_state=42, n_components=2, metric='hellinger').fit_transform(word_doc_matrix)
    # embeddings = reducer.fit(word_doc_matrix)
    visualize_embeddings(classify, embeddings, 'UMAP projection of the Bilibili dataset')