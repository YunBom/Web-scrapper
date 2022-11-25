from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs
from extractors.jobkorea import extract_jobkorea_jobs

"""                 job_data = {
                    "title" : title.replace(",", " "),
                    "company" : company.string.replace(",", " "),
                    "location" : location.string.replace(",", " "),
                    "link" : f"https://kr.indeed.com{link}",
                } """

keyword = input("what do you want to search for?")

indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)
# jobkorea = extract_jobkorea_jobs(keyword)

jobs = indeed + wwr

file = open(f'{keyword}.csv', "w")
file.write("Title, Company, Location, Link/n")




