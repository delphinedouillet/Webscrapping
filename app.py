from flask import Flask, render_template, redirect
import pymongo
import scrape_mars


app = Flask(__name__)

client = pymongo.MongoClient()
db = client.mars_db
collection = db.mars_facts

@app.route("/")
def echo():
    mars = list(db.mars_facts.find())
    return render_template("index.html", mars=mars)


@app.route('/scrape')
def scrape():
    mars = scrape_mars.scrape()
    db.mars_facts.insert_one(mars)
    return redirect("/results")

@app.route("/results")
def results():
    return render_template("results.html")


if __name__ == "__main__":
    app.run(debug=True)