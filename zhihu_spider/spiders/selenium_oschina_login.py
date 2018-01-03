#!/usr/bin/env python3        #跨平台注释
# -*- coding: utf-8 -*-       #中文支持注释

from selenium import webdriver
import time

# Get local session of Chrome
chromedriver = "D:\software\webdriver\chromedriver.exe"
browser = webdriver.Chrome(chromedriver)
browser.get("http://www.oschina.net/")

browser.find_element_by_css_selector(".box .user-info a:first-child").click()
time.sleep(1)

browser.find_element_by_id("userMail").send_keys("331072550@qq.com")
time.sleep(1)
browser.find_element_by_id("userPassword").send_keys("xxxxxxxxxxx")
time.sleep(1)
browser.find_element_by_css_selector(".form-item.form-button button").click()
time.sleep(1)

print("done")


