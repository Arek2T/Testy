from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import subprocess
from datetime import datetime
from pathlib import Path
import os


base_dir = Path(__file__).parent
chromeDriver_path = base_dir / 'chromedriver.exe'

service = Service(executable_path=chromeDriver_path)
driver = webdriver.Chrome(service=service)

#Cooldown wczytania nastepnego kroku
sleepTime = 0.2 #Wartość 0 moze powodowac bledy, zalecane min to 0.02 

urlLogin = 'http://localhost:4200/login'
urlData = 'http://localhost:4200/changeUserData'
driver.get(urlLogin)
time.sleep(sleepTime)

#Logowanie i przejście na stronę
email_field = driver.find_element(By.NAME, 'email')
email_field.send_keys('krzysztof.duda@example.com')
time.sleep(sleepTime)
password_field = driver.find_element(By.NAME, 'password')
password_field.send_keys('SuperTajneHaslo123!@#')
time.sleep(sleepTime)
login_button = driver.find_element(By.XPATH, '//p-button[@label="Login"]')
login_button.click()
time.sleep(sleepTime)
driver.get(urlData)
time.sleep(sleepTime)

#Wpisanie wartości do pola hasło
passw_field = driver.find_element(By.NAME, 'Password')
passw_field.clear()
time.sleep(sleepTime)
passw = "Qwerty12#$"
passw_field.send_keys(passw)
time.sleep(sleepTime)

#Znalezienie i nacisniecie przycisku Edit 
edit_button = driver.find_element(By.XPATH, '//p-button[@label="Edit"]')
edit_button.click()
time.sleep(sleepTime)
print("hasło zresetowane do Qwerty12#$")