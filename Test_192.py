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
xpath_okr_button = '/html/body/div[2]/div[1]/ul[2]/li[6]/a'
xpath_okr_report = '//*[@id="pane2"]/div[2]/a[3]/div'
xpath_okr_id = '//*[@id="pane2"]/div[2]/a[3]/div/div[1]'
xpath_okr_title = '//*[@id="pane3"]/div/div[2]/div[1]'

time.sleep(2)
browser.get(main_site_url)

time.sleep(2)
browser.find_element_by_xpath(xpath_email_element).send_keys(xpath_email_credentials)
time.sleep(2)
browser.find_element_by_xpath(xpath_password_element).send_keys(xpath_password_credentials)
time.sleep(2)
browser.find_element_by_xpath(xpath_submit_button).click()

time.sleep(5)
browser.find_element_by_xpath(xpath_okr_button).click()

time.sleep(4)
browser.find_element_by_xpath(xpath_okr_report).click()
time.sleep(3)

time.sleep(4)
okr = browser.find_element_by_xpath(xpath_okr_id)
okr_title = okr.text
okr.click

assert okr_title == browser.find_element_by_xpath(xpath_okr_title).text #checking if the matching report opens
browser.close()