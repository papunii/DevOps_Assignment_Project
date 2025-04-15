from flask import Flask, render_template, request, redirect
import json
import subprocess

app = Flask(__name__)

SCRAPED_FILE = "scraped_data.json"

def run_scraper(url):
    subprocess.run(["node", "scrape.js"], env={"SCRAPE_URL": url}, check=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_url = request.form.get("url")
        if user_url:
            try:
                run_scraper(user_url)
            except Exception as e:
                return f"<h2>Scraping Failed</h2><p>{e}</p>"

    try:
        with open(SCRAPED_FILE, "r") as f:
            data = json.load(f)
        return render_template("index.html", title=data.get("title"), heading=data.get("heading"))
    except Exception:
        return render_template("index.html", title="No Data", heading="Please enter a URL to scrape.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

