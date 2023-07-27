from pandas import DataFrame
with open('columns.json', 'r') as file:
    columns = json.load(file)

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
