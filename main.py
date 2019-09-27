from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



browser= webdriver.Chrome(executable_path=r"C:\\Users\\Windows 10\\PycharmProjects\\untitled\\pyselenium\\chromedriver.exe")
browser.get("https://www.facebook.com/")
#username
username = browser.find_elements_by_css_selector("input[name=email]")
username[0].send_keys('**********')
#password

password=browser.find_elements_by_css_selector("input[name=pass]")
password[0].send_keys('*************')

loginButton = browser.find_elements_by_css_selector("input[type=submit]")
loginButton[0].click()
print(browser.title)
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[id^='u_0_'] textarea[name=xhpc_message]")))
browser.find_element_by_css_selector("div[id^='u_0_'] textarea[name=xhpc_message]").send_keys("Hie")
print("Typed Hie within Facebook Status Box")