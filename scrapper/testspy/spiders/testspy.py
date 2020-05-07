import scrapy
from scrapy.crawler import CrawlerProcess

class Aviadata(scrapy.Spider):
    name = "testdata"
    start_urls = [
        'https://scrapoxy.readthedocs.io/en/master/tutorials/python-scrapy-blacklisting/',
    ]
    
    def parse(self, response):
        for quote in response.xpath('//h2/text()'):
            yield {'quote': quote.extract(), 'error': 'none'}
