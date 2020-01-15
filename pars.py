from bs4 import BeautifulSoup
from decorators import none_if_exception


@none_if_exception
def find_definition(def_block):
    return def_block.find('div', {'class': 'def ddef_d db'}).text


@none_if_exception
def find_examples(def_block):
    examples = def_block \
        .find('div', {'class': 'def-body ddef_b'}) \
        .find_all('span', {'class': 'eg deg'})
    return [example.text for example in examples]


@none_if_exception
def find_phrase(phrase_block):
    return phrase_block \
        .find('span', {'class': 'phrase-title dphrase-title'}).text


@none_if_exception
def find_phrase_definition(phrase_block):
    return phrase_block \
        .find('div', {'class': 'def ddef_d db'}).text


@none_if_exception
def find_phrase_examples(phrase_block):
    phrase_examples = phrase_block \
        .find('div', {'class': 'def-body ddef_b'}) \
        .find_all('span', {'class': 'eg deg'})
    return [example.text for example in phrase_examples]


def pars_word_page(html_text):
    result = list()
    html_obj = BeautifulSoup(html_text, 'html.parser')

    def_blocks = html_obj.find_all('div', {'class': 'def-block ddef_block'})
    phrase_blocks = html_obj.select('div.pr.phrase-block.dphrase-block')

    for def_block in def_blocks:
        definition = find_definition(def_block)
        examples = find_examples(def_block)
        result.append({'definition': definition, 'examples': examples})

    for phrase_block in phrase_blocks:
        phrase = find_phrase(phrase_block)
        phrase_definition = find_phrase_definition(phrase_block)
        phrase_examples = find_phrase_examples(phrase_block)
        result.append({'phrase': phrase,
                       'phrase_definition': phrase_definition,
                       'phrase_examples': phrase_examples})
    return result


def pars_text(html_text):
    html_obj = BeautifulSoup(html_text, 'html.parser')
    title = html_obj.select('#link-7726e0d0 > span:nth-child(1)')[0].text
    article_summary = html_obj.find(id='article-summary').text
    paragraphs = html_obj.select('p.css-exrw3m.evys1bk0')
    text = title + '' + article_summary
    text += ' '.join([paragraph.text for paragraph in paragraphs])
    return text
