import bs4
import requests
from selenium import webdriver
import os
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options as FirefoxOptions

# option = webdriver.ChromeOptions()
# option.add_argument('--headless')
# option.add_argument('--start-maximized')
# option.add_argument('--window-size=1366,768')


# option = Options()
# option.headless = True
#ChromeDriverManager().install()
# driver = webdriver.Chrome(options=option)
options = FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)

url = "https://www.google.com/imghp?hl=en"
driver.get(url)
print(driver.title)
# time.sleep(15)
driver.maximize_window()
# WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,'Gdd5U'))).click()
driver.find_element(By.CLASS_NAME,'Gdd5U').click()
# driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[3]/div[3]/img').click()
time.sleep(2)

container = driver.find_element(By.NAME,'encoded_image')

container.send_keys("/home/ongraph/Desktop/new/static/input1/ffd4f6b1-cdb8-46d9-b54e-be248c448704.Jpeg")

time.sleep(5)
lst = driver.find_elements(By.TAG_NAME,'img')
new = []
for i in lst:
    src = i.get_attribute("src")
    if src[:5]!='https':
        continue
    new.append(src)

print("lent",len(new))
for i in new:
    print(i)

driver.close()


# while(True):
#     pass

