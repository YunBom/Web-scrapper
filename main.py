from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs
from extractors.jobkorea import extract_jobkorea_jobs

keyword = input("what do you want to search for?")

file = open(f'{keyword}.csv'. "w")



indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)
# jobkorea = extract_jobkorea_jobs(keyword)

jobs = indeed + wwr


