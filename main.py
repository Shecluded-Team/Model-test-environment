import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model=pickle.load(open('C:/Users/Public/Documents/streamlit/first_model.pkl','rb'))

#creating a function for prediction
def loan_model(input_data):

    # changing the input data to a numpy array
    input_data_as_np_array = np.asarray(input_data)

    #reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_np_array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    if (prediction[0] == 0):
        return "Not Eligible for loan"
    else:
        return "Eligible for loan"

def main():
    #give a title to the web application
    st.title('Loan Model For Shecluded')

    #getting input data from user
    employment_status = st.text_input('Enter Employment Status')
    marital_status = st.text_input('Enter Marital Status')
    state = st.text_input('Enter you State')
    requested_amount = st.text_input('Enter Requested Amount needed')
    age = st.text_input('How Old are you?')
    final_sal = st.text_input('What is your Monthly Income?')
    gender = st.text_input('Input your Gender')
    loan_duration = st.text_input('what is the loan duration (Months)')


    #convert to int
    employment_status=int(employment_status)
    marital_status=int(marital_status)
    state=int(state)
    requested_amount=int(requested_amount)
    age=int(age)
    final_sal=int(final_sal)
    gender=int(gender)
    loan_duration=int(loan_duration)

    #code for prediction
    result=''

    #creating a button for prediction
    if st.button('Loan Eligibility Result'):
        result= loan_model([employment_status,marital_status,state,requested_amount,age,final_sal,gender,loan_duration])
    st.success(result)


if __name__== '__main__':
    main()

