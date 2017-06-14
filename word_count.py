# -*- coding: utf-8 -*

def words(phrase):

  list_of_words = phrase.split()
  occurence_dictionary = {}
  
  for word in list_of_words:
        if word not in occurence_dictionary:
            occurence_dictionary[word] = 1
        else:
            occurence_dictionary[word] += 1

  return occurence_dictionary


print(words('¡Hola! ¿Qué tal? Привет!'))
#print(words('NevEr\n , Never 1 , 1 , 3'))
  