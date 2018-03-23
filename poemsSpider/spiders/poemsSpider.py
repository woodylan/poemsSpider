import scrapy
import re
from bs4 import BeautifulSoup

from poemsSpider.items import PoemsSpiderItem


class PoemsSpider(scrapy.Spider):
    name = "poems"
    allowed_domains = ['gushiwen.org']

    def start_requests(self):
        url = 'http://www.gushiwen.org/gushi/xiaoxue.aspx'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        poemList = response.css('div.sons').xpath('div/span/a')
        for poem in poemList:
            url = poem.xpath('@href').extract()[0]

            yield scrapy.Request(url, callback=self.parse_content)

    def parse_content(self, response):
        item = PoemsSpiderItem()

        title = response.css('div.sons h1').xpath('text()').extract()[0]
        print(title)

        item['title'] = response.css('div.sons h1').xpath('text()').extract()[0]

        try:
            author = response.css('div.cont p.source a').xpath('text()').extract()[1]
        except:
            author = ''

        content = response.xpath('//div[@class="contson"]')[0].extract()

        "过滤掉html标签"
        content = BeautifulSoup(content, 'xml').get_text()
        "过滤掉空格"
        content = content.strip().replace("\n", "").replace(' ', '')
        "去掉空格里的内容"
        content = re.sub('\([^)]*\)', '', content)
        content = re.sub('\（[^)]*\）', '', content)

        # 换行
        content = re.sub("。", "。\n", content)
        content = content.rstrip("\n")

        item['author'] = author
        item['content'] = content

        yield item
