import nltk
from nltk.util import ngrams

text = "hey , this is vyankatesh"

tokens = nltk.word_tokenize(text)

print(tokens)

unigram = list(ngrams(tokens,1))

print("Unigrams : ", unigram)

bigram = list(ngrams(tokens,2))

print("bigrams : " ,bigram)


trigram = list(ngrams(tokens,3))

print("trigrams : " ,trigram)

