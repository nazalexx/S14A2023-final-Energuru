CSCI S-14A - Building Interactive Web Applications for Data Analysis

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

### Data Description

The National Renewable Energy Laboratory (NREL) and its research partners [have developed](https://www.nrel.gov/buildings/end-use-load-profiles.html) a database of end-use load profiles (EULP) representing all major end uses, building types, and climate regions in the U.S. commercial and residential building stock. The particular database `baseline_metadata_and_annual_results.csv` (1.5 GB) with approximately 550,000 residential buildings nationwide can be downloaded [here](https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix=nrel-pds-building-stock%2Fend-use-load-profiles-for-us-building-stock%2F2022%2Fresstock_amy2018_release_1%2Fmetadata_and_annual_results%2Fnational%2Fcsv%2F).

### Data Cleaning

The (reproducible) data cleaning process is documented in `/model/data_cleaning.ipynb`. The notebook was written as part of the final project for CSCI E-109A Introduction to Data Science at Harvard Extension School by Aleksejs Nazarovs, Ari Neumann, Melina Sotiriou Droz and Sergei Zhits in 2022. It goes over each column of the raw dataset, deletes columns with no information and those irrelevant to (total) energy consumption prediction as well as tries to eliminate variables which essentially contain the same information as some other ones. The notebook also makes sure all the variables are assigned the simplest possible data types. Finally, it converts categorical variables into binary dummy variables. The only change that was made to this notebook as part of this CSCI S-14A project was that the process of dummy variable creation does not exclude the first category anymore. It simplifies user inputs convertion into model inputs but does not cause overfitting since the only model class used for this project is gradient boosting. The cleaned dataset is stored in `/data/energy_cleaned.parquet`.

### Data Reformatting and Model Creation

The process documented in `/model/model.ipynb` contains some additional minor data cleaning as well as converts the data file from csv to parquet format, for faster reading efficiency and ability to upload to GitHub. The notebook then defines changeable and unchangeable features, which were determined via a thorough and extensive data exploration. The column titles are then reformatted for better readability on the website. Some code elements from the aforementioned project by Nazarovs et al. were borrowed to train the model yet the model itself (namely, histogram-based gradient boosting regressor) was tuned and trained on the updated data. The model was saved as a joblib file, to use it from within the app. The notebook then generates three mock inputs (to be offered to fill out the form by on the website): one for "inefficient", one for "average" and one for "efficient" dwelling unit in terms of energy consumption. The notebook also defines a function to convert user inputs (dictionary without dummy variables) into model input (pandas.DataFrame with dummy variables) as well as a function to generate prediction and biggest possible consumption reductions by feature. Finally, the notebook saves the necessary data (changeable features, feature names and possible values, the three inputs, etc.) into json files.

### App Description

The main page of the app will contain logo, brief description, useful links, some energy saving motivation, etc. The user will be offered to fill out a form with their dwelling unit's features. Upon filling it, its energy consumption prediction will be made and a bar chart will appear, showing by improving which features and how the best consumption reduction can be achieved. A page with historical results of our users will be deployed too.


## Challenges
- Getting info boxes to work with or without JS
- Splitting the form into 3 columns for the computer version
- Reduce the current prediction time of 20 seconds (vectorize the loop) and/or add a progress bar
- ...


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
├─── results.json                  # (server-only)
└─── utils.py
```

### Templates

#### `index.html`
The base template.

#### `form0.html`
A miniform with just one input - username. Upon submitting, the main form gets initiated.

#### `form.html`
The main form. It also contains another mini-form with a selection of autofill if user wants one. The main form itself loops over all the dwelling unit's features. Upon submitting, makes a POST request to the `result` function (`/results/<username>`).

#### `result.html`
Displays a single result of one user. A prediction of annual consumption and a chart with consumption reduction options.

#### `results.html`
The same as `result.html` but loops over all the users.


### Endpoints

#### `/`
- **GET**: Displays the index template (main page).

#### `/form`
- **GET**: Renders the `form0.html` template, which is a mini-form to enter the username, to start the main form.
- **POST**: Checks if the username exists in the database. Redirects to `/results/<username>` if it does. Redirects to `/form/<username>` if it does not.

#### `/form/<username>`
- **GET**: Takes all the necessary information from the json files and renders the `form.html` template with it (main form). If the user chooses to autofill the form, the parameters are passed to the url, e.g. `?autofill=efficient` and the template is rendered with the autofilled inputs.

#### `/results`
- **GET**: Just displays all the historical results of the app by rendering the `results.html` template.

#### `/results/<username>`
- **GET**: Just displays the result for this particular username if it exists in the database (`result.html`) or displays an error if it does not.
- **POST**: This method is in action upon submitting the form. If the user already exists in the database, an error is returned. If not, the inputs are passed to the `utils.predict_and_advise` function. The database gets updated with the new result and it gets passed to the `result.html` template.


## Project Timeline

### Milestone 1 Tasks (07-02-2023)

Aleksejs Nazarovs:
1. Start the process book **COMPLETE**

​
All:
1. Create a GitHub repository **COMPLETE**
2. Discuss the project plan **COMPLETE**
   ​

### Milestone 2 Tasks (07-09-2023)

All:
1. Agree on a revised data topic **COMPLETE**
2. Choose the data set **COMPLETE**
3. Divide the work **COMPLETE**


### Milestone 3 Tasks (07-16-2023)

Aleksejs Nazarovs:
1. Further explore and clean the data **COMPLETE**
2. Reformat the data to satisfy the project needs **COMPLETE**
3. Divide the features into those that can be realistically changed and those that cannot **COMPLETE**

​
Jayden Wang:
1. Get to know the data cleaning process **COMPLETE**
2. Explore the data **COMPLETE**


All:
1. Decide on what exactly we will try to achieve **COMPLETE**


### Milestone 4 Tasks (07-23-2023)

Aleksejs Nazarovs:
1. Create a function to transform user inputs into model input **COMPLETE**
2. Create a function to predict and advise based on the inputs **COMPLETE**
3. Generate inefficient, average and efficient dwelling unit inputs **COMPLETE**
4. Record all the necessary metadata **COMPLETE**

​
Jayden Wang:
1. Decide on what data visualizations to make **COMPLETE**
2. Understand how to implement these visualizations on the website **COMPLETE**
3. Decide on how to integrate it with the website's template **COMPLETE**


All:
1. Decide on the design and the layot of the website **COMPLETE**
2. Decide on the main pages of the website **COMPLETE**
3. Outline the basic logic of the app **COMPLETE**


### Milestone 5 Tasks (07-30-2023)

Aleksejs Nazarovs:
1. Train the model **COMPLETE**
2. Create a logo **COMPLETE**
3. Implement the backend logic of the form and result generation **COMPLETE**
4. Create the main form template **COMPLETE**
5. Document everything in the README **COMPLETE**

​
Jayden Wang:
1. Create the base template, with all the statics **COMPLETE**
2. Place the logo on the main page **IN PROCESS**
3. Make a prototype template for the results **IN PROCESS**


All:
1. Create a droplet on DigitalOcean **COMPLETE**


### Milestone 6 Tasks (08-04-2023)

Aleksejs Nazarovs:
1. Finalize the form design **IN PROCESS**
2. Add information boxes to the form **IN PROCESS**
3. Rerun the model notebook, to correct mistakes **IN PROCESS**

​
Jayden Wang:
1. Finalize the result templates **IN PROCESS**


All:
1. Task 1 **IN PROCESS**
2. Task 2 **IN PROCESS**
3. Task 3 **IN PROCESS**​


### Milestone 7 Tasks (08-06-2023)

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
1. Task 1 **IN PROCESS**
2. Task 2 **IN PROCESS**
3. Task 3 **IN PROCESS**


## References & Citations

- The Stanford GraphBase: A Platform for Combinatorial Computing by Donald E. Knuth (New York: ACM Press, 1994), viii+576pp.
https://www-cs-faculty.stanford.edu/~knuth/sgb.html
