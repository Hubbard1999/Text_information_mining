#%%

# import gensim
# import sklearn
# from sklearn.datasets import fetch_20newsgroups, load_digits
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
# from gensim import corpora, models
# from gensim.utils import simple_preprocess
# from gensim.parsing.preprocessing import STOPWORDS
# from gensim.corpora import Dictionary
# import os
# from pprint import pprint
import numpy as np

# import pandas as pd
import umap

# import umap.plot

# Some plotting libraries
import matplotlib.pyplot as plt

data_path = "testUmap.txt"
data_stop_path = "baidu_stopwords.txt"

a = open(data_path, encoding='utf-8').readlines()
a = [line.strip("\n") for line in a]
data_stop_list = open(data_stop_path, encoding='utf-8').readlines()
data_stop_list = [line.strip("\n") for line in data_stop_list]

def visualize_embeddings(dataset, embeddings, title):
    plt.scatter(embeddings[:, 0], embeddings[:, 1], cmap='Spectral', s=5)
    plt.gca().set_aspect('equal', 'datalim')
    plt.colorbar(boundaries=np.arange(11)-0.5).set_ticks(np.arange(10))
    plt.title(title)
    plt.show()

vectorizer = CountVectorizer(stop_words=data_stop_list) #min_df=5, stop_words='english'

#%%

word_doc_matrix = vectorizer.fit_transform(a)
# vectorizer.fit(a[0:20])

#%%

import time
import sys
import os
start_time = time.clock()

embeddings = umap.UMAP(random_state=42, n_components=2, metric = 'hellinger').fit_transform(word_doc_matrix)
# embeddings = reducer.fit(word_doc_matrix)
visualize_embeddings(embeddings, embeddings, 'UMAP projection of the Bilibili dataset')

stop_time = time.clock()
cost = stop_time - start_time
print("%s cost %s second" % (os.path.basename(sys.argv[0]), cost))