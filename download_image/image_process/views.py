import bs4
import requests
from requests import Response
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
from rest_framework.views import APIView
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Save_img


@csrf_exempt
def getimage(request):
    return render(request, "get_image.html")


@csrf_exempt
def processimage(request):
    if request.method == 'POST':
        files = request.FILES
        img = files.get('myImage')
        print(img.__dict__)
        if img:
            Save_img.objects.create(upload=img)
        # print(request.POST.FILES('myImage').__dict__)
        from selenium.webdriver.firefox.options import Options
        options = FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options,
                                   executable_path=r'C:\Users\Ongraph Technologies\Downloads\geckodriver-v0.31.0-win64\geckodriver.exe')

        url = "https://www.google.com/imghp?hl=en"
        driver.get(url)
        print(driver.title)
        # time.sleep(15)
        driver.maximize_window()
        # WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,'Gdd5U'))).click()
        driver.find_element(By.CLASS_NAME, 'Gdd5U').click()
        # driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[3]/div[3]/img').click()
        time.sleep(2)

        container = driver.find_element(By.NAME, 'encoded_image')
        img = Save_img.objects.first()
        container.send_keys(img.upload.path)

        time.sleep(5)
        lst = driver.find_elements(By.TAG_NAME, 'img')
        new = []
        for i in lst:
            src = i.get_attribute("src")
            if src[:5] != 'https':
                continue
            new.append(src)

        print("lent", len(new))
        for i in new:
            print(i)

        driver.close()
        img.delete()
        return HttpResponse('<h3> check console</h3>')

    # while(True):

# class Image(APIView):
#     def get(self,request):
#
#     def post(self, request):
#         image = request.data['image']
#         print(image)
