from flask import Flask, request, render_template, redirect, url_for
import os
import json
import utils



app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html')



@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/blog')
def blog():
    return render_template('blog.html')



@app.route('/data')
def data():
    return render_template('data.html')



@app.route('/mk')
def ml():
    return render_template('mkit/index.html')



@app.route('/form', methods=['GET', 'POST'])
def form():
    
    with open('model/allowed_choices.json', 'r') as file:
        allowed_choices = json.load(file)
    with open('model/columns.json', 'r') as file:
        columns = json.load(file)
    with open('model/col_descriptions.json', 'r') as file:
        col_descriptions = json.load(file)
    with open('model/inefficient_inputs.json', 'r') as file:
        inefficient_inputs = json.load(file)
    with open('model/average_inputs.json', 'r') as file:
        average_inputs = json.load(file)
    with open('model/efficient_inputs.json', 'r') as file:
        efficient_inputs = json.load(file)
    enterable_features = [col for col in columns[1:] if col.split(' / ')[0] not in allowed_choices]

    metadata = {
        'allowed_choices': allowed_choices,
        'enterable_features': enterable_features,
        'col_descriptions': col_descriptions, 
        'inefficient_inputs': inefficient_inputs,
        'average_inputs': average_inputs,
        'efficient_inputs': efficient_inputs,
        'default_inputs': None if request.method == 'GET' else request.form.get('default_inputs')
    }
    return render_template('form.html', metadata=metadata)



@app.route('/results')
def results(user):
    with open('results.json', 'r') as file:
        results = json.load(file)
        return render_template('results.html', results=results)



@app.route('/results/<user>', methods=['GET', 'POST'])
def result(user):
    
    if request.method == 'GET':
        with open('results.json', 'r') as file:
            results = json.load(file)
        if user in results:
            prediction = results[user]['prediction']
            max_reductions = results[user]['max_reductions']
            return render_template('result.html', prediction=prediction, max_reductions=max_reductions)
        else:
            return f'No results for {user} in our database :('

    elif request.method == 'POST':
        if os.path.exists('results.json'):
            with open('results.json', 'r') as file:
                results = json.load(file)
        else:
            results = []
        users = [result['user'] for result in results]
        if user in users:
            return f'There is already {user} in our database. Please input another user name!'
        
        with open('model/allowed_choices.json', 'r') as file:
            allowed_choices = json.load(file)
        args = request.form
        inputs = {key: value if key in allowed_choices else int(value) for key, value in args.items()}
        prediction, max_reductions = predict_and_advise(inputs)
        results.append({'user': user, 'prediction': prediction, 'max_reductions': max_reductions})
        with open('results.json', 'w') as file:
            json.dump(results, file)

        return render_template('result.html', user=user, prediction=prediction, max_reductions=max_reductions)

