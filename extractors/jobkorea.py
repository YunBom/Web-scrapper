# 주소 https://www.jobkorea.co.kr/Search/?stext=python

from requests import get
from bs4 import BeautifulSoup

# Title, Company, Location, Link

def extract_jobkorea_jobs(keyword):
    results = []
    base_url = 'https://www.jobkorea.co.kr/Search/?stext='
    response = get(f'{base_url}{keyword}')
    if response.status_code != 200:
        print(f'Error code : {response.status_code}')
    else:
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.find_all('li', class_="list-post")
        for job_post in jobs:
            job_info = job_post.find_all('div', class_="post-list-info")
            # 회사이름 추출 (어떻게??)
            job_corp = job_post.find_all('div', class_="post-list-corp")
            print(job_corp)
            print(".")
            print(".")
            for info in job_info:
                a = info.find_all('a')
                # title 결과 추출
                title = a[0].string

extract_jobkorea_jobs("python")




