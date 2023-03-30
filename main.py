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

    # Define a dictionary mapping the encoded values to their respective labels
    employment_status_dict = {1: 'Business', 0: 'Employee'}
    marital_status_dict = {1: 'Single', 2: 'Married', 3: 'Divorced', 4: 'Widow'}
    state_dict = {0: 'Abia' , 2: 'Adamawa', 19: 'Akwa-Ibom', 4: 'Anambra', 7: 'Bauchi', 6: 'Bayelsa', 5: 'Benue', 36: 'Borno', 9: 'Cross-River',10: 'Delta',
                  11: 'Ebonyi', 12: 'Edo', 13: 'Ekiti', 14: 'Enugu' , 15: 'Gombe' , 16: 'Imo' , 17: 'Jigawa' , 18: 'Kaduna', 3: 'Kano' , 21: 'Katsina',
                  20: 'Kebbi', 22: 'Kogi' , 23: 'Kwara' , 24: 'Lagos' , 25: 'Nasarawa' , 26: 'Niger' , 27: 'Ogun', 28: 'Ondo' , 29: 'Osun', 30: 'Oyo',
                  31: 'Plateau', 32: 'Rivers', 33: 'Sokoto' , 35: 'Taraba', 34: 'Yobe' , 8: 'Zamfara', 1: 'FCT-Abuja'}
    gender_dict = {1: 'Female'}

    # Get input data from the user
    employment_status = st.selectbox('Employment Status', list(employment_status_dict.values()))
    marital_status = st.selectbox('Marital Status', list(marital_status_dict.values()))
    state = st.selectbox('State', list(state_dict.values()))
    requested_amount = st.text_input('Enter Requested Amount needed')
    age = st.text_input('How Old are you?')
    final_sal = st.text_input('What is your Monthly Income?')
    gender = st.selectbox('Gender', list(gender_dict.values()))
    loan_duration = st.text_input('What is the loan duration (Months)?')

    # Convert input data to integers
    employment_status = list(employment_status_dict.keys())[list(employment_status_dict.values()).index(employment_status)]
    marital_status = list(marital_status_dict.keys())[list(marital_status_dict.values()).index(marital_status)]
    state = list(state_dict.keys())[list(state_dict.values()).index(state)]
    requested_amount = int(requested_amount)
    age = int(age)
    final_sal = int(final_sal)
    gender = list(gender_dict.keys())[list(gender_dict.values()).index(gender)]
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

