import scrapy

from ..items import QuotetutorialItem


class Quote_Spider(scrapy.Spider):

    name = 'quotes'
    page_number = 2
    start_urls = [
        'https://quotes.toscrape.com/'
    ]

    def parse(self, response, **kwargs):
        all_quotes = response.css('div.quote')

        items = QuotetutorialItem()
        for quotes in all_quotes:
            title = quotes.css('span.text::text').extract()
            authors = quotes.css('.author::text').extract()
            tags = quotes.css('.tag::text').extract()

            items['title'] = title
            items['authors'] = authors
            items['tags'] = tags

            yield items

            next_page = 'https://quotes.toscrape.com/page/' + str(Quote_Spider.page_number) + '/'

            if Quote_Spider.page_number <= 100:
                Quote_Spider.page_number += 1
                yield response.follow(next_page, callback=self.parse)



