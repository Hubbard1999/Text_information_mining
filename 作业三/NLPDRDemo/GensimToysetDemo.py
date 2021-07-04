from re import T
from gensim import corpora, models, similarities
from pprint import pprint

from numpy.lib.twodim_base import diag, mask_indices

# documents = ["Human machine interface for lab abc computer applications",
#              "A survey of user opinion of computer system response time",
#              "The EPS user interface management system",
#              "System and human system engineering testing of EPS",
#              "Relation of user perceived response time to error measurement",
#              "The generation of random binary unordered trees",
#              "The intersection graph of paths in trees",
#              "Graph minors IV Widths of trees and well quasi ordering",
#              "Graph minors A survey"]

documents = []

def GenDictandCorpus(documents):
    texts = [[word for word in document.lower().split()]
             for document in documents]
    dictionary = corpora.Dictionary(texts)

    corpus = [dictionary.doc2bow(text) for text in texts]
    print(dictionary)
    print(corpus)
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
def LSI(dictionary, corpus_tfidf, num_topics):
    lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=num_topics)
    print(lsi)

def RP(corpus_tfidf, num_topics):

    rp = models.RpModel(corpus_tfidf, num_topics=num_topics)
    print(rp)
def gensim_demo():
    dictionary, corpus = GenDictandCorpus(documents)

    tfidf = TFIDF(corpus)

    # print(tfidf)

    LDA(dictionary, corpus, tfidf, 6)

    # LSI(dictionary, tfidf, 2)

    # RP(tfidf, 2)

if __name__=='__main__':
    data_list = open('fenci2_deleteStop.txt', encoding='utf-8').readlines()
    documents = [line.strip("\n") for line in data_list]
    gensim_demo()