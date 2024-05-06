#Chooses randomly a word with the same ammount of letters has the number the user has inputted
import requests
import random

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)

WORDS = response.content.splitlines()


word = random.choice(WORDS)

z = input("How many letters do you want your word to have?")

while len(word) != int(z):
 
 word=random.choice(WORDS)
 
 if len(word) == int(z):
  print(word)