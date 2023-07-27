from flask import Flask, request, render_template, redirect, url_for
import json
import os
import utils



app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html')



@app.route('/form', methods=['GET', 'POST'])
def form():
    
    with open('allowed_choices.json', 'r') as file:
        allowed_choices = json.load(file)
    with open('columns.json', 'r') as file:
        columns = json.load(file)
    with open('col_descriptions.json', 'r') as file:
        col_descriptions = json.load(file)
    with open('inefficient_inputs.json', 'r') as file:
        inefficient_inputs = json.load(file)
    with open('average_inputs.json', 'r') as file:
        average_inputs = json.load(file)
    with open('efficient_inputs.json', 'r') as file:
        efficient_inputs = json.load(file)
    enterable_features = [col for col in columns[1:] if col not in allowed_choices]

    return render_template('calculator.html', 
                           allowed_choices = allowed_choices, 
                           enterable_features = enterable_features, 
                           inefficient_inputs = inefficient_inputs, 
                           average_inputs = average_inputs, 
                           efficient_inputs = efficient_inputs,
                           default_inputs = None if request.method == 'GET' else request.form.get('default_inputs')
                          )



@app.route('/results/<user>', methods=['GET', 'POST'])
def results(user):

    if request.method == 'GET':
        args = request.args
        if 'user' in args.keys():
            user = args['user']
            # Load USER info
            if user:
                return render_template('result.html', user=user)
            else:
                return f'No results for {user} in our database :('
        else:
            # Load all users
            return ''

    elif request.method == 'POST':
        with open('allowed_choices.json', 'r') as file:
            allowed_choices = json.load(file)

        args = request.form
        user = args['user']
        inputs = {}
        for key, value in args.items():
            if key == 'user':
                continue
            elif key in allowed_choices:
                inputs[key] = value
            else:
                inputs[key] = int(value)

        prediction, max_reductions = predict_and_advise(inputs)


@app.route('/results')
def results():
    return render_template('results.html')

