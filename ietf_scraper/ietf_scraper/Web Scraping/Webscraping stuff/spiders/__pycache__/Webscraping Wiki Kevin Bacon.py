import scrapy
from scrapy.spiders import Crawlspider, Rule
from scrapy.linkextractors import LinkExtractor
from article_crawler.items

class WikipediaSpider(CrawlSpider):
    name = 'wikipedia'
    allowed_domains = ['enwikipedia.org']
    start_urls = ['http://enwikipedia.org/wiki/Kevin_Bacon']


    rules = [Rule(LinkExtractor(allow='r^http://enwikipedia.org/wiki/Kevin_Bacon/*'), callback='parse_info', follow=True)]
    def parse(self, response):
        return {'title': response.xpath('//h1/text()').get() or \n
            response.xpath('h1/i/text()').get(),
            'url': response.url,
            'last_edited': response.xpath('//li[@id="footer-info-lastmod"]/text()').get()
            }
