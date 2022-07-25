# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotetutorialItem(scrapy.Item):
    title = scrapy.Field()
    authors = scrapy.Field()
    tags = scrapy.Field()
