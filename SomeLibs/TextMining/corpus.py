import matplotlib.pyplot as plt
import nltk
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords
from matploblit.colors import ListedColormap
from wordcloud import WordCloud
import string

corpus = PlaintextCorpusReader('dados','*') #cria um corpus

arq = corpus.fileids() #retorna uma lista cm tds os arq de dados
texto = corpus.raw('1.text') #acessa o texto do arq 1.text; sem o parametro, vem tds os textos de tds os arq
td_texto = corpus.raw()
word = corpus.words() #retorna uma lista com tds as palavras, onde cada elemento é uma palavra

stops = stopwords.words('english') #lista com tds as stopWord em ingles
mapa_cores = ListedColormap(['orange','green','red','magenta'])
nuvem = WordCloud(background_color='white',colormap=mapa_cores,stopwords=stops,max_words=100) #cria a nuvem
nuvem.generate(td_texto) #gera a nuvem
plt.imshow(nuvem) #imprimi a nuvem

noStops = [p for p in word if p not in stops] #pega tds as palavras q n sao stops
noPontuation = [p for p in noStops if p not in string.punctuation] #retira as pontuações
freq = nltk.FreqDist(noPontuation) #retorna um datagrama, onde mostra a qtd q cada palavra aparece
mais_comuns = freq.most_common(100) #mostra as 100 palavras mais comuns