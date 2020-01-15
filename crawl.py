from pars import pars_text, pars_word_page
from request import send_get_request


def crawl_word(url):
    response = send_get_request(url)
    return pars_word_page(response.text)


def crawl_text(url):
    response = send_get_request(url)
    return pars_text(response.text)
