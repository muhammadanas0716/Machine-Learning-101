## Goal: Predict the price of an unknown car. 

#### BY: [Montek Singh Kundan](https://github.com/Montekkundan)

## ABSTRACT
Using car price prediction data to predict car prices from user inputs. Using Random Forest Regressor model, we can have an accuracy of 91% with the testing data, which helps predict the selling price of the car, from the user inputs in the flask app.

## INTRODUCTION

Using Kaggle I used the training data to train the model with Random Forest Regressor, to get the best accuracy with the testing data which was used by splitting the training data in the ratio of 8:2. I tried using Linear Regression and Decision Tree Regressor but using Random Forest Regressor the model had the most accuracy with the testing data.

Exporting the model using ‘pickle’ in ‘.pkl’ format I used the model in the flask app. The website takes inputs from the user and sends them to the model which outputs the result to the webpage.

## Using Linear Regression

Using Linear Regression gave an accuracy of 70% with the test data and 72% with the training data, which is quite less as compared to the others which we’ll cover next.

## Using Decision Tree Regressor

Using Linear Regression gave an accuracy of 99% with the test data, which is amazing, and 83% with the training data, I was going to use this but later testing with Random Forest Regressor changed my opinion.

## Using Random Forest Regressor

Using Linear Regression gave an accuracy of 98% with the test data and 91% with the training data, the accuracy with testing data is more than that of the Decision tree model, so finally used this.

## 1. Cleaning the data

Clearing all the null values from the training data and dropping the rows. And having clean data.

## 1. Feature Selection

Reviewing the data, The top features that change the Price of the vehicle are Location, Fuel type, Transmission, and Owner type.

Location:

![](https://github.com/muhammadanas0716/Machine-Learning-Projects-101/blob/main/Projects/Used%20Car%20Price%20Prediction/README_assets/Aspose.Words.3093594f-dc43-4af7-9567-c4ef5becf082.001.png)

Fuel type:

![](https://github.com/muhammadanas0716/Machine-Learning-101/blob/main/Projects/Used%20Car%20Price%20Prediction/README_assets/img.png)

Transmission:

![](https://github.com/muhammadanas0716/Machine-Learning-101/blob/main/Projects/Used%20Car%20Price%20Prediction/README_assets/img_1.png)

Using One-hot encoding on every feature except Owner type, as it has ordered data.
In the end, we have these features:

![](https://github.com/muhammadanas0716/Machine-Learning-Projects-101/blob/main/Projects/Used%20Car%20Price%20Prediction/README_assets/Aspose.Words.3093594f-dc43-4af7-9567-c4ef5becf082.002.png)

The website:

![](https://github.com/muhammadanas0716/Machine-Learning-Projects-101/blob/main/Projects/Used%20Car%20Price%20Prediction/README_assets/Aspose.Words.3093594f-dc43-4af7-9567-c4ef5becf082.003.png)

The features are asked as inputs from the user.

## RESULT:

![](https://github.com/muhammadanas0716/Machine-Learning-Projects-101/blob/main/Projects/Used%20Car%20Price%20Prediction/README_assets/Aspose.Words.3093594f-dc43-4af7-9567-c4ef5becf082.004.png)


## METHODOLOGY

Finally storing the features in a new variable, and storing the price from the data in a variable X and other features in a new variable Y.

Using Linear Regression, Decision Tree, and Random Forest to make an appropriate model.

And we get a linear graph for the model

![](https://github.com/muhammadanas0716/Machine-Learning-Projects-101/blob/main/Projects/Used%20Car%20Price%20Prediction/README_assets/Aspose.Words.3093594f-dc43-4af7-9567-c4ef5becf082.005.png)

Creating the flask app and storing 0 as a variable for every feature in an array.

As the user inputs the values in the HTML form, the flask app updates the data in the array and when the form has been submitted the values in the array are sent to the model as per the values required by the model, and the result in stored in a variable which is shown in the HTML file.


## CONCLUSION:
Using the model in the flask app allows us to input values and predict car prices, this was tested with family and relatives and the result as per 91% accuracy was amazingly accurate.


