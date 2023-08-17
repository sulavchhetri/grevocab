from curl_cffi import requests
from bs4 import BeautifulSoup
from vocabulary import get_definitions
import json

headers = {
    'authority': 'www.vocabulary.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.5',
    'origin': 'https://www.vocabulary.com',
    'referer': 'https://www.vocabulary.com/',
    'sec-ch-ua': '"Chromium";v="110", "Not)A;Brand";v="24", "Brave";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}


# url = "https://www.vocabulary.com/dictionary/definition.ajax?search=repudiate"

# res = requests.get(url, headers=headers, impersonate='chrome110')

# print(res.status_code)

# data = res.text

# with open("r.txt", 'w', encoding='utf-8') as file:
#     file.write(data)

# exit()




result = {}

with open('r.txt', 'r', encoding='utf-8') as file:
    data = file.read()

soup = BeautifulSoup(data, "html.parser")

with open('k.json', 'w', encoding='utf-8') as file:
    json.dump(get_definitions(soup), file, ensure_ascii=False)
