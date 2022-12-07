#사이트 주소 : https://kr.indeed.com/?from=gnav-viewjob
# https://kr.indeed.com/jobs?q=python&l=&from=searchOnHP&vjk=e9dde247a0106af2
# html 태그를 찾기 위해 Beautifulsoup 이용

from bs4 import BeautifulSoup
from selenium import webdriver


driver = webdriver.Chrome()

# 페이지 갯수 추출
def get_page_count(keyword):
    base_url = f'https://kr.indeed.com/jobs?q={keyword}&sort=date&'
    driver.get(base_url)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    pagination = soup.find("nav", attrs={"aria-label" : "pagination"})
    page_count = len(pagination)
    if page_count >= 5:
        return 5
    elif page_count == 0 or page_count == None:
        return 1
    else:
        return page_count


def extract_indeed_jobs(keyword):
    pages = get_page_count(keyword)
    results = []
    for page in range(pages):
        print(keyword, "found", pages, "pages of", page+1, "page")
        base_url = f'https://kr.indeed.com/jobs?q={keyword}&sort=date&&start={page*10}'
        driver.get(base_url)
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
                    "site" : "indeed",
                    "title" : title.replace(",", " "),
                    "company" : company.string.replace(",", " "),
                    "location" : location.string.replace(",", " "),
                    "link" : f"https://kr.indeed.com{link}",
                }
                results.append(job_data)
    # print(results)
    return results

# jobs = extract_indeed_jobs("python")

# while (True):
#     pass
