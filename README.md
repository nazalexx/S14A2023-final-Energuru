CSCI S-14A - Building Interactive Web Applications for Data Analysis

# Energuru

## Project Plan

**Meeting Times**: Fridays & Sundays at 12:30pm PDT / 3:30pm EDT / 10:30pm EEST

**Zoom Link**: https://harvard.zoom.us/j/98692370300

**Github Repo**: https://github.com/Harvard-DCE-BIWADA/S14A2023-final-Energuru

**Website Design Template**: https://getbootstrap.com/docs/5.3/examples/carousel/

**Website Location**: http://energuru.ai/ (http://164.92.97.192/)

### Team Members

- Aleksejs Nazarovs - aln755@g.harvard.edu / a.nazarovs@outlook.com
- Jayden Wang - jaw0880@g.harvard.edu / jaydenwang0105@gmail.com


## Project Basics

The purpose of this project is to create a predictive model and an interactive web-based tool for predicting dwelling unit's energy consumption based on its features and location. This tool will aim to assist homeowners, prospective buyers and real estate professionals in estimating the potential energy consumption of a dwelling unit, coupled with tailored recommendations for reducing energy use. The tool will provide transparency and valuable data-driven insights that can inform negotiations, guide investment decisions and foster a more sustainable and energy-conscious property market.


## Project Description

### Data Description

The National Renewable Energy Laboratory (NREL) and its research partners [have developed](https://www.nrel.gov/buildings/end-use-load-profiles.html) a database of end-use load profiles (EULP) representing all major end uses, building types, and climate regions in the U.S. commercial and residential building stock. The particular database `baseline_metadata_and_annual_results.csv` (1.5 GB) with approximately 550,000 residential buildings nationwide can be downloaded [here](https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix=nrel-pds-building-stock%2Fend-use-load-profiles-for-us-building-stock%2F2022%2Fresstock_amy2018_release_1%2Fmetadata_and_annual_results%2Fnational%2Fcsv%2F).

### Data Cleaning

The (reproducible) data cleaning process is documented in `model/data_cleaning.ipynb`. The notebook was written as part of the final project for CSCI E-109A Introduction to Data Science at Harvard Extension School by Aleksejs Nazarovs, Ari Neumann, Melina Sotiriou Droz and Sergei Zhits in 2022. It goes over each column of the raw dataset, deletes columns with no information and those irrelevant to (total) energy consumption prediction as well as tries to eliminate variables which essentially contain the same information as some other ones. The notebook also makes sure all the variables are assigned the simplest possible data types. Finally, it converts categorical variables into binary dummy variables. The only change that was made to this notebook as part of this CSCI S-14A project was that the process of dummy variable creation does not exclude the first category anymore. It simplifies user inputs convertion into model inputs but does not cause overfitting since the only model class used for this project is gradient boosting. The cleaned dataset is stored in `data/energy_cleaned.parquet`.

### Data Reformatting and Model Creation

The process documented in `model/model.ipynb` contains some additional minor data cleaning as well as converts the data file from csv to parquet format, for faster reading efficiency and ability to upload to GitHub. The notebook then defines changeable and unchangeable features, which were determined via a thorough and extensive data exploration. The column titles are then reformatted for better readability on the website. Some code elements from the aforementioned project by Nazarovs et al. were borrowed to train the model yet the model itself (namely, histogram-based gradient boosting regressor) was tuned and trained on the updated data. The model was saved as a joblib file, to use it from within the app. The notebook then generates three mock inputs (to be offered to fill out the form by on the website): one for "inefficient", one for "average" and one for "efficient" dwelling unit in terms of energy consumption. The notebook also defines a function to convert user inputs (dictionary without dummy variables) into model input (pandas.DataFrame with dummy variables) as well as a function to generate prediction and biggest possible consumption reductions by feature. Finally, the notebook saves the necessary data (changeable features, feature names and possible values, the three inputs, etc.) into json files.

### App Description

Welcome to Energuru, a revolutionary tool aimed at making energy consumption and efficiency transparent, data-driven, and user-friendly. It predicts a dwelling unit's energy usage and suggests tailored energy reduction strategies.

Energuru is built with Python using Flask web framework. It leverages a comprehensive dataset containing energy profiles of half a million residential buildings across the U.S. After extensive data cleaning, a predictive model was trained, using histogram-based gradient boosting algorithm with the learning rate and the base estimator’s depth being carefully tuned to maximize predictive ability on put-aside test data.

The website is simple and intuitive. You are offered to fill out your information and you receive the result in seconds.

So, let’s get started!

The form is designed to specify each and every detail from location to lightbulbs used and in case you do it, the results will be most accurate. However, if you are interested in a quick analysis of particular features of your apartment and you are interested in approximate results, you can autofill the form with pre-defined inputs of either ‘efficient’, ‘inefficient’ or ‘average’ dwelling unit in terms of energy consumption. You can then specify the particular features you are interested in while being provided with detailed information on every parameter.

Once the form is submitted, Energuru estimates the annual energy consumption in kilowatt-hours while presenting a plot showing where the most energy can be saved, providing particular values and the most efficient substitutes in your particular case. In future, financial savings estimates will be also available.

Energuru has immense potential in fostering a more sustainable and energy-conscious property market. Whether you're a homeowner, a prospective buyer, or a real estate professional, Energuru can assist in making informed, eco-friendly decisions.


## Project Structure

```
S14A2023-final-Energuru/
├─── data/
│    └─── energy_cleaned.parquet   # Cleaned data that was used to train the model
├─── model/
│    ├─── allowed_choices.json     # Choices to select from for features with string inputs
│    ├─── average_inputs.json      # Generated inputs for an average dwelling unit in terms of energy consumption
│    ├─── changeable_features.json # Features that the app can offer to change
│    ├─── col_descriptions.csv     # Descriptions of each feature in the (cleaned) dataset
│    ├─── columns.json             # Columns in the dataset
│    ├─── data_cleaning.ipynb      # Notebook containing the whole data cleaning process
│    ├─── efficient_inputs.json    # Generated inputs for an efficient dwelling unit in terms of energy consumption
│    ├─── inefficient_inputs.json  # Generated inputs for an inefficient dwelling unit in terms of energy consumption
│    ├─── model.ipynb              # Notebook with model creation, changeable feature selection, input generation, etc.
│    └─── model.joblib             # Model itself
├─── static/                       # All static files: CSS, website logo, favicons
│    ├─── dist/
│    │    ├─── css/
│    │    │    ├─── bootstrap.min.css
│    │    │    └─── bootstrap.min.css.map
│    │    └─── js/
│    │         ├─── bootstrap.bundle.min.js
│    │         └─── bootstrap.bundle.min.js.map
│    ├─── favicons/
│    │    ├─── android-chrome-192x192.png
│    │    ├─── android-chrome-512x512.png
│    │    ├─── apple-touch-icon.png
│    │    ├─── favicon-16x16.png
│    │    ├─── favicon-32x32.png
│    │    ├─── favicon.ico
│    │    └─── site.webmanifest
│    ├─── js/
│    │    └─── color-modes.js
│    ├─── energuru.css
│    └─── logo.png
├─── templates/
│    ├─── _navigation.html         # Displays a menu with website's pages
│    ├─── about.html               # Displays info about the app and the team
│    ├─── blog.html                # Displays the blog
│    ├─── data.html                # Displays the data description
│    ├─── form.html                # Displays the main form to enter dwelling unit's details
│    ├─── form0.html               # Displays a mini-form to enter username, to start the main form
│    ├─── index.html               # Base template to extend from
│    ├─── result.html              # Displays prediction and consumption reduction options for a particular user
│    └─── results.html             # Displays prediction and consumption reduction options for all users
├─── .gitignore                    # Files ignored by git
├─── README.md                     # Project description
├─── app.py                        # App itself
├─── requirements.txt              # Required Python packages to run the app
├─── results.json                  # (ignored by git) Contains all the results from the users of the app
└─── utils.py                      # Util functions to process user inputs and generate predictions
```

### Templates

#### `index.html`
The base template and the main page.

#### `form0.html`
A miniform with just one input - username. Upon submitting, the main form gets initiated.

#### `form.html`
The main form. It also contains another mini-form with a selection of autofill if user wants one. The main form itself loops over all the dwelling unit's features. Upon submitting, makes a POST request to the `result` function (`/results/<username>`).

#### `result.html`
Displays a single result of one user. A prediction of annual consumption and a chart with consumption reduction options (bar chart).

#### `results.html`
The same as `result.html` but loops over all the users.

Here is an example of the Results Page!

![graph for Energuru](https://github.com/Harvard-DCE-BIWADA/S14A2023-final-Energuru/assets/87246689/dd732834-8397-45f9-a24f-5d569d90ce34)


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
4. Try to optimize the prediction time (currently 20 seconds) or create a progress bar **IN PROCESS**
5. ...

​
Jayden Wang:
1. Finalize the result templates **IN PROCESS**
2. ...


All:
1. ...​


### Milestone 7 Tasks (08-06-2023)

Aleksejs Nazarovs:
1. ...


Jayden Wang:
1. ...


All:
1. ...


## References & Citations

- Nazarovs, A., Neumann, A., Sotiriou Droz, M., and Zhits, S., 2022. US Residential Energy Consumption. Final Project for CSCI E-109A: Introduction to Data Science. Harvard Extension School. Unpublished.
