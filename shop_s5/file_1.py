from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def shop(x):
    service = Service('C:/Users/rayan/Desktop/selenium/driver/chromedriver-win64/chromedriver.exe')  
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        driver.get(f"https://torob.com/search/?query={x}")
        wait = WebDriverWait(driver, 10)
        search_input = wait.until(EC.presence_of_element_located((By.ID, "search-query-input")))
        search_input.clear()
        search_input.send_keys(x)
        
        search_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "searchbox_searchBtnHome__T5Vic")))
        search_button.click()
        
        
        time.sleep(5)
        print(f"Search for '{x}' completed successfully!")
    except TimeoutException as e:
        print(f"Error occurred: {e}")
    finally:
        driver.quit()

