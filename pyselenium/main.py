from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait




browser= webdriver.Chrome(executable_path=r"C:\\Users\\Windows 10\\PycharmProjects\\untitled\\pyselenium\\chromedriver.exe")
browser.get("https://www.facebook.com/")
#username
username = browser.find_elements_by_css_selector("input[name=email]")
username[0].send_keys('**********@youremail.com')
#password

password=browser.find_elements_by_css_selector("input[name=pass]")
password[0].send_keys('**********')

loginButton = browser.find_elements_by_css_selector("input[type=submit]")
loginButton[0].click()
print ("Done")
input('Press anything to quit')
driver.quit()
print("Finished") 