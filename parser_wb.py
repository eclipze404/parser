import time
import datetime
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.FirefoxOptions()
ua = UserAgent().random
options.add_argument(f'user-agent={ua}')
options.add_argument("--log-level=3")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('--headless')


def pars_wb(product):
    with webdriver.Firefox(options=options) as browser:
        

        #product
        browser.get(f'https://www.wildberries.ru/catalog/0/search.aspx?search={product}')

        #result
        result_data = []

        # find all items with class 'product-card'
        WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'product-card'))
            )
        
        products = browser.find_elements(By.CLASS_NAME, 'product-card')
        for product in products:
            link = product.find_element(By.CLASS_NAME,'product-card__link')
            link_name = link.get_attribute('href')
            
            article = (product.get_attribute('id')).split('c')[1]

            name =  product.find_element(By.CLASS_NAME,'j-card-link')
            name_name = name.get_attribute('aria-label')

            price_element = product.find_element(By.CLASS_NAME, 'price__lower-price')
            price_element = price_element.text

            result_data.append({'link': link_name,
                                'name': name_name,
                                'article_num': article,
                                'price': price_element
                                })
            
        with open('result.json','w',encoding='utf-8') as file:
            json.dump(result_data,file,indent=4,ensure_ascii=False)
        print('Done!')

product = input('Write the name of the product: ')
pars_wb(product)


