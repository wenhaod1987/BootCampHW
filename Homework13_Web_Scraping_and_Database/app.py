import pymongo
from scrape_mars import scrape
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
	
	conn = 'mongodb://localhost:27017'
	client = pymongo.MongoClient(conn)
	db = client.MarsDB
	dic = db.mars.find()[0]
	
	return render_template("index.html", dict = dic)

    

@app.route("/scrape")
def scrape_page():

	conn = 'mongodb://localhost:27017'
	client = pymongo.MongoClient(conn)
	db = client.MarsDB
	db.mars.drop()
	dic_insert = scrape()
	db.mars.insert_one(dic_insert)
	return "Scraping finished. Please go back to:http://127.0.0.1:5000/" 



if __name__ == "__main__":
    app.run(debug=True)

