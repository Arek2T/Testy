from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from datetime import datetime
from faker import Faker
from selenium.webdriver.common.keys import Keys
from pathlib import Path
import os
import subprocess


base_dir = Path(__file__).parent
chromeDriver_path = base_dir / 'chromedriver.exe'
testLogin_path = base_dir / 'testLogin.py'

service = Service(executable_path=chromeDriver_path)
driver = webdriver.Chrome(service=service)


#Cooldown wczytania nastepnego kroku
sleepTime = 0.2 #Wartość 0 moze powodowac bledy, zalecane min to 0.02 

filename = os.path.join(base_dir, "testRaport.txt")
filename2 = os.path.join(base_dir, "daneRaport.txt")
success=0
tests=0
fake = Faker()
current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")




urlLogin = 'http://localhost:4200/login'
urlRegister = 'http://localhost:4200/register'
driver.get(urlLogin)

with open(filename, 'a') as file:
    file.write("\n\nTest Rejestracja")
    file.write("\n\nT1: Rejestrowanie poprawne, T2: Niepoprawny email, T3: Brak hasla, T4: Brak imienia, T5: Brak nazwiska, T6: Brak daty urodzenia,\nT7: Brak adresu, T8: Brak kodu pocztowego, T9:Brak lokacji, T10: Brak telefonu, T11: Email zajety")

#Nacisniecie guzika Register
register_button = driver.find_element(By.CSS_SELECTOR, 'a[routerlink="/register"]')
register_button.click()
time.sleep(sleepTime)

#########################################################################################################################################################################################################################################################

#Rejestracja poprawna

#Wpisanie wartości do pola email
random_email = "test" + fake.user_name() + "@test.com"
email_field = driver.find_element(By.NAME, 'Mail')
email_field.send_keys(random_email)
time.sleep(sleepTime)

#Wpisanie wartości do pola haslo
random_password = "test" + fake.password()
password_field = driver.find_element(By.NAME, 'Password')
password_field.send_keys(random_password)
time.sleep(sleepTime)

#Wpisanie wartości do pola first name
random_name = "test" + fake.first_name()
firstName_field = driver.find_element(By.NAME, 'FirstName')
firstName_field.send_keys(random_name)
time.sleep(sleepTime)

#Wpisanie wartości do pola last name
random_Lastname = "test" + fake.last_name()
lastName_field = driver.find_element(By.NAME, 'LastName')
lastName_field.send_keys(random_Lastname)
time.sleep(sleepTime)

#Wybranie dany urodzenia
date_input = driver.find_element(By.XPATH, '//input[@type="date"]')
date_input.click()
date_input.send_keys(Keys.SPACE)
date_input.send_keys(Keys.ENTER)

time.sleep(sleepTime)

#Wybranie plci
sex_input = driver.find_element(By.NAME, 'Sex')
sex_input.click()
sex_input.send_keys(Keys.ARROW_DOWN)
sex_input.send_keys(Keys.ENTER)
time.sleep(sleepTime)

#Wpisanie wartości do pola default address
random_address = "test" #+ fake.address() #z jakiegos powodu selenium ma problemy z adresem i miastem. Mimo że generuje i akceptuje to po nacisnieciu register wyskakuje Registration error
defaultAddress_field = driver.find_element(By.NAME, 'DefaultAddress')
defaultAddress_field.send_keys(random_address)
time.sleep(sleepTime)

#Wpisanie wartości do pola postal code
random_postalCode = "test" + fake.postalcode()
defaultPostalCode_field = driver.find_element(By.NAME, 'DefaultPostalcode')
defaultPostalCode_field.send_keys(random_postalCode)
time.sleep(sleepTime)

#Wpisanie wartości do pola default location
random_location= "test" #+ fake.city()
defaultLocation_field = driver.find_element(By.NAME, 'DefaultLocation')
defaultLocation_field.send_keys(random_location)
time.sleep(sleepTime)

#Wpisanie wartości do pola phone
random_phone= "test" + fake.phone_number()
phone_field = driver.find_element(By.NAME, 'Phone')
phone_field.send_keys(random_phone)
time.sleep(sleepTime)

#Znalezienie i nacisniecie przycisku register 
register_button = driver.find_element(By.XPATH, '//p-button[@label="Register"]')
register_button.click()
time.sleep(sleepTime)
time.sleep(sleepTime)
time.sleep(sleepTime)


#Sprawdzenie zmiany url
if urlRegister != driver.current_url:
    print("\033[92mRejestrowanie poprawne.\033[0m")
    with open(filename, 'a') as file:
        file.write("\nT1:T, ")
    tests+=1
    success+=1
else:
    print("\033[91mRejestrowanie niepoprawne.\033[0m")
    with open(filename, 'a') as file:
        file.write("\nT1:F, ")
    tests+=1


#Powrot na strone rejestrowania
driver.get(urlRegister)
time.sleep(sleepTime)

#########################################################################################################################################################################################################################################################

#Rejestracja niepoprawna: zly email

#Wpisanie wartości do pola email
random_email = "test" + fake.user_name() 
email_field = driver.find_element(By.NAME, 'Mail')
email_field.send_keys(random_email)
time.sleep(sleepTime)

#Wpisanie wartości do pola haslo
random_password = "test" + fake.password()
password_field = driver.find_element(By.NAME, 'Password')
password_field.send_keys(random_password)
time.sleep(sleepTime)

#Wpisanie wartości do pola first name
random_name = "test" + fake.first_name()
firstName_field = driver.find_element(By.NAME, 'FirstName')
firstName_field.send_keys(random_name)
time.sleep(sleepTime)

#Wpisanie wartości do pola last name
random_Lastname = "test" + fake.last_name()
lastName_field = driver.find_element(By.NAME, 'LastName')
lastName_field.send_keys(random_Lastname)
time.sleep(sleepTime)

#Wybranie dany urodzenia
date_input = driver.find_element(By.XPATH, '//input[@type="date"]')
date_input.click()
date_input.send_keys(Keys.SPACE)
date_input.send_keys(Keys.ENTER)
time.sleep(sleepTime)

#Wybranie plci
sex_input = driver.find_element(By.NAME, 'Sex')
sex_input.click()
sex_input.send_keys(Keys.ARROW_DOWN)
sex_input.send_keys(Keys.ENTER)
time.sleep(sleepTime)

#Wpisanie wartości do pola default address
random_address = "test" + fake.last_name()#+ fake.address() #z jakiegos powodu selenium ma problemy z adresem i miastem. Mimo że generuje i akceptuje to po nacisnieciu register wyskakuje Registration error
defaultAddress_field = driver.find_element(By.NAME, 'DefaultAddress')
defaultAddress_field.send_keys(random_address)
time.sleep(sleepTime)

#Wpisanie wartości do pola postal code
random_postalCode = "test" + fake.postalcode()
defaultPostalCode_field = driver.find_element(By.NAME, 'DefaultPostalcode')
defaultPostalCode_field.send_keys(random_postalCode)
time.sleep(sleepTime)

#Wpisanie wartości do pola default location
random_location= "test" + fake.last_name()#+ fake.city()
defaultLocation_field = driver.find_element(By.NAME, 'DefaultLocation')
defaultLocation_field.send_keys(random_location)
time.sleep(sleepTime)

#Wpisanie wartości do pola phone
random_phone= "test" + fake.phone_number()
phone_field = driver.find_element(By.NAME, 'Phone')
phone_field.send_keys(random_phone)
time.sleep(sleepTime)
time.sleep(sleepTime)

# #Znalezienie i nacisniecie przycisku register 
# register_button2 = driver.find_element(By.XPATH, '//p-button[@label="Register"]')
# register_button2.click()
# time.sleep(sleepTime)
# time.sleep(sleepTime)

#Sprawdzenie zmiany url
if urlRegister != driver.current_url:
    print("\033[91mZły email.\033[0m")
    with open(filename, 'a') as file:
        file.write("T2:F, ")
    tests+=1
else:
    print("\033[92mZły email.\033[0m")
    with open(filename, 'a') as file:
        file.write("T2:T, ")
    tests+=1
    success+=1


#Powrot na strone rejestrowania
driver.get(urlRegister)
time.sleep(sleepTime)

#########################################################################################################################################################################################################################################################

#Rejestracja niepoprawna: brak hasla

#Wpisanie wartości do pola email
random_email = "test" + fake.user_name() + "@test.com"
email_field = driver.find_element(By.NAME, 'Mail')
email_field.send_keys(random_email)
time.sleep(sleepTime)

#Wpisanie wartości do pola haslo
random_password = ""
password_field = driver.find_element(By.NAME, 'Password')
password_field.send_keys(random_password)
time.sleep(sleepTime)

#Wpisanie wartości do pola first name
random_name = "test" + fake.first_name()
firstName_field = driver.find_element(By.NAME, 'FirstName')
firstName_field.send_keys(random_name)
time.sleep(sleepTime)

#Wpisanie wartości do pola last name
random_Lastname = "test" + fake.last_name()
lastName_field = driver.find_element(By.NAME, 'LastName')
lastName_field.send_keys(random_Lastname)
time.sleep(sleepTime)

#Wybranie dany urodzenia
date_input = driver.find_element(By.XPATH, '//input[@type="date"]')
date_input.click()
date_input.send_keys(Keys.SPACE)
date_input.send_keys(Keys.ENTER)
time.sleep(sleepTime)

#Wybranie plci
sex_input = driver.find_element(By.NAME, 'Sex')
sex_input.click()
sex_input.send_keys(Keys.ARROW_DOWN)
sex_input.send_keys(Keys.ENTER)
time.sleep(sleepTime)

#Wpisanie wartości do pola default address
random_address = "test" + fake.last_name()#+ fake.address() #z jakiegos powodu selenium ma problemy z adresem i miastem. Mimo że generuje i akceptuje to po nacisnieciu register wyskakuje Registration error
defaultAddress_field = driver.find_element(By.NAME, 'DefaultAddress')
defaultAddress_field.send_keys(random_address)
time.sleep(sleepTime)

#Wpisanie wartości do pola postal code
random_postalCode = "test" + fake.postalcode()
defaultPostalCode_field = driver.find_element(By.NAME, 'DefaultPostalcode')
defaultPostalCode_field.send_keys(random_postalCode)
time.sleep(sleepTime)

#Wpisanie wartości do pola default location
random_location= "test" + fake.last_name()#+ fake.city()
defaultLocation_field = driver.find_element(By.NAME, 'DefaultLocation')
defaultLocation_field.send_keys(random_location)
time.sleep(sleepTime)

#Wpisanie wartości do pola phone
random_phone= "test" + fake.phone_number()
phone_field = driver.find_element(By.NAME, 'Phone')
phone_field.send_keys(random_phone)
time.sleep(sleepTime)
time.sleep(sleepTime)

#Sprawdzenie zmiany url
if urlRegister != driver.current_url:
    print("\033[91mBrak hasła.\033[0m")
    with open(filename, 'a') as file:
        file.write("T3:F, ")
    tests+=1
else:
    print("\033[92mBrak hasła.\033[0m")
    with open(filename, 'a') as file:
        file.write("T3:T, ")
    tests+=1
    success+=1


#Powrot na strone rejestrowania
driver.get(urlRegister)
time.sleep(sleepTime)

#########################################################################################################################################################################################################################################################

#Rejestracja niepoprawna: brak imienia

#Wpisanie wartości do pola email
random_email = "test" + fake.user_name() + "@test.com"
email_field = driver.find_element(By.NAME, 'Mail')
email_field.send_keys(random_email)
time.sleep(sleepTime)

#Wpisanie wartości do pola haslo
random_password = "test" + fake.password()
password_field = driver.find_element(By.NAME, 'Password')
password_field.send_keys(random_password)
time.sleep(sleepTime)

#Wpisanie wartości do pola first name
random_name = "" #+ fake.first_name()
firstName_field = driver.find_element(By.NAME, 'FirstName')
firstName_field.send_keys(random_name)
time.sleep(sleepTime)

#Wpisanie wartości do pola last name
random_Lastname = "test" + fake.last_name()
lastName_field = driver.find_element(By.NAME, 'LastName')
lastName_field.send_keys(random_Lastname)
time.sleep(sleepTime)

#Wybranie dany urodzenia
date_input = driver.find_element(By.XPATH, '//input[@type="date"]')
date_input.click()
date_input.send_keys(Keys.SPACE)
date_input.send_keys(Keys.ENTER)
time.sleep(sleepTime)

#Wybranie plci
sex_input = driver.find_element(By.NAME, 'Sex')
sex_input.click()
sex_input.send_keys(Keys.ARROW_DOWN)
sex_input.send_keys(Keys.ENTER)
time.sleep(sleepTime)

#Wpisanie wartości do pola default address
random_address = "test" + fake.last_name()#+ fake.address() #z jakiegos powodu selenium ma problemy z adresem i miastem. Mimo że generuje i akceptuje to po nacisnieciu register wyskakuje Registration error
defaultAddress_field = driver.find_element(By.NAME, 'DefaultAddress')
defaultAddress_field.send_keys(random_address)
time.sleep(sleepTime)

#Wpisanie wartości do pola postal code
random_postalCode = "test" + fake.postalcode()
defaultPostalCode_field = driver.find_element(By.NAME, 'DefaultPostalcode')
defaultPostalCode_field.send_keys(random_postalCode)
time.sleep(sleepTime)

#Wpisanie wartości do pola default location
random_location= "test" + fake.last_name()#+ fake.city()
defaultLocation_field = driver.find_element(By.NAME, 'DefaultLocation')
defaultLocation_field.send_keys(random_location)
time.sleep(sleepTime)

#Wpisanie wartości do pola phone
random_phone= "test" + fake.phone_number()
phone_field = driver.find_element(By.NAME, 'Phone')
phone_field.send_keys(random_phone)
time.sleep(sleepTime)
time.sleep(sleepTime)


#Sprawdzenie zmiany url
if urlRegister != driver.current_url:
    print("\033[91mBrak imienia.\033[0m")
    with open(filename, 'a') as file:
        file.write("T4:F, ")
    tests+=1
else:
    print("\033[92mBrak imienia.\033[0m")
    with open(filename, 'a') as file:
        file.write("T4:T, ")
    tests+=1
    success+=1

#Powrot na strone rejestrowania
driver.get(urlRegister)
time.sleep(sleepTime)

#########################################################################################################################################################################################################################################################

#Rejestracja niepoprawna: brak nazwiska

#Wpisanie wartości do pola email
random_email = "test" + fake.user_name() + "@test.com"
email_field = driver.find_element(By.NAME, 'Mail')
email_field.send_keys(random_email)
time.sleep(sleepTime)

#Wpisanie wartości do pola haslo
random_password = "test" + fake.password()
password_field = driver.find_element(By.NAME, 'Password')
password_field.send_keys(random_password)
time.sleep(sleepTime)

#Wpisanie wartości do pola first name
random_name = "test" + fake.first_name()
firstName_field = driver.find_element(By.NAME, 'FirstName')
firstName_field.send_keys(random_name)
time.sleep(sleepTime)

#Wpisanie wartości do pola last name
random_Lastname = "" #+ fake.last_name()
lastName_field = driver.find_element(By.NAME, 'LastName')
lastName_field.send_keys(random_Lastname)
time.sleep(sleepTime)

#Wybranie dany urodzenia
date_input = driver.find_element(By.XPATH, '//input[@type="date"]')
date_input.click()
date_input.send_keys(Keys.SPACE)
date_input.send_keys(Keys.ENTER)
time.sleep(sleepTime)

#Wybranie plci
sex_input = driver.find_element(By.NAME, 'Sex')
sex_input.click()
sex_input.send_keys(Keys.ARROW_DOWN)
sex_input.send_keys(Keys.ENTER)
time.sleep(sleepTime)

#Wpisanie wartości do pola default address
random_address = "test" + fake.last_name()#+ fake.address() #z jakiegos powodu selenium ma problemy z adresem i miastem. Mimo że generuje i akceptuje to po nacisnieciu register wyskakuje Registration error
defaultAddress_field = driver.find_element(By.NAME, 'DefaultAddress')
defaultAddress_field.send_keys(random_address)
time.sleep(sleepTime)

#Wpisanie wartości do pola postal code
random_postalCode = "test" + fake.postalcode()
defaultPostalCode_field = driver.find_element(By.NAME, 'DefaultPostalcode')
defaultPostalCode_field.send_keys(random_postalCode)
time.sleep(sleepTime)

#Wpisanie wartości do pola default location
random_location= "test" + fake.last_name()#+ fake.city()
defaultLocation_field = driver.find_element(By.NAME, 'DefaultLocation')
defaultLocation_field.send_keys(random_location)
time.sleep(sleepTime)

#Wpisanie wartości do pola phone
random_phone= "test" + fake.phone_number()
phone_field = driver.find_element(By.NAME, 'Phone')
phone_field.send_keys(random_phone)
time.sleep(sleepTime)
time.sleep(sleepTime)


#Sprawdzenie zmiany url
if urlRegister != driver.current_url:
    print("\033[91mBrak nazwiska.\033[0m")
    with open(filename, 'a') as file:
        file.write("T5:F, ")
    tests+=1
else:
    print("\033[92mBrak nazwiska.\033[0m")
    with open(filename, 'a') as file:
        file.write("T5:T, ")
    tests+=1
    success+=1

#Powrot na strone rejestrowania
driver.get(urlRegister)
time.sleep(sleepTime)

#########################################################################################################################################################################################################################################################

#Rejestracja niepoprawna: brak daty urodzenia

#Wpisanie wartości do pola email
random_email = "test" + fake.user_name() + "@test.com"
email_field = driver.find_element(By.NAME, 'Mail')
email_field.send_keys(random_email)
time.sleep(sleepTime)

#Wpisanie wartości do pola haslo
random_password = "test" + fake.password()
password_field = driver.find_element(By.NAME, 'Password')
password_field.send_keys(random_password)
time.sleep(sleepTime)

#Wpisanie wartości do pola first name
random_name = "test" + fake.first_name()
firstName_field = driver.find_element(By.NAME, 'FirstName')
firstName_field.send_keys(random_name)
time.sleep(sleepTime)

#Wpisanie wartości do pola last name
random_Lastname = "test" + fake.last_name()
lastName_field = driver.find_element(By.NAME, 'LastName')
lastName_field.send_keys(random_Lastname)
time.sleep(sleepTime)

# #Wybranie dany urodzenia
# date_input = driver.find_element(By.XPATH, '//input[@type="date"]')
# date_input.click()
# date_input.send_keys(Keys.SPACE)
# date_input.send_keys(Keys.ENTER)
# time.sleep(sleepTime)

#Wybranie plci
sex_input = driver.find_element(By.NAME, 'Sex')
sex_input.click()
sex_input.send_keys(Keys.ARROW_DOWN)
sex_input.send_keys(Keys.ENTER)
time.sleep(sleepTime)

#Wpisanie wartości do pola default address
random_address = "test" + fake.last_name()#+ fake.address() #z jakiegos powodu selenium ma problemy z adresem i miastem. Mimo że generuje i akceptuje to po nacisnieciu register wyskakuje Registration error
defaultAddress_field = driver.find_element(By.NAME, 'DefaultAddress')
defaultAddress_field.send_keys(random_address)
time.sleep(sleepTime)

#Wpisanie wartości do pola postal code
random_postalCode = "test" + fake.postalcode()
defaultPostalCode_field = driver.find_element(By.NAME, 'DefaultPostalcode')
defaultPostalCode_field.send_keys(random_postalCode)
time.sleep(sleepTime)

#Wpisanie wartości do pola default location
random_location= "test" + fake.last_name()#+ fake.city()
defaultLocation_field = driver.find_element(By.NAME, 'DefaultLocation')
defaultLocation_field.send_keys(random_location)
time.sleep(sleepTime)

#Wpisanie wartości do pola phone
random_phone= "test" + fake.phone_number()
phone_field = driver.find_element(By.NAME, 'Phone')
phone_field.send_keys(random_phone)
time.sleep(sleepTime)
time.sleep(sleepTime)


#Sprawdzenie zmiany url
if urlRegister != driver.current_url:
    print("\033[91mBrak daty urodzenia.\033[0m")
    with open(filename, 'a') as file:
        file.write("T6:F, ")
    tests+=1
else:
    print("\033[92mBrak daty urodzenia.\033[0m")
    with open(filename, 'a') as file:
        file.write("T6:T, ")
    tests+=1
    success+=1

#Powrot na strone rejestrowania
driver.get(urlRegister)
time.sleep(sleepTime)

#########################################################################################################################################################################################################################################################

#Rejestracja niepoprawna: brak adresu

#Wpisanie wartości do pola email
random_email = "test" + fake.user_name() + "@test.com"
email_field = driver.find_element(By.NAME, 'Mail')
email_field.send_keys(random_email)
time.sleep(sleepTime)

#Wpisanie wartości do pola haslo
random_password = "test" + fake.password()
password_field = driver.find_element(By.NAME, 'Password')
password_field.send_keys(random_password)
time.sleep(sleepTime)

#Wpisanie wartości do pola first name
random_name = "test" + fake.first_name()
firstName_field = driver.find_element(By.NAME, 'FirstName')
firstName_field.send_keys(random_name)
time.sleep(sleepTime)

#Wpisanie wartości do pola last name
random_Lastname = "test" + fake.last_name()
lastName_field = driver.find_element(By.NAME, 'LastName')
lastName_field.send_keys(random_Lastname)
time.sleep(sleepTime)

#Wybranie dany urodzenia
date_input = driver.find_element(By.XPATH, '//input[@type="date"]')
date_input.click()
date_input.send_keys(Keys.SPACE)
date_input.send_keys(Keys.ENTER)
time.sleep(sleepTime)

#Wybranie plci
sex_input = driver.find_element(By.NAME, 'Sex')
sex_input.click()
sex_input.send_keys(Keys.ARROW_DOWN)
sex_input.send_keys(Keys.ENTER)
time.sleep(sleepTime)

#Wpisanie wartości do pola default address
random_address = "" #+ fake.last_name()#+ fake.address() #z jakiegos powodu selenium ma problemy z adresem i miastem. Mimo że generuje i akceptuje to po nacisnieciu register wyskakuje Registration error
defaultAddress_field = driver.find_element(By.NAME, 'DefaultAddress')
defaultAddress_field.send_keys(random_address)
time.sleep(sleepTime)

#Wpisanie wartości do pola postal code
random_postalCode = "test" + fake.postalcode()
defaultPostalCode_field = driver.find_element(By.NAME, 'DefaultPostalcode')
defaultPostalCode_field.send_keys(random_postalCode)
time.sleep(sleepTime)

#Wpisanie wartości do pola default location
random_location= "test" + fake.last_name()#+ fake.city()
defaultLocation_field = driver.find_element(By.NAME, 'DefaultLocation')
defaultLocation_field.send_keys(random_location)
time.sleep(sleepTime)

#Wpisanie wartości do pola phone
random_phone= "test" + fake.phone_number()
phone_field = driver.find_element(By.NAME, 'Phone')
phone_field.send_keys(random_phone)
time.sleep(sleepTime)
time.sleep(sleepTime)


#Sprawdzenie zmiany url
if urlRegister != driver.current_url:
    print("\033[91mBrak adresu.\033[0m")
    with open(filename, 'a') as file:
        file.write("T7:F, ")
    tests+=1
else:
    print("\033[92mBrak adresu.\033[0m")
    with open(filename, 'a') as file:
        file.write("T7:T, ")
    tests+=1
    success+=1

#Powrot na strone rejestrowania
driver.get(urlRegister)
time.sleep(sleepTime)

#########################################################################################################################################################################################################################################################

#Rejestracja niepoprawna: brak kodu pocztowego

#Wpisanie wartości do pola email
random_email = "test" + fake.user_name() + "@test.com"
email_field = driver.find_element(By.NAME, 'Mail')
email_field.send_keys(random_email)
time.sleep(sleepTime)

#Wpisanie wartości do pola haslo
random_password = "test" + fake.password()
password_field = driver.find_element(By.NAME, 'Password')
password_field.send_keys(random_password)
time.sleep(sleepTime)

#Wpisanie wartości do pola first name
random_name = "test" + fake.first_name()
firstName_field = driver.find_element(By.NAME, 'FirstName')
firstName_field.send_keys(random_name)
time.sleep(sleepTime)

#Wpisanie wartości do pola last name
random_Lastname = "test" + fake.last_name()
lastName_field = driver.find_element(By.NAME, 'LastName')
lastName_field.send_keys(random_Lastname)
time.sleep(sleepTime)

#Wybranie dany urodzenia
date_input = driver.find_element(By.XPATH, '//input[@type="date"]')
date_input.click()
date_input.send_keys(Keys.SPACE)
date_input.send_keys(Keys.ENTER)
time.sleep(sleepTime)

#Wybranie plci
sex_input = driver.find_element(By.NAME, 'Sex')
sex_input.click()
sex_input.send_keys(Keys.ARROW_DOWN)
sex_input.send_keys(Keys.ENTER)
time.sleep(sleepTime)

#Wpisanie wartości do pola default address
random_address = "test" + fake.last_name()#+ fake.address() #z jakiegos powodu selenium ma problemy z adresem i miastem. Mimo że generuje i akceptuje to po nacisnieciu register wyskakuje Registration error
defaultAddress_field = driver.find_element(By.NAME, 'DefaultAddress')
defaultAddress_field.send_keys(random_address)
time.sleep(sleepTime)

#Wpisanie wartości do pola postal code
random_postalCode = "" #+ fake.postalcode()
defaultPostalCode_field = driver.find_element(By.NAME, 'DefaultPostalcode')
defaultPostalCode_field.send_keys(random_postalCode)
time.sleep(sleepTime)

#Wpisanie wartości do pola default location
random_location= "test" + fake.last_name()#+ fake.city()
defaultLocation_field = driver.find_element(By.NAME, 'DefaultLocation')
defaultLocation_field.send_keys(random_location)
time.sleep(sleepTime)

#Wpisanie wartości do pola phone
random_phone= "test" + fake.phone_number()
phone_field = driver.find_element(By.NAME, 'Phone')
phone_field.send_keys(random_phone)
time.sleep(sleepTime)
time.sleep(sleepTime)


#Sprawdzenie zmiany url
if urlRegister != driver.current_url:
    print("\033[91mBrak kodu pocztowego.\033[0m")
    with open(filename, 'a') as file:
        file.write("T8:F, ")
    tests+=1
else:
    print("\033[92mBrak kodu pocztowego.\033[0m")
    with open(filename, 'a') as file:
        file.write("T8:T, ")
    tests+=1
    success+=1

#Powrot na strone rejestrowania
driver.get(urlRegister)
time.sleep(sleepTime)

#########################################################################################################################################################################################################################################################

#Rejestracja niepoprawna: brak lokacji

#Wpisanie wartości do pola email
random_email = "test" + fake.user_name() + "@test.com"
email_field = driver.find_element(By.NAME, 'Mail')
email_field.send_keys(random_email)
time.sleep(sleepTime)

#Wpisanie wartości do pola haslo
random_password = "test" + fake.password()
password_field = driver.find_element(By.NAME, 'Password')
password_field.send_keys(random_password)
time.sleep(sleepTime)

#Wpisanie wartości do pola first name
random_name = "test" + fake.first_name()
firstName_field = driver.find_element(By.NAME, 'FirstName')
firstName_field.send_keys(random_name)
time.sleep(sleepTime)

#Wpisanie wartości do pola last name
random_Lastname = "test" + fake.last_name()
lastName_field = driver.find_element(By.NAME, 'LastName')
lastName_field.send_keys(random_Lastname)
time.sleep(sleepTime)

#Wybranie dany urodzenia
date_input = driver.find_element(By.XPATH, '//input[@type="date"]')
date_input.click()
date_input.send_keys(Keys.SPACE)
date_input.send_keys(Keys.ENTER)
time.sleep(sleepTime)

#Wybranie plci
sex_input = driver.find_element(By.NAME, 'Sex')
sex_input.click()
sex_input.send_keys(Keys.ARROW_DOWN)
sex_input.send_keys(Keys.ENTER)
time.sleep(sleepTime)

#Wpisanie wartości do pola default address
random_address = "test" + fake.last_name()#+ fake.address() #z jakiegos powodu selenium ma problemy z adresem i miastem. Mimo że generuje i akceptuje to po nacisnieciu register wyskakuje Registration error
defaultAddress_field = driver.find_element(By.NAME, 'DefaultAddress')
defaultAddress_field.send_keys(random_address)
time.sleep(sleepTime)

#Wpisanie wartości do pola postal code
random_postalCode = "test" + fake.postalcode()
defaultPostalCode_field = driver.find_element(By.NAME, 'DefaultPostalcode')
defaultPostalCode_field.send_keys(random_postalCode)
time.sleep(sleepTime)

#Wpisanie wartości do pola default location
random_location= "" #+ fake.last_name()#+ fake.city()
defaultLocation_field = driver.find_element(By.NAME, 'DefaultLocation')
defaultLocation_field.send_keys(random_location)
time.sleep(sleepTime)

#Wpisanie wartości do pola phone
random_phone= "test" + fake.phone_number()
phone_field = driver.find_element(By.NAME, 'Phone')
phone_field.send_keys(random_phone)
time.sleep(sleepTime)
time.sleep(sleepTime)


#Sprawdzenie zmiany url
if urlRegister != driver.current_url:
    print("\033[91mBrak lokacji.\033[0m")
    with open(filename, 'a') as file:
        file.write("T9:F, ")
    tests+=1
else:
    print("\033[92mBrak lokacji.\033[0m")
    with open(filename, 'a') as file:
        file.write("T9:T, ")
    tests+=1
    success+=1

#Powrot na strone rejestrowania
driver.get(urlRegister)
time.sleep(sleepTime)


#########################################################################################################################################################################################################################################################

#Rejestracja niepoprawna: brak telefonu

#Wpisanie wartości do pola email
random_email = "test" + fake.user_name() + "@test.com"
email_field = driver.find_element(By.NAME, 'Mail')
email_field.send_keys(random_email)
time.sleep(sleepTime)

#Wpisanie wartości do pola haslo
random_password = "test" + fake.password()
password_field = driver.find_element(By.NAME, 'Password')
password_field.send_keys(random_password)
time.sleep(sleepTime)

#Wpisanie wartości do pola first name
random_name = "test" + fake.first_name()
firstName_field = driver.find_element(By.NAME, 'FirstName')
firstName_field.send_keys(random_name)
time.sleep(sleepTime)

#Wpisanie wartości do pola last name
random_Lastname = "test" + fake.last_name()
lastName_field = driver.find_element(By.NAME, 'LastName')
lastName_field.send_keys(random_Lastname)
time.sleep(sleepTime)

#Wybranie dany urodzenia
date_input = driver.find_element(By.XPATH, '//input[@type="date"]')
date_input.click()
date_input.send_keys(Keys.SPACE)
date_input.send_keys(Keys.ENTER)
time.sleep(sleepTime)

#Wybranie plci
sex_input = driver.find_element(By.NAME, 'Sex')
sex_input.click()
sex_input.send_keys(Keys.ARROW_DOWN)
sex_input.send_keys(Keys.ENTER)
time.sleep(sleepTime)

#Wpisanie wartości do pola default address
random_address = "test" + fake.last_name()#+ fake.address() #z jakiegos powodu selenium ma problemy z adresem i miastem. Mimo że generuje i akceptuje to po nacisnieciu register wyskakuje Registration error
defaultAddress_field = driver.find_element(By.NAME, 'DefaultAddress')
defaultAddress_field.send_keys(random_address)
time.sleep(sleepTime)

#Wpisanie wartości do pola postal code
random_postalCode = "test" + fake.postalcode()
defaultPostalCode_field = driver.find_element(By.NAME, 'DefaultPostalcode')
defaultPostalCode_field.send_keys(random_postalCode)
time.sleep(sleepTime)

#Wpisanie wartości do pola default location
random_location= "test" + fake.last_name()#+ fake.city()
defaultLocation_field = driver.find_element(By.NAME, 'DefaultLocation')
defaultLocation_field.send_keys(random_location)
time.sleep(sleepTime)

#Wpisanie wartości do pola phone
random_phone= "" #+ fake.phone_number()
phone_field = driver.find_element(By.NAME, 'Phone')
phone_field.send_keys(random_phone)
time.sleep(sleepTime)
time.sleep(sleepTime)


#Sprawdzenie zmiany url
if urlRegister != driver.current_url:
    print("\033[91mBrak telefonu.\033[0m")
    with open(filename, 'a') as file:
        file.write("T10:F, ")
    tests+=1
else:
    print("\033[92mBrak telefonu.\033[0m")
    with open(filename, 'a') as file:
        file.write("T10:T, ")
    tests+=1
    success+=1

#Powrot na strone rejestrowania
driver.get(urlRegister)
time.sleep(sleepTime)

#########################################################################################################################################################################################################################################################

#Rejestracja niepoprawna: email zajety

#Wpisanie wartości do pola email
random_email = "krzysztof.duda@example.com" 
email_field = driver.find_element(By.NAME, 'Mail')
email_field.send_keys(random_email)
time.sleep(sleepTime)

#Wpisanie wartości do pola haslo
random_password = "test" + fake.password()
password_field = driver.find_element(By.NAME, 'Password')
password_field.send_keys(random_password)
time.sleep(sleepTime)

#Wpisanie wartości do pola first name
random_name = "test" + fake.first_name()
firstName_field = driver.find_element(By.NAME, 'FirstName')
firstName_field.send_keys(random_name)
time.sleep(sleepTime)

#Wpisanie wartości do pola last name
random_Lastname = "test" + fake.last_name()
lastName_field = driver.find_element(By.NAME, 'LastName')
lastName_field.send_keys(random_Lastname)
time.sleep(sleepTime)

#Wybranie dany urodzenia
date_input = driver.find_element(By.XPATH, '//input[@type="date"]')
date_input.click()
date_input.send_keys(Keys.SPACE)
date_input.send_keys(Keys.ENTER)
time.sleep(sleepTime)

#Wybranie plci
sex_input = driver.find_element(By.NAME, 'Sex')
sex_input.click()
sex_input.send_keys(Keys.ARROW_DOWN)
sex_input.send_keys(Keys.ENTER)
time.sleep(sleepTime)

#Wpisanie wartości do pola default address
random_address = "test" + fake.last_name()#+ fake.address() #z jakiegos powodu selenium ma problemy z adresem i miastem. Mimo że generuje i akceptuje to po nacisnieciu register wyskakuje Registration error
defaultAddress_field = driver.find_element(By.NAME, 'DefaultAddress')
defaultAddress_field.send_keys(random_address)
time.sleep(sleepTime)

#Wpisanie wartości do pola postal code
random_postalCode = "test" + fake.postalcode()
defaultPostalCode_field = driver.find_element(By.NAME, 'DefaultPostalcode')
defaultPostalCode_field.send_keys(random_postalCode)
time.sleep(sleepTime)

#Wpisanie wartości do pola default location
random_location= "test" + fake.last_name()#+ fake.city()
defaultLocation_field = driver.find_element(By.NAME, 'DefaultLocation')
defaultLocation_field.send_keys(random_location)
time.sleep(sleepTime)

#Wpisanie wartości do pola phone
random_phone= "test" + fake.phone_number()
phone_field = driver.find_element(By.NAME, 'Phone')
phone_field.send_keys(random_phone)
time.sleep(sleepTime)
time.sleep(sleepTime)

#Sprawdzenie zmiany url
if urlRegister != driver.current_url:
    print("\033[91mEmail zajęty.\033[0m")
    with open(filename, 'a') as file:
        file.write("T11:F ")
    tests+=1
else:
    print("\033[92mEmail zajęty.\033[0m")
    with open(filename, 'a') as file:
        file.write("T11:T ")
    tests+=1
    success+=1


#Obliczenie procentu powodzenia do calkowitej ilosci testow 
percent_success = (success / tests) * 100
print("Procent powodzenia: {:.2f}%".format(percent_success) + " " + str(success) + "/" + str(tests))


#Zapisywanie danych przygotowywanych do raportu
with open(filename2, "w") as file:
    file.write("tests=" + str(tests) + "\n")
    file.write("success=" + str(success))

#Zapisanie wynikow w pliku raport.txt
with open(filename, 'a') as file:
    file.write("\nProcent powodzenia: {:.2f}%".format(percent_success) + " " + str(success) + "/" + str(tests) + "\n" )
    file.write(format(formatted_datetime))


#########################################################################################################################################################################################################################################################

#Utworzenie konta testowego

driver.get(urlRegister)
time.sleep(sleepTime)

#Wpisanie wartości do pola email
testMainEmail = "testMain" + fake.user_name() + "@testMain.com"
email_field = driver.find_element(By.NAME, 'Mail')
email_field.send_keys(testMainEmail)
time.sleep(sleepTime)

#Wpisanie wartości do pola haslo
testMainPassword = "testMain" + fake.user_name()
password_field = driver.find_element(By.NAME, 'Password')
password_field.send_keys(testMainPassword)
time.sleep(sleepTime)

#Wpisanie wartości do pola first name
random_name = "testMain"
firstName_field = driver.find_element(By.NAME, 'FirstName')
firstName_field.send_keys(random_name)
time.sleep(sleepTime)

#Wpisanie wartości do pola last name
random_Lastname = "testMain" 
lastName_field = driver.find_element(By.NAME, 'LastName')
lastName_field.send_keys(random_Lastname)
time.sleep(sleepTime)

#Wybranie dany urodzenia
date_input = driver.find_element(By.XPATH, '//input[@type="date"]')
date_input.click()
date_input.send_keys(Keys.SPACE)
date_input.send_keys(Keys.ENTER)

time.sleep(sleepTime)

#Wybranie plci
sex_input = driver.find_element(By.NAME, 'Sex')
sex_input.click()
sex_input.send_keys(Keys.ARROW_DOWN)
sex_input.send_keys(Keys.ENTER)
time.sleep(sleepTime)

#Wpisanie wartości do pola default address
random_address = "test" #+ fake.address() #z jakiegos powodu selenium ma problemy z adresem i miastem. Mimo że generuje i akceptuje to po nacisnieciu register wyskakuje Registration error
defaultAddress_field = driver.find_element(By.NAME, 'DefaultAddress')
defaultAddress_field.send_keys(random_address)
time.sleep(sleepTime)

#Wpisanie wartości do pola postal code
random_postalCode = "testMain" 
defaultPostalCode_field = driver.find_element(By.NAME, 'DefaultPostalcode')
defaultPostalCode_field.send_keys(random_postalCode)
time.sleep(sleepTime)

#Wpisanie wartości do pola default location
random_location= "test" #+ fake.city()
defaultLocation_field = driver.find_element(By.NAME, 'DefaultLocation')
defaultLocation_field.send_keys(random_location)
time.sleep(sleepTime)

#Wpisanie wartości do pola phone
random_phone= "testMain" + fake.phone_number()
phone_field = driver.find_element(By.NAME, 'Phone')
phone_field.send_keys(random_phone)
time.sleep(sleepTime)

#Znalezienie i nacisniecie przycisku register 
register_button = driver.find_element(By.XPATH, '//p-button[@label="Register"]')
register_button.click()
time.sleep(sleepTime)
time.sleep(sleepTime)
time.sleep(sleepTime)

#Zapisanie testMain konta
with open(filename2, "w") as file:
    file.write("tests=" + str(tests) + "\n")
    file.write("success=" + str(success)+ "\n")
    file.write("testMainEmail="+ str(testMainEmail)+ "\n")
    file.write("testMainPassword="+ str(testMainPassword)+ "\n")


time.sleep(sleepTime)

driver.quit()
subprocess.run(['python', testLogin_path], check=True)
