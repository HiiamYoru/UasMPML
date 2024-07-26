import pickle
import streamlit as st
import numpy as np

# Membaca model
online_model = pickle.load(open('OnlineFoods.sav','rb'))

# Judul web
st.title('Prediksi Output Online Food')

# Input data dengan contoh angka valid untuk pengujian
Marital_Status = st.text_input('Marital_Status')
Occupation = st.text_input('Occupation')
Monthly_Income = st.text_input('Monthly_Income')
Educational_Qualifications = st.text_input('Educational_Qualifications')
Feedback = st.text_input('Feedback')
Age = st.text_input('Age')
Family_size = st.text_input('Family_size')
latitude= st.text_input('latitude')
longitude=st.text_input('longitude')

prediksi_Onlinefood = ''

# Membuat tombol untuk prediksi
if st.button('Prediksi'):
    try:
        # Konversi input menjadi numerik
        inputs = np.array([[float(Marital_Status), float(Occupation), float(Monthly_Income), float(Educational_Qualificatuons),
                  float(Feedback), float(Age), float(Family_size), float(laitude), float(longitude)]])
        # Lakukan prediksi
        online_prediksi = online_model.predict(inputs)
        
        if online_prediksi[0] == 1:
            prediksi_online = 'Yes'
            st.success(prediksi_online)
        else:
            prediksi_online = '<span style="color:red">No/span>'
            st.markdown(prediksi_online, unsafe_allow_html=True)
    except ValueError:
        st.error("Pastikan semua input diisi dengan angka yang valid.")
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
