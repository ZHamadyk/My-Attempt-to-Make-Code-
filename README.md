# My-Attempt-to-Make-Code-
novice projects in legislative text analysis and text analysis of legal terms and conditions. 
#!/bin/sh

# clean_legHTML.py
# 
#
# Created by G.Zach Hamadyk on May/27/2015.

import urllib
from urllib import urlopen
import nltk
from nltk import word_tokenize
import nltk.collocations
from bs4 import BeautifulSoup



       
info = raw_input("Enter your html link: ")
url = urllib.urlopen(info)
web_html = url.read()
soup = BeautifulSoup(web_html)
web_html = soup.get_text()
webLeg_tokens = nltk.word_tokenize(web_html)
leg_text = nltk.Text(webLeg_tokens)

leg_text.collocations(num=100)
print

def leg_concordance():
    """finds concordance of raw input from input text"""
    while True:
        find_concordance = raw_input("Enter Concordance Search: ")
        
        if find_concordance == "Done":
            break
        
        else:
            leg_text.concordance(find_concordance)
            print



from nltk.tokenize import sent_tokenize
webLeg_sents = sent_tokenize(web_html)
leg_textSents = nltk.Text(webLeg_sents)

def wordSearch():
    """returns more of a context for a word or phrase within the input text"""
    while True:
        word_search = raw_input("What word do you want me to locate? ")
        
        if word_search == "Done":
            break
        
        else:
            word_find = [w for w in leg_textSents if word_search in w]
            print word_find
            print

leg_concordance()
wordSearch()
