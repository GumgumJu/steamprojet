# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from datetime import date
import scrapy


class SteamItem(scrapy.Item):
    title = scrapy.Field()
    image = scrapy.Field()
    date  = scrapy.Field()
    price = scrapy.Field()
    discount = scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
