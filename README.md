CSCI S14A - Building Interactive Web Applications for Data Analysis

# Energuru

## Project Plan

**Meeting Times**: Fridays & Sundays at 12:30pm PDT / 3:30pm EDT / 10:30pm EEST

**Zoom Link**: https://harvard.zoom.us/j/98692370300

**Github Repo**: https://github.com/Harvard-DCE-BIWADA/S14A2023-final-Energuru

**Website Design Template**: https://getbootstrap.com/docs/5.3/examples/carousel/

**Website Location**: http://164.92.97.192/

### Team Members

- Aleksejs Nazarovs - aln755@g.harvard.edu
- Jayden Wang - jaw0880@g.harvard.edu

## Project Basics

The purpose of this project is to create a predictive model and an interactive web-based tool for predicting property's energy consumption based on its features and location. This tool will aim to assist homeowners, prospective buyers and real estate professionals in estimating the potential energy consumption of a property, coupled with tailored recommendations for reducing energy use. The tool will provide transparency and valuable data-driven insights that can inform negotiations, guide investment decisions and foster a more sustainable and energy-conscious property market. It will be implemented in Python, using Flask and scikit-learn.

## Project Description

1. Data description + source
2. Data cleaning (cite)
3. Model creation + reformatting everything for the website to work
4. Website general description and how it will work
   
## Project Structure

```
S14A2023-final-Energuru/
├─── data/
│    └─── energy_cleaned.parquet   # Cleaned data that was used to train the model
├─── model/
│    ├─── allowed_choices.json     # Choices to select from for features with string inputs
│    ├─── average_inputs.json      # Generated inputs for an average property in terms of energy consumption
│    ├─── changeable_features.json # Features that the app can offer to change
│    ├─── col_descriptions.csv     # Descriptions of each feature in the (cleaned) dataset
│    ├─── columns.json             # Columns in the dataset
│    ├─── data_cleaning.ipynb      # Notebook containing the whole data cleaning process
│    ├─── efficient_inputs.json    # Generated inputs for an efficient property in terms of energy consumption
│    ├─── inefficient_inputs.json  # Generated inputs for an inefficient property in terms of energy consumption
│    ├─── model.ipynb              # Notebook with model creation, changeable feature selection, input generation, etc.
│    └─── model.joblib             # Model itself
├─── static/
├─── templates/
│    ├─── _footer.html
│    ├─── _navigation.html
│    ├─── about.html
│    ├─── base.html
│    ├─── blog.html
│    ├─── data.html
│    ├─── form.html
│    ├─── home.html
│    ├─── index.html
│    ├─── result.html
│    └─── results.html
├─── .gitignore
├─── README.md
├─── app.py
├─── requirements.txt
├─── results.json (server-only)
└─── utils.py
```

### Endpoints

1. **Base** -
2. **Component X** - This component does X. It uses Google Tensorflow to do ...
3. **Component Y** - This component does Y. It uses Z to add W features.

## Project Timeline

### Milestone 1 Tasks

Aleksejs Nazarovs:
1. Process book **COMPLETE**

​
All:
1. Github repository **COMPLETE**
2. Project plan **COMPLETE**
   ​

### Milestone 2 Tasks


Aleksejs Nazarovs:
1. Task 1 **IN PROCESS**
2. Task 2 **IN PROCESS**
3. Task 3 **IN PROCESS**
​
Jayden Wang:
1. Task 1 **IN PROCESS**
2. Task 2 **IN PROCESS**
3. Task 3 **IN PROCESS**

All:
1. Agree on revised data topic **COMPLETE**
2. Choose data set **COMPLETE**
3. Divide the work **COMPLETE**


### Milestone 3 Tasks


Aleksejs Nazarovs:
1. Build a model **IN PROCESS**
2. Task 2 **IN PROCESS**
3. Task 3 **IN PROCESS**

​
Jayden Wang:
1. Play with data **IN PROCESS**
2. Build charts **IN PROCESS**
3. Task 3 **IN PROCESS**


All:
1. Task 1 **IN PROCESS**
2. Task 2 **IN PROCESS**
3. Task 3 **IN PROCESS**


### Milestone 4 Tasks


Aleksejs Nazarovs:
1. Build a model **IN PROCESS**
2. Task 2 **IN PROCESS**
3. Task 3 **IN PROCESS**

​
Jayden Wang:
1. Play with data **IN PROCESS**
2. Build charts **IN PROCESS**
3. Task 3 **IN PROCESS**


All:
1. Task 1 **IN PROCESS**
2. Task 2 **IN PROCESS**
3. Task 3 **IN PROCESS**


### Milestone 5 Tasks


Aleksejs Nazarovs:
1. Build a model **IN PROCESS**
2. Task 2 **IN PROCESS**
3. Task 3 **IN PROCESS**

​
Jayden Wang:
1. Play with data **IN PROCESS**
2. Build charts **IN PROCESS**
3. Task 3 **IN PROCESS**


All:
1. Task 1 **IN PROCESS**
2. Task 2 **IN PROCESS**
3. Task 3 **IN PROCESS**​


## References & Citations

- The Stanford GraphBase: A Platform for Combinatorial Computing by Donald E. Knuth (New York: ACM Press, 1994), viii+576pp.
https://www-cs-faculty.stanford.edu/~knuth/sgb.html

- Whitesides, Sue H., and Symposium on Graph Drawing. Graph Drawing : 6th International Symposium, GD '98, Montréal, Canada, August 13-15, 1998 : Proceedings. Springer, 1998.

​- Di Battista, Giuseppe. Graph Drawing : 5th International Symposium, GD'97, Rome, Italy, September 18-20, 1997 : Proceedings. Springer Verlag, 1998.
