# -*- coding: utf-8 -*-
import scrapy

from auspostcodes.items import AuspostcodesItem, PostcodeItem 

class PostCodePagesSpider(scrapy.Spider):
    name = "pcpages"
    base_url = 'http://auspost.com.au'
    start_url = base_url+'/postcode/suburb-index/a'
    start_urls = ( start_url, )

    seen_indexs = set()
    def parse(self, response):
        print "parse_link"
        for i in self.parse_link(response): yield i
        print "parse_a2z"
        for r in self.parse_a2z(response): yield r


    def parse_a2z(self, response):
        module_index = response.selector.xpath(r".//div[@class='module-index']/a")
        for indexpage in module_index:
            href = indexpage.xpath('@href').extract()
            href = self.base_url+href.pop()
            if href in self.seen_indexs:
                yield None
            else:
                self.seen_indexs.add(href)
                yield scrapy.Request(url=href, callback=self.parse_link)


    def parse_link(self, response):
        sel = response.selector.xpath(r".//*[@id='suburb-index-list']/a")
        for x in sel:
            i = AuspostcodesItem()
            i['url'] = self.base_url+x.xpath('@href').extract().pop()
            i['suburb'] = x.xpath('text()').extract().pop()
            print i
            yield (i)

