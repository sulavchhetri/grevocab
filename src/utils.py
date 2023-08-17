import os
import csv
import json
from pathlib import Path
from curl_cffi import requests
from bs4 import BeautifulSoup

files_path = os.path.join(Path(__file__).parent.parent,
                          "files", "gregmat_words.csv")

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


def get_soup(word):
    url = f"https://www.vocabulary.com/dictionary/definition.ajax?search={word}"

    res = requests.get(url, headers=headers, impersonate='chrome110')

    if res.status_code != 200:
        return None

    return BeautifulSoup(res.text, "html.parser")


def get_gregmat_words():
    bad_words = ['Group','Take Test','Review']
    word_list = []

    with open(files_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            for word in row:
                if word and not any(item in word for item in bad_words):
                    word_list.append(word.strip())
    with open("r.json",'w',encoding='utf-8') as file:
        json.dump(word_list,file)
    # # Print the generated word list
    # a = 0
    # for word in word_list:
    #     if word and word !="Review":
    #         a+=1
    #         print(f"{a} : {word}")
get_gregmat_words()