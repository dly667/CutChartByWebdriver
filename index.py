# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import os,sys,time
from selenium.webdriver.chrome.options import Options
import util
chrome_options = Options()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-infobars')
chrome_options.add_argument('--start-maximized')
 
# chrome_options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
driver=webdriver.Chrome(chrome_options=chrome_options)


current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
current_time1 = time.strftime("%Y-%m-%d", time.localtime(time.time()))
print(current_time )
print(current_time1 )
# 必须打印图片路径HTMLTestRunner才能捕获并且生成路径，\image\**\\**.png 是获取路径的条件,必须这样的目录
#设置存储图片路径，测试结果图片可以按照每天进行区分



#通过if进行断言判断
driver.get("https://baidu.com/")
#新创建路径“.”表示当前整个.py文件的路径所在的位置，“\\”路径分割符，其中的一个是“\”表示转义字符
pic_path = 'haha.png'
print(pic_path)
time.sleep(5)
print(driver.title)
#截取当前url页面的图片，并将截取的图片保存在指定的路径下面（pic_path），注：以下两种方法都可以
driver.save_screenshot(pic_path)

driver.quit()