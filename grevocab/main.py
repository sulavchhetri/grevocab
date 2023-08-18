"""
    This module is used to scrape the words from the vocabulary.com
"""
import random
import time
from loguru import logger
from grevocab.vocabulary import get_definitions
from grevocab.utils import get_soup

def scrape_words(words):
    """
        This function used to scrape the data about the words like definitions, synonyms

        Args: words(list) : List of words to scrape

        Returns: list[dict] : Info about the words
    """
    result = {}
    count = 0
    for word in words:
        logger.info("The word is {}",word)
        if count == 5:
            logger.info("word {} is in count {}",word, count)
            return result
        soup = get_soup(word)
        if not soup:
            count += 1
            time.sleep(random.uniform(8, 12))
            continue
        result[word] = get_definitions(soup)
        time.sleep(random.uniform(1, 4))
    return result
