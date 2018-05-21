from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app)


@app.route("/")
def index():
    mars_complete = mongo.db.mars_complete.find_one()
    return render_template('index.html', mars_complete=mars_complete)


@app.route('/scrape')
def scraper():
    mars_complete = mongo.db.mars_complete
    mars_complete_data = scrape_mars.scrape()
    mars_complete.update(
        {},
        mars_complete_data,
        upsert=True
    )
    return redirect("http://localhost:5000/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
