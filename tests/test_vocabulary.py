from bs4 import BeautifulSoup
from grevocab.vocabulary import *

with open("r.html",'r',encoding='utf-8') as file:
    data= file.read()

soup = BeautifulSoup(data, "html.parser")


print(get_definitions(soup))