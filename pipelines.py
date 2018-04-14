# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import json
import xlwt
import os
import draw

class TaobaoPipeline(object):
    def __init__(self):
        if os._exists('/home/sephiroth/桌面/Taobao/Taobao/taobao.xlsx'):
            os.remove('/home/sephiroth/桌面/Taobao/Taobao/taobao.xlsx')
        self.f = xlwt.Workbook()
        self.sheet = self.f.add_sheet(u'sheet1',cell_overwrite_ok=True)
        titles = ['name','title','price','fee','area','sales','isTmall','detail_url']
        for i in range(0,len(titles)):
            self.sheet.write(0,i,titles[i])
        self.row = 1
        self.data = []

    def process_item(self, item_list, spider):
        # for item in item_list:
        self.sheet.write(self.row,0,item_list['name'])
        self.sheet.write(self.row,1,item_list['title'])
        self.sheet.write(self.row,2,item_list['price'])
        self.sheet.write(self.row,3,item_list['fee'])
        self.sheet.write(self.row,4,item_list['area'])
        self.sheet.write(self.row,5,item_list['sales'])
        self.sheet.write(self.row,6,item_list['isTmall'])
        self.sheet.write(self.row,7,item_list['detail_url'])
        self.row += 1
        self.data.append(item_list)

    def draw_pic(self):
        data1 = {'包邮':0, '不包邮':0}
        data2 = {'天猫':0, '淘宝':0}
        data3 = {}
        for item in self.data:
            if item['fee'] == '0.00':
                data1['包邮'] += 1
            else:
                data1['不包邮'] += 1
            if item['isTmall'] == '是':
                data2['天猫'] += 1
            else:
                data2['淘宝'] += 1
            data3[item['area'].split(' ')[0]] = data3.get(item['area'].split(' ')[0], 0) +1
            # print(data1)
        print(data3)
        print(type(data3))
        draw.pie(data1, '是否包邮')
        draw.pie(data2, '是否为天猫')
        draw.pie(data3, '地区分布')


    def close_spider(self,spider):
        # print(1)
        self.draw_pic()
        self.f.save('/home/sephiroth/桌面/Taobao/Taobao/taobao.xlsx')
        # self.draw_pic()
