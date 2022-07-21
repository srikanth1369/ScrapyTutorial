import scrapy

from ..items import QuotetutorialItem


class Quote_Spider(scrapy.Spider):

    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/'
    ]

    def parse(self, response, **kwargs):
        all_quotes = response.css('div.quote')
        items = QuotetutorialItem()
        for quotes in all_quotes:
            small_title = quotes.css('span.text::text').extract()
            authors = quotes.css('small.author::text').extract()
            tags = quotes.xpath("//a[@class='tag']/text()").extract()
            next_link = quotes.css("li.next a").xpath("@href").extract()

            items['small_title'] = small_title
            items['authors'] = authors
            items['tags'] = tags
            items['next_link'] = next_link

            yield items



