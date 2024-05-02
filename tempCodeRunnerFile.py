import os
try:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.common.exceptions import NoSuchElementException
    from selenium.common.exceptions import TimeoutException
except:
    os.system("python3 install selenium")
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.common.exceptions import NoSuchElementException
    from selenium.common.exceptions import TimeoutException
import time
import json

def read_user_agent_from_json():
    with open('user_agent.json', "r") as file:
        data = json.load(file)
        user_agent = data["user_agent"]
    return user_agent

def open_browser(num_windows):
    screen_width = 1920
    screen_height = 500
    num_windows

    window_width = screen_width // num_windows
    window_height = screen_height
    window_x_position = 0

    user_agent = read_user_agent_from_json()
    with open('proxy.json', 'r') as file:
        proxy_info = json.load(file)

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
    options.add_argument('--disable-webgl')
    options.add_argument('--disable-session-crashed-bubble')
    options.add_argument('--disable-translation')
    options.add_argument('--disable-background-media-suspend')
    options.add_argument('--disable-quic')
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
    return(driver)

def check_login(driver):
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
        time.sleep(0.25)
        user = driver.find_element(By.NAME, 'password')
        user.send_keys(data['password'])
        time.sleep(0.25)
        driver.find_element(By.ID, 'button-login').click()
        wait = WebDriverWait(driver, 1000)
        wait.until(EC.invisibility_of_element_located((By.ID, 'button-login')))
        driver.get('https://aviso.bz/work-youtube')
        WebDriverWait(driver, 1000).until(EC.visibility_of_element_located((By.TAG_NAME, 'body')))

# def ads(driver):
#     driver.switch_to.window(driver.window_handles[0])
#     driver.get('https://aviso.bz/work-serf')
#     nhiem_vu = driver.find_elements(By.XPATH, "(//div[contains(@id, 'start-serf-')]/a)")

#     if not nhiem_vu:
#         print("Không có nhiệm vụ quảng cáo.")
#         return

#     for index, nhiemvu in enumerate(nhiem_vu):
#         try:
#             nhiemvu.click()
#             time.sleep(3)
#             start_yes_serf_element = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.CLASS_NAME, "start-yes-serf"))
#             )
#             start_yes_serf_element.click()
#             time.sleep(3)
#             driver.switch_to.window(driver.window_handles[-1])
#             time.sleep(4)
#             iframe_xpath = "//frameset//frame[1]"
#             iframe = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, iframe_xpath)))
#             driver.switch_to.frame(iframe)
#             timer_element = driver.find_element(By.XPATH, "(//span[@id='timer_inp'])[1]")
#             timer_value = int(timer_element.text.strip())
#             time.sleep(timer_value)
#             time.sleep(3)
#             button_element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn_capt")))
#             button_element.click()
#             driver.close()
#             driver.switch_to.window(driver.window_handles[0])
#         except TimeoutException:
#             print("Không tìm thấy phần tử 'start-yes-serf' sau khi click")
#         except NoSuchElementException:
#             print("Không tìm thấy phần tử timer hoặc button")
#         except Exception as e:
#             print(f"Lỗi khi thực hiện nhiệm vụ quảng cáo: {str(e)}")

#     print("Hết nhiệm vụ quảng cáo")


def job_ytb(driver):
    nhiem_vu = driver.find_elements(By.CSS_SELECTOR, "[id^='link_ads_start']")
    for index, nhiemvu in enumerate(nhiem_vu):
        try:
            driver.switch_to.window(driver.window_handles[0])
            print("Nhiệm vụ thứ :", index, end='\r')
            nhiemvu.click()
            try:
                driver.switch_to.window(driver.window_handles[1])
                time_job = int(driver.find_element(By.ID,'tmr').text)
                iframe = driver.find_element(By.ID,"video-start") 
                driver.switch_to.frame(iframe)
                play_button_elements = driver.find_elements(By.CLASS_NAME,"ytp-large-play-button") 
                found = False
                for element in play_button_elements: 
                    classes = element.get_attribute("class") 
                    if "ytp-large-play-button-red-bg" in classes: 
                        found = True 
                        break 
                if found: 
                    # Gọi hàm đợi trang web load xong sau khi video được tìm thấy
                    wait = WebDriverWait(driver, 25)
                    play_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "ytp-large-play-button")))
                    play_button.click()
                    time.sleep(time_job + 3)
                    # Thực hiện thêm 3 giây
                    try:
                        driver.switch_to.default_content()
                        tmr_element = WebDriverWait(driver, 10).until(
                            EC.visibility_of_element_located((By.ID, 'tmr'))
                        )
                        time_job_2 = int(tmr_element.text)
                        iframe = driver.find_element(By.ID, "video-start")
                        driver.switch_to.frame(iframe)
                        play_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "ytp-large-play-button")))
                        play_button.click()
                        time.sleep(4)
                        time.sleep(time_job_2 + 2)
                        driver.close()
                    except:
                        driver.close()
                else:
                    print("Video không được tìm thấy", end='\r')
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
            except:
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
        except:
            
            pass
            
    # time.sleep(2)
    # ads(driver)

def main():
    while True:
        num_windows = 3
        driver = open_browser(num_windows)
        check_login(driver)
        job_ytb(driver)
        driver.quit()
        print("Cho 5 phut")
        time.sleep(60 * 5)

if __name__ == "__main__":
    main()