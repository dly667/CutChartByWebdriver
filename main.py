from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import util
import os
import time
from lxml import etree
chrome_options = Options()

class Transfom():

    def main(self):
        
        for root, dirs, files in os.walk("./",topdown=True):  
            
            break
        # a = os.walk("./",topdown=True)[0]
        # print(a)
        # print(dirs)  
        url_list = []
        for dir in dirs:
            url = os.path.join(dir, "report.html")
            if os.path.exists(url):
                url_list.append('./'+url)
                # url_list = append(url_list,url)

            
        for url in url_list:
            with open(url, 'r', encoding='utf-8') as f:
                # print(f.read())
                html = etree.HTML(f.read())
                html_data = html.xpath('//*[@id="menuItem0"]/@href')
                html_text = html.xpath('//*[@id="menuItem0"]/text()')
                # print(html)
                for i in range(len(html_data)):
                  
                    print(url+"/../"+html_data[i])
                    # self.save_one(url+"/../"+html_data[i],"",html_text[i])
               
            # save_one(url)
    def save_one(self,url,dir,filename):
        pass
        #chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-infobars')
        chrome_options.add_argument('--start-maximized')
        
        # chrome_options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        driver=webdriver.Chrome(chrome_options=chrome_options)
        driver.get("file:///home/dai/python/htmltopdf/report%20new/"+url)
        #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
       
        util.fullpage_screenshot(driver, filename+".png")
        driver.close()
        driver.quit()
if __name__ == "__main__":
    Transfom().main()