from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('C:\python\chromedriver_win32\chromedriver.exe')
driver.implicitly_wait(3)
driver.get('https://www.twilio.com/login')
# 아이디/비밀번호를 입력해준다.
driver.find_element_by_name('email').send_keys('oth5447@naver.com')
driver.find_element_by_class_name('btn btn-primary btn-filled m-r-sm m-b-sm').click()
#driver.find_element_by_name('pw').send_keys('4305447oo')
# 로그인 버튼을 눌러주자.
#driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()