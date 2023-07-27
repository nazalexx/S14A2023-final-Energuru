from flask import Flask, request, render_template, redirect, url_for
import json
import os


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/calculator')
def calculator():
    return render_template('calculator.html')


@app.route('/results')
def results():
    return render_template('results.html')

