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
    # selenium配置
    chromedriver = "D:\software\webdriver\chromedriver.exe"
    browser = webdriver.Chrome(chromedriver)
    # scrapy配置
    name="zhihu"
    allowed_domains = ["www.zhihu.com"]
    start_urls = [
            r'https://www.zhihu.com/people/figo-zhu/followers?page=1',
        ]
    pageNum = 1

    def parse(self, response):
        self.browser.get(response.url)
        time.sleep(1)

        body = self.browser.page_source
        selector = Selector(text=body)
        fansLink = selector.css("div#Profile-following div.ContentItem-head a.UserLink-link::attr(href)").extract()
        for link in fansLink:
            self.writeData(link.replace("/people/", ""))

        nextPage = selector.css("button.Button.PaginationButton.PaginationButton-next.Button--plain").extract()
        if len(nextPage) == 1:
            self.pageNum += 1
            nextPageUrl = "https://www.zhihu.com/people/figo-zhu/followers?page=%s" %self.pageNum
            print("url is %s" %nextPageUrl)
            yield Request(url=nextPageUrl, callback=self.parse)

    # 用于记录所有粉丝的link
    def writeData(self, data):
        print(data)
        with open("z:/zhihu.txt", 'a') as f:
            f.write(data + "\n")