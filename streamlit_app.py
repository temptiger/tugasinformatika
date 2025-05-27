import streamlit as st

st.title("🐸halo, selamat datang!")
st.write(
"aku suka fore"
)
st.image("instc 2025-05-19 165801.026.jpeg", width=200)

st.title("Aplikasi Sederhana")
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("tulis sebuah angka:", value=0, step=1)

if (angka % 2) == 0:
    st.write(f"{angka} adalah bilangan genap"
             else:
    st.write(f"{angka} adalah bilangan ganjil")
