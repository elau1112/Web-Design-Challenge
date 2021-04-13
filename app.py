from flask import Flask, render_template, request, redirect
import pandas as pd
import os
import csv


app = Flask(__name__)
path1="Resources/cities.csv"
d=pd.read_csv(path1)
df = d
df1=df.to_dict('split')
df1
headings = df1["columns"]
data = df1[["data"]]


@app.route("/")
def index():
    return render_template("index.html", headings=headings, data=data)

@app.route("/data")
def table():
    return render_template("Data.html", headings=headings, data=data)

if __name__ == "__main__":
    app.run(debug=True)