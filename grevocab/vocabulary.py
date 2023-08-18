"""
    This module is used to parse the details of the word from the soup
"""

def get_other_forms(soup):
    """
        This function get the other forms of the word

        like : play, played, playing
    """
    other_forms_tag = soup.find("p", {"class": "word-forms"})
    words = other_forms_tag.b.text
    return words.split(";")


def get_short_meaning(soup):
    """
        This function returns the short meaning of the word
    """
    tag = soup.find("p", {"class": "short"})
    return tag.text


def get_long_meaning(soup):
    """
        This function returns the long meaning of the word
    """
    tag = soup.find("p", {"class": "long"})
    return tag.text


def get_more_info(tag):
    """
        This function returns the synonyms, antonyms, and the context in which they
        are used like type, type_of
    """
    result = {}
    if not tag:
        return result
    infos = tag.find_all("dl", {"class": "instances"})
    if not infos:
        return result
    for info in infos:
        name = info.span.text[:-1].lower()
        value = [item.text for item in info.find_all("a")]
        result[name] = value
    return result


def get_definitions(soup):
    """
        This function is used to get the details of the word
    """
    result = []
    tag = soup.find("div", {"class": "word-definitions"})
    if not tag:
        return result
    words = tag.find_all("li")
    if not words:
        return result
    for word in words:
        defintion_tag = word.find("div", {"class": "definition"})
        data = str(defintion_tag).split("</div>")[1:]
        definition = ''.join(data).strip()
        word_type = defintion_tag.find("div", {"class": "pos-icon"}).text
        examples = [item.text.replace("\n", "") for item in word.find_all(
            "div", {"class": "example"})]
        result.append({
            'definition': definition,
            'word_type': word_type,
            'info': get_more_info(word),
            'examples': examples
        })
    return result
