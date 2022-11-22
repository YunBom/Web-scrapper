from requests import get
from bs4 import BeautifulSoup


def extract_wwr_jobs(keyword):
    base_url = "https://weworkremotely.com/remote-jobs/search?term="
    head_url = "https://weworkremotely.com"

    response = get(f"{base_url}{keyword}")
    if response.status_code != 200:
        print(f"Error Code {response.status_code}")
    else:
        results = []
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.find_all('section', class_="jobs")  
        for job_section in jobs:
            job_posts = job_section.find_all('li')
            job_posts.pop(-1)
            for post in job_posts:
                anchors = post.find_all('a')
                anchor = anchors[1]
                link = anchor['href']
                company, kind, location = anchor.find_all('span', class_="company")
                title = anchor.find('span', class_="title")
                job_data = {
                    "title" : title.string.replace(",", " "),
                    "company" : company.string.replace(",", " "),
                    "kind" : kind.string.replace(",", " "),
                    "location" : location.string.replace(",", " "),
                    "link" : f'{head_url}{link}'
                }
                results.append(job_data)
        # print(results)

        # 리스트 형식으로 결과 리턴
        return results

extract_wwr_jobs("python")
