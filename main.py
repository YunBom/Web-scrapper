# pip install flask
# HTML 화면 구현

from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs
from extractors.remoteok import extract_remote_jobs
from flask import Flask, render_template, request

app = Flask("JobScrapper")

@app.route("/")
def home():
    return render_template("home.html", name="BomYi")

@app.route("/search")
def search():
    print(request.args)
    keyword = request.args.get("keyword")
    indeed = extract_indeed_jobs(keyword)
    wwr = extract_wwr_jobs(keyword)
    remoteok = extract_remote_jobs(keyword)
    jobs = wwr + indeed + remoteok
    return render_template("search.html", keyword = keyword, jobs=jobs)

app.run("0.0.0.0")
