from bs4 import BeautifulSoup, Tag
import requests


URL = 'https://en.wikipedia.org/wiki/List_of_the_most_common_passwords'
TABLE_NAME = 'Top 25 most common passwords by year according to SplashData'


def get_wiki_page(url):
    return requests.get(url).text


def get_parsed_passwords(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    tables = soup.find_all('table')
    result_table = list(filter(lambda x: TABLE_NAME in x.text, tables))[0]
    results = []
    for i in result_table.find_all('td', align='left'):
        if isinstance(i, Tag):
            results.append(i.contents[0].text.replace('\n', ''))
    return list(set(results))


if __name__ == '__main__':
    content = get_wiki_page(url=URL)
    passwords = get_parsed_passwords(html_content=content)
    print(*passwords, sep='\n')