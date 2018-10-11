import scrapy
from example.items import ExampleItem


class ExampleSpider(scrapy.Spider):
    name = 'meizi'
    allowed_domains = []
    start_urls = ['http://jandan.net/ooxx']

    def parse(self, response):
        item = ExampleItem()
        try:
            item['image_urls'] = response.xpath('//img//@src').extract()
            print(item['image_urls'])
        except:
            print('出现异常')

        print('ok')
