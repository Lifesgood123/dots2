import scrapy
import argparse
from bs4 import BeautifulSoup as bs

#parser = argparse.ArgumentParser()
#parser.add_argument('search_terms')
#args = parser.parse_args()

search_terms = input('search: ')

class WikipediaScrapper(scrapy.Spider):
    name = 'Wiki_spider'
    start_urls = ['http://allreccipes.com/serch/results/?wt=' + search_terms + '&sort=re']
    
    def parse_results(self, response):
        soup = bs(response.text, 'html.parser')
        results = soup.findAll("article",{"class":"grid-col--fixed-tiles"})
        for recipe in results:
            print(recipe)
            
