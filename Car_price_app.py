import streamlit as st
import pickle 
import pandas as pd

st.title('Car Price Prediction')
#st displays all we want
st.write('This web app predicts **Car Price** based in some references, please select the correct option.')

#to read the model from the pickle file
with open('model_lr_cp_c0922989.pkl', 'rb') as file:
    model_cp = pickle.load(file)
#model_cp=pickle.load(open('model_lr_cp_c0922989.pkl','rb'))

#get the input from the users
car_brand=st.number_input('**Select the brand:** Kia:0, Chevrolet:1, Mercedes:2, Audi:3, Volkswagen:4, Toyota:5, Honda:6, BMW:7, Hyundai:8, Ford:9')
car_model=st.number_input('**Car Model:**')
car_year=st.number_input('**Year**')
car_mileage=st.number_input('**Mileage**')
car_doors=st.number_input('**Number of Doors**')
car_owner=st.number_input('Number of owners')
car_Fuel_Type_Diesel=st.number_input('**Type of fuel Diesel Yes:1 No:0')
car_Fuel_Type_Electric=st.number_input('**Type of fuel Electric Yes:1 No:0')
car_Fuel_Type_Hybrid=st.number_input('**Type of fuel Hybrid Yes:1 No:0')
car_Fuel_Type_Petrol=st.number_input('**Type of fuel Petrol Yes:1 No:0')


#with this code we can request the input but we need to convert those inputs into dataframes
#to do that we would need to use pandas
#convert the user input to a dataframe
car_data=pd.DataFrame({'Brand':car_brand, 'Model':car_model, 'Year':car_year, 'Mileage':car_mileage, 'Doors':car_doors, 'Owner_Count':car_owner, 
                       'Fuel_Type_Diesel':car_Fuel_Type_Diesel,'Fuel_Type_Electric':car_Fuel_Type_Electric , 'Fuel_Type_Hybrid':car_Fuel_Type_Hybrid,
                       'Fuel_Type_Petrol': car_Fuel_Type_Petrol },index=[0])
#Keys should be the same as column names and also the sequence should be the same

#Predict the price
prediction=model_cp.predict(car_data)

    #display the result
if st.button('Predict'):
    formatted_prediction = f"${prediction[0]:,.2f}"
    st.write(f'The predicted car price is {formatted_prediction}')