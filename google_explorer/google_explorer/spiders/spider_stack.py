import scrapy
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from scrapy.contrib.spiders import CrawlSpider
from scrapy.utils.response import open_in_browser
from scrapy.item import Item, Field
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from selenium.common.exceptions import NoSuchElementException       


class googleSpider(CrawlSpider):
 
    name = "googlish"
    allowed_domains = ["google.com"]
    start_urls = ["http://www.google.com"]
            
    def __init__(self):
        self.driver = webdriver.Firefox()
   
    def parse(self, response):
        self.driver.get(response.url)      
        login_form = self.driver.find_element_by_name('q')        
        login_form.send_keys("scrapy\n")
        time.sleep(4)
        found = False
        while not found:
            try :
                for element in self.driver.find_elements_by_xpath("//div[@class='rc']"):
                    print element.text + "\n"
   
                for i in self.driver.find_elements_by_id('pnnext'):
                    i.click()
                time.sleep(5)        
            except NoSuchElementException:
                found = True
                pass

        self.driver.close()




