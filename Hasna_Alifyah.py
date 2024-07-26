import pickle
import streamlit as st
import numpy as np

# Load the model
try:
    online_model = pickle.load(open('OnlineFoods_new.sav', 'rb'))
except Exception as e:
    st.error(f"Error loading model: {e}")

# Title of the web app
st.title('Prediksi Output Online Food')

# Input fields for user data
Marital_Status = st.text_input('Marital_Status')
Occupation = st.text_input('Occupation')
Monthly_Income = st.text_input('Monthly_Income')
Educational_Qualifications = st.text_input('Educational_Qualifications')
Feedback = st.text_input('Feedback')
Age = st.text_input('Age')
Family_size = st.text_input('Family_size')
latitude = st.text_input('latitude')
longitude = st.text_input('longitude')

prediksi_Onlinefood = ''

# Create a button for prediction
if st.button('Prediksi'):
    try:
        # Convert input to numeric values
        inputs = np.array([[float(Marital_Status), float(Occupation), float(Monthly_Income), float(Educational_Qualifications),
                            float(Feedback), float(Age), float(Family_size), float(latitude), float(longitude)]])
        
        # Make prediction
        online_prediksi = online_model.predict(inputs)
        
        # Display prediction
        if online_prediksi[0] == 1:
            prediksi_online = 'Yes'
            st.success(prediksi_online)
        else:
            prediksi_online = '<span style="color:red">No</span>'
            st.markdown(prediksi_online, unsafe_allow_html=True)
    except ValueError:
        st.error("Pastikan semua input diisi dengan angka yang valid.")
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
