from time import sleep
from selenium import webdriver

browser = webdriver.Firefox()
browser.implicitly_wait(5)

browser.get('https://www.instagram.com/')

login_link = browser.find_element_by_xpath("//body/div[@id='react-root']/section[1]/main[1]/article[1]/div[2]/div["
                                           "1]/div[1]/form[1]/div[1]/div[1]/div[1]/label[1]/input[1]")
login_link.click()

sleep(2)

username_input = browser.find_element_by_css_selector("input[type='text' i]")
password_input = browser.find_element_by_css_selector("input[type='password' i]")

username_input.send_keys("head_like_a_hole_")
password_input.send_keys("gangsta9128")

login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()

await_button = browser.find_element_by_xpath("//button[contains(text(),'Не сейчас')]")
await_button.click()

push_button = browser.find_element_by_xpath("//button[contains(text(),'Не сейчас')]")
push_button.click()
direct = browser.find_element_by_xpath("//body/div[@id='react-root']/section[1]/nav[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/a[1]")
direct.click()
sleep(5)
