from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pyperclip
import time

global id
global password

def login():
    id_input = driver.find_element(By.CSS_SELECTOR, "#id")
    id_input.click()
    pyperclip.copy(id)
    # Window 운영체제라면 Keys.CONTROL
    id_input.send_keys(Keys.COMMAND, 'v')

    pw_input = driver.find_element(By.CSS_SELECTOR,'#pw')
    pw_input.click()
    pyperclip.copy(password)

    pw_input.send_keys(Keys.COMMAND, 'v')

    but = driver.find_element(By.CSS_SELECTOR, '#log\.login')
    but.click()

driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))

url = "https://nid.naver.com/nidlogin.login"
driver.get(url)

print("아이디를 알려주세요")
id = input()

print("비밀번호를 입력하세요")
password = input()

login()

# 현재 창 핸들 저장
main_window_handle = driver.current_window_handle

while True:
    # 모든 창 핸들 가져오기
    all_handles = driver.window_handles

    # 현재 창 핸들이 모든 핸들 목록에 없으면 창이 닫힌 것으로 간주
    if main_window_handle not in all_handles:
        print("창이 닫혔습니다. 종료합니다.")
        break

    time.sleep(1)  # 1초마다 확인

driver.quit()  # 드라이버 종료



