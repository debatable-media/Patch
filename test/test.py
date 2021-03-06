import nltk
import math
from textblob import *
from textblob.wordnet import *
from nltk.corpus import wordnet as wn
import matplotlib as plt 
from pylab import *

import sys

sys.path.append("ui/cgi")

from api import *
from api2 import *
from rhine import *
from rhine_reader import *

'''
conn_grapher([[1,0.22,0.08],[0,1,0.18],[0,0,1]])

distance_graph = [1,0,0],[0,1,0],[0,0,1]

paths = ['./data/article1.txt','./data/articleFox.txt', './data/article3.txt']
for pathi in xrange(len(paths)):
    for pathj in xrange(pathi+1, len(paths)):
        # Pull out news articles
        f1 = open(paths[pathi])
        a = f1.read()
        a = a.decode('utf-8').encode('ascii','ignore')
        text1 = TextBlob(a)
        sentences1 = text1.sentences
        f2 = open(paths[pathj])
        b = f2.read()
        b = b.decode('utf-8').encode('ascii','ignore')
        text2 = TextBlob(b)
        sentences2 = text2.sentences


        #rhine_dist = rhine_n_similarity_flow(sentences, 3, "NNP", 1)

        #sents = []

        #for n in [1,2,3]:
        #    sents.append(path_n_similarity_flow(sentences, 5, "NN", n))

        #sents.append(rhine_dist)
        dat1 = make_flow_data(sentences1)
        dat2 = make_flow_data(sentences2)
        flow1 = flow_fusion(dat1, 4)
        flow2 = flow_fusion(dat2, 4)

        minima1 = find_arguments(flow1)
        minima2 = find_arguments(flow2)

        args1 = []
        args2 = []

        for i in xrange(len(minima1)):
                if i+1 < len(minima1):
                        args1.append(sentences1[minima1[i]:minima1[i+1]-1])
                else:
                        args1.append(sentences1[minima1[i]:])

        for i in xrange(len(minima2)):
                if i+1 < len(minima2):
                        args2.append(sentences2[minima2[i]:minima2[i+1]-1])
                else:
                        args2.append(sentences2[minima2[i]:])


        argblob1 = ''
        for el in args1:
            for els in el:
                argblob1 += els.string
        argblob1 = TextBlob(argblob1)

        argblob2 = ''
        for el in args2:
            for els in el:
                argblob2 += els.string
        argblob2 = TextBlob(argblob2)

        arg_reps1 = []
        arg_reps2 = []

        for arg in args1:
                arg_reps1.append(representative_blob(argblob1.sentences, 10, ""))
        for arg in args2:
                arg_reps2.append(representative_blob(argblob2.sentences, 10, ""))

        a = ''
        for rep in arg_reps1:
            a = a + rep.string + ' '
        blobs1 = TextBlob(a)
        b = ''
        for rep in arg_reps2:
            b = b + rep.string + ' '
        blobs2 = TextBlob(b)

        print blobs1.sentences
        print blobs2.sentences

        conns = connection_matrix(blobs1.sentences, blobs2.sentences)

        print conns

        l = []
        for el in conns:
            l.append(sum(el)/len(el))

        distance_graph[pathi][pathj] = sum(l)/len(l)


print distance_graph

'''



a = TextBlob('Goldman Sachs has long had a comprehensive approach for addressing potential conflicts, the New York based bank said in a statement.')
b = TextBlob('Mr Shelby stated that no one in the financial industry should be able to buy their way out from culpability when it is so strong it defies rationality - I agree with Warren on that.')
c = TextBlob('It is unacceptable if, because of lack of preparedness and planning and global preperation, people are dying.')
d = TextBlob('So, it should be no suprise then that, last week, Secretary of State John Kerry, told the United Nation\'s Security Council that in the fight against the Islamic State, There is a role for nearly every country in the world to play, including Iran')
e = TextBlob('The kitten liked to play with the pretty bear')
f = TextBlob('Often animals will enjoy playful interactions with each other')
rblobs = [a,b,c,d,e,f]

clusters = []
for i in xrange(len(rblobs)):
    idx = is_in_cluster(rblobs[i],clusters)
    if idx == -1:
        clusters.append(rblobs[i])
        print
        print
        print "Forming new cluster: "
        print rblobs[i]
        print
        print
    else:
        print
        print
        print rblobs[i]
        print 
        print
        print " paired with "
        print
        print
        print clusters[idx]
        print
        print



