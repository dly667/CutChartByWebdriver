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
        
        for root, dirs, files in os.walk("./",topdown=True):  
            
            break
        # a = os.walk("./",topdown=True)[0]
        # print(a)
        # print(dirs)  

        url_list = []
        dir_list = []
        for dir in dirs:
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
                    pass
                    self.save_one(url+"/../"+html_data[i],dir_list[flag],html_text[i])
            flag += 1   
    def save_one(self,url,dir,filename):
        pass
        #chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-infobars')
        chrome_options.add_argument('--start-maximized')
        
        # chrome_options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        driver=webdriver.Chrome(chrome_options=chrome_options)
       
        driver.get("file:///home/dly667/python/CutChartByWebdriver/"+url)
        #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL, '-')
        driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL, '-')
        driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL, '-')
        driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL, '-')
        util.fullpage_screenshot(driver, filename+".png",dir)
        driver.close()
        driver.quit()
    def splice_image(self):
       
        for root, dirs, files in os.walk("./output",topdown=True):  
            
            break
        for dir in dirs:
            total_width = 0
            total_height = 0
            f_list = []

            for root, dirs, files in os.walk("./output/"+dir,topdown=True):
                # print(files)
                for file in files:
                    with Image.open("./output/"+dir+"/"+file) as f:
                        f_list.append(f)
                        tup = f.size
                        if tup[0] >total_width:
                            total_width = tup[0]
                        total_height += tup[1]
                        # img.paste(img,(100,100),None)
                        # img = Image.new('RGB',(total_width, total_height))
                print(total_height,total_width)
            blank_image = Image.new("RGB",(1885, total_height))
            temp = 0
            
            for root, dirs, files in os.walk("./output/"+dir,topdown=True):
                # print(files)
                for file in files:
                    with Image.open("./output/"+dir+"/"+file) as f:
                        tup= f.size
                        blank_image.paste(f,(0,temp+2))
                        temp = tup[1]
                    break
                blank_image.save("data/"+file,quality = 95)

if __name__ == "__main__":
    # Transfom().splice_image()
    Transfom().main()