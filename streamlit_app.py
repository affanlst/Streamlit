import pickle
import streamlit as st
import pandas as pd
import os
import numpy as np
import altair as alt
import streamlit as st
import urllib.request



# Fungsi untuk menampilkan halaman utama
def main_page():
    st.title("Halaman Utama")
    st.header("Selamat datang di aplikasi Streamlit!")
    st.subheader("Dibuat Oleh : ")
    st.markdown("Nama   : Affan Naufal Syarif AL Ghifari")
    st.markdown("NIM    : 223307088")
    st.markdown("Kelas  : 3D")

# Membuat sidebar
sidebar = st.sidebar.selectbox("Navigasi", ("Home", "Car Price","Bar","About"))

def carPrice_page():
    url = 'https://github.com/affanlst/streamlit/blob/3e562cf996d505f4a529355ffe961c00360a4f73/model_prediksi_harga_mobil.sav'
    response = urllib.request.urlopen(url)
    data = response.read()

    print(data)
    model = pickle.load(open('https://github.com/affanlst/streamlit/blob/3e562cf996d505f4a529355ffe961c00360a4f73/model_prediksi_harga_mobil.sav', 'rb'))

    st.title('Prediksi Harga Mobil')

    st.header("Dataset")
    url = "https://github.com/affanlst/streamlit/blob/main/CP.csv"
    column = ['car_ID','symboling','CarName','fueltype','aspiration','doornumber','carbody','drivewheel','enginelocation','wheelbase','carlength','carwidth','carheight','curbweight','enginetype','cylindernumber','enginesize','fuelsystem','boreratio','stroke','compressionratio','horsepower','peakrpm','citympg','highwaympg','price'
]
    df1 = pd.read_csv('CP.csv', names=column)
    st.dataframe(df1)

    st.write("Grafik Highway-mpg")
    chart_highwaympg = pd.DataFrame(df1, columns=["highwaympg"])
    st.line_chart(chart_highwaympg)

    st.write("Grafik curbweight")
    chart_curbweight = pd.DataFrame(df1, columns=["curbweight"])
    st.line_chart(chart_curbweight)

    st.write("Grafik horsepower")
    chart_horsepower = pd.DataFrame(df1, columns=["horsepower"])
    st.line_chart(chart_horsepower)

    highwaympg = st.number_input('Highway-mpg', 0, 10000000)
    curbweight = st.number_input('Curbweight', 0, 10000000)
    horsepower = st.number_input('Horsepower', 0, 10000000)

    if st.button('Prediksi'):
        car_prediction = model.predict([[highwaympg, curbweight, horsepower]])

        harga_mobil_str = np.array(car_prediction)
        harga_mobil_float = float(harga_mobil_str[0])

        harga_mobil_formatted = "{:,.2f}".format(harga_mobil_float)
        st.markdown(f'Harga Mobil: $ {harga_mobil_formatted}')
def bar_page():
    st.markdown("<h1 style='text-align: center;'>Menampilkan Bar</h1>", unsafe_allow_html=True)
    df  = pd.DataFrame(
        np.random.randn(10,2),
        columns=['x','y']
    )
    st.line_chart(df)
    st.bar_chart(df)
    st.area_chart(df)
def about_page():
    st.markdown("<h1 style='text-align: center;'>About Page</h1>", unsafe_allow_html=True)
    st.subheader("Streamlit Aplication")
    st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.svg')
    st.caption("Streamlit adalah sebuah framework open-source yang digunakan untuk membangun antarmuka pengguna (UI) interaktif untuk aplikasi data science. Framework ini dirancang khusus untuk mempermudah pengembangan aplikasi web dengan menggunakan Python.")

if sidebar == "Home":
    main_page()
elif sidebar == "Car Price":
    carPrice_page()
elif sidebar == "Bar":
    bar_page()
elif sidebar == "About":
    about_page()
