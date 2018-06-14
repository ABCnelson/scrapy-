# encoding=utf-8
__author__ = 'Nelson Yeh'

from scrapy import Request
from scrapy.spiders import Spider
from test100.items import ShushanItem #需根据自己的项目名称和Item类修改，可不修改

class ShushanSpider(Spider):
    name = "shushan" #爬虫命名，可按照自己要求修改，可不修改
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    } #代理设置，可参考本人设置
    def start_requests(self):
        url = 'http://www.shushan.net.cn/index.php?_m=mod_product&_a=prdlist&cap_id=69'#访问的初始地址，一般为自己要爬取的网页的第一页地址，必须修改
        yield Request(url, headers=self.headers)
    def parse(self, response):
        item = ShushanItem() #参考Item.py里面的设置，根据爬取的内容项取的名字，可随意取，但此处必须引用
        row_all = response.xpath('//div[@class="prod_list_con"]/div[@class="prod_list_list"]')#需学习xpath语法，地址：http://www.w3school.com.cn/xpath/xpath_syntax.asp，此处获取的是所有item的上层元素位置，必须修改
        for row in row_all:#定义单个行或块，可不修改
            item['name'] = row.xpath(
                './/div[@class="prod_list_name"]/a/text()').extract()[0]#获取name项的元素位置，并用extract()[0]提取值，必须修改
            item['category'] = row.xpath(
                './/div[@class="prod_list_type"]/a/text()').extract()[0]#获取category项的元素位置，并用extract()[0]提取值，必须修改
            yield item
        next_url = response.xpath('//a[contains(text(),"下一页")]/@href').extract()#获取下一页的网址，根据初始访问地址页面底部，下一页元素的href设置，必须修改
        if next_url: #如果next_url不空
            next_url = 'http://www.shushan.net.cn/index.php?_m=mod_product&_a=prdlist&cap_id=69' + next_url[0]#获取下一页的访问地址，必须修改
            yield Request(next_url, headers=self.headers) # 循环访问下一页的数据，获取name项和category项的值