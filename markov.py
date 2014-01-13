import string
filetomarkov = open("sampletext.txt")
import nltk, re, pprint
import random

allwords = filetomarkov.read().replace('\n', ' ')

cleanwordlist = nltk.clean_html(allwords) 

#print allwords

cleanwordlist = allwords.split()

#print wordlist
#print cleanwordlist


def tokenizeHTML(url):
    #html = urlopen(url).read()
    #html[:18]

    ## next, extract and tokenize the plain text
    html = nltk.clean_html(html) ## helper function to remove markup
    tokens = nltk.word_tokenize(html)
    return tokens[27:]


#cleanlist = tokenizeHTML(wordlist)
#Identify all word pairs
wordpairs = {}
for word in cleanwordlist:
    if word in wordpairs:
            wordpairs[word] += 1
    else:
            wordpairs[word] = 1

#wordpairs = nltk.clean_html(wordpairs) 
#print wordpairs


def generate_markov_text(plaintext):
    size = 25
    #seed = random.randint(0, plaintext.word_size-3)
    seed = random.randint(0, 5)
    seed_word, next_word = plaintext.words[seed], plaintext.words[seed+1]
    seed_word, next_word = plaintext[seed], plaintext[seed+1]
    w1, w2 = seed_word, next_word
    gen_words = []
    for i in xrange(size):
        gen_words.append(w1)
        #w1, w2 = w2, random.choice(plaintext.cache[(w1, w2)])
        w1, w2 = w2, random.choice(next_word)
        gen_words.append(w2)
    return ' '.join(gen_words)

l =[]
for key in wordpairs:
    l +=[key]
    l +=[wordpairs[key]]
    
markovtext = generate_markov_text(l)

print markovtext

#print cleanlist


#for wordpairs in words:
    #if wordpairs #some regex :
        #append to tuple
    
#remove wordpairs that contain any numerals


#Identify LIST of following words for each word-pair.
#Identify probability - no. word occurances / length of list
#output based on probability




    
