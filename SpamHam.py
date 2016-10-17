import os

#Initializing the file list in folder
def init_list(folder):
    a_list=[]
    file_list=os.listdir(folder)
    for a_list in file_list:
        f=open(folder+a_file,'r')
        a_list.append(f.read())
    f.close();
return a_list

#Tokenising and preprocessing the text
from nltk import word_tokenize, WordNetLemmatizer 
def preprocess(sentence):
    #lemmatizer.lemmatize(word.lower()) for word in word_tokenize(sentence)
    return [lemmatizer.lemmatize(word.lower()) for word in word_tokenize(sentence)]

from nltk.corpus import stopword


spam=init_lists('enron1/spam/')
ham=init_list('enron1/ham/')

all_emails =[(email,'spam') for email in spam]
all_emails+=[(email,'ham') for email in ham]
