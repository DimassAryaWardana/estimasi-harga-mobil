import pickle
import streamlit as st
import numpy as np

# Load model
model = pickle.load(open('estimasi_mobil.sav', 'rb'))

st.title('Estimasi Harga Mobil Bekas')

year = st.number_input('Input Tahun Mobil')
mileage = st.number_input('Input Kilometer Mobil')
tax = st.number_input('Input Pajak Mobil')
mpg = st.number_input('Input Konsumsi BBM (mpg)')
engineSize = st.number_input('Input Engine Size')

predict = ''

if st.button('Estimasi Harga'):
  predict = model.predict(
      [[year, mileage, tax, mpg, engineSize]]
  )
  st.write ('Estimasi Harga Mobil Bekas dalam Ponds : ', predict)
  st.write ('Estimasi Harga Mobil Bekas dalam IDR (Juta) : ', predict*22000)
