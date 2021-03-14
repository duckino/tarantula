import scrapy


class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    start_urls = ["http://brickset.com/sets/year-2016"]
    user_agent = (
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
    )

    def parse(self, resp):
        SET_SELECTOR = ".set"
        for brickset in resp.css(SET_SELECTOR):
            NAME_SELECTOR = "h1 ::text"
            PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
            MINIFIGS_SELECTOR = './/dl[dt/text() = "Minifigs"]/dd[2]/a/text()'
            IMAGE_SELECTOR = "img ::attr(src)"

            yield {
                "name": brickset.css(NAME_SELECTOR).extract_first(),
                "pieces": brickset.xpath(PIECES_SELECTOR).extract_first(),
                "minifigs": brickset.xpath(MINIFIGS_SELECTOR).extract_first(),
                "image": brickset.css(IMAGE_SELECTOR).extract_first(),
            }

        NEXT_PAGE_SELECTOR = ".next a ::attr(href)"
        next_page = resp.css(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
            yield scrapy.Request(resp.urljoin(next_page), callback=self.parse)
