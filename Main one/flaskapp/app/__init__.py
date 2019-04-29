
from flask import Flask, render_template, redirect, url_for, request



app=Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/animal')
def animal():
	return render_template("animal.html")

@app.route('/global')
def globall():
	return render_template("global.html")


@app.route('/climate')
def climate():
	return render_template("climate.html")


@app.route('/future')
def future():
	return render_template("future.html")

@app.route('/hey')
def hey():
	return render_template("hey.html")

@app.route('/donate', methods=['GET', 'POST'])
def donate():
	return render_template("donate.html")





