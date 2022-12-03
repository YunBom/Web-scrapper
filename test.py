# 스크랩 데이터 파일로 저장

from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs

keyword = input("search?")

file = open(f'{keyword}.csv', "w")

indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)
jobs = indeed + wwr

file.write("title, company, url\n")

for job in jobs:
    file.write(f"{job['title']},{job['company'],{job['link']}}\n")

file.close