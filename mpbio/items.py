# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MpbioItem(scrapy.Item):

    name = scrapy.Field()
    price=scrapy.Field()
    sku = scrapy.Field()
    cas_number  = scrapy.Field()
    molecular_formula = scrapy.Field()
    descript_table = scrapy.Field()
    categories = scrapy.Field()
    # name = scrapy.Field()
    # pass

