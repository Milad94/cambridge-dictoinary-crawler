from crawl import crawl_text, crawl_word
from mongo import save_words_to_tb
from text_process import find_unique_words

if __name__ == "__main__":
    text = crawl_text(
        "https://www.nytimes.com/2020/01/14/world/"
        "europe/spain-chemical-plant-explosion.html")
    words = find_unique_words(text)
    words_list = list()
    for word in words:
        data = crawl_word(
            f'https://dictionary.cambridge.org/dictionary/english/{word}')
        words_list.append({'word': word, 'data': data})
    save_words_to_tb(words_list)
