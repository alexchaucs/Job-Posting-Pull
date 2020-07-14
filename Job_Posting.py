import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import time

URL = "https://au.indeed.com/jobs?q=Data+Scientist&l=Sydney+NSW" 

#conducting a request of the stated URL above:
page = requests.get(URL)

##specifying a desired format of “page” using the html parser - this allows python to read the various components of the page, rather than treating it as one long string.

soup = BeautifulSoup(page.text, "html.parser")

#printing soup in a more structured tree format that makes for easier reading
print(soup.prettify())


def extract_job_title_from_result(soup): 
    jobs = []
    for div in soup.find_all(name= "div", attrs={"class":"row"}):
        for a in div.find_all(name= "a", attrs={"data-tn-element": "jobTitle"}):
            jobs.append(a["title"])
    return(jobs)

def extract_company_from_result(soup): 
    companies = []
    for div in soup.find_all(name="div", attrs={"class":"row"}):
        company = div.find_all(name="span", attrs={"class":"company"})
        if len(company) > 0:
            for b in company:
                companies.append(b.text.strip())
        else:
            sec_try = div.find_all(name="span", attrs={"class":"result-link-source"})
            for span in sec_try:
                companies.append(span.text.strip())
    return(companies)
 

def extract_location_from_result(soup): 
    locations = []
    count = 0
    for div in soup.find_all(name= "div", attrs={"class":"row"}):
        try:
             locations.append(div.find(name = 'span', attrs = {"class":"location"}).text.strip())
        except:
             locations.append("Nothing Found")
    return(locations)

def extract_salary_from_result(soup): 
    salaries = []
    for div in soup.find_all(name = "div", attrs = {"class":"row"}):
        try:
            salaries.append(div.find(name = 'span', attrs = {"class":"salaryText"}).text.strip())
        except:
            salaries.append("Nothing Found")
    return salaries


def extract_summary_from_result(soup): 
    summaries = []
    divs = soup.findAll("div", attrs={"class": "summary"})
    for div in divs:
        summaries.append(div.text.strip())
    return(summaries)


def extract_date_from_result(soup): 
    dates = []
    for div in soup.find_all(name= "div", attrs={"class":"row"}):
        for div in div.find_all(name = "span", attrs = {"class":"date"}): 
            dates.append(div.text)
    return(dates)

 

# def extract_job_links(soup):
#     links = []
#     for div in soup.find_all(name= "div", attrs={"class":"row"}):
#         for link in div.findAll('a',href = True):
#             links.append(link.get('href').text)
#     return(links)

def extract_job_links(soup): 
    links = []
    for div in soup.find_all(name= "div", attrs={"class":"row"}):
        for a in div.find_all(name= "a", attrs={"data-tn-element": "jobTitle"}):
            links.append("https://au.indeed.com"+a["href"])
    return(links)

############ 

dict_lists = {"Job Title": extract_job_title_from_result(soup),
              "Company" :extract_company_from_result(soup),
              "Location" : extract_location_from_result(soup),
              "Salary": extract_salary_from_result(soup),
              "Summary":extract_summary_from_result(soup),
              "Date Submitted" : extract_date_from_result(soup),
              "Links": extract_job_links(soup)} 

data_frame_indeed = pd.DataFrame(dict_lists)

print(data_frame_indeed)
data_frame_indeed.to_csv(r'C:\Users\alexc\Desktop\Automation Projects\Job Posting\Job_Application.csv', index = False)
=======
extract_location_from_result(soup)
extract_company_from_result(soup)

