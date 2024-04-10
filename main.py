from flask import Flask, render_template, request
from extractors.indeed import get_jobs

app = Flask("JobScrapper")


@app.route("/")
def home():
    return render_template("home.html", name="discphy")


@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    jobs = get_jobs(keyword)
    return render_template("search.html", keyword=keyword, jobs=jobs)


app.run("0.0.0.0")
