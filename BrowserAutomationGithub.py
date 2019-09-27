from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



browser= webdriver.Chrome(executable_path=r"C:\\Users\\Windows 10\\PycharmProjects\\untitled\\pyselenium\\chromedriver.exe")
browser.get("https://www.github.com")
#SigninPage
username=browser.find_element_by_link_text("Sign in")
username.click()

#userblock
userblock=browser.find_element_by_id("login_field")
userblock.send_keys("youremail@youremail.com")

#passwordbox

password_box=browser.find_element_by_link_text("password")
password_box.send_keys("Yourpasswordhere")
password_box.submit()
#verification that you are human

assert "Yourusername" in browser.page_source
profile_link=browser.find_element_by_class_name("user-profile-link")

link_label=profile_link.get_attribute("innerHTML")

assert "yourusernameforgithub" in link_label

