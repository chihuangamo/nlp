# -*- coding: utf-8 -*-
"""
Created on Sat May 18 17:09:39 2019

@author: user
"""
#%% Read txt 
import trad2simp

with open("news_for_test.txt") as f:
    news_trad = f.read()
news_sim = trad2simp.Trad2Simp(news_trad)

with open("ptt_for_test.txt") as f:
    ptt_trad = f.read()
ptt_sim = trad2simp.Trad2Simp(ptt_trad)

#%% jeiba
import jieba
ptt_sim_tok = jieba.cut(ptt_sim)
print(" ".join(ptt_sim_tok))

ptt_trad_tok = jieba.cut(ptt_trad)
print(" ".join(ptt_trad_tok))

#簡體較準

#%% stanfordcorenlp 
from stanfordcorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP('C:/Users/user/Desktop/NLP/stanford-corenlp-full-2018-10-05', lang = "zh")
nlp.word_tokenize(ptt_sim)

#不知為啥超九
#%% NLTK StanfordSegmenter
from nltk.tokenize import StanfordSegmenter
#from nltk.tokenize.stanford_segmenter import StanfordSegmenter
segmenter = StanfordSegmenter(
        java_class="edu.stanford.nlp.ie.crf.CRFClassifier",
        path_to_jar="C:/Users/user/Desktop/NLP/stanford-segmenter-2015-12-09/stanford-segmenter.jar",
        #path_to_slf4j="C:/Users/user/Desktop/NLP/stanford-corenlp-full-2018-10-05/slf4j-api.jar",
        path_to_sihan_corpora_dict="C:/Users/user/Desktop/NLP/stanford-segmenter-2015-12-09/data",
        path_to_model="C:/Users/user/Desktop/NLP/sanford-segmenter-2015-12-09/data/pku.gz",
        path_to_dict="C:/Users/user/Desktop/NLP/stanford-segmenter-2015-12-09/data/dict-chris6.ser.gz",    
                    )

text = ("这是斯坦福中文分词器测试")
segmenter.segment(text)

#這台跑不出來QQ

#%% NLTK CoreNLPParser
#必須先在cmd執行java(nlp start server.txt)
from nltk.parse.corenlp import CoreNLPParser 
corenlp_parser = CoreNLPParser('http://localhost:9001', encoding='utf8')
token_list = list(corenlp_parser.tokenize(ptt_sim))

#%% thulac
import thulac   

thu1 = thulac.thulac(seg_only=True)  
thu1.cut(ptt_sim, text=True)
thu1.cut(news_sim, text=True)

#%% CKIWP
import os
import subprocess

def ckipws_tokenizes(input):
    os.chdir("C:/Users/user/Desktop/NLP/CKIPWS")
    with open("input/input.txt", "w") as f:
       f.write(input) 
    subprocess.call(['CKIPWSTester', 'ws.ini', 'input/input.txt','output\output.txt'])
    
    with open("output\output.txt", "r", encoding = "utf-16") as f:
       output = f.read() 
    
    segments = output.replace("\u3000", " ")    
    return segments

ptt_trad_tok = ckipws_tokenizes(ptt_trad)
