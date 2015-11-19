import sys
reload(sys)
sys.setdefaultencoding('Cp1252')



from bs4 import BeautifulSoup as BS
import urllib
input = raw_input("Enter URL: ")
r = urllib.urlopen(input).read()
# create a soup that
soup = BS(r).body.get_text()
#print soup



def space():
	print
	print

import nltk
from nltk import word_tokenize
import nltk.collocations
body_tokens = nltk.word_tokenize(soup)
body_text = nltk.Text(body_tokens)
body_text.collocations(num=50)



# finding the 20 most common words
from nltk.corpus import stopwords
stopwords = nltk.corpus.stopwords.words('english')
common_text = [w for w in body_text if w.lower() not in stopwords]
from collections import Counter
import re
common_search = re.findall('\w+', str(common_text))
most_common = Counter(common_search).most_common(20)
print "build"
print most_common


# allows you to search concordance of individual words
def leg_concordance():
	"""find concordance of input search term"""
	while True:
		search = raw_input("Enter search term: ")
		if search == "Done":
			break
		else:
			body_text.concordance(search)
			space()


# see how a term or phrase occurs within a larger context
from nltk.tokenize import sent_tokenize
soupSents = sent_tokenize(soup)
soupText = nltk.Text(soupSents)
def wordSearch():
	"""returns a context for word or phrase within the input text"""
	while True:
		search = raw_input("Enter word or phrase to locate: ")
		if search == "Done":
			break
		else:
			word_find = [w for w in soupText if search in w]
			for line in word_find:
				print line
				space()

# legislative grammatical counts and their implications
# redo using list comprehnsion
# redo using a function, then construct as an object to be called
# take len of text, counts of each grammatical component and graph them (pyplot)
terms = ['shall', 'shall not', 'may', 'may not', 'must']
#def term_count():
#    for term in terms:
#        print terms.count(term), term

shall_count = body_text.count('shall')
must_count = body_text.count('must')
may_count = body_text.count('may')
# 'term not' requires regex
#shallNot_count = body_text.count('shall not')
#mayNot_count = body_text.count('may not')
space()

print "'shall' occurs {} times in this bill.".format(shall_count)
print "Remember 'shall' requires some action be taken, expresses a prediction or intention."
space()
print "'must' occurs {} times in this bill.".format(must_count)
print "Use of 'must' creates ambiguity; the word implies more obligation than command. However the Fed manual says to use 'must' instead of 'shall'"
space()
print "'may' occurs {} times in this bill.".format(may_count)
print "Using 'may' can express capability or possibility as well as authoirty."
space()
#print "'shall not' occurs {} times in this bill.".format(shallNot_count)
#print """'shall not' when direct-
#    ing that an action not be taken. Arguably a distinction exists that "shall not" speaks to
#    the person subject to the prohibition and is silent as to whether an act done by a person
#    in violation of the prohibition is nevertheless valid (particularly as to a third party)."""
#space()
#print "'may not' occurs {} times in this bill.".format(mayNot_count)
#print "'may not' when denying a right, privilege, or power, and for placing prohibitions"

# beginning part
print "Lets do some basic search of this text!"
leg_concordance()
wordSearch()
#term_count()
