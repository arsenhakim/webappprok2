import streamlit as st
import numpy as np
import pandas as pd


# Set judul halaman
st.title('Simple Statistik App')

# Tambahkan deskripsi singkat
st.markdown("""
    #### Arsen Awali Rahman Hakim **2043221129**
""")
if st.checkbox('Operasi Matriks'): 
    tipe = st.radio('Pilih tipe operasi', ['Penjumlahan', 'Pengurangan', 'Perkalian','Determinan'])
with st.form('Pilih Ukuran'):
    if tipe == 'Penjumlahan':
        #masukkan ukuran matriks A dan B
        row1 = st.number_input('ukuran baris dari matrix pertama', min_value=1, step=1)
        col1 = st.number_input('ukuran kolom dari matrix pertama ', min_value=2, step=1)
        row2 = st.number_input('ukuran baris dari matrix kedua', min_value=1, step=1)
        col2 = st.number_input('ukuran kolom dari matrix kedua', min_value=2, step=1)
        st.form_submit_button('kirim ukuran')
    elif tipe == 'Pengurangan':
        row1 = st.number_input('ukuran baris dari matrix pertama', min_value=1, step=1)
        col1 = st.number_input('ukuran kolom dari matrix pertama ', min_value=2, step=1)
        row2 = st.number_input('ukuran baris dari matrix kedua', min_value=1, step=1)
        col2 = st.number_input('ukuran kolom dari matrix kedua', min_value=2, step=1)
        st.form_submit_button('kirim ukuran') 
    elif tipe == 'Perkalian':
        row1 = st.number_input('ukuran baris dari matrix pertama', min_value=1, step=1)
        col1 = st.number_input('ukuran kolom dari matrix pertama ', min_value=2, step=1)
        row2 = st.number_input('ukuran baris dari matrix kedua', min_value=1, step=1)
        col2 = st.number_input('ukuran kolom dari matrix kedua', min_value=2, step=1)
        st.form_submit_button('kirim ukuran')
    elif tipe == 'Determinan':
        ukuran_det = st.number_input('ukuran baris dari matrix pertama', min_value=2, step=1)
        st.form_submit_button('kirim ukuran')

with st.form('operasi matrx'):
    if tipe == 'Determinan':
        st.write('Masukkan matriks')
        df_d = pd.DataFrame(columns=range(1,ukuran_det+1), index=range(1,ukuran_det+1), dtype=float) #untuk membuat tabel kosong
        df_d_input = st.experimental_data_editor(df_d, use_container_width=True, key=1)
        
        dfdet = st.form_submit_button('Cari Determinan')
    else:

        st.write('data untuk matrix pertama')
        df_1 = pd.DataFrame(columns=range(1,col1+1), index=range(1,row1+1), dtype=float) #untuk membuat tabel kosong
        df_1_input = st.experimental_data_editor(df_1, use_container_width=True, key=1)

    
        st.write('data untuk matrix kedua')
        df_2 = pd.DataFrame(columns=range(1,col2+1), index=range(1,row2+1), dtype=float) #untuk membuat tabel kosong
        df_2_input = st.experimental_data_editor(df_2, use_container_width=True, key=2)

        A_dan_B = st.form_submit_button('hitung')

    matrix1 = df_1_input.fillna(0).to_numpy()
    
    matrix2 = df_2_input.fillna(0).to_numpy()
    
    matrixd = df_d_input.fillna(0).to_numpy()
    
    if tipe == 'Penjumlahan':
        if (row1+col1 - row2-col2) != 0:
            st.write(' Tidak bisa melakukan operasi karena ordo matriks berbeda')
        else:
            pnjum = matrix1+matrix2
            hasil = st.write(pnjum)
    elif tipe == 'Pengurangan':
        if (row1+col1 - row2-col2) != 0:
            st.write(' Tidak bisa melakukan operasi karena ordo matriks berbeda')
        else:
            pgur = matrix1-matrix2
            hasil = st.write(pgur)
    elif tipe == 'Perkalian':
        if (col1-row2) != 0:
            st.write('Tidak bisa melakukan perkalian karena dimensi berbeda')
        else:
            prkl = np.matmul(matrix1,matrix2)
            st.write(prkl)
    elif tipe == 'Determinan':
        print('halo')
