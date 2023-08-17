import random
import time
from grevocab.vocabulary import get_definitions
from grevocab.utils import get_soup


def scrape_words(words):
    result = {}
    count = 0
    for word in words:
        if count == 5:
            return result
        soup = get_soup(word)
        if not soup:
            count += 1
            time.sleep(random.uniform(8, 12))
            continue
        result[word] = get_definitions(soup)
        time.sleep(random.uniform(1, 4))
    return result
