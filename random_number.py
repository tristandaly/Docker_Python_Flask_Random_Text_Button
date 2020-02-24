from nltk import sent_tokenize
from urllib import request
import random

url = "https://www.gutenberg.org/files/61236/61236-0.txt"
response = request.urlopen(url)
raw = response.read().decode('utf8')
sentence = sent_tokenize(raw)

# result = random.choice(sentence)
print(random.choice(sentence))
