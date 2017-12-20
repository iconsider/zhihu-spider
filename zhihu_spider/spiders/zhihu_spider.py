#!/usr/bin/env python3        #跨平台注释
# -*- coding: utf-8 -*-       #中文支持注释

import scrapy
from scrapy.selector import Selector

class zhihu(scrapy.Spider):
    name="zhihu"
    allowed_domains = ["www.zhihu.com"]
    start_urls = [
            r'https://www.zhihu.com/people/liancheng/followers',
        ]

    def parse(self, response):
        selector = Selector(response)
        fans1 = selector.css('div.Profile-mainColumn:first-child')
        print(response.body)
        print("----------------")
        print(fans1)


