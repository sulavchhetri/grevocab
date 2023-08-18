"""
    This module is used to scrape the words from the vocabulary.com
"""
import os
import json
import random
import time
from pathlib import Path
from loguru import logger
from grevocab.vocabulary import get_definitions
from grevocab.utils import get_soup

all_words_path = os.path.join(Path(__file__).parent.parent,
                              "files", "all_words.json")


def get_all_words():
    """
        This function is used to get the all_words file
    """
    try:
        with open(all_words_path, 'r', encoding='utf-8') as file:
            all_words = json.load(file)
        return all_words
    except:
        return {}


def save_all_words(data):
    """
        This function is used to get the all_words file
    """
    try:
        with open(all_words_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, default=str)
    except:
        pass


def scrape_words(words):
    """
        This function used to scrape the data about the words like definitions, synonyms

        Args: words(list) : List of words to scrape

        Returns: list[dict] : Info about the words
    """
    all_words = get_all_words()
    result = {}
    count = 0
    for word in words:
        if all_words.get(word, None):
            result[word] = all_words[word]
            continue
        logger.info("The word is {}", word)
        if count == 5:
            logger.info("word {} is in count {}", word, count)
            return result
        soup = get_soup(word)
        if not soup:
            count += 1
            time.sleep(random.uniform(8, 12))
            continue
        result[word] = get_definitions(soup)
        time.sleep(random.uniform(1, 4))
    all_words.update(**result)
    save_all_words(all_words)
    return result
