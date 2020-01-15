from crawl import crawl_text, crawl_word
from text_process import find_unique_words

if __name__ == "__main__":
    text = crawl_text(
        "https://www.nytimes.com/2020/01/14/world/europe/spain-chemical-plant-explosion.html")
    words = find_unique_words(text)
