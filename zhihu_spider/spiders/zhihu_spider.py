#!/usr/bin/env python3        #跨平台注释
# -*- coding: utf-8 -*-       #中文支持注释

import scrapy
from scrapy.selector import Selector

class zhihu(scrapy.Spider):
    name="zhihu"
    allowed_domains = ["www.zhihu.com"]
    start_urls = [
            r'https://www.zhihu.com/people/liancheng/followers?page=1',
        ]

    def parse(self, response):
        selector = Selector(response)

        fans = selector.css("div#Profile-following a.UserLink-link::attr(href)").extract()
        print(response.body)
        print("----------------")
        #只能获取前3个粉丝的url（每页总共20个粉丝）
        print(fans)


