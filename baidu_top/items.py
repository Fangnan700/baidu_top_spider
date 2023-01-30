# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BaiduTopDay(scrapy.Item):
    time = scrapy.Field()
    data = scrapy.Field()

