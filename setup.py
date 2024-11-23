import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models
diabetes_model = pickle.load(open("/Users/emily/Downloads/model.pkl", 'rb'))

#sidebar for navigate
with st.sidebar:
    selected = option_menu('Disease Prediction System',
                           ['Diabetes Prediction'],
                           icons=['activity'],
                           default_index = 0)
    

# , hypertension, heart_disease, bmi, HbA1c_level, blood_glucose_level
#Diabetes prediction Page
if(selected == 'Diabetes Prediction'):
    
    #page title
    st.title('Diabetes Prediction using ML')
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Please enter your age-')
        
    with col2:
        hypertension = st.text_input('0 for yes, 1 for no')
    
    with col3:
        heart_disease = st.text_input('0 for yes, 1 for no')
    
    with col1:
        bmi = st.text_input('Please enter your BMI- ')
    
    with col2:
        HbA1c_level = st.text_input('Please enter your Hemoglobin a1c level- ')
    
    with col3:
        blood_glucose_level = st.text_input('Enter your Blood Glusoce Level- ')
    

    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
   
    if st.button('Diabetes Test Result'):
       diab_prediction = diabetes_model.predict([[age, hypertension, heart_disease, bmi, blood_glucose_level]])
       
       if (diab_prediction[0] == 1):
         diab_diagnosis = 'The person is diabetic'
       else:
         diab_diagnosis = 'The person is not diabetic'
       
    st.success(diab_diagnosis)
