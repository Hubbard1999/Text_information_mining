import gensim
import sklearn
from sklearn.datasets import fetch_20newsgroups, load_digits
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from gensim import corpora, models
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from gensim.corpora import Dictionary
import os
from pprint import pprint
import numpy as np

import pandas as pd
import umap

# import umap.plot



# Some plotting libraries
import matplotlib.pyplot as plt

# utilize sklearn toolkit to fetch the dataset
# it will download the given dataset if not available locally
# its default folder: anaconda3\Lib\site-packages\sklearn\datasets\data\ or somewhere
# you might use datasets.get_data_home() to obtain the default folder 
# in my case: C:\Users\YYY\scikit_learn_data
def fetch_dataset():
    news_dataset = fetch_20newsgroups(subset='all', remove=('headers', 'footers', 'quotes'))

    documents = news_dataset.data

    print ("In the dataset there are", len(documents), "textual documents")
    print ("And this is the first one:\n", documents[0])

    return news_dataset

def TrainLSI(path = 'D:/data/wiki/'):

    mode_name = 'zhiwiki_lsi.model'

    if not os.path.exists(mode_name):
        # load id->word mapping (the dictionary)
        zhwiki_id2word = corpora.Dictionary.load_from_text(path + "zhwiki_wordids.txt.bz2")
        #  load corpus iterator,即文本库
        zhwiki_corpus = corpora.MmCorpus(path + "zhwiki_tfidf.mm")

        zhiwiki_lsi_model = models.lsimodel.LsiModel(corpus=zhwiki_corpus, id2word=zhwiki_id2word, num_topics=400)
        zhiwiki_lsi_model.save(mode_name)
    else:
        print ('mode exists : ', mode_name)
        zhiwiki_lsi_model = models.lsimodel.LsiModel.load(mode_name)

        # pprint(zhiwiki_lsi_model.print_topics(5))
    
    topics = zhiwiki_lsi_model.get_topics()


    print ('no. topics ', len(topics))

def TrainLDA(path = 'D:/data/wiki/'):
    mode_name = 'zhwiki_lda.model'

    if not os.path.exists(mode_name):
        zhwiki_id2word = corpora.Dictionary.load_from_text(path + "zhwiki_wordids.txt.bz2")
        zhwiki_corpus = corpora.MmCorpus(path + "zhwiki_tfidf.mm")
        zhwiki_lda = models.ldamodel.LdaModel(corpus= zhwiki_corpus, id2word= zhwiki_id2word, num_topics=100)
        zhwiki_lda.save(mode_name)
    else:
        print ('model exists :', mode_name)
        zhwiki_lda = models.ldamodel.LdaModel.load(mode_name)
        pprint(zhwiki_lda.print_topics(5))

    topics = zhwiki_lda.get_topics()

    print ('no. topics ', len(topics))

def UMAP(dataset, num_dimensions):
    vectorizer = CountVectorizer(min_df=5, stop_words='english')
    word_doc_matrix = vectorizer.fit_transform(dataset.data)
    category_labels = [dataset.target_names[x] for x in dataset.target]
    hover_df = pd.DataFrame(category_labels, columns=['category'])

    embedding = umap.UMAP(n_components=num_dimensions, metric='hellinger').fit(word_doc_matrix)

    return embedding
    # f = umap.plot.points(embedding, labels=hover_df['category'])

def train20newsgroup(dr = 'umap'):
    dataset = fetch_20newsgroups(subset='all', remove=('headers', 'footers', 'quotes'))

   
    if dr == 'umap':
        vectorizer = CountVectorizer(min_df=5, stop_words='english')
        word_doc_matrix = vectorizer.fit_transform(dataset.data)
        embeddings = umap.UMAP(random_state=42, n_components=2, metric = 'hellinger').fit_transform(word_doc_matrix)
        # embeddings = reducer.fit(word_doc_matrix)
        visualize_embeddings(dataset, embeddings, 'UMAP projection of the 20newsgroup dataset')
    else:
        print ('dimension reduction method not defined! pls implement it by yourself')



def train_wiki():
    TrainLSI()
    TrainLDA()


def visualize_digits():
    reducer = umap.UMAP(random_state=42, n_components=2)
    digits = load_digits()
    embeddings = reducer.fit_transform(digits.data)

    visualize_embeddings(digits, embeddings, 'UMAP projection of the Digits dataset')

def visualize_embeddings(dataset, embeddings, title):
    plt.scatter(embeddings[:, 0], embeddings[:, 1], c=dataset.target, cmap='Spectral', s=5)
    plt.gca().set_aspect('equal', 'datalim')
    plt.colorbar(boundaries=np.arange(11)-0.5).set_ticks(np.arange(10))
    plt.title(title)
    plt.show()



if __name__=='__main__':
    print (sklearn.datasets.get_data_home())
    
    # 1. visualize the digits dataset
    # visualize_digits()


    # 2. train by 20 news group, and do some visualize
    train20newsgroup()

    # 3. train the wiki dataset
    # train_wiki()

    

    