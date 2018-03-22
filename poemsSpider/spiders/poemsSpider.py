import scrapy
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

        item['title'] = response.css(
            'div.sons h1').xpath('text()').extract()[0]

        try:
            author = response.css('div.cont p.source a').xpath('text()').extract()[1]
        except:
            author = ''

        content = response.xpath('//div[@class="contson"]')[0].extract()
        item['author'] = author
        item['content'] = content.strip()

        yield item
