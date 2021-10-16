import requests
from bs4 import BeautifulSoup, SoupStrainer

feed_url = "https://www.acouplecooks.com/category/recipes/"

HEADER = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}

def scraper():

    article_links = []
    try:

        r = requests.get(feed_url, headers=HEADER)
        soup = BeautifulSoup(r.content, "html.parser")
        links = soup.find_all('a', href=True)
        for link in links:
            print(link['href'])
        # print(links[0]['href'])
        # print(soup)
    except Exception as e:
        print('Something happend bad: ', e)


print('starting scraping')
tipnut_scraper()
print('finished scraping')