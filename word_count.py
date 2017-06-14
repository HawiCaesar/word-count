
"""
Find the number  of  word occurences in a phrase or sentence
takes one argument and returns a dictionary of words with their occurence
"""

def words(phrase):
	occurence_dictionary = {}

	list_of_words = phrase.split()

	for word in list_of_words:

		if word.isdigit():
			occurence_dictionary[int(word)] = list_of_words.count(word)
		else:
			occurence_dictionary[word] = list_of_words.count(word)


	return occurence_dictionary

  