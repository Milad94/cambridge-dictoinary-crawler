from pars import pars_text
from request import send_get_request


def crawl_word():
    pass


def crawl_text(url):
    response = send_get_request(url)
    return pars_text(response.text)

