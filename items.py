# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TaobaoItem(scrapy.Item):
    # "title": item["title"],
    # "price": item["view_price"],
    # "fee": '否' if item["view_fee"] else '是',
    # "area": item["item_loc"],
    # "sales": item["view_sales"],
    # "name": item["nick"],
    # "isTmall": '是' if item["shopcard"]["isTmall"] else '否',
    # "detail_url": item["detail_url"]
    title = scrapy.Field()
    price = scrapy.Field()
    fee = scrapy.Field()
    area = scrapy.Field()
    sales = scrapy.Field()
    name = scrapy.Field()
    isTmall = scrapy.Field()
    detail_url = scrapy.Field()