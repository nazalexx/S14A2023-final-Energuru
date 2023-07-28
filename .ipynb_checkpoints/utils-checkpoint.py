from pandas import DataFrame
import json
import joblib
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
    model_input = user_inputs_to_model_input(inputs)
    prediction = int(np.exp(model.predict(model_input))[0])
    
    ignore_values = ['None', 'Other', 'Other Fuel', 'Uninsulated', 'Finished, Uninsulated', 'Unfinished, Uninsulated']
    max_reductions = {}
    for col in changeable_features:
        col_reductions = {}
        for value in [value for value in allowed_choices[col] if value not in ignore_values and 'ninsulated' not in value]:
            new_inputs = inputs
            new_inputs[col] = value
            new_model_input = user_inputs_to_model_input(new_inputs)
            new_prediction = int(np.exp(model.predict(new_model_input))[0])
            if new_prediction < prediction:
                col_reductions[value] = prediction-new_prediction
        if len(col_reductions)>0:
            max_key = max(col_reductions, key=col_reductions.get)
            max_reduction_amount = col_reductions[max_key]
            max_reductions[col] = [max_key, max_reduction_amount]
    if len(max_reductions)>0:
        sorted_items = sorted(max_reductions.items(), key = lambda item: item[1][1], reverse=True)
        max_reductions = dict(sorted_items)
    return prediction, max_reductions
