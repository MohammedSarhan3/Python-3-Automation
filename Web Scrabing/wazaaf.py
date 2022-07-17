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
