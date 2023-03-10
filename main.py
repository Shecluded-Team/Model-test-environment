import numpy as np
import pickle
import streamlit as st
import os

# Determine the absolute path to the directory containing this script
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Construct the path to the model file
MODEL_PATH = os.path.join(BASE_DIR, 'first_model.pkl')

# Load the saved model
with open(MODEL_PATH, 'rb') as f:
    loaded_model = pickle.load(f)

# Define a function for prediction
def loan_model(input_data):
    # Convert input data to a NumPy array
    input_data_as_np_array = np.asarray(input_data)

    # Reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_np_array.reshape(1, -1)

    # Make a prediction using the loaded model
    prediction = loaded_model.predict(input_data_reshaped)

    if (prediction[0] == 0):
        return "Not Eligible for loan"
    else:
        return "Eligible for loan"

# Define the main function for the Streamlit app
def main():
    # Set the title of the Streamlit app
    st.title('Loan Model For Shecluded')

    # Get input data from the user
    employment_status = st.text_input('Enter Employment Status')
    marital_status = st.text_input('Enter Marital Status')
    state = st.text_input('Enter you State')
    requested_amount = st.text_input('Enter Requested Amount needed')
    age = st.text_input('How Old are you?')
    final_sal = st.text_input('What is your Monthly Income?')
    gender = st.text_input('Input your Gender')
    loan_duration = st.text_input('what is the loan duration (Months)')

    # Convert input data to integers
    employment_status = int(employment_status)
    marital_status = int(marital_status)
    state = int(state)
    requested_amount = int(requested_amount)
    age = int(age)
    final_sal = int(final_sal)
    gender = int(gender)
    loan_duration = int(loan_duration)

    # Make a prediction using the loan_model function
    result = ''
    if st.button('Loan Eligibility Result'):
        result = loan_model([employment_status, marital_status, state, requested_amount, age, final_sal, gender, loan_duration])

    # Display the prediction result to the user
    st.success(result)

# Call the main function to start the Streamlit app
if __name__ == '__main__':
    main()
