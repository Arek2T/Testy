from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import subprocess
from datetime import datetime
from pathlib import Path
import os

base_dir = Path(__file__).parent
testChangeData_path = base_dir / 'testChangeData.py'
chromeDriver_path = base_dir / 'chromedriver.exe'

#testRegister_path = 'testy/testRegister.py'

service = Service(executable_path=chromeDriver_path)
driver = webdriver.Chrome(service=service)

#Cooldown wczytania nastepnego kroku
sleepTime = 0.2 #Wartość 0 moze powodowac bledy, zalecane min to 0.02 

#filename = "testRaport.txt"
#filename2 = "daneRaport.txt"

filename = os.path.join(base_dir, "testRaport.txt")
filename2 = os.path.join(base_dir, "daneRaport.txt")

current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
urlLogin = 'http://localhost:4200/login'
driver.get(urlLogin)
time.sleep(sleepTime)

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


with open(filename, 'a') as file:
    file.write("\n\nTest Logowanie")
    file.write("\n\nT1: Logowanie poprawne, T2: Niepoprawny email, T3: Niepoprawne haslo")

#########################################################################################################################################################################################################################################################

#Logowanie poprawne

#Wpisanie wartości do pola email
email_field = driver.find_element(By.NAME, 'email')
email_field.send_keys(testMainEmail)
time.sleep(sleepTime)

#Wpisanie wartości do pola haslo
password_field = driver.find_element(By.NAME, 'password')
password_field.send_keys(testMainPassword)
time.sleep(sleepTime)

#Znalezienie i nacisniecie przycisku login 
login_button = driver.find_element(By.XPATH, '//p-button[@label="Login"]')
login_button.click()
time.sleep(sleepTime)

#Sprawdzenie zmiany url
if urlLogin != driver.current_url:
    print("\033[92mLogowanie poprawne.\033[0m")
    with open(filename, 'a') as file:
        file.write("\nT1:T, ")
    success+=1
    tests+=1
else:
    print("\033[91mLogowanie niepoprawne.\033[0m")
    with open(filename, 'a') as file:
        file.write("\nT1:F, ")
    tests+=1


#Powrot na strone logowania
driver.get(urlLogin)
time.sleep(sleepTime)

#########################################################################################################################################################################################################################################################

#Logowanie niepoprawne: złe hasło

#Wpisanie wartości do pola email
email_field = driver.find_element(By.NAME, 'email')
email_field.send_keys('zly.email@example.com')
time.sleep(sleepTime)

#Wpisanie wartości do pola haslo
password_field = driver.find_element(By.NAME, 'password')
password_field.send_keys('Qwerty12#$')
time.sleep(sleepTime)

#Znalezienie i nacisniecie przycisku login 
login_button = driver.find_element(By.XPATH, '//p-button[@label="Login"]')
login_button.click()
time.sleep(sleepTime)

#Sprawdzenie zmiany url
if urlLogin != driver.current_url:
    print("\033[91mZłe hasło.\033[0m")
    with open(filename, 'a') as file:
        file.write("T2:F, ")
    tests+=1
else:
    print("\033[92mZłe hasło.\033[0m")
    with open(filename, 'a') as file:
        file.write("T1:T, ")
    success+=1
    tests+=1

#Powrot na strone logowania
driver.get(urlLogin)
time.sleep(sleepTime)

#########################################################################################################################################################################################################################################################

#Logowanie niepoprawne: zły email

#Wpisanie wartości do pola email
email_field = driver.find_element(By.NAME, 'email')
email_field.send_keys('krzysztof.duda@example.com')
time.sleep(sleepTime)

#Wpisanie wartości do pola haslo
password_field = driver.find_element(By.NAME, 'password')
password_field.send_keys('zlehaslo')
time.sleep(sleepTime)

#Znalezienie i nacisniecie przycisku login 
login_button = driver.find_element(By.XPATH, '//p-button[@label="Login"]')
login_button.click()
time.sleep(sleepTime)

#Sprawdzenie zmiany url
if urlLogin != driver.current_url:
    print("\033[91mZły email.\033[0m")
    with open(filename, 'a') as file:
        file.write("T3:F ")
    tests+=1
else:
    print("\033[92mZły email.\033[0m")
    with open(filename, 'a') as file:
        file.write("T3:T ")
    success+=1
    tests+=1


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

#Uruchomienie kolejnego skryptu do testowania
#subprocess.run(['python', testRegister_path])
subprocess.run(['python', testChangeData_path], check=True)



# for _ in range(500):
#     login_button.click()
#     time.sleep(0.5)  

# Zamknij przeglądarkę
# driver.quit()