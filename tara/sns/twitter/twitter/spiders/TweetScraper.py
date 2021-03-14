import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class TweetScraper(CrawlSpider):
    name = "TweetScraper"
    allow_domains = ["twitter.com"]

    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
