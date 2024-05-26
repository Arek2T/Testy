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
from selenium.webdriver.common.action_chains import ActionChains

testChangeData_path = 'testy/ChangeData.py'

base_dir = Path(__file__).parent
chromeDriver_path = base_dir / 'chromedriver.exe'

testSuspend_path = base_dir / 'testSuspend.py'
testPostpone_path = base_dir / 'testPostpone.py'

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


with open(filename, 'a') as file:
    file.write("\n\nTest Wyslanie Paczki")
    file.write("\n\nT1: Wyslanie paczki S, T2: Wyslanie paczki M, T3: Wyslanie paczki L")


urlLogin = 'http://localhost:4200/login'
urlData = 'http://localhost:4200/changeUserData'
urlSendParcel = 'http://localhost:4200/sendParcel'
urlOrders = 'http://localhost:4200/orders'

driver.get(urlLogin)
time.sleep(sleepTime)

#Logowanie i przejście na stronę
email_field = driver.find_element(By.NAME, 'email')
email_field.send_keys("krzysztof.duda@example.com")
time.sleep(sleepTime)
password_field = driver.find_element(By.NAME, 'password')
password_field.send_keys("Qwerty12#$")
time.sleep(sleepTime)
login_button = driver.find_element(By.XPATH, '//p-button[@label="Login"]')
login_button.click()
time.sleep(sleepTime)
driver.get(urlSendParcel)
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
#add_click_marker(window_width / 2 - 200, window_height / 2 - 120 )


#########################################################################################################################################################################################################################################################

#Wysłanie paczki Size S

size_element = driver.find_element(By.XPATH, '//p[text()="Size: S"]')
size_element.click()

time.sleep(sleepTime)

input_element = driver.find_element(By.ID, 'ReceiverMail')
# Wpisz tekst w pole input
input_element.send_keys('krzysztof.duda@example.com')

time.sleep(sleepTime)


actions = ActionChains(driver)
actions.move_by_offset(window_width / 2 - 100, window_height / 2 - 120).click().perform()

# Zresetuj pozycję kursora 
actions = ActionChains(driver)
actions.move_by_offset(-(window_width / 2 - 100), -(window_height / 2 - 120)).perform()

time.sleep(sleepTime)

input_element = driver.find_element(By.ID, 'Description')
# Wpisz tekst w pole input
input_element.send_keys('Test opis')

time.sleep(sleepTime)

button = driver.find_element(By.XPATH, '//button[@label="Select Machines" and @icon="pi pi-plus"]')
button.click()

time.sleep(sleepTime)
time.sleep(sleepTime)
time.sleep(sleepTime)
time.sleep(sleepTime)


#add_click_marker(window_width / 2 + 80, window_height / 2 + 180 )

#Nacisniecie przycisku minus na mapie
actions = ActionChains(driver)
actions.move_by_offset(window_width / 2 + 80, window_height / 2 + 180).click().perform() 

for _ in range(7):
    # Wykonaj kliknięcie
    actions.click().perform()
    time.sleep(sleepTime)
    

# Zresetuj pozycję myszy
actions = ActionChains(driver)
actions.move_by_offset(-(window_width / 2 + 80), -(window_height / 2 + 180)).perform()
time.sleep(sleepTime)

# Nacisniecie guzika Set From
button = driver.find_element(By.XPATH, '//span[text()="Set From"]')
button.click()

# Kliknij w paczkomat Set From
actions = ActionChains(driver)
actions.move_by_offset(window_width / 2 - 50, window_height / 2 + 50).click().perform()

# Zresetuj pozycję myszy
actions = ActionChains(driver)
actions.move_by_offset(-(window_width / 2 - 50), -(window_height / 2 + 50)).perform()
time.sleep(sleepTime)


# Nacisniecie guzika Set To
button = driver.find_element(By.XPATH, '//span[text()="Set To"]')
button.click()
time.sleep(sleepTime)


# Kliknij w paczkomat Set To
actions = ActionChains(driver)
actions.move_by_offset(window_width / 2 + 50, window_height / 2 - 60).click().perform()

# Zresetuj pozycję myszy
actions = ActionChains(driver)
actions.move_by_offset(-(window_width / 2 + 50), -(window_height / 2 - 60)).perform()
time.sleep(sleepTime)

# Nacisniecie guzika Confirm
button = driver.find_element(By.XPATH, '//span[text()="Confirm"]')
button.click()
time.sleep(sleepTime)


# Nacisniecie guzika Send
button = driver.find_element(By.XPATH, '//span[text()="Send"]')
button.click()

time.sleep(sleepTime)


print("\033[92mDodanie paczki S poprawne.\033[0m")
with open(filename, 'a') as file:
    file.write("\nT1:T ")
tests+=1
success+=1

#########################################################################################################################################################################################################################################################

#Wyslanie paczki M

driver.get(urlSendParcel)

#add_click_marker(window_width / 2 + 250, window_height / 2 - 200 )

time.sleep(sleepTime)

size_element = driver.find_element(By.XPATH, '//p[text()="Size: M"]')
size_element.click()

time.sleep(sleepTime)

input_element = driver.find_element(By.ID, 'ReceiverMail')
# Wpisz tekst w pole input
input_element.send_keys('krzysztof.duda@example.com')

time.sleep(sleepTime)


actions = ActionChains(driver)
actions.move_by_offset(window_width / 2 - 100, window_height / 2 - 120).click().perform()

# Zresetuj pozycję kursora 
actions = ActionChains(driver)
actions.move_by_offset(-(window_width / 2 - 100), -(window_height / 2 - 120)).perform()

time.sleep(sleepTime)

input_element = driver.find_element(By.ID, 'Description')
# Wpisz tekst w pole input
input_element.send_keys('Test opis')

time.sleep(sleepTime)

button = driver.find_element(By.XPATH, '//button[@label="Select Machines" and @icon="pi pi-plus"]')
button.click()

time.sleep(sleepTime)
time.sleep(sleepTime)
time.sleep(sleepTime)
time.sleep(sleepTime)


#add_click_marker(window_width / 2 + 80, window_height / 2 + 180 )

#Nacisniecie przycisku minus na mapie
actions = ActionChains(driver)
actions.move_by_offset(window_width / 2 + 80, window_height / 2 + 180).click().perform() 

for _ in range(7):
    # Wykonaj kliknięcie
    actions.click().perform()
    time.sleep(sleepTime)
    

# Zresetuj pozycję myszy
actions = ActionChains(driver)
actions.move_by_offset(-(window_width / 2 + 80), -(window_height / 2 + 180)).perform()
time.sleep(sleepTime)

# Nacisniecie guzika Set From
button = driver.find_element(By.XPATH, '//span[text()="Set From"]')
button.click()

# Kliknij w paczkomat Set From
actions = ActionChains(driver)
actions.move_by_offset(window_width / 2 - 50, window_height / 2 + 50).click().perform()

# Zresetuj pozycję myszy
actions = ActionChains(driver)
actions.move_by_offset(-(window_width / 2 - 50), -(window_height / 2 + 50)).perform()
time.sleep(sleepTime)


# Nacisniecie guzika Set To
button = driver.find_element(By.XPATH, '//span[text()="Set To"]')
button.click()
time.sleep(sleepTime)


# Kliknij w paczkomat Set To
actions = ActionChains(driver)
actions.move_by_offset(window_width / 2 + 50, window_height / 2 - 60).click().perform()

# Zresetuj pozycję myszy
actions = ActionChains(driver)
actions.move_by_offset(-(window_width / 2 + 50), -(window_height / 2 - 60)).perform()
time.sleep(sleepTime)


# Nacisniecie guzika Confirm
button = driver.find_element(By.XPATH, '//span[text()="Confirm"]')
button.click()
time.sleep(sleepTime)


# Nacisniecie guzika Send
button = driver.find_element(By.XPATH, '//span[text()="Send"]')
button.click()

time.sleep(sleepTime)

print("\033[92mDodanie paczki M poprawne.\033[0m")
with open(filename, 'a') as file:
    file.write("T2:T ")
tests+=1
success+=1

#########################################################################################################################################################################################################################################################

#Wyslanie paczki L

driver.get(urlSendParcel)

#add_click_marker(window_width / 2 + 250, window_height / 2 - 200 )

time.sleep(sleepTime)

size_element = driver.find_element(By.XPATH, '//p[text()="Size: L"]')
size_element.click()

time.sleep(sleepTime)

input_element = driver.find_element(By.ID, 'ReceiverMail')
# Wpisz tekst w pole input
input_element.send_keys('krzysztof.duda@example.com')

time.sleep(sleepTime)


actions = ActionChains(driver)
actions.move_by_offset(window_width / 2 - 100, window_height / 2 - 120).click().perform()

# Zresetuj pozycję kursora 
actions = ActionChains(driver)
actions.move_by_offset(-(window_width / 2 - 100), -(window_height / 2 - 120)).perform()

time.sleep(sleepTime)

input_element = driver.find_element(By.ID, 'Description')
# Wpisz tekst w pole input
input_element.send_keys('Test opis')

time.sleep(sleepTime)

button = driver.find_element(By.XPATH, '//button[@label="Select Machines" and @icon="pi pi-plus"]')
button.click()

time.sleep(sleepTime)
time.sleep(sleepTime)
time.sleep(sleepTime)
time.sleep(sleepTime)


#add_click_marker(window_width / 2 + 80, window_height / 2 + 180 )

#Nacisniecie przycisku minus na mapie
actions = ActionChains(driver)
actions.move_by_offset(window_width / 2 + 80, window_height / 2 + 180).click().perform() 

for _ in range(7):
    # Wykonaj kliknięcie
    actions.click().perform()
    time.sleep(sleepTime)
    

# Zresetuj pozycję myszy
actions = ActionChains(driver)
actions.move_by_offset(-(window_width / 2 + 80), -(window_height / 2 + 180)).perform()
time.sleep(sleepTime)

# Nacisniecie guzika Set From
button = driver.find_element(By.XPATH, '//span[text()="Set From"]')
button.click()

# Kliknij w paczkomat Set From
actions = ActionChains(driver)
actions.move_by_offset(window_width / 2 - 50, window_height / 2 + 50).click().perform()

# Zresetuj pozycję myszy
actions = ActionChains(driver)
actions.move_by_offset(-(window_width / 2 - 50), -(window_height / 2 + 50)).perform()
time.sleep(sleepTime)


# Nacisniecie guzika Set To
button = driver.find_element(By.XPATH, '//span[text()="Set To"]')
button.click()
time.sleep(sleepTime)


# Kliknij w paczkomat Set To
actions = ActionChains(driver)
actions.move_by_offset(window_width / 2 + 50, window_height / 2 - 60).click().perform()

# Zresetuj pozycję myszy
actions = ActionChains(driver)
actions.move_by_offset(-(window_width / 2 + 50), -(window_height / 2 - 60)).perform()
time.sleep(sleepTime)


# Nacisniecie guzika Confirm
button = driver.find_element(By.XPATH, '//span[text()="Confirm"]')
button.click()
time.sleep(sleepTime)


# Nacisniecie guzika Send
button = driver.find_element(By.XPATH, '//span[text()="Send"]')
button.click()

time.sleep(sleepTime)

print("\033[92mDodanie paczki L poprawne.\033[0m")
with open(filename, 'a') as file:
    file.write("T3:T ")
tests+=1
success+=1

#########################################################################################################################################################################################################################################################

driver.get(urlOrders)

#Sprawdzenie nadanych paczek
actions = ActionChains(driver)
actions.move_by_offset(window_width / 2 - 250, window_height / 2 - 250).click().perform()

# Zresetuj pozycję myszy
actions = ActionChains(driver)
actions.move_by_offset(-(window_width / 2 - 250), -(window_height / 2 - 250)).perform()
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

#add_click_marker(window_width / 2 - 250, window_height / 2 - 250 )

driver.quit()

#subprocess.run(['python', testPostpone_path], check=True)

#subprocess.run(['python', testSuspend_path], check=True)
#subprocess.run(['python', testChangeData_path], check=True)

