#!/usr/bin/python3.7  
# -*- coding: utf-8 -*-  

from selenium import webdriver
import os
from lxml import etree
import time
import sys
import re

# 19100132030 
#Drivers.execute_script("$('input[type=text]').val('13800138000')")# 自动输入账号
#Drivers.execute_script("$('input[type=password]').val('test')")# 自动输入密码

def spd(values):

        time.sleep(30)
        
        driver.get("https://www.tianyancha.com/search?key="+values)# 搜索
       
        time.sleep(5)
        
        js_bottom = "var q=document.documentElement.scrollTop=10000"
        
        for i in range(5):
        
            res = driver.page_source # 获取源代码
            
            html = etree.HTML(res) # 解析
            
            pattern = re.compile(r'1[34578]\d{9}') # 正则
            
            result_list=[]
            
            result = pattern.findall(res)
            
            result_list.append(result)
            
            time.sleep(3)
            
            driver.execute_script(js_bottom) # 移动到浏览器底部
            
            time.sleep(5)
            
            print(list(set(result)))
            
            elem = driver.find_element_by_xpath("//*[@class='num -next']").click() # 点击翻页
            
        
        
        time.sleep(5) #间隔五秒再调用函数，如遇错误手动刷新
        
        return 

        
if __name__ == "__main__":

    try:
        driver = webdriver.Chrome() # 初始化webdriver
        values = input() # 输入要爬的内容
        num = 1
        driver.get("https://www.tianyancha.com/search/p?key="+values) #首次打开并登入
        driver.maximize_window()
    except:
        print("搞啥子呢？")
        time.sleep(3)
        driver.close() # 异常则关闭
    


    spd(values)
    
    
    
