from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie_num = "cookies"
PPP = "productPrice"
PP = "product"

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "langSelect-EN"))
)

english = driver.find_element(By.ID, "langSelect-EN")
english.click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "bigCookie"))
)

cookie = driver.find_element(By.ID, "bigCookie")

while True:
    cookie.click()
    cookie_count = driver.find_element(By.ID, cookie_num).text.split(" ")[0]
    cookie_count = int(cookie_count.replace(",", ""))
    if cookie_count >= 80000:
        print(cookie_count)

    for i in range(10):
        ProdP = driver.find_element(By.ID, PPP + str(i)).text.replace(",","")

        if not ProdP.isdigit():
            continue

        ProdP = int(ProdP)

        if cookie_count >= ProdP:
            product = driver.find_element(By.ID, PP + str(i))
            product.click()
            break


time.sleep(10)

driver.quit