from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.service import Service
from colorama import init, Fore, Style  
import time 
import os

path = "C:/Users/rayan/Desktop/selenium/driver/chromedriver-win64/chromedriver.exe"
service = Service(path)
driver = webdriver.Chrome(service=service)
driver.get('https://web.whatsapp.com/')  
input("In\nRUN??\n\n") 
init()  
os.system('cls')  
Message = input(Fore.LIGHTCYAN_EX+ 'Enter a  message: '+Fore.WHITE)
time.sleep(0.3) 
Names = input(Fore.LIGHTCYAN_EX+ 'Enter Names [& splited] : ' + Fore.WHITE).split('&') 
time.sleep(0.3)
NumberRange =int(input(Fore.LIGHTCYAN_EX+ 'Enter Number :'+Fore.WHITE))
time.sleep(0.8)  
for name in Names:
    driver.find_element(By.XPATH,f'//span[@title ="{name}"]').click()
    for number in range(NumberRange):
        driver.find_element(By.XPATH, '//div[@role="textbox" and @data-tab="10"]').send_keys(Message+ Keys.ENTER)
    else:
        print(Fore.LIGHTMAGENTA_EX + '[+] -' + Fore.RED + name)
    
    input('\n\EXIT??\n\n')
