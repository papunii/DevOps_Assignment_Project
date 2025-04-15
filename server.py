from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def serve_html():
    try:
        with open("scraped_data.json", "r") as file:
            data = json.load(file)
        return render_template("index.html", title=data.get("title", "No Title"), heading=data.get("heading", "No Heading"))
    except Exception as e:
        return f"<h1>Error:</h1><p>{str(e)}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
