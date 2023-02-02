## Introduction to the Project
This project will introduce some foundation Machine Learning and Data Science concepts by exploring the problem of heart disease **classification**.

It is intended to be an end-to-end example of what a Data Science and Machine Learning **proof of concept** might look like.

## What we'll end up with

Since we already have a dataset, we'll approach the problem with the following Machine Learning modeling framework.

More specifically, we'll look at the following topics.

* **Exploratory data analysis (EDA)** - the process of reviewing a dataset and finding out more about it.
* **Model training** - create a model(s) to learn to predict a target variable based on other variables.
* **Model evaluation** - evaluating a models predictions using problem-specific evaluation metrics. 
* **Model comparison** - comparing several different models to find the best one.
* **Model fine-tuning** - once we've found a good model, how can we improve it?
* **Feature importance** - since we're predicting the presence of heart disease, are there some more important things for prediction?
* **Cross validation** - if we build a good model, can we be sure it will work on unseen data?
* **Reporting what we've found** - if we had to present our work, what would we show someone?

To work through these topics, we'll use **Pandas**, **Matplotlib**, and **NumPy** for Data Analysis, as well as, **Scikit-Learn** for Machine Learning and modeling tasks.

We'll work through each step and by the end of the notebook, we'll have a handful of models, all of which can predict whether or not a person has heart disease based on a number of different parameters at a considerable accuracy. 

You'll also be able to describe which parameters are more indicative than others, for example, sex may be more important than age.

## Data Source 
What you'll want to do here is dive into the data your problem definition is based on. This may involve, sourcing, defining different parameters, talking to experts about it, and finding out what you should expect.

The original data came from the [Cleveland database](https://archive.ics.uci.edu/ml/datasets/heart+Disease) from UCI Machine Learning Repository.

However, we've downloaded it in a formatted way from [Kaggle](https://www.kaggle.com/ronitf/heart-disease-uci/).

The original database contains 76 attributes, but here only 14 attributes will be used. **Attributes** (also called **features**) are the variables what we'll use to predict our **target variable**.

Attributes and features are also referred to as **independent variables** and a target variable can be referred to as a **dependent variable**.

> We use the independent variables to predict our dependent variable.

Or in our case, the independent variables are a patient's different medical attributes and the dependent variable is whether or not they have heart disease.
