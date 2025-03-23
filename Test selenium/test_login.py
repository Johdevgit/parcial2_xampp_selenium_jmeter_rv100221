import pytest
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# Configuración del log
logging.basicConfig(
    filename="resultados_selenium.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

class TestLogin:
    def setup_method(self, method):
        logging.info("Iniciando el navegador y configurando el driver...")
        service = Service(executable_path="C:/Users/Johan/Downloads/gecko/geckodriver.exe")
        options = Options()
        self.driver = webdriver.Firefox(service=service, options=options)
        self.vars = {}

    def teardown_method(self, method):
        logging.info("Cerrando el navegador...")
        self.driver.quit()

    def test_login(self):
        logging.info("El script de prueba ha comenzado.")
        
        for i in range(100):
            try:
                logging.info(f"Ejecutando prueba {i + 1}/10...")
                
                self.driver.get("http://localhost/Login-registration-System-PHP-and-MYSQL/index.php")
                self.driver.set_window_size(550, 721)
                
                logging.info(f"Página cargada para prueba {i + 1}")

                username = self.driver.find_element(By.NAME, "uname")
                password = self.driver.find_element(By.NAME, "password")
                login_button = self.driver.find_element(By.CSS_SELECTOR, "button")
                
                username.send_keys("elias")
                time.sleep(0.5)
                password.send_keys("123")
                time.sleep(0.5)
                login_button.click()

                logging.info(f"Datos enviados en la prueba {i + 1}")

                time.sleep(1)

                logging.info(f"Prueba {i + 1} completada con éxito.")
            
            except Exception as e:
                logging.error(f"Error en la prueba {i + 1}: {str(e)}")

# Ejecutar el test solo si no se está utilizando pytest directamente
if __name__ == "__main__":
    test = TestLogin()
    test.setup_method(None)
    test.test_login()
    test.teardown_method(None)