from flask import Flask, request, render_template, redirect, url_for
import json
import os



app = Flask(__name__)



@app.route('/')
def get_datetime():
    return f'Hello world!'



@app.route('/calculator')
def get_datetime():
    return f'Hello calculator!'



@app.route('/results')
def get_datetime():
    return f'Hello results!'


