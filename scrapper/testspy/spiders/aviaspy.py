import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.spiders.crawl import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class Rec(scrapy.Item):
    name = scrapy.Field()
    country = scrapy.Field()
    aircraft = scrapy.Field()
    active = scrapy.Field()
    
class Aviadata(CrawlSpider):
    name = "aviadata"
    def __init__(self, url, *args, **kwargs):
        self.start_urls.append(url)
        super(Aviadata, self).__init__(*args, **kwargs)

    start_urls = [
#        'https://www.airfleets.net/recherche/airline.htm'
#	'https://www.airfleets.net/recherche/list-airline-a.htm'
    ]
    
    rules = (
        Rule(LinkExtractor(allow=('list\-airline\-'),) , follow=True),
        Rule(LinkExtractor(allow=('flottecie'), restrict_xpaths=('/html/body/main/div[1]/div/div[1]/table/tr[*]/td[3]/a[2]', )), callback='parse_item', follow=True),
#         Rule(LinkExtractor(allow=('flottecie')), callback='parse_item', follow=True),
    )
    
    def parse_item(self, response):
        name = response.xpath('/html/body/main/div[1]/div/div[2]/table[1]/tr[2]/td/h1/a/text()')  #/html/body/table[4]/tbody/tr[1]/td/table[1]/tbody/tr/td[2]/table[1]/tbody/tr[2]/td/h1/a
        country = response.xpath('/html/body/main/div[1]/div/div[2]/table[1]/tr[2]/td/table/tr/td[1]/table/tr[1]/td[2]/a/text()')
        for line in response.xpath('/html/body/main/div[1]/div/div[5]/div[2]/table/tr') :
            res= { 
                'name': name.extract(),
                'country': country.extract(),
                'aircraft': line.xpath('td[1]/a/b/text()').extract(),
                'active': line.xpath('td[2]/a/b/text()').extract(),
                'parked': line.xpath('td[3]/a/b/text()').extract()
            }
            if res['aircraft']:
                yield res
