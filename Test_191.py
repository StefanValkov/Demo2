# SoftServe Academy || Automation with Python || Demo2 || Stefan Valkov

from selenium import webdriver
import time

browser = webdriver.Chrome()  # initialization the webdriver
browser.maximize_window() # maximize Chrome windows

main_site_url = 'http://demo.fluxday.io/users/sign_in'

xpath_email_element = '//*[@id="user_email"]'
xpath_email_credentials = "lead@fluxday.io"
xpath_password_element = '//*[@id="user_password"]'
xpath_password_credentials = "password"
xpath_submit_button = '//*[@id="new_user"]/div[2]/div[3]/button'
xpath_teamlead_button = '/html/body/div[2]/div[1]/ul[3]/li[1]/a'
xpath_gear_option = '//*[@id="pane3"]/div/div[1]/div[2]/a/div'
xpath_change_password = '//*[@id="drop1"]/li[2]'
xpath_change_password_title = '//*[@id="edit_user_12"]/div[3]/div[1]'

time.sleep(2)
browser.get(main_site_url)

time.sleep(2)
browser.find_element_by_xpath(xpath_email_element).send_keys(xpath_email_credentials)
time.sleep(2)
browser.find_element_by_xpath(xpath_password_element).send_keys(xpath_password_credentials)
time.sleep(2)
browser.find_element_by_xpath(xpath_submit_button).click()

time.sleep(5)

browser.find_element_by_xpath(xpath_teamlead_button).click()
time.sleep(3)

browser.find_element_by_xpath(xpath_gear_option).click()
time.sleep(3)

change_password = browser.find_element_by_xpath(xpath_change_password)
change_password_title = change_password.text
change_password.click()

time.sleep(4)

assert change_password_title == browser.find_element_by_xpath(xpath_change_password_title).text
#checking if we are in the change password option
browser.close()