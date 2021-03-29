import requests
import sys
from bs4 import BeautifulSoup
from textwrap import TextWrapper

from news_scraper import NewsScraper
from user_settings import settings, set_file_name, change_settings

url = sys.argv[1]

change_settings()

file_name = set_file_name(url)
wrapper = TextWrapper(width=settings['max_symbols_in_line'])

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
headlines = [soup.find_all('h' + str(num)) for num in range(1, 7)]

headline = NewsScraper.get_main_headline(headlines)
# главный заголовок должен лежать под тегом <h1>,
# соответственно в списке
# под нулевым индексом
if headline is not None:
    headline = headline.text
    headline = wrapper.fill(headline)
    print(headline)
    print('\n')
    with open(file_name, 'w+', encoding='utf-8') as file:
        file.write(headline + '\n')  # записать заголовок в файл

body = soup.find(itemprop='articleBody')

if body is not None:

    body = NewsScraper.handle_article_body(body)

    for paragraph in body:
        body = wrapper.fill(paragraph)
        print('\n' + body)
        with open(file_name, 'a+', encoding='utf-8') as file:
            file.write('\n' + body + '\n')  # записать каждый абзац в файл
else:
    whitelist = [
        'p'
    ]

    body = [t for t in soup.find_all(text=True) if t.parent.name in whitelist]

    for paragraph in body:
        body = wrapper.fill(paragraph)
        body = body.replace(u'\xa0', ' ')  # escape &nbsp
        print('\n' + body)
        with open(file_name, 'a+', encoding='utf-8') as file:
            file.write('\n' + body + '\n')  # записать каждый абзац в файл
