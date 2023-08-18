import json
from grevocab.main import scrape_words
from grevocab.utils import get_gregmat_words
from grevocab.utils import get_soup


if __name__ == "__main__":
    words = get_gregmat_words()
    result = scrape_words(words)

    with open("gre.json", 'w', encoding='utf-8') as file:
        json.dump(result, file, default=str, ensure_ascii=False)
