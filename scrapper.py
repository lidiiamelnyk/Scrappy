import codecs
import re
from datetime import datetime, date, timedelta
from pprint import pprint

import requests
from lxml import html

START_DATE = '01032014'
END_DATE = '28022017'
CORPUS_FILE_NAME = 'corpus.txt'


def get_news_post_links(url):
    page_archive = requests.get(url)
    tree_archive = html.fromstring(page_archive.content)

    url_domain = "https://www.pravda.com.ua"
    link_list = []

    pattern = re.compile("/news/\d+/\d+/\d+/\d+/")
    for element, attribute, link, pos in tree_archive.iterlinks():

        if not pattern.match(link):
            continue
        link_list.append(url_domain + link)

    return link_list


def get_news_post_content(url):
    page = requests.get(url)
    tree = html.fromstring(page.content)
    post = ''
    for element in tree.xpath('//div[@class="post_news__text"]//p'):
        post += " " + element.text_content()

    return post


# builds daterange
def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


# datetime format 01012014 DATMONTHYEAR
def get_archive_pages():
    pattern_string = "https://www.pravda.com.ua/archives/date_"
    start_date_object = datetime.strptime(START_DATE, '%d%m%Y')
    end_date_object = datetime.strptime(END_DATE, '%d%m%Y')

    link_date_list = []
    for i in daterange(start_date_object, end_date_object):
        url_string = pattern_string + i.strftime('%d%m%Y')
        link_date_list.append(url_string)

    return (link_date_list)


def get_full_news_urls_list():
    archive_pages_urls = get_archive_pages()

    post_pages_urls = []
    for i in archive_pages_urls:
        post_pages_urls.extend(get_news_post_links(i))

    return post_pages_urls


def save_content_to_file():
    filename = CORPUS_FILE_NAME
    urls_list = get_full_news_urls_list()
    with codecs.open(filename, "w", encoding="utf-8") as f:
        for url in urls_list:
            content = get_news_post_content(url)
            print("content for url downloaded: " + url)
            f.write(content)


def main():
    save_content_to_file()


main()
