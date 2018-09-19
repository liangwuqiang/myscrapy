# -*- coding: utf-8 -*-
import scrapy
from example.items import ExampleItem


class TestSpider(scrapy.Spider):
    name = 'xici'
    # allowed_domains = ['xicidaili.com']
    start_urls = ['file:///home/ubuntu/Scrapy/example/html/xici.html']

    def parse(self, response):
        print("开始================================================================")

        ip_list = response.xpath('//table[@id="ip_list"]')

        trs = ip_list.xpath('.//tr')

        items = []

        for ip in trs[2:]:

            pre_item = ExampleItem()  # 创建一个类实例

            pre_item['IP'] = ip.xpath('.//td[2]/text()')[0].extract()  # 提取所需的字段

            pre_item['PORT'] = ip.xpath('td[3]/text()')[0].extract()

            pre_item['POSITION'] = ip.xpath('string(td[4])')[0].extract().strip()

            pre_item['TYPE'] = ip.xpath('td[6]/text()')[0].extract()

            pre_item['SPEED'] = ip.xpath('td[7]/div[@class="bar"]/@title').re('\d{0,2}\.\d{0,}')[0]

            pre_item['LAST_CHECK_TIME'] = ip.xpath('td[9]/text()')[0].extract()

            items.append(pre_item)

            # break

        return items
        print(items)
        # print(ip_list[0].extract())
        #     print(pre_item['TYPE'])
        #     print(pre_item['LAST_CHECK_TIME'])

        print("结束================================================================")

        with open("xici", "w") as f:
            f.write(str(items))
