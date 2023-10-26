import pickle
import streamlit as st

harga_rumah = pickle.load(open('rumah_boston.sav', 'rb'))

st.title('Estimasi Harga Rumah Di Boston')

CRIM = st.number_input('Tingkat Rawan Kriminalitas dalam satu tahun terakhir')
ZN = st.number_input('Tingkat Kepadatan Penduduk per 25.000 sq.ft')
CHAS = st.selectbox('Apakah ingin dekat sungai atau tidak ?', ['Ya', 'Tidak'])

if CHAS == 'YA':
    CHAS = 1
else:
    CHAS = 0
NOX = st.number_input('Tingkat Keasaman Tanah')
RM = st.number_input('Jumlah Ruangan Hunian')
AGE = st.number_input('Usia Bangunannya')
DIS = st.number_input('Jarak dari pusat pekerjaan terdekat')
TAX = st.number_input('Rata rata pajak per $10,000')

prediksi = ''

if st.button('Estimasi'):
    prediksi = harga_rumah.predict([[CRIM,ZN,CHAS,NOX,RM,AGE,DIS,TAX]])

    st.write ('Estimasi harga dalam USD per $1000 : ', prediksi)
    st.write ('Atau : ', prediksi*1000)
    st.write ('Dalam Rupiah : ', (prediksi*1000)*14000)