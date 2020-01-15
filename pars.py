from bs4 import BeautifulSoup


def pars_text(html_text):
    html_obj = BeautifulSoup(html_text, 'html.parser')
    title = html_obj.select('#link-7726e0d0 > span:nth-child(1)')[0].text
    article_summary = html_obj.find(id='article-summary').text
    paragraphs = html_obj.select('p.css-exrw3m.evys1bk0')
    text = title + '' + article_summary
    text += ' '.join([paragraph.text for paragraph in paragraphs])
    return text
