from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
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
from datetime import datetime


base_dir = Path(__file__).parent
chromeDriver_path = base_dir / 'chromedriver.exe'
testLogin_path = base_dir / 'testLogin.py'
testSendParcel_path = base_dir / 'testSendParcel.py'
urlLogin = 'http://localhost:4200/login'
urlFavBox = "http://localhost:4200/favouriteMSBox"


filename = os.path.join(base_dir, "testRaport.txt")
filename2 = os.path.join(base_dir, "daneRaport.txt")
success=0
tests=0
current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

#Cooldown wczytania nastepnego kroku
sleepTime = 0.2 #Wartość 0 moze powodowac bledy, zalecane min to 0.02 


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
    file.write("\n\nTest Ulubione paczkomaty")
    file.write("\n\nT1: Dodanie ulubionego paczkomatu, T2: Usuniecie ulubionego paczkomatu")

service = Service(executable_path=chromeDriver_path)
driver = webdriver.Chrome(service=service)

#driver.maximize_window()
driver.implicitly_wait(30)
driver.get(urlLogin)
wait = WebDriverWait(driver, 10)


#Logowanie poprawne

#Wpisanie wartości do pola email
email_field = driver.find_element(By.NAME, 'email')
#email_field.send_keys(testMainEmail)
email_field.send_keys("krzysztof.duda@example.com")
time.sleep(sleepTime)

#Wpisanie wartości do pola haslo
password_field = driver.find_element(By.NAME, 'password')
#password_field.send_keys(testMainPassword)
password_field.send_keys("Qwerty12#$")
time.sleep(sleepTime)

#Znalezienie i nacisniecie przycisku login 
login_button = driver.find_element(By.XPATH, '//p-button[@label="Login"]')
login_button.click()
time.sleep(sleepTime)

driver.get(urlFavBox)

time.sleep(sleepTime)

# Pobierz szerokość i wysokość okna przeglądarki
window_width = driver.execute_script("return window.innerWidth;")
window_height = driver.execute_script("return window.innerHeight;")


# Funkcja do wstawienia wskaźnika kliknięcia na stronie
def add_click_marker(x, y):
    script = f"""
    var marker = document.createElement('div');
    marker.style.position = 'absolute';
    marker.style.top = '{y - 5}px';
    marker.style.left = '{x - 5}px';
    marker.style.width = '10px';
    marker.style.height = '10px';
    marker.style.backgroundColor = 'red';
    marker.style.borderRadius = '50%';
    marker.style.zIndex = '9999';
    document.body.appendChild(marker);
    """
    driver.execute_script(script)

# Dodaj marker w miejscu kliknięcia
# add_click_marker(window_width / 2 + 390, window_height / 2 - 250)
# add_click_marker(window_width / 2 + 390, window_height / 2 - 200)
# add_click_marker(window_width / 2 + 390, window_height / 2 - 150)
# add_click_marker(window_width / 2 + 390, window_height / 2 - 100)
# add_click_marker(window_width / 2 + 390, window_height / 2 - 50)
# add_click_marker(window_width / 2 + 390, window_height / 2 - 0)


# Pierwsze kliknięcie w odpowiednim miejscu
actions = ActionChains(driver)
actions.move_by_offset(window_width / 2 + 390, window_height / 2 - 250).click().perform()


# Zresetuj pozycję kursora 
actions = ActionChains(driver)
actions.move_by_offset(-(window_width / 2 + 390), -(window_height / 2 - 250)).perform()

# Drugie kliknięcie w nowym miejscu
actions.move_by_offset(window_width / 2 + 390, window_height / 2 - 200).click().perform()

# Zresetuj pozycję kursora 
actions = ActionChains(driver)
actions.move_by_offset(-(window_width / 2 + 390), -(window_height / 2 - 200)).perform()

# Trzecie kliknięcie w nowym miejscu
actions.move_by_offset(window_width / 2 + 390, window_height / 2 - 150).click().perform()

# Zresetuj pozycję kursora 
actions = ActionChains(driver)
actions.move_by_offset(-(window_width / 2 + 390), -(window_height / 2 - 150)).perform()


driver.get(urlFavBox)


#Znalezienie i nacisniecie przycisku add favourite 
fav_button = driver.find_element(By.XPATH, '//button[.//span[text()="Add Favorite"]]')
time.sleep(sleepTime)
fav_button.click()
time.sleep(sleepTime)
time.sleep(sleepTime)
time.sleep(sleepTime)


#Nacisniecie przycisku minus na mapie
actions = ActionChains(driver)
actions.move_by_offset(window_width / 2 + 120, window_height / 2 + 120).click().perform() 

for _ in range(7):
    # Wykonaj kliknięcie
    actions.click().perform()
    time.sleep(sleepTime)
    

#Pierwszy favourite box

#Znalezienie i nacisniecie przycisku add favourite w pup-upie
fav_button2 = driver.find_element(By.XPATH, "(//button[.//span[text()='Add Favorite']])[2]")
time.sleep(sleepTime)
fav_button2.click()

time.sleep(sleepTime)

# Zresetuj pozycję myszy
actions = ActionChains(driver)
actions.move_by_offset(-(window_width / 2 + 120), -(window_height / 2 + 120)).perform()
time.sleep(sleepTime)

# Kliknij ponownie
actions = ActionChains(driver)
actions.move_by_offset(window_width / 2 - 50, window_height / 2 + 50).click().perform()


#Drugi favourite box

#Znalezienie i nacisniecie przycisku add favourite w pup-upie
fav_button2 = driver.find_element(By.XPATH, "(//button[.//span[text()='Add Favorite']])[2]")
time.sleep(sleepTime)
fav_button2.click()

# Zresetuj pozycję myszy
actions = ActionChains(driver)
actions.move_by_offset(-(window_width / 2 -50), -(window_height / 2 + 50)).perform()
time.sleep(sleepTime)

# Kliknij ponownie
actions = ActionChains(driver)
actions.move_by_offset(window_width / 2 + 50, window_height / 2 - 60).click().perform()


#Trzeci favourite box

#Znalezienie i nacisniecie przycisku add favourite w pup-upie
fav_button2 = driver.find_element(By.XPATH, "(//button[.//span[text()='Add Favorite']])[2]")
time.sleep(sleepTime)
fav_button2.click()

# Zresetuj pozycję myszy
actions = ActionChains(driver)
actions.move_by_offset(-(window_width / 2 + 50), -(window_height / 2 - 60)).perform()
time.sleep(sleepTime)

# Kliknij ponownie
actions = ActionChains(driver)
actions.move_by_offset(window_width / 2 - 40, window_height / 2 - 30).click().perform()

# Zresetuj pozycję myszy
actions = ActionChains(driver)
actions.move_by_offset(-(window_width / 2 -40), -(window_height / 2 - 30)).perform()


print("\033[92mDodanie ulubionego paczkomatu poprawne.\033[0m")
with open(filename, 'a') as file:
    file.write("\nT1:T, ")
tests+=1
success+=1


time.sleep(sleepTime)

time.sleep(sleepTime)

driver.get(urlFavBox)

time.sleep(sleepTime)
time.sleep(sleepTime)
time.sleep(sleepTime)
time.sleep(sleepTime)
time.sleep(sleepTime)


# Pierwsze kliknięcie w odpowiednim miejscu
actions = ActionChains(driver)
actions.move_by_offset(window_width / 2 + 390, window_height / 2 - 250).click().perform()

time.sleep(sleepTime)

# Zresetuj pozycję kursora 
actions = ActionChains(driver)
actions.move_by_offset(-(window_width / 2 + 390), -(window_height / 2 - 250)).perform()

# Drugie kliknięcie w nowym miejscu
actions.move_by_offset(window_width / 2 + 390, window_height / 2 - 200).click().perform()

# Zresetuj pozycję kursora 
actions = ActionChains(driver)
actions.move_by_offset(-(window_width / 2 + 390), -(window_height / 2 - 200)).perform()

# Trzecie kliknięcie w nowym miejscu
actions.move_by_offset(window_width / 2 + 390, window_height / 2 - 150).click().perform()

# Zresetuj pozycję kursora 
actions = ActionChains(driver)
actions.move_by_offset(-(window_width / 2 + 390), -(window_height / 2 - 150)).perform()

time.sleep(sleepTime)

driver.get(urlFavBox)

time.sleep(sleepTime)
time.sleep(sleepTime)
time.sleep(sleepTime)

print("\033[92mUsunięcie ulubionego paczkomatu poprawne.\033[0m")
with open(filename, 'a') as file:
    file.write("T2:T ")
tests+=1
success+=1

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

subprocess.run(['python', testSendParcel_path], check=True)
