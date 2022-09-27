import bs4
import requests
from requests import Response
from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Save_img
from django.views import View
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt,name='dispatch')
class AllImages(View):
    def get(self, request):
        return render(request, "get_image.html")

    def post(self,request):
        # data = request.
        # print(data)

        files = request.FILES
        print("jdiuei",files)
        img = files.get('myImage')
        print("*************************")
        print(img)
        if img:
            Save_img.objects.create(upload=img)
        # print(request.POST.FILES('myImage').__dict__)
        
        options = FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)

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
        print("################   ",img.upload.path)
        container.send_keys(img.upload.path)

        time.sleep(5)
        lst = driver.find_elements(By.TAG_NAME, 'img')
        new = []
        for i in lst:
            src = i.get_attribute("src")
            if src[:5] != 'https':
                continue
            new.append(src)
        if len(new)==1:
            print("In if condition ++++++++++++++++")
            time.sleep(2)
            lst = driver.find_elements(By.TAG_NAME, 'img')
            for i in lst:
                src = i.get_attribute("src")
                if src[:5] != 'https':
                    continue
                new.append(src)
        print("lent", len(new))
        for i in new:
            print(i)
        
        img.delete()

        driver.close()
        
        return JsonResponse({'data':new})


# @csrf_exempt
# def getimage(request):
#     return render(request, "get_image.html")


# @csrf_exempt
# def processimage(request):
#     if request.method == 'POST':
#         files = request.FILES
#         img = files.get('myImage')
#         print(img.__dict__)
#         if img:
#             Save_img.objects.create(upload=img)
#         # print(request.POST.FILES('myImage').__dict__)
#         from selenium.webdriver.firefox.options import Options
#         options = FirefoxOptions()
#         options.add_argument("--headless")
#         driver = webdriver.Firefox(options=options)

#         url = "https://www.google.com/imghp?hl=en"
#         driver.get(url)
#         print(driver.title)
#         # time.sleep(15)
#         driver.maximize_window()
#         # WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,'Gdd5U'))).click()
#         driver.find_element(By.CLASS_NAME, 'Gdd5U').click()
#         # driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[3]/div[3]/img').click()
#         time.sleep(2)

#         container = driver.find_element(By.NAME, 'encoded_image')
#         img = Save_img.objects.first()
#         container.send_keys(img.upload.path)

#         time.sleep(5)
#         lst = driver.find_elements(By.TAG_NAME, 'img')
#         new = []
#         for i in lst:
#             src = i.get_attribute("src")
#             if src[:5] != 'https':
#                 continue
#             new.append(src)

#         print("lent", len(new))
#         for i in new:
#             print(i)

#         driver.close()
#         img.delete()
#         return JsonResponse({'data':new})

#     # while(True):

# # class Image(APIView):
# #     def get(self,request):
# #
# #     def post(self, request):
# #         image = request.data['image']
# #         print(image)
