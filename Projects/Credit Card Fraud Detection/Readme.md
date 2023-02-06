
# Introduction

Hey there, this notebook shall go through a very famous, yet overlooked problem - Credit Card Fraud Detection. This project is special, in the sense that this project is highly imbalanced. To solve this problem we'll use techniques like SMOTE, and we'll surely learn something new.

Especially, in these volatile cases, where there is a very less amount of fraud, you need to make a classification machine learning model that'd predict if a transaction is a fraud or not - and without some pre-processing, our model would always predict as NOT fraud, even when it is!

So this project mainly revolves around the idea of imbalance and the techniques used to balance our data before modeling

# About Data

The dataset contains transactions made by credit cards in September 2013 by European cardholders. This dataset presents transactions that occurred in two days, where we have 492 frauds out of 284,807 transactions. The dataset is highly unbalanced, the positive class (frauds) accounts for 0.172% of all transactions.

It contains only numerical input variables which are the result of a PCA transformation. Unfortunately, due to confidentiality issues, we cannot provide the original features and more background information about the data. Features V1, V2, … V28 is the principal components obtained with PCA, the only features which have not been transformed with PCA are 'Time' and 'Amount'. Feature 'Time' contains the seconds elapsed between each transaction and the first transaction in the dataset. The feature 'Amount' is the transaction Amount, this feature can be used for example-dependent cost-sensitive learning. Feature 'Class' is the response variable and it takes value 1 in case of fraud and 0 otherwise.


# Evaluation

Given the class imbalance ratio, we'll measure the accuracy using the Area Under the Precision-Recall Curve (AUPRC). Confusion matrix accuracy is not meaningful for unbalanced classification

As this is just a dataset (And not a Kaggle competition), we'll take 0.2% of our data as our test set, and then we'll begin modelling.

The Dataset/Kaggle Link: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud
