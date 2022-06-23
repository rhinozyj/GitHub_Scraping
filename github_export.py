# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 10:14:37 2022

@author: Irene Zhang
"""

import pickle
import time
import csv
import re
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import InvalidArgumentException

## Define Save and Read function for Pickle
def save_obj(obj, saveFileName):
    with open(saveFileName + ".pkl", "wb") as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(saveFileName):
    with open(saveFileName + ".pkl", "rb") as f:
        return pickle.load(f)

option = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

## change company name
apple = load_obj("apple")

## bg
bg_dict_list = []
for m in apple:        
    linkedin = ''
    email = ''
    twitter = ''
    other_profile = ''
    for profile in m[6]:
        if re.search('linkedin', profile) != None:
            linkedin = profile
        elif re.search('.@', profile) != None:
            email = profile
        elif re.search('^@', profile) != None:
            twitter = profile
        else:
            if re.search('\.', profile) != None:
                other_profile = profile 
    if linkedin == '' and other_profile != '':
        browser.get(other_profile) 
        try:
            linkedin = browser.find_elements(By.XPATH,".//a[contains(@href,'linkedin')]")[0].get_attribute("href")
        except WebDriverException:
            pass
        except InvalidArgumentException:
            try:
                other_profile = "http://"+other_profile
                linkedin = browser.find_elements(By.XPATH,".//a[contains(@href,'linkedin')]")[0].get_attribute("href")
            except:
                pass
        except IndexError:
            pass
        finally:
            time.sleep(2)
            print(linkedin)
    bg_dict = {
        'id': apple.index(m)+1,
        "github_link":''.join(m[0]),
        "name":''.join(m[1]),
        "username":''.join(m[2]),
        "company":'Apple',
        "location":''.join(m[4]),
        "years":m[5][0],
        "linkedin":linkedin,
        "email":email,
        "twitter":twitter,
        "other_profile":other_profile,
        "self_intro":''.join(m[7])}
    bg_dict_list.append(bg_dict)

try:
    ## change file name
    with open("apple_bg.csv", 'w', encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, ['id','github_link','name','username',
                                                'company','location','years',
                                                "linkedin","email","twitter",
                                                "other_profile",'self_intro'], 
                                lineterminator='\n')
        writer.writeheader()
        for data in bg_dict_list:
            writer.writerow(data)
except IOError:
    print("I/O error")


# repo
repo_dict_list = []
for m in apple:
    for i in range(0,len(m[-5])):
        if len(m[-5][i])>0:
            repo_dict = {
                'id': apple.index(m)+1,
                "name":''.join(m[1]),
                "username":''.join(m[2]),
                "repo_id": i+1,
                "repo_link":m[-5][i],
                "title": m[-4][i],
                "language": m[-3][i],
                "description": m[-2][i],
                "stars":m[-1][i]}
            repo_dict_list.append(repo_dict)

try:
    # change file name
    with open("apple_repo.csv", 'w', encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, ['id','name',"username","repo_id",'repo_link',
                                          'title','language','description','stars'], 
                                lineterminator='\n')
        writer.writeheader()
        for data in repo_dict_list:
            writer.writerow(data)
except IOError:
    print("I/O error")
    
    
