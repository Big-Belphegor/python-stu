__author__ = "Alien"
from selenium import webdriver

cookies = [xxx]

browser=webdriver.Chrome()
browser.get("https://www.jd.com")
for cookie in cookies:
    browser.add_cookie(cookie)

# driver = webdriver.Chrome()
# driver.get("https://www.jd.com")
# print(driver.title)



