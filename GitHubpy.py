# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 10:51:03 2022

@author: Irene Zhang
"""

import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

#%%

## Open GitHub and manually place filters
option = webdriver.ChromeOptions()
option.add_argument("--incognito")
# browser = webdriver.Chrome(executable_path='C:/Web Scraping/chromedriver.exe', chrome_options=option)
browser = webdriver.Chrome(ChromeDriverManager().install())
url = "https://github.com/0b01"

# Go to desired website
browser.get(url)


#%%
# Switch to the browser window
browser.switch_to.window(browser.window_handles[-1])


# initiate the number of pages to be scraped
def inputbox():
    print(
        " #############################################\n#####  Please enter the number of people: #####\n################################################"
    )
    people = int(input())
    pages = round(people / 25) + 1
    return pages


pages = inputbox()


#%%
# Start scraping the recruiter url
# Use explicit waits instead of time.sleep() to wait more time on loading data,
# and save time on faster loaded data (move next earlier).
cphref = []

try:
    for i in range(pages - 1):
        next_page = WebDriverWait(browser, 20).until(EC.visibility_of_element_located(
            (
                By.XPATH, "//img[@class='avatar avatar-user width-full border color-bg-default']")
            ))
        time.sleep(2)
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        browser.execute_script("window.scroll(0, 0);")
        for j in range(1, 26):
            path = (
                '//li[@class="ember-view profile-list__border-bottom"]['
                + str(j)
                + "]//a"
            )
            try:
                explicit_wait = WebDriverWait(browser, 15).until(
                    EC.presence_of_element_located((By.XPATH, path))
                )
                element = browser.find_element_by_xpath(path)
                browser.execute_script("arguments[0].scrollIntoView();", element)
            except:
                pass
        time.sleep(2)
        cphref.append(
            [
                ele.get_attribute("href")
                for ele in browser.find_elements_by_xpath(
                    '//li[@class="ember-view profile-list__border-bottom"]//div[@class="artdeco-entity-lockup__title ember-view"]//a'
                )
            ]
        )

        next_page.click()
        print("Scraped! ")
except:
    print("passed!")
    pass

# scrape the last page
time.sleep(20)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
browser.execute_script("window.scroll(0, 0);")
cphref.append(
    [
        ele.get_attribute("href")
        for ele in browser.find_elements_by_xpath(
            '//li[@class="ember-view profile-list__border-bottom"]//div[@class="artdeco-entity-lockup__title ember-view"]//a'
        )
    ]
)

#%%
# Wait 20 seconds for page to load
timeout = 20
try:
    # Wait until the avatar link is loaded.
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//img[@class='avatar avatar-user width-full border color-bg-default']")))
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()


# BG info
# Get self-introduction
try:
    intro_element = browser.find_elements(By.XPATH, "//div[@class='p-note user-profile-bio mb-3 js-user-profile-bio f4']")
    intro = [x.text for x in intro_element]
except:
    intro.append('')
# print response in terminal
print("SELF-INTRODUCTION:")
print(intro, '\n')

# Get company
try:
    company_element = browser.find_elements(By.XPATH, "//span[@class='p-org']")
    company = [x.text for x in company_element]
except:
    company.append('')
# print response in terminal
print("COMPANY:")
print(company, '\n')

# Get location
try:
    location_element = browser.find_elements(By.XPATH, "//li[@itemprop='homeLocation']")
    location = [x.text for x in location_element]
except:
    location.append('')
# print response in terminal
print("LOCATION:")
print(location, '\n')

# Get other profiles
try:
    profile_element = browser.find_elements(By.XPATH, "//a[@class='Link--primary']")
    profiles = [x.text for x in profile_element]
except:
    profiles.append('')
# print response in terminal
print("PROFILES:")
print(profiles, '\n')


# Click repo
browser.find_element(By.XPATH, "//a[@data-tab-item='repositories']").click()

#%%
# repo info
# The problem here is that I cannot include null value in the result list, there should be something wrong 
# in first the X.PATH of repo_elements and the for loop below.
repo_elements = browser.find_elements(By.XPATH, "//div[@class='col-10 col-lg-9 d-inline-block']")
titles = []
languages = []
links = []
descs = []
stars = []

//li[contains(@class,"col-12")]
//li[contains(@class,"col-12")][1]//a[contains(@href,'stargazers')]

for i in repo_elements:
    print (i.attribute("class"))
    
    
# Get repo titles
    # titles_list = i.find_elements(By.XPATH, "//a[@itemprop='name codeRepository']")
    # for x in titles_list:
    #     try:
    #         titles_element = x.text
    #     except:
    #         titles_element = 'NA'
    #     titles.append(titles_element)

# Get repo languages
    # languages_list = i.find_elements(By.XPATH, "//span[@itemprop='programmingLanguage']")
    # for x in languages_list:
    #     try:
    #         languages_element = x.text
    #     except:
    #         languages_element = ''
    #     languages.append(languages_element)

# Get repo links
    # links_list = i.find_elements(By.XPATH, "//h3[@class='wb-break-all']/a")
    # for x in links_list:
    #     try:
    #         links_element = x.get_attribute("href")
    #     except:
    #         links_element = ''
    #     links.append(links_element)

# Get repo descriptions
#     descs_list = i.find_elements(By.XPATH, "//p[@itemprop='description']")
#     for x in descs_list:
#         try:
#             descs_element = x.text
#         except:
#             descs_element = ''
#         descs.append(descs_element)

# Get repo stars
    # stars_list = i.find_elements(By.XPATH, "//a[contains(@href,'stargazers')]")
    # for x in stars_list:
    #     try:
    #         stars_element = x.text
    #         print(stars_element)
    #     except:
    #         stars_element = ''
    #     stars.append(stars_element)
    
# print response in terminal
# print('TITLES:')
# print(titles, '\n')
# print("LANGUAGES:")
# print(languages, '\n')
# print("LINKS:")
# print(links, '\n')
# print("DESCRIPTIONS:")
# print(descs, '\n')
# print("STARS:")
# print(stars, '\n')
