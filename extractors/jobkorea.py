# 주소 https://www.jobkorea.co.kr/Search/?stext=python

from requests import get
from bs4 import BeautifulSoup

# Title, Company, Location, Link

def extract_jobkorea_jobs(keyword):
    results = []
    head_url = 'https://www.jobkorea.co.kr'
    base_url = 'https://www.jobkorea.co.kr/Search/?stext='
    response = get(f'{base_url}{keyword}')
    if response.status_code != 200:
        print(f'Error code : {response.status_code}')
    else:
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.find_all('li', class_="list-post")
        for job_post in jobs:
            job_info = job_post.find_all('div', class_="post-list-info")
            job_corp = job_post.find_all('div', class_="post-list-corp")
            for a in job_corp:
                a = a.find_all('a')
    # company 추출 / <div class="post-list-corp"> -> <a>에서 string만
                company = a[0].string
            for info in job_info:
    # title 추출 / <div class="post-list-info"> -> <a>에서 string만
                a = info.find_all('a')
                title = a[0].string
    # link 추출

    # location 추출
                options = info.find_all('p', class_="option")
                for option in options :
                    span = option.find_all('span', class_="loc long")
        # location 정보가 들어있는 <span class="loc long"> 추출시 정체모를 빈 []가 자꾸만 추출되는 현상 해결 
                    if span != []:
                        location = span[0].string


extract_jobkorea_jobs("python")



