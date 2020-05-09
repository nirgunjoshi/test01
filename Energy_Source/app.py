import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask import redirect, request
from flask_sqlalchemy import SQLAlchemy
import json

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import pickle

app = Flask(__name__)

#################################################
# Database Setup
#################################################

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/Alltypes.sqlite"
# db = SQLAlchemy(app)

# # reflect an existing database into a new model
# Base = automap_base()
# # reflect the tables
# Base.prepare(db.engine, reflect=True)

# # Save references to each table
# Samples_Metadata = Base.classes.sample_metadata
# Samples = Base.classes.samples

# db ="sqlite:///db/Alltypes.sqlite"
db = "postgres://xxlseihlmohnre:6667aa7c4ad666c7e6c92755418ff0486278365bde892a02ab7243afd5ca65ad@ec2-50-19-127-115.compute-1.amazonaws.com:5432/denrnahfu7g51u"

ratio = 1000


def one_var_prediction(pred_model, temperature):
    data = pd.DataFrame(np.array([[temperature]]))

    polynomial_features = PolynomialFeatures(degree=2)
    x_poly = polynomial_features.fit_transform(data)

    result = pred_model.predict(x_poly) / ratio

    prediction = float(result.round(2))
    return prediction


def two_var_prediction(pred_model, temperature, coal_consumption):
    data = pd.DataFrame(np.array([[coal_consumption * ratio, temperature]]))

    polynomial_features = PolynomialFeatures(degree=2)
    x_poly = polynomial_features.fit_transform(data)

    result = pred_model.predict(x_poly) / ratio

    prediction = float(result.round(2))
    return prediction


@app.route("/machinelearning")
def machinelearning():

    return render_template("machinelearning.html")


@app.route("/bio")
def bio():

    return render_template("bio.html")


@app.route("/resources")
def resources():

    return render_template("resources.html")


if __name__ == "__main__":
    app.run(port=5006, debug=True)
    # app.run()
