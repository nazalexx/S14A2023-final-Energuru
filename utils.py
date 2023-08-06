import numpy as np
from pandas import DataFrame, concat
import json
import joblib
import plotly
import plotly.express as px
with open('model/columns.json', 'r') as file:
    columns = json.load(file)
with open('model/changeable_features.json', 'r') as file:
    changeable_features = json.load(file)
with open('model/allowed_choices.json', 'r') as file:
    allowed_choices = json.load(file)
model = joblib.load('model/model.joblib')



# Convert user's inputs to model input
def user_inputs_to_model_input(inputs):
    model_input = []
    for col in columns[1:]:
        if len(col.split(' / ')) > 1:
            if col.split(' / ')[1]==inputs[col.split(' / ')[0]]:
                model_input.append(1)
            else:
                model_input.append(0)
        else:
            model_input.append(inputs[col])
    model_input = DataFrame([model_input], columns=columns[1:])
    return model_input

def predict_and_advise(inputs):
    model_inputs_df = user_inputs_to_model_input(inputs)

    ignore_values = ['None', 'Other', 'Other Fuel', 'Uninsulated', 'Finished, Uninsulated', 'Unfinished, Uninsulated']
    for col in changeable_features:
        for value in [value for value in allowed_choices[col] 
                      if value != inputs[col] and value not in ignore_values and 'ninsulated' not in value]:
            new_inputs = inputs.copy()
            new_inputs[col] = value
            new_model_input = user_inputs_to_model_input(new_inputs)
            new_model_input.index = [col + ' / ' + value]
            model_inputs_df = concat([model_inputs_df, new_model_input])
    
    predictions = np.exp(model.predict(model_inputs_df))
    prediction = int(predictions[0])
    reductions = predictions[0] - predictions[1:]
    reductions = {name: int(red) for name, red in zip(list(model_inputs_df.index[1:]), list(reductions))}
    
    reductions = {col: {name.split(' / ')[1]: red for name, red in reductions.items() if col==name.split(' / ')[0]} 
                  for col in changeable_features}
    max_reductions = {key: [max(values, key=values.get), values[max(values, key=values.get)]] for key, values in reductions.items()}

    max_reductions = {k: v for k, v in max_reductions.items() if v[1]>0}
    if len(max_reductions)>0:
        sorted_items = sorted(max_reductions.items(), key = lambda item: item[1][1], reverse=True)
        max_reductions = dict(sorted_items)

    return prediction, max_reductions



# Plotting
def plot_results(username, prediction, max_reductions, X=15):
    topX_max_reductions = dict(list(max_reductions.items())[:X])
    df = DataFrame.from_dict(topX_max_reductions, orient='index', columns=['Target', 'Value'])
    fig = px.bar(df, y='Value', text='Value', labels={'index':'Label', 'Value':'Height'}, hover_data=['Target'])
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside',
                      hovertemplate='CHANGE TO: %{customdata[0]}',
                      marker=dict(color='rgb(25,135,84)'))
    fig.update_layout(
    title_text=f"<br>Energuru's annual consumption's estimate<br>for {username}: {prediction} kWh.",
    xaxis_title=None, 
    yaxis_title='Annual Savings (kWh)',
    yaxis=dict(range=[0, 1.15*df['Value'].max()]), 
    plot_bgcolor='white',
    margin=dict(
        t=110,
    )
    )
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON
