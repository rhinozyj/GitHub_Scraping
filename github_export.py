# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 10:14:37 2022

@author: Irene Zhang
"""

import pickle
import csv

## Define Save and Read function for Pickle
def save_obj(obj, saveFileName):
    with open(saveFileName + ".pkl", "wb") as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(saveFileName):
    with open(saveFileName + ".pkl", "rb") as f:
        return pickle.load(f)

microsoft_2 = load_obj("Microsoft_2")
microsoft_3 = load_obj("Microsoft_3")
microsoft = microsoft_2 + microsoft_3


## bg
bg_dict_list = []
for m in microsoft:
    try:
        profile_1 = m[6][0]
    except:
        profile_1 = ''
    try:
        profile_2 = m[6][1]
    except:
        profile_2 = ''
    try:
        profile_3 = m[6][2]
    except:
        profile_3 = ''
    try:
        profile_4 = m[6][3]
    except:
        profile_4 = ''
    bg_dict = {
        'id': microsoft.index(m)+1,
        "github_link":''.join(m[0]),
        "name":''.join(m[1]),
        "username":''.join(m[2]),
        "company":'Microsoft',
        "location":''.join(m[4]),
        "years":m[5][0],
        "profile_1":profile_1,
        "profile_2":profile_2,
        "profile_3":profile_3,
        "profile_4":profile_4,
        "self_intro":''.join(m[7])}
    bg_dict_list.append(bg_dict)

try:
    with open("test_bg.csv", 'w', encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, ['id','github_link','name','username',
                                                'company','location','years',
                                                "profile_1","profile_2","profile_3",
                                                "profile_4",'self_intro'], 
                                lineterminator='\n')
        writer.writeheader()
        for data in bg_dict_list:
            writer.writerow(data)
except IOError:
    print("I/O error")


# repo
repo_dict_list = []
for m in microsoft:
    for i in range(0,len(m[-5])):
        if len(m[-5][i])>0:
            repo_dict = {
                'id': microsoft.index(m)+1,
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
    with open("test_repo.csv", 'w', encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, ['id','name',"username","repo_id",'repo_link',
                                          'title','language','description','stars'], 
                                lineterminator='\n')
        writer.writeheader()
        for data in repo_dict_list:
            writer.writerow(data)
except IOError:
    print("I/O error")
    
    
# ## combined
# combined_dict_list = []
# for m in microsoft_2[:50]:
#     try:
#         profile_1 = m[6][0]
#     except:
#         profile_1 = ''
#     try:
#         profile_2 = m[6][1]
#     except:
#         profile_2 = ''
#     try:
#         profile_3 = m[6][2]
#     except:
#         profile_3 = ''
#     try:
#         profile_4 = m[6][3]
#     except:
#         profile_4 = ''
#     for i in range(0,len(m[-5])):
#         if len(m[-5][i])>0:
#             combined_dict = {
#                 'id': microsoft_2.index(m)+1,
#                 "github_link":''.join(m[0]),
#                 "name":''.join(m[1]),
#                 "username":''.join(m[2]),
#                 "company":'Microsoft',
#                 "location":''.join(m[4]),
#                 "years":m[5][0],
#                 "profile_1":profile_1,
#                 "profile_2":profile_2,
#                 "profile_3":profile_3,
#                 "profile_4":profile_4,
#                 "self_intro":''.join(m[7]),
#                 "repo_link":m[-5][i],
#                 "title": m[-4][i],
#                 "language": m[-3][i],
#                 "description": m[-2][i],
#                 "stars":m[-1][i]}
#             combined_dict_list.append(combined_dict)

# # print(repo_dict_list)

# try:
#     with open("test_combined.csv", 'w') as csvfile:
#         writer = csv.DictWriter(csvfile, fieldnames= ['id','github_link','name',
#                                                       'username','company','location',
#                                                       'years',"profile_1","profile_2",
#                                                       "profile_3","profile_4",'self_intro',
#                                                       'repo_link','title','language',
#                                                       'description','stars'], 
#                                 lineterminator='\n')
#         writer.writeheader()
#         for data in combined_dict_list:
#             writer.writerow(data)
# except IOError:
#     print("I/O error")