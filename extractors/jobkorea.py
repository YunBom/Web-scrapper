# 주소 https://www.jobkorea.co.kr/Search/?stext=python

from requests import get
from bs4 import BeautifulSoup


def extract_jobkorea_jobs(keyword):
    base_url = 'https://www.jobkorea.co.kr/Search/?stext='
    response = get(f'{base_url}{keyword}')
    if response.status_code != 200:
        print(f'Error code : {response.status_code}')
    else:
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.find_all('li', class_="list-post")
        for job_post in jobs:
            job_info = job_post.find_all('div', class_="post-list-info")
            print(job_info)
            print(".")
            print(".")
            print(".")



extract_jobkorea_jobs("python")




