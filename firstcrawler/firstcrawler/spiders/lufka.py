from scrapy.spiders import CrawlSpider , Rule
from scrapy.linkextractors import LinkExtractor



class CrawlerSpider(CrawlSpider):
        name = "mycrawler"
        allowed_domains = ['https://www.pracuj.pl']
        start_url = ["https://it.pracuj.pl"]

        rules = (
                Rule(LinkExtractor(allow=""))
        )