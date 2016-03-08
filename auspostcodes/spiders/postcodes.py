# -*- coding: utf-8 -*-
import scrapy
from scrapy.utils.project import get_project_settings

from auspostcodes.items import AuspostcodesItem, PostcodeItem 

import json

from pprint import pprint

class PostCodeSpider(scrapy.Spider):
    name = "postcodes"
    base_url = 'http://auspost.com.au'

    def __init__(self, *args, **kwargs):
        super(PostCodeSpider, self).__init__(*args, **kwargs)
        settings = get_project_settings()
        pcfile = settings.get("POSTCODE_PAGES_JSON")
        if not pcfile:
            raise ValueError("POSTCODE_PAGES_JSON file not found"
                            " Please run pcpages spider first")
        else:
            with open(pcfile, 'r') as jsonfile:
                self.start_urls = [x['url'] for x in json.load(jsonfile)]


    def parse(self, response):
        sel = response.selector.xpath(r".//*[contains(@class, 'resultsWindow')]/*/tbody/tr")
        i = PostcodeItem()
        pcode = sel.xpath(r"//td[@class='first']/a/text()").extract()[0]
        sub_state = sel.xpath(r"//td[@class='second']/a/text()").extract()[0]
        pprint (sub_state)
        i['postcode'] = pcode
        i['suburb'] = sub_state.split(',')[0].strip()
        i['state'] = sub_state.split(',')[1].strip()
        yield i