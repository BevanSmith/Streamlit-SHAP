import streamlit as st
import shap
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import pandas as pd

# Define constants
EDUCATION_OPTIONS = ['High School', 'Bachelors', 'Masters', 'PhD']
OCCUPATION_OPTIONS = ['Admin', 'Tech', 'Medical', 'Teaching']

# Load data
X = pd.read_csv("X_streamlit.csv")
y = pd.read_csv("y_streamlit2.csv").values.ravel()
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X, y)

# Define SHAP explainer
explainer = shap.TreeExplainer(rf_model)

# Streamlit UI
st.title("SHAP Explanation App")

education = st.selectbox("Select Education", EDUCATION_OPTIONS)
occupation = st.selectbox("Select Occupation", OCCUPATION_OPTIONS)

# Map selected options to one-hot encoded features
education_index = EDUCATION_OPTIONS.index(education)
occupation_index = OCCUPATION_OPTIONS.index(occupation)
input_data = np.zeros((1, 8))
input_data[0, education_index] = 1
input_data[0, 4 + occupation_index] = 1
 

# Explain the prediction using SHAP
shap_values = explainer.shap_values(input_data)

# Plot SHAP values
st.subheader("SHAP Values")
shap.summary_plot(shap_values, feature_names=['High School', 'Bachelors', 'Masters', 'PhD', 'Admin', 'Tech', 'Medical', 'Teaching'])

# Display plot in Streamlit
st.pyplot(plt.gcf())
