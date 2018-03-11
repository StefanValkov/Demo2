# SoftServe Academy || Automation with Python || Demo2 || Stefan Valkov

from selenium import webdriver
import time

browser = webdriver.Chrome() # initialization the webdriver
browser.maximize_window() # maximize Chrome windows

main_site_url = 'http://demo.fluxday.io/users/sign_in'

xpath_email_element = '//*[@id="user_email"]'
xpath_email_credentials = "lead@fluxday.io"
xpath_password_element = '//*[@id="user_password"]'
xpath_password_credentials = "password"
xpath_submit_button = '//*[@id="new_user"]/div[2]/div[3]/button'
xpath_depatment_button = '/html/body/div[2]/div[1]/ul[2]/li[3]/a'
xpath_testing_department = '//*[@id="pane2"]/div[2]/a[2]/div/div[2]/div[1]'
xpath_element = '//*[@id="project-teams"]/div[4]/div[1]/a'
xpath_testing_tag = '//*[@id="pane3"]/div/div[2]/div[2]/div'

time.sleep(2)

browser.get(main_site_url)

time.sleep(2)
browser.find_element_by_xpath(xpath_email_element).send_keys(xpath_email_credentials)
time.sleep(2)
browser.find_element_by_xpath(xpath_password_element).send_keys(xpath_password_credentials)
time.sleep(2)
browser.find_element_by_xpath(xpath_submit_button).click()

time.sleep(5)

browser.find_element_by_xpath(xpath_depatment_button).click()

time.sleep(4)

browser.find_element_by_xpath(xpath_testing_department).click()

time.sleep(4)
element = browser.find_element_by_xpath(xpath_element)
element_title = element.text
element.click()

time.sleep(4)

assert element_title == browser.find_element_by_xpath(xpath_testing_tag).text #checking if this is the right page
browser.close()
