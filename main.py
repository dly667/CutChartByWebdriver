from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import util
import os
import time
from PIL import Image
from lxml import etree
from selenium.webdriver.common.keys import Keys
chrome_options = Options()

class Transfom():

    def main(self):
        # 获取当前目录和文件
        for root, dirs, files in os.walk("./",topdown=True):  
            
            break
      

        url_list = []
        dir_list = []

        for dir in dirs:
            # 拼接地址
            url = os.path.join(dir, "report.html")
            if os.path.exists(url):
                url_list.append('./'+url)
                dir_list.append(dir)
                if not os.path.exists("output/"+dir):
                    os.mkdir("output/"+dir)
                # url_list = append(url_list,url)

        flag = 0

        for url in url_list:

            with open(url, 'r', encoding='utf-8') as f:
                html = etree.HTML(f.read())
                html_data = html.xpath('//div[@id="nav_container"]//dt//a/@href')  
                # //*[@id="main_nav_list"]/dt//a[@target="detail_report_content"]
                html_text = html.xpath('//*[@id="main_nav_list"]/dt//a/text()')
                for i in range(len(html_data)):
                    
                    self.save_one(url+"/../"+html_data[i],dir_list[flag],html_text[i])
            flag += 1   
            # break
    def save_one(self,url,dir,filename):
        # 开启无界面模式
        chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--disable-gpu')
        # chrome_options.add_argument('--disable-infobars')
        # chrome_options.add_argument('--start-maximized')
        
        # chrome_options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        driver=webdriver.Chrome(chrome_options=chrome_options)
       
        driver.get("file:///Users/dly667/dev/CutChartByWebdriver/"+url)
        # 网页缩放
        driver.execute_script('document.getElementsByTagName("body")[0].style.zoom=0.38')
        # 隐藏X和Y轴的滚动条
        driver.execute_script("document.body.parentNode.style.overflowY = 'hidden';")
        driver.execute_script("document.body.parentNode.style.overflowX = 'hidden';")

        # 全屏截图
        util.fullpage_screenshot(driver, filename+".png",dir)
        # 关闭
        driver.close()
        # 退出
        driver.quit()
    # 合成全图
    def splice_image(self):
       
        for root, dirs, files in os.walk("./output",topdown=True):  
            break
        for dir in dirs:
            total_width = 0
            total_height = 0
            f_list = []

            for root, dirs, files in os.walk("./output/"+dir,topdown=True):
                for file in files:
                    try:
                        with Image.open("./output/"+dir+"/"+file) as f:
                            f_list.append(f)
                            tup = f.size
                            if tup[0] >total_width:
                                total_width = tup[0]
                            total_height += tup[1]
                         
                            # img.paste(img,(100,100),None)
                            # img = Image.new('RGB',(total_width, total_height))
                    except IOError:
                        continue
            blank_image = Image.new("RGB",(total_width, total_height))
            temp = 0
        
            for root, dirs, files in os.walk("./output/"+dir,topdown=True):
                # print(files)
                for file in files:
                    try:
                        with Image.open("./output/"+dir+"/"+file) as f:
                            tup= f.size
                            blank_image.paste(f,(0,temp+2))
                            temp += tup[1]
                    except IOError:
                        continue
                blank_image.save("data/"+dir+".png",quality = 95)

if __name__ == "__main__":
    Transfom().main()
    Transfom().splice_image()