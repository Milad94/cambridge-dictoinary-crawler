from config import words_collection
from decorators import exception_logger


@exception_logger
def __word_is_exist(word):
    return len(list(words_collection.find({'word': word})))


@exception_logger
def save_words_to_tb(word_list):
    for word in word_list:
        if not __word_is_exist(word['word']):
            words_collection.insert(word)
