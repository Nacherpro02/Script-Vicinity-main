from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pynput.keyboard import Key, Controller

def main():
    # Configuración del navegador
    driver = webdriver.Chrome()  # Asegúrate de tener el driver de Chrome instalado y en el PATH
    keyboard = Controller()
    # URL de la página
    url_1 = "www.vicinityclo.de/products/akimbo-lows-pristina-moss"
    url = "https://www.vicinityclo.de/password"
    url2 = "https://www.vicinityclo.de/products/akimbo-lows-asphalt-black?variant=49460835942666"

    def press():
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)

    def open_browser():
        # Abrir la página
        driver.get(url2)
        
        # Esperar a que el botón sea visible (modifica el selector según la página)
        time.sleep(2)  # Ajusta según el tiempo de carga
        boton = driver.find_element(By.CLASS_NAME, "__pf_password-btn")  # Cambia por el selector correcto
        boton.click()

        # Esperar a que el input aparezca
        time.sleep(2)
        input_texto = driver.find_element(By.NAME, "password")  # Cambia por el selector correcto
        input_texto.send_keys("BFCM24")
        time.sleep(1)
        input_texto.send_keys(Keys.RETURN)

        # Ahora estás en el portal principal (si todo salió bien)
        time.sleep(2)  # Tiempo para verificar visualmente el resultado
    
        driver.get(url2)
        time.sleep(6)  # Tiempo para verificar visualmente el resultado
        """for i in range(9):
            press()"""
        press()
        press()
        press()
        press()
        press()
        press()
        press()
        press()
        keyboard.press(Key.enter)
        keyboard.release(Key.enter) 
        carrito = driver.find_element(By.ID, "ProductSubmitButton-template--24253188636938__main")
        carrito.click()

        time.sleep(5)
        driver.close()

    try:
        open_browser()
        time.sleep(5)

    except Exception as e:
        print(f"Error: {e}")
        driver.quit()  # Cierra el navegador
        exe = False
