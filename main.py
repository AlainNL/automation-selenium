import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to your chromedriver
service = Service(executable_path="./chromedriver")

# Initialize the WebDriver
driver = webdriver.Chrome(service=service)

try:

    driver.get("https://google.com")


    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[text()='Tout accepter']"))
    ).click()


    input_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "q"))
    )


    input_element.send_keys("tech with tim")


    input_element.submit()


    time.sleep(10)

except Exception as e:
    print("An error occurred:", e)

finally:

    driver.quit()
