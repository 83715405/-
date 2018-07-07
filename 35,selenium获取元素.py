from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
hao123 = driver.find_element_by_link_text("hao123")
print(hao123.location)
hao123 = driver.find_element_by_class_name("mnav")
print(hao123.get_attribute("href"))
hao123 = driver.find_element_by_css_selector("#u1 > a:nth-child(2)")
print(hao123.text)
news = driver.find_element_by_xpath('//*[@id="u1"]/a[2]')
print(news.text)
news = driver.find_elements_by_xpath('//*[@id="u1"]/a')
for new in news:
    print(new.text)

driver.quit()