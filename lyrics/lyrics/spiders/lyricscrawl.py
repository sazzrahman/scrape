import scrapy


class LyricscrawlSpider(scrapy.Spider):
    name = 'lyricscrawl'
    allowed_domains = ['lyrics.com']
    start_urls = ['http://lyrics.com/']

    def parse(self, response):
        links = response.css("a::attr(href)").getall()

        yield {
            "links":links
        }


