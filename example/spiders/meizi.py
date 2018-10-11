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
"""
class jiandanSpider(scrapy.Spider):
    name = 'jiandan'
    allowed_domains = []
    start_urls = ["http://jandan.net/ooxx"]
     
    def parse(self, response):
        item = JiandanItem()
        item['image_urls'] = response.xpath('//img//@src').extract()#提取图片链接
        # print 'image_urls',item['image_urls']
        yield item
        new_url= response.xpath('//a[@class="previous-comment-page"]//@href').extract_first()#翻页
        # print 'new_url',new_url
        if new_url:
            yield scrapy.Request(new_url,callback=self.parse)
"""