import random
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import os
import time


def segundos():
    yield random.uniform(2.95,3.5) + random.uniform(-1.5,3.5)

with open('modulos_clases.json', encoding = 'latin1') as json_file:
    opciones = json.load(json_file)

modulos = opciones['modulos']
clases = opciones['clases']

#os.environ.get('PLAYGROUND_USER')
#os.environ.get('PLAYGROUND_PASS')

class Proceso():

    def __init__(self, numero_curso, cod_modulo, cod_clase, username, password) -> None:
        self.curso = str(numero_curso)
        self.modulo = str(cod_modulo)
        self.clase = str(cod_clase)
        self.username = str(username)
        self.password = str(password)

    def descarga_encuesta(self):

        modulo_elegido = str(modulos.get(self.modulo)[1])
        clase_elegida = str(clases.get(self.clase)[1])

        chromeOptions = Options()
        chromeOptions.add_argument("--start-maximized")
        chromeOptions.add_argument("--enable-automation")

        driver = webdriver.Chrome(r'C:\Users\user\chromedriver.exe', options=chromeOptions)



        #open the webpage
        driver.get("https://playground.digitalhouse.com/login")

        #target username
        username_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='username']")))
        password_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='input-password']")))

        #enter username and password
        username_box.clear()
        username_box.send_keys(self.username)
        password_box.clear()
        password_box.send_keys(self.password)
        time.sleep(next(segundos()))

        #target the login button and click it
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")), message = 'Fallo aca').click()
        time.sleep(5)

        #Accedo a la pestaña de cursos
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id='id-Cursos']"))).click()
        time.sleep(next(segundos()))

        #Elijo el curso que quiero ver
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'div[id="more_options_{self.curso}"]'))).click()
        time.sleep(next(segundos()))

        #Selecciono el botón de mas opciones
        WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="more_options_{self.curso}"]/ul/li[9]'))).click()
        time.sleep(next(segundos()))

        WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[4]/div[1]/div[2]/div/div[2]/i'))).click()
        time.sleep(next(segundos()))

        #cuestionarios
        WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="quizzesReportDropdown"]/div[2]'))).click()
        time.sleep(5)

        #elijo el módulo
        WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[1]/div/div[1]/i'))).click()
        time.sleep(next(segundos()))
        WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="{modulo_elegido}"]'))).click()

        #boton de clase
        WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[2]/div/div[1]/i'))).click()
        time.sleep(next(segundos()))
        WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="{clase_elegida}"]'))).click()


        #Ultimos dos bloques son siempre los mismos
        WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[3]/div/div[1]/i'))).click()
        time.sleep(1)
        WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="evaluableActivityTopicDropdownOption0"]'))).click()
        time.sleep(1)

        WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[4]/div[2]/div[4]/div/div[1]/i'))).click()
        time.sleep(1)
        WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="evaluableActivityBlockDropdownOption0"]'))).click()
        time.sleep(5)

        #boton de descargar
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id='DownloadQuizReportButton']"))).click()

        time.sleep(10)
        driver.quit()


prueba = Proceso(numero_curso = '2806', cod_modulo = 'M1', cod_clase = 'C2', username = os.environ.get('PLAYGROUND_USER'), password = os.environ.get('PLAYGROUND_PASS'))


prueba.descarga_encuesta()