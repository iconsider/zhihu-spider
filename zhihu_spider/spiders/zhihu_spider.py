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
from zhihu_spider.items import UserItem

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
            userTemp = UserItem()
            userTemp["userId"] = link.replace("/people/", "")
            # 继承scrapy.Item的类的对象都会被Pipeline抓取到
            yield userTemp

        nextPage = selector.css("button.Button.PaginationButton.PaginationButton-next.Button--plain").extract()
        if len(nextPage) == 1:
            self.pageNum += 1
            nextPageUrl = "https://www.zhihu.com/people/figo-zhu/followers?page=%s" %self.pageNum
            print("url is %s" %nextPageUrl)
            yield Request(url=nextPageUrl, callback=self.parse)
