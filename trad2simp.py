# -*- coding: utf-8 -*-
"""
Created on Sat May 18 16:38:51 2019

@author: user
"""

from langconv import *

def Trad2Simp(sentence):
    sentence = Converter('zh-hans').convert(sentence)
    return sentence
