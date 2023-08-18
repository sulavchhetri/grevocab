"""
    This module is used to provide utilitary functions
"""

import os
import csv
from pathlib import Path
from curl_cffi import requests
from bs4 import BeautifulSoup
from loguru import logger

files_path = os.path.join(Path(__file__).parent.parent, "files")


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
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
}


def get_soup(word):
    """
        This function is used to return the soup of the word containing all the details

        Args: word(str) : word to scrape
        Returns: Soup(word)
    """
    url = f"https://www.vocabulary.com/dictionary/definition.ajax?search={word}"
    try:
        res = requests.get(url, headers=headers,
                           impersonate='chrome110', timeout=20)

        if res.status_code != 200:
            return None

        return BeautifulSoup(res.text, "html.parser")
    except Exception as err:
        logger.info(err)
        return None


def get_gregmat_words():
    """
        This function returns the list of words from the vocabmountains csv file

        Returns: list :- List of words
    """
    bad_words = ['Group', 'Take Test', 'Review']
    word_list = []

    with open(os.path.join(files_path, 'gregmat_words.csv'), 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            for word in row:
                if word and not any(item in word for item in bad_words):
                    word_list.append(word.strip())
    return word_list


def get_magoosh_words():
    """
        This function returns the list of words from the magoosh csv file

        Returns: list :- List of words
    """
    word_list = []
    with open(os.path.join(files_path, "magoosh_1000_words.csv"), 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            word = row['word'].strip() if 'word' in row else None
            if word:
                word_list.append(word)

    return list(set(word_list))
