# -*- coding: utf-8 -*
import re

def words(phrase):

	list_of_words = phrase.strip()
	occurence_dictionary = {}
	  
  	for word in list_of_words:
  		if word.isdigit():
  			occurence_dictionary[int(word)] = list_of_words.count(word)
  		else:
  			occurence_dictionary[word] = list_of_words.count(word)

	return occurence_dictionary


#print(words('NevEr\n , Never 1 , 1 , 3'))
print(words('one fish two fish red fish blue fish'))
  