## Introduction
Hey everyone! In this project, we're going to go through an end-to-end machine learning project with the goal of predicting if the passenger will be transferred to an alternate dimension or not.

Since we're trying to predict a class (`True` or `False`), this kind of problem is known as a classification problem.

The data we'll use is here from a [Kaggle competition](https://www.kaggle.com/competitions/spaceship-titanic/overview) - Spaceship Titanic, Predict which passengers are transported to an alternate dimension.

## Background & Problem Statement (Copied from Kaggle)
Welcome to the year 2912, where your data science skills are needed to solve a cosmic mystery. We've received a transmission from four lightyears away and things aren't looking good.

The Spaceship Titanic was an interstellar passenger liner launched a month ago. With almost 13,000 passengers on board, the vessel set out on its maiden voyage transporting emigrants from our solar system to three newly habitable exoplanets orbiting nearby stars.

While rounding Alpha Centauri en route to its first destination—the torrid 55 Cancri E—the unwary Spaceship Titanic collided with a spacetime anomaly hidden within a dust cloud. Sadly, it met a similar fate as its namesake from 1000 years before. Though the ship stayed intact, almost half of the passengers were transported to an alternate dimension!

## Data

Looking at the [dataset from Kaggle](https://www.kaggle.com/competitions/spaceship-titanic/data).

There are 2 datasets:

* Train.csv - Personal records for about two-thirds (~8700) of the passengers, to be used as training data. The target variable is the `Transported` column
* Test.csv - Personal records for the remaining one-third (~4300) of the passengers, to be used as test data. Your task is to predict the value of `Transported` for the passengers in this set. 

## Evaluation

For this problem, [Kaggle has set the evaluation metric to being [classification accuracy](https://developers.google.com/machine-learning/crash-course/classification/accuracy) (Classification Accuracy)](https://www.kaggle.com/competitions/spaceship-titanic/overview/evaluation).

To see how well our model is doing, we'll make our predictions on the test set, create a DataFrame with the results and submit our DataFrame (After converting to CSV) to Kaggle and get out the result.
