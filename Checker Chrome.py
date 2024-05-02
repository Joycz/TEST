import os
try:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.common.exceptions import NoSuchElementException
except:
    os.system("pip install selenium")
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.common.exceptions import NoSuchElementException
import time
import json


with open('user_agent.json', "r") as file:
    data = json.load(file)
    user_agent = data["user_agent"]

with open('proxy.json', 'r') as file:
    proxy_info = json.load(file)

screen_width = 1920
screen_height = 500
num_windows = 3

window_width = screen_width // num_windows
window_height = screen_height
window_x_position = 0

user_agent


options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--disable-extensions')
options.add_argument('--disable-plugins')
options.add_argument('--disable-popup-blocking')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--disable-web-security')
options.add_argument('--disable-geolocation')
options.add_argument('--disable-logging')
options.add_argument('--disable-sync')
options.add_argument('--disable-background-networking')
options.add_argument('--disable-client-side-phishing-detection')
options.add_argument('--disable-hardware-acceleration')
options.add_argument('--disable-canvas-aa')
options.add_argument('--disable-backgrounding-occluded-windows')
options.add_argument('--disable-component-extensions-with-background-pages')
options.add_argument('--disable-default-apps')
options.add_argument('--disable-device-discovery-notifications')
options.add_argument('--disable-session-crashed-bubble')
options.add_argument('--disable-translation')
options.add_argument('--disable-background-media-suspend')
options.add_argument('--disable-quic')
options.add_argument('--disable-setuid-sandbox')
options.add_argument('--disable-spell-checking')
options.add_argument('--disable-speech-api')

options.add_argument('--disable-gpu')
options.add_argument('--disable-background-timer-throttling')
options.add_argument('--disable-predictive-services')
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--start-maximized")
options.add_argument("--disable-features=VizDisplayCompositor")
options.add_argument("--disable-remote-fonts")
options.add_argument("--no-sandbox")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--mute-audio')
options.add_argument(f"--proxy-server={proxy_info['Proxy']}")
options.add_argument(f"--window-size={window_width},{window_height}")
options.add_argument(f"--window-position={window_x_position},{0}")
options.add_argument(f"user-agent={user_agent}")
driver = webdriver.Chrome(options=options)

driver.switch_to.window(driver.window_handles[-1])

driver.get('https://aviso.bz/work-youtube')
check_url_login = "https://aviso.bz/work-youtube"
if driver.current_url == check_url_login:
    print("Đã Login", end='\r')
else:
    print("Chưa login, thực hiện đăng nhập!")
with open('account.json', 'r') as f:
    data = json.load(f)

user = driver.find_element(By.NAME, 'username')
user.send_keys(data['account'])

user = driver.find_element(By.NAME, 'password')
user.send_keys(data['password'])
time.sleep(0.25)
driver.find_element(By.ID, 'button-login').click()
wait = WebDriverWait(driver, 60)
wait.until(EC.invisibility_of_element_located((By.ID, 'button-login')))
time.sleep(2)
driver.get('https://aviso.bz/work-youtube')
input()