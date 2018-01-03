#!/usr/bin/env python3        #跨平台注释
# -*- coding: utf-8 -*-       #中文支持注释


import scrapy
import time
from scrapy.selector import Selector
from scrapy.http import Request
from selenium import webdriver
import io
import sys

#改变标准输出的默认编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')


class zhihu(scrapy.Spider):
    name="zhihu"
    allowed_domains = ["www.zhihu.com"]
    start_urls = [
            r'https://www.zhihu.com/people/qin.chao/activities',
        ]

    def parse(self, response):
        selector = Selector(response)

        url = selector.css('.Button.NumberBoard-item.Button--plain:nth-child(2)::attr(href)').extract()
        url_full = "http://" + self.allowed_domains[0] + url[0]
        tuple = (url_full,)
        yield Request(url=tuple[0], callback=self.parse_post, dont_filter=True)

    def parse_post(self, response):
        print("url is2: " + response.url)
        chromedriver = "D:\software\webdriver\chromedriver.exe"
        browser = webdriver.Chrome(chromedriver)
        browser.get(response.url)

        time.sleep(1)
        print(browser.page_source)







