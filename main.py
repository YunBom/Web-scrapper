#사이트 주소 : https://kr.indeed.com/?from=gnav-viewjob
# html 태그를 찾기 위해 Beautifulsoup 이용

from requests import get
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs

from selenium import webdriver

keyword = "python"

driver = webdriver.Chrome()
base_url = f'https://kr.indeed.com/jobs?q={keyword}&l=&from=searchOnHP&vjk=89395b6ac5014113'
driver.get(base_url)

def indeed_scrap():
    results = []
    soup = BeautifulSoup(driver.page_source, "html.parser")
    job_list = soup.find('ul', class_="jobsearch-ResultsList")
    jobs = job_list.find_all('li', recursive=False)
    for job in jobs:
        zone = job.find("div", class_="mosaic-zone")
        if zone == None:
            anchor = job.select_one("h2 a")
            title = anchor['aria-label']
            link = anchor['href']
            company = job.find('span', class_='companyName')
            location = job.find('div', class_='companyLocation')
            job_data = {
                "link" : f"https://kr.indeed.com{link}",
                "title" : title,
                "company" : company.string,
                "location" : location.string,
            }
            results.append(job_data)
    for result in results:
        print(result, ".........")

""" while (True):
    pass """

indeed_scrap()
