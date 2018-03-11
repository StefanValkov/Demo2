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
xpath_search_field = '//*[@id="search_keyword"]'
xpath_search_term = 'Team'
xpath_found_item = '//*[@id="paginator"]/div/a/div/div[3]'


time.sleep(2)

browser.get(main_site_url)


time.sleep(2)
browser.find_element_by_xpath(xpath_email_element).send_keys(xpath_email_credentials)
time.sleep(2)
browser.find_element_by_xpath(xpath_password_element).send_keys(xpath_password_credentials)
time.sleep(2)
browser.find_element_by_xpath(xpath_submit_button).click()

time.sleep(11)
browser.find_element_by_xpath(xpath_search_field).send_keys(xpath_search_term)

time.sleep(4)
browser.find_element_by_xpath(xpath_search_field).submit()

search = browser.find_elements_by_xpath(xpath_found_item)

assert len(search) > 0, 'Issue' #checking if the search found any results
browser.close()