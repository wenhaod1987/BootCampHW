#copy setup from jupyter notebook
import numpy as np
import pandas as pd
import datetime as dt
# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)


# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def homepage():
	return(
		f"This is Hawaii weather station API!</br>"
		f"date and precipitation for last year: /api/v1.0/precipitation</br>"
		f"Station: /api/v1.0/stations</br>"
		f"temperature for last year: /api/v1.0/tobs</br>"
		f"min, ave, and max temperature: /api/v1.0/<start>  or  /api/v1.0/<start>/<end>"
			)

@app.route("/api/v1.0/precipitation")
def prcp():
	one_year_ago = dt.date.today() - dt.timedelta(days=365)
	prcp_query = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >=one_year_ago ).all()
	date_ls=[]
	prcp_ls=[]
	for x in prcp_query:
		date_ls.append(x.date)
		prcp_ls.append(x.prcp)
	prcp_dic = dict(zip(date_ls,prcp_ls))
	return jsonify(prcp_dic)

@app.route("/api/v1.0/stations")
def stations():
	station_query = session.query(Station.name).all()
	station_list = list(np.ravel(station_query))

	return jsonify(station_list)

@app.route("/api/v1.0/tobs")
def temp():
	one_year_ago = dt.date.today() - dt.timedelta(days=365)
	temp_query = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >=one_year_ago ).all()
	date_ls=[]
	tobs_ls=[]
	for x in temp_query:
		date_ls.append(x.date)
		tobs_ls.append(x.tobs)
	tobs_dic = dict(zip(date_ls,tobs_ls))
	return jsonify(tobs_dic)

@app.route("/api/v1.0/<start>")
def start_only(start):
	result = session.query(func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs)).\
		filter(Measurement.date>=start)
	result_ls = list(np.ravel(result))
	return jsonify(result_ls)

@app.route("/api/v1.0/<start>/<end>")
def start_n_end(start, end)
	result = session.query(func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs)).\
		filter(Measurement.date>=start).filter(Measurement.date<=end)
	result_ls = list(np.ravel(result))
	return jsonify(result_ls)


if __name__ == "__main__":
    app.run(debug=True)
