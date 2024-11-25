from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuración del navegador
driver = webdriver.Chrome()  # Asegúrate de tener el driver de Chrome instalado y en el PATH

# URL de la página
url = "https://www.vicinityclo.de/password"
url2 = "https://www.vicinityclo.de/products/akimbo-lows-asphalt-black"

def open_browser():
    # Abrir la página
    driver.get(url)
    
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
    time.sleep(10)  # Tiempo para verificar visualmente el resultado
    boton_cookies = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='uc-accept-all-button']"))
    )
    boton_cookies.click()
    driver.get(url2)
    time.sleep(5)  # Tiempo para verificar visualmente el resultado

try:
    open_browser()
    time.sleep(60)
    open_browser()
except Exception as e:
    print(f"Error: {e}")
    driver.quit()  # Cierra el navegador

