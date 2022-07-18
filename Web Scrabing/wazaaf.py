# 1st step install and import modules
import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

job_title =[]
company_name = []
locations_name = []
skills = []
links=[]
salary=[]
responsapility = []
date =[]

while True:
    # 2nd step use requstes to fatch the url
    try:
        page_number = 0
        result = requests.get(f"https://wuzzuf.net/search/jobs/?a=hpb&q=python&start={page_number}")

        # 3rd step save page cntent/markup
        src = result.content

        # 4th step creat soup object to parse content
        soup = BeautifulSoup(src, "lxml")
        page_limit = int(soup.find("strong").text)
        if (page_number > page_limit // 15):
            break

        # 5th step find the elements containing info we need
        job_titles = soup.find_all("h2", {"class":"css-m604qf"} )
        company_names = soup.find_all("a",{"class":"css-17s97q8"})
        locations_names = soup.find_all("span",{"class":"css-5wys0k"})
        jop_skills = soup.find_all("div",{"class":"css-y4udm8"})
        posted_new= soup.find_all("div",{"class":"css-4c4ojb"})
        posted_old= soup.find_all("div",{"class":"css-do6t5g"})
        posted=[*posted_new,*posted_old]

        # 6th step loop over returned lists to extrect needed info into other lists
        for i in range(len(job_titles)):
            job_title.append(job_titles[i].text)
            links.append(job_titles[i].find("a",{"class":"css-o171kl"}).attrs['href'])
            company_name.append(company_names[i].text)
            locations_name.append(locations_names[i].text)
            skills.append(jop_skills[i].text)
            date_text = posted[i].text.replace("-","").strip()
            date.append(date_text)
        page_number +=1
        print("page switched")
    except:
        print("eror")
        break
for ilnk in links:
    results = requests.get(links)
    src = results.content
    soup = BeautifulSoup(src , "lxml")
    salaries = soup.find_all("span",{"class":"css-4xky9y"})
    salary.append(salaries.text.strip())
    requrments=soup.find("div",{"class":"css-1t5f0fr"}).ul
    respon_text=""
    for li in requrments.find_all("li"):
        respon_text += li.text + "|"
    respon_text=respon_text[0:-2]
    responsapility.append(respon_text)


#print(job_title,company_name,locations_name, skills)

# 7th step create csv file and fill it with values
file_list =[job_title,company_name,locations_name,skills,links,salary,responsapility,date]
exported = zip_longest(*file_list)
with open("E:\mohammad\dijongo\myprojects\AUTOMATION/momo.csv", "w") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["job title","company name", "lacation", "skills","links","salaryes","responsapility","posted job"] )
    wr.writerows(exported)
