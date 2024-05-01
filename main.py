from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
import time

global id
global password
global islogin
global keyword
global comment

def keyword_search():
    driver.get(blog_url)
    print('원하는 키워드를 입력하세요')
    keyword = input()
    wait = WebDriverWait(driver, 3)
    keyword_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#header > div.header_common > div > div.area_search > form > fieldset > div > input")))
    keyword_input.click()

    keyword_input.send_keys(keyword)
    
    search_btn = driver.find_element(By.CSS_SELECTOR, '#header > div.header_common > div > div.area_search > form > fieldset > a.button.button_blog')
    search_btn.click()

    print('원하는 댓글을 입력해 주세요')
    comment = input()
    write_comment()

def write_comment():
    post = driver.find_element(By.CSS_SELECTOR, '#content > section > div.area_list_search > div:nth-child(1) > div > div.info_post > div.desc > a.desc_inner > strong > span')
    post.click()
    print('포스트 클릭 완료')

    wait = WebDriverWait(driver, 10)  # 최대 10초 동안 대기
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body")))  # body 요소가 로딩될 때까지 대기
    print('웹사이트 로드 완료')
    driver.execute_script("window.scrollTo(0, 1500)")
    print('??')


    comment_btn = driver.find_element(By.CSS_SELECTOR, '#Comi223419280474')
    
    # comment_btn = driver.find_element(By.CSS_SELECTOR, '#btn_comment_2')
    comment_btn.click()
    print('댓글 클릭 완료')


    comment_write = driver.find_element(By.CSS_SELECTOR, '#naverComment_201_223423629833 > div > div.u_cbox_write_wrap > div.u_cbox_write_box.u_cbox_type_logged_in > form > fieldset > div > div > div.u_cbox_write_area > div > label')
    comment_write.click()
    print('댓글상자 클릭 완료')

    comment_write.send_keys(comment)

    write_btn = driver.find_element(By.CSS_SELECTOR, '#naverComment_201_223423629833 > div > div.u_cbox_write_wrap > div.u_cbox_write_box.u_cbox_type_logged_in > form > fieldset > div > div > div.u_cbox_upload > button')
    write_btn.click()
    print('작성버튼 클릭 완료')

    wait = WebDriverWait(driver, 3)
    print(f'댓글 등록이 완료되었습니다. 사이트 :{driver.current_url} ')
    driver.get(blog_url)




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

    islogin = True
    keyword_search()



driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))
islogin = False
url = "https://nid.naver.com/nidlogin.login"
blog_url = "https://section.blog.naver.com/BlogHome.naver?directoryNo=0&currentPage=1&groupId=0"
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



