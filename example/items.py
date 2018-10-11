# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ExampleItem(scrapy.Item):
    # 西刺代理
    # IP = scrapy.Field()
    # PORT = scrapy.Field()
    # POSITION = scrapy.Field()
    # TYPE = scrapy.Field()
    # SPEED = scrapy.Field()
    # LAST_CHECK_TIME = scrapy.Field()

    # 天猫商城
    GOODS_PRICE = scrapy.Field()
    GOODS_NAME = scrapy.Field()
    GOODS_URL = scrapy.Field()
    SHOP_NAME = scrapy.Field()
    SHOP_URL = scrapy.Field()
    COMPANY_NAME = scrapy.Field()
    COMPANY_ADDRESS = scrapy.Field()

    # 图片链接
    image_urls = scrapy.Field()


