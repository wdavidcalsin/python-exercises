import pedir_nombre
import salario_bruto
import mayor_de_edad
import contrasenia
import two_numbers
import par_impar


from bs4 import BeautifulSoup

import urllib.request

import nltk

from nltk.corpus import stopwords

response = urllib.request.urlopen('http://php.net/')

html = response.read()

soup = BeautifulSoup(html, "html5lib")

text = soup.get_text(strip=True)

tokens = [t for t in text.split()]

clean_tokens = tokens[:]

sr = stopwords.words('english')

for token in tokens:

    if token in stopwords.words('english'):

        clean_tokens.remove(token)

freq = nltk.FreqDist(clean_tokens)

for key, val in freq.items():

    print(str(key) + ':' + str(val))

freq.plot(20, cumulative=False)

# nltk.download()

# pedir_nombre.welcome()
# salario_bruto.salario()
# mayor_de_edad.edad()
# contrasenia.contrasenia()
# two_numbers.division()
# par_impar.par_impar()
