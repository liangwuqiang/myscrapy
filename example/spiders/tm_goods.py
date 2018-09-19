# -*- coding: utf-8 -*-
import scrapy
from example.items import ExampleItem


class TmGoodsSpider(scrapy.Spider):
    name = 'tm_goods'
    # allowed_domains = ['tmall.com']
    # start_urls = ['https://list.tmall.com/search_product.htm?spm=a220m.'
    #               '1000858.1000724.4.40ec5a1dhV7q0v&q=%D3%B2%C5%CC&sort='
    #               'd&style=g&from=3c..pc_1_searchbutton#J_Filter']
    start_urls = ['file:///home/ubuntu/Scrapy/example/html/tm.html']
    # start_urls = ['file:///home/ubuntu/Scrapy/example/html/xici.html']

    def parse(self, response):
        print('开始=============================================================')
        # divs = response.xpath("//div[@id='J_ItemList']/div[@class='product']/div")
        divs = response.xpath("//div[@id='J_ItemList']/div[@class='product  ']/div")

        if not divs:
            print("列表页出错--%s" % response.url)

        for div in divs:
            item = ExampleItem()
            # 商品价格
            item["GOODS_PRICE"] = div.xpath("p[@class='productPrice']/em/@title")[0].extract()
            # 商品名称
            item["GOODS_NAME"] = div.xpath("p[@class='productTitle']/a/@title")[0].extract()
            # 商品连接
            pre_goods_url = div.xpath("p[@class='productTitle']/a/@href")[0].extract()
            item["GOODS_URL"] = pre_goods_url if "https:" in pre_goods_url else ("https:" + pre_goods_url)

            # yield scrapy.Request(url=item["GOODS_URL"], meta={'item': item}, callback=self.parse_detail,
            #                      dont_filter=True)
            yield scrapy.Request(url=item["GOODS_URL"], callback=self.parse_detail)
            # print(item["GOODS_URL"])

    def parse_detail(self, response):

        # div = response.xpath('//div[@class="extend"]/ul')
        # print(response.url)
        print('结束=============================================================')
