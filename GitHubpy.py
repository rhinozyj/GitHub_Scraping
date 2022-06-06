# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 10:51:03 2022

@author: Irene Zhang
"""

import io
import requests
import time
import random
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# #%%

# ## Define unwind function
# def unwind(data):
#     linklist = []
#     for d in data:
#         linklist += d
#     return linklist

# ## Open GitHub and manually place filters
# option = webdriver.ChromeOptions()

# # browser = webdriver.Chrome(executable_path='C:/Web Scraping/chromedriver.exe', chrome_options=option)
# browser = webdriver.Chrome(ChromeDriverManager().install())
# url = "https://github.com"

# # Go to desired website
# browser.get(url)


# #%%
# # Switch to the browser window
# browser.switch_to.window(browser.window_handles[-1])

# # initiate the number of pages to be scraped
# def inputbox():
#     print(
#         " #############################################\n#####  Please enter the number of people: #####\n################################################"
#     )
#     people = int(input())
#     pages = round(people / 30) + 1
#     return pages


# pages = inputbox()


# # Start scraping the recruiter url
# # Use explicit waits instead of time.sleep() to wait more time on loading data,
# # and save time on faster loaded data (move next earlier).
# cphref = []

# try:
#     for i in range(pages - 1):
#         next_page = WebDriverWait(browser, 20).until(
#             EC.visibility_of_element_located(
#             (
#                 By.XPATH, '//a[@class="next_page"]'
#                 )
#             )
#         )
#         time.sleep(2)
#         browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(2)
#         browser.execute_script("window.scroll(0, 0);")
#         for j in range(1, 31):
#             path = (
#                 '//li[@class="d-flex flex-items-center flex-justify-end member-list-item js-bulk-actions-item border border-top-0 "]['
#                 + str(j)
#                 + "]//a"
#             )
#             try:
#                 explicit_wait = WebDriverWait(browser, 15).until(
#                     EC.presence_of_element_located((By.XPATH, path))
#                 )
#                 element = browser.find_element(By.XPATH, path)
#                 browser.execute_script("arguments[0].scrollIntoView();", element)
#             except:
#                 pass
#         time.sleep(2)
#         cphref.append(
#             [ele.get_attribute("href") 
#              for ele in browser.find_elements(By.XPATH,
#                  "//li[@class='d-flex flex-items-center flex-justify-end member-list-item js-bulk-actions-item border border-top-0 ']//div[@class='py-3 css-truncate pl-3 flex-auto']//a")])

#         next_page.click()
#         print("Scraped! ")
# except:
#     print("passed!")
#     pass

# # scrape the last page
# time.sleep(20)
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(2)
# browser.execute_script("window.scroll(0, 0);")
# cphref.append(
#     [ele.get_attribute("href") 
#      for ele in browser.find_elements(By.XPATH,
#          "//li[@class='d-flex flex-items-center flex-justify-end member-list-item js-bulk-actions-item border border-top-0 ']//div[@class='py-3 css-truncate pl-3 flex-auto']//a")])


# hreflist = unwind(cphref)


# #%%


# print(len(hreflist))
# recruite_profile_links = []

# cnt = 0

# for recruiterlink in hreflist:
#     print(cnt)
#     browser.get(recruiterlink)
#     # load the page
#     try:
#         explicit_wait = WebDriverWait(browser, 20).until(
#             EC.presence_of_element_located(
#                 (By.XPATH, "//img[@class='avatar avatar-user width-full border color-bg-default']")
#             )
#         )
#     except:
#         pass 
    
#     browser.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
#     time.sleep(0.5)
#     browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(0.5)
    
#     # bg info 
#     # Get name
#     try:
#         name_element = browser.find_elements(By.XPATH, "//h1[@class='vcard-names ']//span[@itemprop='name']")
#         name = [x.text for x in name_element]
#     except:
#         name.append('')
    
#     # Get username
#     try:
#         username_element = browser.find_elements(By.XPATH, "//h1[@class='vcard-names ']//span[@itemprop='additionalName']")
#         username = [x.text for x in username_element]
#     except:
#         username.append('')
        
#     # Get self-introduction
#     try:
#         intro_element = browser.find_elements(By.XPATH, "//div[@class='p-note user-profile-bio mb-3 js-user-profile-bio f4']")
#         intro = [x.text for x in intro_element]
#     except:
#         intro.append('')
        
#     # Get company
#     try:
#         company_element = browser.find_elements(By.XPATH, "//span[@class='p-org']")
#         company = [x.text for x in company_element]
#     except:
#         company.append('')
        
#     # Get location
#     try:
#         location_element = browser.find_elements(By.XPATH, "//li[@itemprop='homeLocation']")
#         location = [x.text for x in location_element]
#     except:
#         location.append('')
        
#     # Get other profiles
#     try:
#         profile_element = browser.find_elements(By.XPATH, "//li//a[@class='Link--primary']")
#         profiles = [x.text for x in profile_element]
#     except:
#         profiles.append('')
    
#     # repo info

#     # Click repo
#     browser.find_element(By.XPATH, "//a[@data-tab-item='repositories']").click()
#     titles = []
#     languages = []
#     links = []
#     descs = []
#     stars = []
#     browser.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
#     time.sleep(0.5)
#     browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(0.5)
#     for j in range(1, 31):
#         path = (
#             '//li[contains(@class,"col-12")]['
#             + str(j)
#             + "]"
#             )  

#     # Get repo titles
#         try:
#             titles_element = browser.find_elements(By.XPATH, path+"//a[@itemprop='name codeRepository']")[0].text
#         except:
#             titles_element = ''
#         titles.append(titles_element)

#     # Get repo languages
#         try:
#             languages_element = browser.find_elements(By.XPATH, path+"//span[@itemprop='programmingLanguage']")[0].text
#         except:
#             languages_element = ''
#         languages.append(languages_element)

#     # Get repo links
#         try:
#             links_element = browser.find_elements(By.XPATH, path+"//h3[@class='wb-break-all']/a")[0].get_attribute("href")
#         except:
#             links_element = ''
#         links.append(links_element)

#     # Get repo descriptions
#         try:
#             descs_element = browser.find_elements(By.XPATH, path+"//p[@itemprop='description']")[0].text
#         except:
#             descs_element = ''
#         descs.append(descs_element)

#     # Get repo stars
#         try:
#             stars_element = browser.find_elements(By.XPATH, path+"//a[contains(@href,'stargazers')]")[0].text
#         except:
#             stars_element = ''
#         stars.append(stars_element)

#     # print response in terminal
#     print("NAME:")
#     print(name, '\n')
#     print("USERNAME:")
#     print(username, '\n')
#     print("SELF-INTRODUCTION:")
#     print(intro, '\n')
#     print("COMPANY:")
#     print(company, '\n')    
#     print("PROFILES:")
#     print(profiles, '\n')    
#     print("LOCATION:")
#     print(location, '\n') 
#     print('TITLES:')
#     print(titles, '\n')      
#     print("LANGUAGES:")
#     print(languages, '\n')
#     print("LINKS:")
#     print(links, '\n')
#     print("DESCRIPTIONS:")
#     print(descs, '\n')
#     print("STARS:")
#     print(stars, '\n')
    
#     cnt += 1
#     if cnt % 50 == 0:
#         time.sleep(random.random() * 10)

#%%
# repo_next_page
option = webdriver.ChromeOptions()

browser = webdriver.Chrome(ChromeDriverManager().install())
url = "https://github.com/clintkitson?tab=repositories"

# Go to desired website
browser.get(url)

# count pages
repo_number = browser.find_elements(By.XPATH, "//a//span[@class='Counter']")[0].text
repo_pages = round(int(repo_number) / 30) + 1

# try:
#     for i in range(repo_pages - 1):
#         browser.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
#         time.sleep(0.5)
#         browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(0.5)
#         titles = []
#         for j in range(1, 31):
#             path = (
#                 '//li[contains(@class,"col-12")]['
#                 + str(j)
#                 + "]")
#             try:
#                 titles_element = browser.find_elements(By.XPATH, path+"//a[@itemprop='name codeRepository']")[0].text
#             except:    
#                 titles_element = ''
#             titles.append(titles_element)
new_url = browser.find_element(By.XPATH, '//a[@class="next_page"]')
# except:
#     print("passed!")
#     pass
# print('TITLES:')
# print(titles, '\n') 

# # scrape the last page
# time.sleep(20)
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(2)
# browser.execute_script("window.scroll(0, 0);")
# try:
#     titles_element = browser.find_elements(By.XPATH, path+"//a[@itemprop='name codeRepository']")[0].text
# except:    
#     titles_element = ''
# titles.append(titles_element)
# print('TITLES:')
# print(titles, '\n')
