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

testRegister_path = 'testRegister.py'

base_dir = Path(__file__).parent
chromeDriver_path = base_dir / 'chromedriver.exe'
testSuspend_path = base_dir / 'testSuspend.py'

service = Service(executable_path=chromeDriver_path)
driver = webdriver.Chrome(service=service)

#Cooldown wczytania nastepnego kroku
sleepTime = 0.5#Wartość 0 moze powodowac bledy, zalecane min to 0.02 

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
driver.get(urlLogin)
time.sleep(sleepTime)

#Logowanie i przejście na stronę
email_field = driver.find_element(By.NAME, 'email')
email_field.send_keys(testMainEmail)
time.sleep(sleepTime)
password_field = driver.find_element(By.NAME, 'password')
password_field.send_keys(testMainPassword)
time.sleep(sleepTime)
login_button = driver.find_element(By.XPATH, '//p-button[@label="Login"]')
login_button.click()
time.sleep(sleepTime)
driver.get(urlData)
time.sleep(sleepTime)

with open(filename, 'a') as file:
    file.write("\n\nTest Zmiana Danych")
    file.write("\n\nT1: Zmiana imienia, T2: Zmiana nazwiska, T3: Zmiana daty urodzenia, T4: Zmiana plci, T5: Zmiana ulicy, T6: Zmiana kodu pocztowego, \nT7: Zmiana miasta, T8: Zmiana numeru telefonu, T9: Zmiana hasla ")

#Wpisanie wartości do pola FirstName
name_field = driver.find_element(By.NAME, 'FirstName')
name_field.clear()
time.sleep(sleepTime)
name = "Christopher"
name_field.send_keys(name)
time.sleep(sleepTime)

#Znalezienie i nacisniecie przycisku Edit 
edit_button = driver.find_element(By.XPATH, '//p-button[@label="Edit"]')
edit_button.click()
time.sleep(sleepTime)

#odświeżenie i sprawdzenie wartości pola
driver.refresh()
time.sleep(sleepTime)
name_field = driver.find_element(By.NAME, 'FirstName')
name_field_value = name_field.get_attribute("value")
time.sleep(sleepTime)

# Check if "example" is present in the field value
if name in name_field_value:
    print("\033[92mZmiana imienia poprawna.\033[0m")
    with open(filename, 'a') as file:
        file.write("\nT1:T, ")
    success+=1
    tests+=1
else:
    print("\033[91mZmiana imienia niepoprawna.")
    with open(filename, 'a') as file:
        file.write("\nT1:F, ")
    tests+=1

#########################################################################################################################################################################################################################################################

#Wpisanie wartości do pola LastName
name2_field = driver.find_element(By.NAME, 'LastName')
name2_field.clear()
time.sleep(sleepTime)
name2 = "Dude"
name2_field.send_keys(name2)
time.sleep(sleepTime)

#Znalezienie i nacisniecie przycisku Edit 
edit_button = driver.find_element(By.XPATH, '//p-button[@label="Edit"]')
edit_button.click()
time.sleep(sleepTime)

#odświeżenie i sprawdzenie wartości pola
driver.refresh()
time.sleep(sleepTime)
name2_field = driver.find_element(By.NAME, 'LastName')
name2_field_value = name2_field.get_attribute("value")
time.sleep(sleepTime)

# Check if "example" is present in the field value
if name2 in name2_field_value:
    print("\033[92mZmiana nazwiska poprawna.\033[0m")
    with open(filename, 'a') as file:
        file.write("T2:T, ")
    success+=1
    tests+=1
else:
    print("\033[91mZmiana nazwiska niepoprawna.\033[0m")
    with open(filename, 'a') as file:
        file.write("T2:F, ")
    tests+=1

#########################################################################################################################################################################################################################################################

#Wpisanie wartości do pola BirthDate
name3_field = driver.find_element(By.NAME, 'BirthDate')
name3_field.clear()
time.sleep(sleepTime)
#name3_field.send_keys(Keys.TAB)

name3 ="1950-01-01"
name3_month = "01"
name3_field.send_keys(name3_month)
#name3_field.send_keys(Keys.TAB)
time.sleep(sleepTime)
name3_day = "01"
name3_field.send_keys(name3_day)
time.sleep(sleepTime)

name3_year = "1950"
name3_field.send_keys(name3_year)
time.sleep(sleepTime)

#Znalezienie i nacisniecie przycisku Edit 
edit_button = driver.find_element(By.XPATH, '//p-button[@label="Edit"]')
edit_button.click()
time.sleep(sleepTime)

#odświeżenie i sprawdzenie wartości pola
driver.refresh()
time.sleep(sleepTime)
name3_field = driver.find_element(By.NAME, 'BirthDate')
name3_field_value = name3_field.get_attribute("value")
time.sleep(sleepTime)

# Check if "example" is present in the field value
if name3 in name3_field_value:
    print("\033[92mZmiana daty urodzin poprawna.\033[0m")
    with open(filename, 'a') as file:
        file.write("T3:T, ")
    success+=1
    tests+=1
else:
    print("\033[91mZmiana daty urodzin niepoprawna.\033[0m")
    print(name3)
    print(name3_field_value)
    with open(filename, 'a') as file:
        file.write("T3:F, ")
    tests+=1

#########################################################################################################################################################################################################################################################

#Wpisanie wartości do pola Sex
name4_field = driver.find_element(By.NAME, 'Sex')
select = Select(name4_field)
name4="Male"
select.select_by_visible_text(name4)
#Znalezienie i nacisniecie przycisku Edit 
edit_button = driver.find_element(By.XPATH, '//p-button[@label="Edit"]')
edit_button.click()
time.sleep(sleepTime)

#odświeżenie i sprawdzenie wartości pola
driver.refresh()
time.sleep(sleepTime)
name4_field = driver.find_element(By.NAME, 'Sex')
select = Select(name4_field)
name4_field_value = select.first_selected_option.text
time.sleep(sleepTime)

# Check if "example" is present in the field value
if name4 in name4_field_value:
    print("\033[92mZmiana płci poprawna.\033[0m")
    with open(filename, 'a') as file:
        file.write("T4:T, ")
    success+=1
    tests+=1
else:
    print("\033[91mZmiana daty płci niepoprawna.\033[0m")
    with open(filename, 'a') as file:
        file.write("T4:F, ")
    tests+=1

#########################################################################################################################################################################################################################################################

#Wpisanie wartości do pola Adress
name5_field = driver.find_element(By.NAME, 'DefaultAddress')
name5_field.clear()
time.sleep(sleepTime)
name5 = "Jana Pawła "
name5_field.send_keys(name5)
time.sleep(sleepTime)

#Znalezienie i nacisniecie przycisku Edit 
edit_button = driver.find_element(By.XPATH, '//p-button[@label="Edit"]')
edit_button.click()
time.sleep(sleepTime)

#odświeżenie i sprawdzenie wartości pola
driver.refresh()
time.sleep(sleepTime)
name5_field = driver.find_element(By.NAME, 'DefaultAddress')
name5_field_value = name5_field.get_attribute("value")
time.sleep(sleepTime)

# Check if "example" is present in the field value
if name5 in name5_field_value:
    print("\033[92mZmiana ulicy poprawna.\033[0m")
    with open(filename, 'a') as file:
        file.write("T5:T, ")
    success+=1
    tests+=1
else:
    print("\033[91mZmiana ulicy niepoprawna.\033[0m")
    with open(filename, 'a') as file:
        file.write("T5:F, ")
    tests+=1
 
#########################################################################################################################################################################################################################################################

#Wpisanie wartości do pola DefaultPostalcode
name6_field = driver.find_element(By.NAME, 'DefaultPostalcode')
name6_field.clear()
time.sleep(sleepTime)
name6 = "65-426"
name6_field.send_keys(name6)
time.sleep(sleepTime)

#Znalezienie i nacisniecie przycisku Edit 
edit_button = driver.find_element(By.XPATH, '//p-button[@label="Edit"]')
edit_button.click()
time.sleep(sleepTime)

#odświeżenie i sprawdzenie wartości pola
driver.refresh()
time.sleep(sleepTime)
name6_field = driver.find_element(By.NAME, 'DefaultPostalcode')
name6_field_value = name6_field.get_attribute("value")
time.sleep(sleepTime)

# Check if "example" is present in the field value
if name6 in name6_field_value:
    print("\033[92mZmiana kodu pocztowego poprawna.\033[0m")
    with open(filename, 'a') as file:
        file.write("T6:T, ")
    success+=1
    tests+=1
else:
    print("\033[91mZmiana kodu pocztowego niepoprawna.\033[0m")
    with open(filename, 'a') as file:
        file.write("T6:F, ")
    tests+=1   
 
#########################################################################################################################################################################################################################################################

#Wpisanie wartości do pola DefaultLocation
name7_field = driver.find_element(By.NAME, 'DefaultLocation')
name7_field.clear()
time.sleep(sleepTime)
name7 = "zielona góra"
name7_field.send_keys(name7)
time.sleep(sleepTime)

#Znalezienie i nacisniecie przycisku Edit 
edit_button = driver.find_element(By.XPATH, '//p-button[@label="Edit"]')
edit_button.click()
time.sleep(sleepTime)

#odświeżenie i sprawdzenie wartości pola
driver.refresh()
time.sleep(sleepTime)
name7_field = driver.find_element(By.NAME, 'DefaultLocation')
name7_field_value = name7_field.get_attribute("value")
time.sleep(sleepTime)

# Check if "example" is present in the field value
if name7 in name7_field_value:
    print("\033[92mZmiana miasta poprawna.\033[0m")
    with open(filename, 'a') as file:
        file.write("T7:T, ")
    success+=1
    tests+=1
else:
    print("\033[91mZmiana miasta niepoprawna.\033[0m")
    with open(filename, 'a') as file:
        file.write("T7:F, ")
    tests+=1   
 
#########################################################################################################################################################################################################################################################

#Wpisanie wartości do pola Phone
name8_field = driver.find_element(By.NAME, 'Phone')
name8_field.clear()
time.sleep(sleepTime)
name8 = "111111111"
name8_field.send_keys(name8)
time.sleep(sleepTime)

#Znalezienie i nacisniecie przycisku Edit 
edit_button = driver.find_element(By.XPATH, '//p-button[@label="Edit"]')
edit_button.click()
time.sleep(sleepTime)

#odświeżenie i sprawdzenie wartości pola
driver.refresh()
time.sleep(sleepTime)
name8_field = driver.find_element(By.NAME, 'Phone')
name8_field_value = name8_field.get_attribute("value")
time.sleep(sleepTime)

# Check if "example" is present in the field value
if name8 in name8_field_value:
    print("\033[92mZmiana numeru telefonu poprawna.\033[0m")
    with open(filename, 'a') as file:
        file.write("T8:T, ")
    success+=1
    tests+=1

#########################################################################################################################################################################################################################################################

#Wpisanie wartości do pola hasło
passw_field = driver.find_element(By.NAME, 'Password')
passw_field.clear()
time.sleep(sleepTime)
passw = "SuperTajneHaslo123!@#"
passw_field.send_keys(passw)
time.sleep(sleepTime)

#Znalezienie i nacisniecie przycisku Edit 
edit_button = driver.find_element(By.XPATH, '//p-button[@label="Edit"]')
edit_button.click()
time.sleep(sleepTime)

#Wylogowanie i się sprawdzenie najpierw starego, potem nowego hasła
logowania = 0

driver.get(urlLogin)

#Logowanie i przejście na stronę
email_field = driver.find_element(By.NAME, 'email')
email_field.send_keys(testMainEmail)
time.sleep(sleepTime)
password_field = driver.find_element(By.NAME, 'password')
password_field.send_keys(testMainPassword)
time.sleep(sleepTime)
login_button = driver.find_element(By.XPATH, '//p-button[@label="Login"]')
login_button.click()
time.sleep(sleepTime)
if urlLogin == driver.current_url:
    logowania = logowania+1
email_field = driver.find_element(By.NAME, 'email')
email_field.clear()
email_field.send_keys(testMainEmail)
time.sleep(sleepTime)
password_field = driver.find_element(By.NAME, 'password')
password_field.clear()
password_field.send_keys('SuperTajneHaslo123!@#')
time.sleep(sleepTime)
login_button = driver.find_element(By.XPATH, '//p-button[@label="Login"]')
login_button.click()
time.sleep(sleepTime)
if urlLogin != driver.current_url:
    logowania = logowania+1
if logowania == 2:
    print("\033[92mZmiana hasła poprawna.\033[0m")
    with open(filename, 'a') as file:
        file.write("T9:T ")
    success+=1
    tests+=1
else:
    print("\033[91mZmiana hasła niepoprawna.\033[0m")
    with open(filename, 'a') as file:
        file.write("T9:F ")
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

subprocess.run(['python', testSuspend_path], check=True)




"""
#Logowanie poprawne

#Wpisanie wartości do pola email
email_field = driver.find_element(By.NAME, 'email')
email_field.send_keys('krzysztof.duda@example.com')
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
    print("Logowanie poprawne.")
    with open(filename, 'a') as file:
        file.write("\nT1:T, ")
    success+=1
    tests+=1
else:
    print("Logowanie niepoprawne.")
    with open(filename, 'a') as file:
        file.write("\nT1:F, ")
    tests+=1


#Powrot na strone logowania
driver.get(urlLogin)
time.sleep(sleepTime)



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
    print("Logowanie poprawne.")
    with open(filename, 'a') as file:
        file.write("T2:F, ")
    tests+=1
else:
    print("Logowanie niepoprawne.")
    with open(filename, 'a') as file:
        file.write("T1:T, ")
    success+=1
    tests+=1

#Powrot na strone logowania
driver.get(urlLogin)
time.sleep(sleepTime)



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
    print("Logowanie poprawne.")
    with open(filename, 'a') as file:
        file.write("T3:F ")
    tests+=1
else:
    print("Logowanie niepoprawne.")
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
    file.write("success=" + str(success))

#Zapisanie wynikow w pliku raport.txt
with open(filename, 'a') as file:
    file.write("\n\nTest Logowanie \n")
    file.write("Procent powodzenia: {:.2f}%".format(percent_success) + " " + str(success) + "/" + str(tests) + "\n" )
    file.write(format(formatted_datetime))


driver.quit()

#Uruchomienie kolejnego skryptu do testowania
subprocess.run(['python', testRegister_path])




# for _ in range(500):
#     login_button.click()
#     time.sleep(0.5)  
"""
# Zamknij przeglądarkę
# driver.quit()