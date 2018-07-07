from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Option对象
options = Options()
# 设置浏览器无界面
options.set_headless()

driver = webdriver.Chrome(options=options)
driver.get("http://www.baidu.com")
# 保存快照
driver.save_screenshot("baidu.png")

driver.quit()
