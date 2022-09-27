
from flask import Flask,request,render_template,jsonify
import os
import time
import bs4
import requests
from requests import Response
from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions

#/home/ongraph/Desktop/googl/download_image/media/uploads/Yael-Shelbia-846x1024_1.webp
app = Flask(__name__, static_url_path="/static", static_folder="static")
app.config['UPLOAD_FOLDER'] = os.path.abspath(os.getcwd())+"/static/media"
updir = app.config["UPLOAD_FOLDER"]

@app.route('/image', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        img = request.files.get('myImage', '')
        print("jdiuei",img.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], img.filename)
        img.save(path)
        print("*************************",path)
        print(path)
        # if img:
        #     Save_img.objects.create(upload=img)
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
        # img = Save_img.objects.first()
        container.send_keys(path)

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
        
        # img.delete()

        driver.close()

        return jsonify({"data":new})

    return render_template("get_image.html")


if __name__ == "__main__":
    app.run(debug=True)