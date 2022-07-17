# 1st step install and import modules
import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

job_title =[]
company_name = []
locations_name = []
skills = []


# 2nd step use requstes to fatch the url

result = requests.get("https://wuzzuf.net/search/jobs/?q=python&a=hpb")

# 3rd step save page cntent/markup

src = result.content

#4th step creat soup object to parse content
soup = BeautifulSoup(src, "lxml")


# 5th step find the elements containing info we need
job_titles = soup.find_all("h2", {"class":"css-m604qf"} )
company_names = soup.find_all("a",{"class":"css-17s97q8"})
locations_names = soup.find_all("span",{"class":"css-5wys0k"})
jop_skills = soup.find_all("div",{"class":"css-y4udm8"})


# 6th step loop over returned lists to extrect needed info into other lists
for i in range(len(job_titles)):
    job_title.append(job_titles[i].text)
    company_name.append(company_names[i].text)
    locations_name.append(locations_names[i].text)
    skills.append(jop_skills[i].text)
#print(job_title,company_name,locations_name, skills)
