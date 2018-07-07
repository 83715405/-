from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://baidu.com")
print(driver.current_url)
print(driver.page_source)
print(driver.get_cookies())
cookie = {cookie["name"]:cookie["value"] for cookie in driver.get_cookies()}
print(cookie)
driver.quit()