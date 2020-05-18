from selenium import webdriver
from PIL import Image
from io import BytesIO
from selenium.webdriver.chrome.options import Options
 
options = Options()
options.headless = True
driver = webdriver.Chrome('C:\python\chromedriver_win32\chromedriver.exe')
driver.get("https://www.weather.go.kr/w/ocean/today.do")
 
# 전체 페이지의 사이즈를 구하여 브라우저의 창 크기를 확대하고 스크린캡처를 합니다.
page_width = driver.execute_script('return document.body.parentNode.scrollWidth')
page_height = driver.execute_script('return document.body.parentNode.scrollHeight')
driver.set_window_size(page_width, page_height)
png = driver.get_screenshot_as_png()
 
# 특정 element의 위치를 구하고 selenium 창을 닫습니다.
element = driver.find_element_by_class_name("over-scroll")
image_location = element.location
image_size = element.size
driver.quit()
 
# 이미지를 element의 위치에 맞춰서 crop 하고 저장합니다.
im = Image.open(BytesIO(png))
left = image_location['x']
top = image_location['y']
right = image_location['x'] + image_size['width']
bottom = image_location['y'] + image_size['height']
im = im.crop((left, top, right, bottom))
im.save('C:\태훈\python 연습\한이음\저장할 파일명.png')