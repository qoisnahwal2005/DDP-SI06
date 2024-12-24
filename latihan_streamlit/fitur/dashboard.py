import streamlit as st

st.title("Halaman Dasboard", )
st.image('image.jpg', caption='Home Sweet home')

# Fungsi menghitung dan menyimpan total
def total():
    total_nabung = sum(a['Jumlah'] 
                    for a in st.session_state['total_semua'] 
                    if a ['Tipe'] == 'Menabung')
    total_penarikan = sum(a['Jumlah']
                    for a in st.session_state['total_semua']
                    if a ['Tipe'] == 'Penarikan')
    saldo = total_nabung - total_penarikan
    return total_nabung, total_penarikan, saldo

    return total_nabung

total_semua = st.session_state['total_semua']
total_nabung, total_penarikan, saldo = total()

st.metric("Total Menabung: ", f"Rp. {total_nabung}")
st.metric("Total Penarikan: ", f"Rp. {total_penarikan}")
st.metric("Sisa saldo anda: ", f"Rp. {saldo}")
