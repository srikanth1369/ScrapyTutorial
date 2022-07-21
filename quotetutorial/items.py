# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotetutorialItem(scrapy.Item):
    # define the fields for your item here like:
    small_title = scrapy.Field()
    authors = scrapy.Field()
    next_link = scrapy.Field()
    tags = scrapy.Field()

