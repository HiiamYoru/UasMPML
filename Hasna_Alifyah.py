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

# Input features
gender = st.selectbox('Gender', ['Male', 'Female'])
marital_status = st.selectbox('Marital Status', ['Single', 'Married', 'Prefer not to say'])
occupation = st.selectbox('Occupation', ['Employee', 'House wife', 'Self Employeed', 'Student'])
monthly_income = st.selectbox('Monthly Income', ['Below Rs.10000', '10001 to 25000', '25001 to 50000', 'More than 50000', 'No Income'])
educational_qualifications = st.selectbox('Educational Qualifications', ['School', 'Graduate', 'Post Graduate', 'Ph.D', 'Uneducated'])
feedback = st.selectbox('Feedback', ['Positive', 'Negative'])
age = st.number_input('Age', min_value=0)
family_size = st.number_input('Family Size', min_value=0)
latitude = st.number_input('Latitude')
longitude = st.number_input('Longitude')


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
