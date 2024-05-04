import os
try:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.common.exceptions import NoSuchElementException
    from selenium.common.exceptions import NoSuchWindowException
    from selenium.common.exceptions import TimeoutException
except:
    os.system("pip install selenium")
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.common.exceptions import NoSuchElementException
    from selenium.common.exceptions import NoSuchWindowException
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
    num_windows = num_windows

    window_width = screen_width // num_windows
    window_height = screen_height
    window_x_position = 0

    user_agent = read_user_agent_from_json()
    # with open('proxy.json', 'r') as file:
    #     proxy_info = json.load(file)

    options = webdriver.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-plugins')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--disable-web-security')
    options.add_argument('--disable-geolocation')
    options.add_argument("--disable-location")
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
    #options.add_argument(f"--proxy-server={proxy_info['Proxy']}")
    options.add_argument(f"--window-size={window_width},{window_height}")
    options.add_argument(f"--window-position={window_x_position},{0}")
    options.add_argument(f"user-agent={user_agent}")
    driver = webdriver.Chrome(options=options)

    driver.switch_to.window(driver.window_handles[-1])
    return driver

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

        try:
            wait = WebDriverWait(driver, 60)
            wait.until(EC.invisibility_of_element_located((By.ID, 'button-login')))
            print("Đã đăng nhập thành công")
        except TimeoutException:
            print("Mạng chậm ...!")
            return False
        
        driver.get('https://aviso.bz/work-youtube')
        
        '''' Thực hiện chờ web load '''
        try:
            WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            print("Trang load hoàn tất")
            return True
        except:
            return
        '''' ---------------------- '''

#phần nhiem_vu nó get về cả id phía sau của nó dưới đây là chỉ bắt được cái link_ads_start thôi chứ không lấy về cụ thể id nằm sau nó, dạng id của các element đó sẽ có kiểu là : link_ads_start-38137,... và nhiều hơn thế, điều này nếu sử dụng theo cách thông thường là lấy phần đầu của nó thì sẽ xảy ra việc không click được. Tôi cần cách để lấy về cả id phía sau để thực hiện click vào nó 

def job_ytb_test(driver):
    completed_tasks = 1  # Initialize completed tasks count
    nhiem_vu = driver.find_elements(By.CSS_SELECTOR, "[id^='link_ads_start']")
    kiemtra = len(nhiem_vu)
    for index, nhiemvu in enumerate(nhiem_vu):
        time.sleep(1.5)
        try:
            driver.switch_to.window(driver.window_handles[0])
            try:
                if kiemtra > 2:
                    element_id = nhiemvu.get_attribute("id")
                    css_selector = f"#{element_id}"
                    specific_element = driver.find_element(By.CSS_SELECTOR, css_selector)
                    specific_element.click()
                    time.sleep(1)
                    driver.switch_to.window(driver.window_handles[1])
                else:
                    print("Hết nhiệm vụ!")
                    break
            except:
                print("Nhiệm vụ lỗi", end='\r')
                time.sleep(2)
                continue #Click không được chạy lại FOR

            '''' Thực hiện chờ web load '''
            try:
                WebDriverWait(driver, 60).until(
                    EC.presence_of_element_located((By.TAG_NAME, "body"))
                )
            except:
                driver.close()
                continue
            '''' ---------------------- '''
            try:
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
                    wait = WebDriverWait(driver, 25)
                    play_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "ytp-large-play-button")))
                    play_button.click()
                    time.sleep(time_job + 3)
                    #------------#
                    try:
                        driver.switch_to.default_content() #Thoát iframe để lấy time tmr
                        tmr_element = WebDriverWait(driver, 10).until(
                            EC.visibility_of_element_located((By.ID, 'tmr'))
                        )
                        time_job_2 = int(tmr_element.text)
                        iframe = driver.find_element(By.ID, "video-start")
                        driver.switch_to.frame(iframe)
                        play_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "ytp-large-play-button")))
                        play_button.click()
                        time.sleep(time_job_2 + 3)
                        driver.close()
                        driver.switch_to.window(driver.window_handles[0])
                    except:
                        driver.close()
                        driver.switch_to.window(driver.window_handles[0])
                    #------------#
                else:
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                    continue
            except:
                print("")
                driver.close()
                continue
        except:
            pass
        #Ngoai FOR
        completed_tasks += 1
        print("Hoàn thành nhiệm vụ : " + str(completed_tasks))
    return completed_tasks

def wait():
    for i in range(60 * 5):
        time.sleep(1)
        print("Chờ : " + str(i), end='\r')
        i += 1
    return

total_completed_tasks = 0

def main():
    global total_completed_tasks
    while True:
        try:
            os.system('cls')
            driver = open_browser(3)
            if not check_login(driver):
                print("Trang load quá lâu")
                driver.quit()
                print("Hết nhiệm vụ. Vui lòng chờ")
                wait()
                continue
            time.sleep(1)
            completed_tasks = job_ytb_test(driver)
            total_completed_tasks += completed_tasks
            driver.quit()
            print("Hết nhiệm vụ. Vui lòng chờ", end='\r')
            wait()
        except Exception as e:
            print("Lỗi:", str(e))
            if 'driver' in locals():
                driver.quit()
            wait()
        finally:
            print("=================================")
            print("Tổng số nhiệm vụ hoàn thành:", total_completed_tasks)
            print("=================================")

if __name__ == "__main__":
    main()