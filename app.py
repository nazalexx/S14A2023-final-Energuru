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
    enterable_features = [col for col in columns[1:] if col.split(' / ')[0] not in allowed_choices]
    
    if request.method == 'POST':
        autofill_name = request.form.get('autofill_name')
        if autofill_name is not None:
            with open('model/' + autofill_name + '.json', 'r') as file:
                autofill = json.load(file)
        else:
            autofill = None
    
    metadata = {'allowed_choices': allowed_choices,
                'enterable_features': enterable_features,
                'col_descriptions': col_descriptions, 
                'options_for_autofill': {'inefficient_inputs': 'Random inefficient dwelling unit', 
                                         'average_inputs': 'Random average dwelling unit', 
                                         'efficient_inputs': 'Random efficient dwelling unit'}, 
                'autofill_name': None if request.method == 'GET' else autofill_name, 
                'autofill': None if request.method == 'GET' else autofill
               }
    return render_template('form.html', metadata=metadata)



@app.route('/results')
def results():
    with open('results.json', 'r') as file:
        results = json.load(file)
        return render_template('results.html', results=results)



@app.route('/results/<username>', methods=['GET', 'POST'])
def result(username):
    
    if request.method == 'GET':
        with open('results.json', 'r') as file:
            results = json.load(file)
        if username in results:
            prediction = results[username]['prediction']
            max_reductions = results[username]['max_reductions']
            return render_template('result.html', prediction=prediction, max_reductions=max_reductions)
        else:
            return f'No results for {username} in our database :('

    elif request.method == 'POST':
        if os.path.exists('results.json'):
            with open('results.json', 'r') as file:
                results = json.load(file)
        else:
            results = []
        usernames = [result['username'] for result in results]
        if username in usernames:
            return f'There is already {username} in our database. Please input another username!'
        
        with open('model/allowed_choices.json', 'r') as file:
            allowed_choices = json.load(file)
        args = request.form
        inputs = {key: value if key in allowed_choices else int(value) for key, value in args.items()}
        prediction, max_reductions = predict_and_advise(inputs)
        result = {'firstname': inputs['firstname'], 
                  'username': inputs['username'], 
                  'prediction': prediction, 
                  'max_reductions': max_reductions
                 }
        results.append(result)
        with open('results.json', 'w') as file:
            json.dump(results, file)

        return render_template('result.html', result=result)

