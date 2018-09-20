# -*- coding: utf-8 -*-
import scrapy
from example.items import ExampleItem


class TmGoodsSpider(scrapy.Spider):
    name = 'tm_goods'
    # allowed_domains = ['tmall.com']
    allowed_domains = ['https://detail.tmall.com/item.htm?id=10152256872&skuId=78140728882&standard=1&user_id=680956838&cat_id=2&is_b=1&rn=25791b57c83899cb6cd226f02961eb3d']
    # start_urls = ['https://list.tmall.com/search_product.htm?spm=a220m.'
    #               '1000858.1000724.4.40ec5a1dhV7q0v&q=%D3%B2%C5%CC&sort='
    #               'd&style=g&from=3c..pc_1_searchbutton#J_Filter']
    start_urls = ['file:///home/lwq/Scrapy/myscrapy/html/tm.html']
    # start_urls = ['file:///home/ubuntu/Scrapy/example/html/tm.html']
    # start_urls = ['file:///home/ubuntu/Scrapy/example/html/xici.html']

    # 记录处理的页数
    count = 0

    def parse(self, response):
        TmGoodsSpider.count += 1

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
            yield scrapy.Request(url=item["GOODS_URL"], meta={'item':item}, callback=self.parse_detail, dont_filter=True)
            # print(item["GOODS_URL"])
            # break

    def parse_detail(self, response):
        div = response.xpath('//div[@class="extend"]/ul')

        if not div:
            print("详情页面出错--%s" % response.url)

        item = response.meta['item']
        div = div[0]
        # 店铺名称
        item["SHOP_NAME"] = div.xpath("li[1]/div/a/text()")[0].extract()
        # 店铺连接
        item["SHOP_URL"] = div.xpath("li[1]/div/a/@href")[0].extract()
        # 公司名称
        item["COMPANY_NAME"] = div.xpath("li[3]/div/text()")[0].extract().strip()
        # 公司所在地
        item["COMPANY_ADDRESS"] = div.xpath("li[4]/div/text()")[0].extract().strip()

        yield item

        print(item["SHOP_NAME"], item["SHOP_URL"], item["COMPANY_NAME"], item["COMPANY_ADDRESS"])
        print('结束=============================================================')
