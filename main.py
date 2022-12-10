from extractors.wwr import extract_wwr_jobs
from extractors.indeed import extract_indeed_jobs
from extractors.remoteok import extract_remote_jobs
from file import save_file
from flask import Flask, render_template, redirect, request, send_file

app = Flask("JobScrapper")

db = {}

@app.route("/")
def home():
    return render_template("home.html", name="BomYi")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    print(request.args)
    if keyword == None:
        return redirect("/")
    if keyword in db:
        jobs = db[keyword]
    else:
        indeed = extract_indeed_jobs(keyword)
        wwr = extract_wwr_jobs(keyword)
        remoteok = extract_remote_jobs(keyword)
        jobs = wwr + indeed + remoteok
        db[keyword] = jobs
    return render_template("search.html", keyword=keyword, jobs=jobs)

@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword not in db :
        return redirect(f'/search?keyword={keyword}')
    save_file(keyword, db[keyword])
    return send_file(f'{keyword}.csv', as_attachment=True)

app.run("0.0.0.0")
