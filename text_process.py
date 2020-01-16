from decorators import exception_logger


@exception_logger
def find_unique_words(text):
    words = text.split(' ')
    words = list(set(words))
    words = [word for word in words if len(word) > 2]
    return words
