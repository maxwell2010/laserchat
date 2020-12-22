import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
from sklearn.utils import shuffle
from sklearn.preprocessing import normalize
from laserembeddings import Laser
from sklearn.neighbors import BallTree 
from sklearn.base import BaseEstimator
from sklearn.neighbors import KDTree
from sklearn.pipeline import make_pipeline

allSet = pd.read_csv('boltun.csv') 

bigData = allSet
bigData = shuffle(bigData)
bigData = bigData.reset_index(drop=True)

class myVectorizer_Laser(object):
    def fit(self, X):
        self.laser = Laser()
        return self
    def transform(self, X):
        return normalize(self.laser.embed_sentences(X, lang='ru'), norm='l2')

vectorizer = myVectorizer_Laser()
vectorizer.fit(bigData.Context)
Martix = vectorizer.transform(bigData.Context)
Martix.shape

def softmax(x):
    proba = np.exp(-x)
    return proba / sum(proba)

class Neighbors(BaseEstimator):

    def __init__(self, k=9, radius = 0.01):
        self.k = k
        self.radius = radius  

    def fit(self, X, y):
        self.tree_ = KDTree(X, metric='euclidean')
        self.y_ = np.array(y)   

    def predict(self, X, random_state = None):
        dist, ind = self.tree_.query(X, return_distance = True, k = self.k)
        result = []
        for d, i in zip(dist, ind):
            result.append(np.random.choice(i, p = softmax(d * self.radius)))
        return self.y_[ind]
    
ns = Neighbors()
ns.fit(Martix, bigData.Response)
pipe = make_pipeline(vectorizer, ns)

inp=''
while(inp!='stop'):
    inp=input('Введите фразу: ')
    z=pipe.predict([inp])
    print(z[0][0])



