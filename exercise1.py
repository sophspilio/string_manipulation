#Write a function that capitalizes the first and fourth letters of a name, e.g.

#old_macdonald('macdonald') --> MacDonald

#Add your code to exercise1.py
#Note: there is a method called "capitalize." The syntax for it is 'macdonald'.capitalize() and it returns 'Macdonald'

'''
Sophie Spiliotopoulos 
Sept. 18,2020
Python 3.6
Create a function that captializes first and fourth letters of a name
'''
word = 'macdonald' #identify word to be used in function
def capfirstfourth(word): #define function with one argument
  wordCap = word[0].capitalize() + word[1:3] + word[3].capitalize() + word[4:]  #concatenate using indexes and .capitalize() to capitlaize first and fourth
  print(wordCap) #print new capitalized word

capfirstfourth(word)

