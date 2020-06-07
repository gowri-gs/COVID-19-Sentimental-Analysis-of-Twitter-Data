import nltk;
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
import numpy as np
import pandas as pd
import re
from pprint import pprint
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel
from nltk.stem import WordNetLemmatizer

import pyLDAvis.gensim
import matplotlib.pyplot as plt

import csv
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

tokenizer = RegexpTokenizer(r'\w+')
from stop_words import get_stop_words

en_stop = get_stop_words('en')
en_stop.extend(['from', 'subject', 're', 'edu', 'use'])

lemmatizer = WordNetLemmatizer()
texts = []
from nltk.corpus import wordnet

def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

with open('C:\\Users\\HP\\Desktop\\exconvo.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)

    with open('C:\\Users\\HP\\Desktop\\exconvo.csv', 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('name', 'msg'))
        writer.writerows(lines)
with open('C:\\Users\\HP\\Desktop\\exconvo.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    ct = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
            continue
        else:
            pred_name=row[0]
            file = "C:\\Users\\HP\\Desktop\\" + row[0] + "1.csv"
            if ct == 0:
                ct = 1
                with open(file, 'w', newline='') as out_file:
                    writer = csv.writer(out_file)
                    writer.writerow((row[1], ''))
            else:
                with open(file, 'a', newline='') as out_file:
                    writer = csv.writer(out_file)
                    writer.writerow((row[1], ''))
with open("C:\\Users\\HP\\Desktop\\" + pred_name + "1.csv", 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
'''''
text_list = []

with open("C:\\Users\\HP\\Desktop\\aGreatGuy1.csv", "r") as my_input_file:
    for line in my_input_file:
        line = line.split(",", 2)
        text_list.append(" ".join(line))

with open("C:\\Users\\HP\\Desktop\\aGreatGuy1.txt", "w") as my_output_file:
    my_output_file.write("#1\n")
    my_output_file.write("double({},{})\n".format(len(text_list), 2))
    for line in text_list:
        my_output_file.write("  " + line)

'''''
predator = "C:\\Users\\HP\\Desktop\\aGreatGuy1.csv"
with open(predator) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
