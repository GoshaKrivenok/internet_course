from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Укажите путь к вашему ChromeDriver
chrome_driver_path = 'C:\\Users\\37529\\Downloads\\chromedriver_win32'

# Настройка опций для Chrome
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Инициализация драйвера
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Открытие веб-страницы
    driver.get('https://example.com')

    # Работа с LocalStorage
    print("Working with LocalStorage...")

    # Установка значения в LocalStorage
    driver.execute_script("localStorage.setItem('key', 'value');")

    # Получение значения из LocalStorage
    value = driver.execute_script("return localStorage.getItem('key');")
    print(f"Value from LocalStorage: {value}")

    # Удаление значения из LocalStorage
    driver.execute_script("localStorage.removeItem('key');")

    # Проверка, что значение удалено
    value_after_deletion = driver.execute_script("return localStorage.getItem('key');")
    print(f"Value after deletion from LocalStorage: {value_after_deletion}")

    # Работа с Cookie
    print("\nWorking with Cookie...")

    # Установка значения в cookie
    driver.add_cookie({'name': 'test_cookie', 'value': 'test_value'})

    # Получение значения из cookie
    cookie = driver.get_cookie('test_cookie')
    print(f"Cookie: {cookie}")

    # Удаление значения из cookie
    driver.delete_cookie('test_cookie')

    # Проверка, что значение удалено
    cookie_after_deletion = driver.get_cookie('test_cookie')
    print(f"Cookie after deletion: {cookie_after_deletion}")

finally:
    # Закрытие браузера
    driver.quit()
