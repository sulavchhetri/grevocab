
def get_other_forms(soup):
    other_forms_tag = soup.find("p", {"class": "word-forms"})
    words = other_forms_tag.b.text
    return words.split(";")


def get_short_meaning(soup):
    tag = soup.find("p", {"class": "short"})
    return tag.text


def get_long_meaning(soup):
    tag = soup.find("p", {"class": "long"})
    return tag.text


def get_more_info(tag):
    result = {}
    if not tag:
        return result
    if infos := tag.find_all("dl", {"class": "instances"}):
        for info in infos:
            name = info.span.text[:-1].lower()
            value = [item.text for item in info.find_all("a")]
            result[name] = value
    return result


def get_definitions(soup):
    result = []
    tag = soup.find("div", {"class": "word-definitions"})
    if not tag:
        return result
    if words := tag.find_all("li"):
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
                'examples': examples,
                'info': get_more_info(word)

            })
    return result
