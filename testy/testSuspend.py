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

testSuspend_path = 'testSuspend.py'

base_dir = Path(__file__).parent
chromeDriver_path = base_dir / 'chromedriver.exe'
testFavouriteBox_path = base_dir / 'testFavouriteBox.py'

service = Service(executable_path=chromeDriver_path)
driver = webdriver.Chrome(service=service)

#Cooldown wczytania nastepnego kroku
sleepTime = 0.2 #Wartość 0 moze powodowac bledy, zalecane min to 0.02 

filename = os.path.join(base_dir, "testRaport.txt")
filename2 = os.path.join(base_dir, "daneRaport.txt")
current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

with open(filename2, "r") as file:
    for line in file:
        key, value = line.strip().split("=")
        if key == "tests":
            tests = int(value)
        elif key == "success":
            success = int(value)
        elif key == "testMainEmail":
            testMainEmail = value
        elif key == "testMainPassword":
            testMainPassword = value

urlLogin = 'http://localhost:4200/login'
urlData = 'http://localhost:4200/changeUserData'
urlSuspend= 'http://localhost:4200/suspendAccount'


with open(filename, 'a') as file:
    file.write("\n\nTest Zawieszenia Konta")
    file.write("\n\nT1: Zawieszenie konta")


driver.get(urlLogin)
time.sleep(sleepTime)

#Logowanie i przejście na stronę
email_field = driver.find_element(By.NAME, 'email')
email_field.send_keys(testMainEmail)
time.sleep(sleepTime)
password_field = driver.find_element(By.NAME, 'password')
password_field.send_keys('SuperTajneHaslo123!@#')
time.sleep(sleepTime)
login_button = driver.find_element(By.XPATH, '//p-button[@label="Login"]')
login_button.click()
time.sleep(sleepTime)
driver.get(urlSuspend)
time.sleep(sleepTime)
yes_button = driver.find_element(By.XPATH, '//button[span[text()="Yes"]]')
yes_button.click()
time.sleep(sleepTime)
yes_button2 = driver.find_element(By.XPATH, "(//button[.//span[text()='Yes']])[2]")
yes_button2.click()

time.sleep(sleepTime)
time.sleep(sleepTime)

#Sprawdzenie zmiany url
if urlSuspend != driver.current_url:
    print("\033[92mZawieszenie konta poprawne.\033[0m")
    with open(filename, 'a') as file:
        file.write("\nT1:T ")
    tests+=1
    success+=1
else:
    print("\033[92mZawiesznie niepoprawne.\033[0m")
    with open(filename, 'a') as file:
        file.write("\nT1:F ")
    tests+=1

    
time.sleep(sleepTime)


#Obliczenie procentu powodzenia do calkowitej ilosci testow 
percent_success = (success / tests) * 100
print("Procent powodzenia: {:.2f}%".format(percent_success) + " " + str(success) + "/" + str(tests))

#Zapisywanie danych przygotowywanych do raportu
with open(filename2, "w") as file:
    file.write("tests=" + str(tests) + "\n")
    file.write("success=" + str(success)+ "\n")
    file.write("testMainEmail="+ str(testMainEmail)+ "\n")
    file.write("testMainPassword="+ str(testMainPassword)+ "\n")

#Zapisanie wynikow w pliku raport.txt
with open(filename, 'a') as file:
    file.write("\nProcent powodzenia: {:.2f}%".format(percent_success) + " " + str(success) + "/" + str(tests) + "\n" )
    file.write(format(formatted_datetime))


driver.quit()

subprocess.run(['python', testFavouriteBox_path], check=True)
