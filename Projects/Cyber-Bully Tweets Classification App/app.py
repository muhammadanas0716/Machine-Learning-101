# importing libraries

from ctypes import alignment
from urllib import response
import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image
import pandas as pd
import numpy as np
import re
import string
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from nltk.tokenize import RegexpTokenizer
from nltk import PorterStemmer, WordNetLemmatizer
from helper import *
import pickle

image = Image.open('images/cyber.jpg')

st.image(image, use_column_width= True)

st.write('''
# Cyber-bulling Tweet Recognition App
This app predicts the nature of the tweet into 6 different categories.
* Age
* Ethnicity
* Gender
* Religion
* Other Cyberbullying
* Not Cyberbullying
***
''')

# Text Box
st.header('Enter Tweet')
tweet_input = st.text_area("Tweet Input", height= 150)
print(tweet_input)
st.write('''
***
''')

# st.header("Prediction")
final_output=""
if tweet_input:
    prediction = custom_input_prediction(tweet_input)
    if prediction == "Age":
        final_output = "Age Cyberbullying"
    elif prediction == "Ethnicity":
        final_output = "Ethnicity Cyberbullying"
    elif prediction == "Gender":
        final_output = "Gender Cyberbullying"
    elif prediction == "Not Cyberbullying":
        final_output = "No Cyberbullying"
    elif prediction == "Other Cyberbullying":
        final_output = "Other Cyberbullying"
    elif prediction == "Religion":
        final_output = "Religion Cyberbullying"
else:
    pass

# print output on webpage
st.header("Tweet Classification")
if final_output:
    final_output
else:
    st.write('''
    ***No Tweet Text Entered!***
    ''')
st.write('''
***
''')



# About section
expand_bar = st.expander("About")
expand_bar.markdown('''
* **Source Code:** [https://github.com/mohd-raza/Cyber-Bully-Classification-App](https://github.com/mohd-raza/Cyber-Bully-Classification-App)
* **Dataset:** [https://www.kaggle.com/datasets/andrewmvd/cyberbullying-classification](https://www.kaggle.com/datasets/andrewmvd/cyberbullying-classification)
''')