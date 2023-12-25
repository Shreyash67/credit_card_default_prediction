# Credit Card Default Prediction

## Overview
Credit Card defaulter prediction is a classification model for a common dataset. Prediction of the next month's credit card defaulter based on customer demographic and last six months' behavioral data.

## Dataset Information
From April 2005 to September 2005, this dataset comprises information on default payments, demographic variables, credit data, payment history, and bill statements for credit card clients in _Taiwan_.

## Technical Aspect
This project is divided into two part:
1. Training a [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html) classification model to predict defaulter as accurate as possible.
	- Cleaning the datasets, fixing all features
	- Apply Classification ML model
2. Building and hosting a Flask web app on Heroku.
	- Build the web app using Flask API
	- Upload the project on GitHub
    - Get the customer information from Web app
    - Display the prediction 

## Installation
The Code is written in Python 3.8. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries.

## Software and Tools Required

1. [Github account](https://github.com)
2. [AWS Account](https://aws.amazon.com/console/)
3. [VS code IDE](https://code.visualstudio.com/)
4. [GitCli](https://git-scm.com/downloads)

Create a new environment of project 

```
conda create -p env python==3.8 -y

```

## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://numpy.org/images/logo.svg" width=100>](https://numpy.org)    [<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Pandas_logo.svg/450px-Pandas_logo.svg.png" width=150>](https://pandas.pydata.org)    [<img target="_blank" src="https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png" width=150>](https://scikit-learn.org/stable)   [<img target="_blank" src="https://www.statsmodels.org/stable/_images/statsmodels-logo-v2-horizontal.svg" width=170>](https://www.statsmodels.org)

[<img target="_blank" src="https://matplotlib.org/_static/logo2_compressed.svg" width=170>](https://matplotlib.org)      [<img target="_blank" src="https://seaborn.pydata.org/_static/logo-wide-lightbg.svg" width=150>](https://seaborn.pydata.org)

[<img target="_blank" src="https://jupyter.org/assets/logos/rectanglelogo-greytext-orangebody-greymoons.svg" width=150>](https://jupyter.org)