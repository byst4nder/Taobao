# -*- coding: utf-8 -*-
import scrapy
import re
import json
import time
from items import TaobaoItem

class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ['taobao.com']
    start_urls = ['https://s.taobao.com/search?q=python&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180408&ie=utf8']
    def parse(self, response):
        # print(response.body.decode('utf-8'))
        js = re.findall(r'g_page_config = (.*?)g_srp_loadCss',response.body.decode('utf-8'),re.S)[0].strip().strip(';')
        item_list = json.loads(js)['mods']['itemlist']['data']['auctions']
        for item in item_list:
            data = TaobaoItem()
            data['title'] = re.sub(r'<span.*?</span>','python',item['title'])
            data['price'] = item['view_price']
            data['fee'] = item['view_fee']
            data['area'] = item['item_loc']
            data['sales'] = item['view_sales']
            data['name'] = item['nick']
            data['isTmall'] = '是' if item['shopcard']['isTmall'] else '否'
            data['detail_url'] = item['detail_url'].strip().strip('/')
            yield data
        url_12 = 'https://s.taobao.com/api?_ksTS=1523179236254_226&callback=jsonp227&ajax=true&m=customized&stats_' \
                 'click=search_radio_all:1&q=python&s=36&imgfile=&initiative_id=staobaoz_20180408&bcoffset=-1' \
                 '&js=1&ie=utf8&rn=d5706a3802513dad625d594a35702a6b'
        yield scrapy.Request(url_12,callback=self.parse_12)

    def parse_12(self, response):
        js = re.findall(r'\((.*)\)',response.body.decode('utf-8'),re.S)[0]
        item_list = json.loads(js)['API.CustomizedApi']['itemlist']['auctions']
        for item in item_list:
            data = TaobaoItem()
            data['title'] = re.sub(r'<span.*?</span>', 'python', item['title'])
            data['price'] = item['view_price']
            data['fee'] = item['view_fee']
            data['area'] = item['item_loc']
            data['sales'] = item['view_sales']
            data['name'] = item['nick']
            data['isTmall'] = '是' if item['shopcard']['isTmall'] else '否'
            data['detail_url'] = item['detail_url'].strip().strip('/')
            yield data
        for i in range(1,100):
            ksts = time.time()
            _ksTs = "%s_%s"%(str(ksts*1000).strip('.')[0],str(ksts*1000).split('.')[1])
            callbacks = "json%s"%(int(str(ksts)[-3:])+1)
            data_value = 44*i
            url_48 = 'https://s.taobao.com/search?data-key=s&data-value={}&ajax=true&_' \
                     'ksTS={}&callback={}&q=python&imgfile=&commend=all&ssid=s5-e&search_' \
                     'type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_' \
                     'id=tbindexz_20170306&bcoffset=3&ntoffset=0&p4ppushleft=1%2C48'.format(data_value,_ksTs,data_value)
            yield scrapy.Request(url_48,callback=self.parse_48)

    def parse_48(self, response):
        # print(response.body.decode('utf-8'))
        js = re.findall(r'\((.*)\)', response.body.decode('utf-8'), re.S)[0]
        # print(js)
        item_list = json.loads(js)['mods']['itemlist']['data']['auctions']
        # print(item_list)
        for item in item_list:
            data = TaobaoItem()
            data['title'] = re.sub(r'<span.*?</span>', 'python', item['title'])
            data['price'] = item['view_price']
            data['fee'] = item['view_fee']
            # print(type(data['fee']))
            data['area'] = item['item_loc']
            data['sales'] = item['view_sales']
            data['name'] = item['nick']
            data['isTmall'] = '是' if item['shopcard']['isTmall'] else '否'
            data['detail_url'] = item['detail_url'].strip().strip('/')
            yield data