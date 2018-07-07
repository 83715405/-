from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")


driver.find_element_by_id("kw").send_keys("传智博客")
driver.find_element_by_id("su").click()
# time.sleep(3)
driver.implicitly_wait(3)
driver.find_element_by_partial_link_text("下一页").click()

# print(driver.page_source)

time.sleep(3)
driver.quit()