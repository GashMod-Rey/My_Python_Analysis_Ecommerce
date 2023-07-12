import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px

sns.set(style='dark')
st.header(":shopping_bags: E-Commerce Dashboard :shopping_bags:")

product = pd.read_csv("https://github.com/GashMod-Rey/Analisis_Data_dengan_Python/blob/8ffefe516a5f6d6e8cd6c0a1ef22e2e6c451daf5/dashboard/product_type_dimension.csv").set_index('product_category_name_english')
table_final = pd.read_csv("https://github.com/GashMod-Rey/Analisis_Data_dengan_Python/blob/8ffefe516a5f6d6e8cd6c0a1ef22e2e6c451daf5/dashboard/credit_card_by_town.csv")

# 1 - Volume
prod_sort = product['volume'].sort_values(ascending=False)

st.write('')
st.write('')
st.write('')
st.subheader('10 Tipe Produk dengan Volume Terbesar')
fig, ax = plt.subplots()
ax.bar(prod_sort.index[:10], prod_sort.values[:10])
ax.set_xlabel('Tipe Produk')
ax.set_xticks(ticks=prod_sort.index[:10])
for label in ax.get_xticklabels():
    label.set_rotation(30)
    label.set_ha('right')
ax.set_ylabel('Volume Produk Rata-Rata (cm3)')
ax.set_ylim(0, 80000)
st.pyplot(fig)

st.write('')
st.write('')
st.write('')
st.subheader('10 Tipe Produk dengan Volume Terkecil')
fig, ax = plt.subplots()
ax.bar(prod_sort.index[-10:], prod_sort.values[-10:])
ax.set_xlabel('Tipe Produk')
ax.set_xticks(ticks=prod_sort.index[-10:])
for label in ax.get_xticklabels():
    label.set_rotation(30)
    label.set_ha('right')
ax.set_ylabel('Volume Produk Rata-Rata (cm3)')
ax.set_ylim(0, 80000)
st.pyplot(fig)

st.write('')
st.write('')
st.write('')
st.subheader('Tabel Lengkap Produk dan Volumenya')
st.write(prod_sort)

# 2 - Panjang
prod_sort = product['product_length_cm'].sort_values(ascending=False)

st.write('')
st.write('')
st.write('')
st.subheader('10 Tipe Produk dengan Panjang Terbesar')
fig, ax = plt.subplots()
ax.bar(prod_sort.index[:10], prod_sort.values[:10])
ax.set_xlabel('Tipe Produk')
ax.set_xticks(ticks=prod_sort.index[:10])
for label in ax.get_xticklabels():
    label.set_rotation(30)
    label.set_ha('right')
ax.set_ylabel('Panjang Produk Rata-Rata (cm)')
ax.set_ylim(0, 70)
st.pyplot(fig)

st.write('')
st.write('')
st.write('')
st.subheader('10 Tipe Produk dengan Panjang Terkecil')
fig, ax = plt.subplots()
ax.bar(prod_sort.index[-10:], prod_sort.values[-10:])
ax.set_xlabel('Tipe Produk')
ax.set_xticks(ticks=prod_sort.index[-10:])
for label in ax.get_xticklabels():
    label.set_rotation(30)
    label.set_ha('right')
ax.set_ylabel('Panjang Produk Rata-Rata (cm)')
ax.set_ylim(0, 70)
st.pyplot(fig)

st.write('')
st.write('')
st.write('')
st.subheader('Tabel Lengkap Produk dan Panjangnya')
st.write(prod_sort)

# 3 - Lebar
prod_sort = product['product_width_cm'].sort_values(ascending=False)

st.write('')
st.write('')
st.write('')
st.subheader('10 Tipe Produk dengan Lebar Terbesar')
fig, ax = plt.subplots()
ax.bar(prod_sort.index[:10], prod_sort.values[:10])
ax.set_xlabel('Tipe Produk')
ax.set_xticks(ticks=prod_sort.index[:10])
for label in ax.get_xticklabels():
    label.set_rotation(30)
    label.set_ha('right')
ax.set_ylabel('Lebar Produk Rata-Rata (cm)')
ax.set_ylim(0, 50)
st.pyplot(fig)

st.write('')
st.write('')
st.write('')
st.subheader('10 Tipe Produk dengan Lebar Terkecil')
fig, ax = plt.subplots()
ax.bar(prod_sort.index[-10:], prod_sort.values[-10:])
ax.set_xlabel('Tipe Produk')
ax.set_xticks(ticks=prod_sort.index[-10:])
for label in ax.get_xticklabels():
    label.set_rotation(30)
    label.set_ha('right')
ax.set_ylabel('Lebar Produk Rata-Rata (cm)')
ax.set_ylim(0, 50)
st.pyplot(fig)

st.write('')
st.write('')
st.write('')
st.subheader('Tabel Lengkap Produk dan Lebarnya')
st.write(prod_sort)

# 4 - Tinggi
prod_sort = product['product_height_cm'].sort_values(ascending=False)

st.write('')
st.write('')
st.write('')
st.subheader('10 Tipe Produk dengan Tinggi Terbesar')
fig, ax = plt.subplots()
ax.bar(prod_sort.index[:10], prod_sort.values[:10])
ax.set_xlabel('Tipe Produk')
ax.set_xticks(ticks=prod_sort.index[:10])
for label in ax.get_xticklabels():
    label.set_rotation(30)
    label.set_ha('right')
ax.set_ylabel('Tinggi Produk Rata-Rata (cm)')
ax.set_ylim(0, 50)
st.pyplot(fig)

st.write('')
st.write('')
st.write('')
st.subheader('10 Tipe Produk dengan Tinggi Terkecil')
fig, ax = plt.subplots()
ax.bar(prod_sort.index[-10:], prod_sort.values[-10:])
ax.set_xlabel('Tipe Produk')
ax.set_xticks(ticks=prod_sort.index[-10:])
for label in ax.get_xticklabels():
    label.set_rotation(30)
    label.set_ha('right')
ax.set_ylabel('Tinggi Produk Rata-Rata (cm)')
ax.set_ylim(0, 50)
st.pyplot(fig)

st.write('')
st.write('')
st.write('')
st.subheader('Tabel Lengkap Produk dan Tingginya')
st.write(prod_sort)

# 5 - Berat
prod_sort = product['product_weight_g'].sort_values(ascending=False)

st.write('')
st.write('')
st.write('')
st.subheader('10 Tipe Produk dengan Berat Terbesar')
fig, ax = plt.subplots()
ax.bar(prod_sort.index[:10], prod_sort.values[:10])
ax.set_xlabel('Tipe Produk')
ax.set_xticks(ticks=prod_sort.index[:10])
for label in ax.get_xticklabels():
    label.set_rotation(30)
    label.set_ha('right')
ax.set_ylabel('Berat Produk Rata-Rata (g)')
ax.set_ylim(0, 14000)
st.pyplot(fig)

st.write('')
st.write('')
st.write('')
st.subheader('10 Tipe Produk dengan Berat Terkecil')
fig, ax = plt.subplots()
ax.bar(prod_sort.index[-10:], prod_sort.values[-10:])
ax.set_xlabel('Tipe Produk')
ax.set_xticks(ticks=prod_sort.index[-10:])
for label in ax.get_xticklabels():
    label.set_rotation(30)
    label.set_ha('right')
ax.set_ylabel('Berat Produk Rata-Rata (g)')
ax.set_ylim(0, 14000)
st.pyplot(fig)

st.write('')
st.write('')
st.write('')
st.subheader('Tabel Lengkap Produk dan Beratnya')
st.write(prod_sort)

st.write('')
st.write('')
st.write('')
st.subheader('Bagaimana Pengaruh Tipe Produk terhadap Dimensi Produk Tersebut?')
with st.expander("Kesimpulan 1"):
    st.write(
        """Tipe produk mempengaruhi dimensi dari produk tersebut. Produk-produk tertentu memiliki dimensi yang cukup besar maupun kecil.
- Lima tipe produk dengan volume terbesar adalah matras dan furnitur, furnitur kantor, furnitur dapur, ruang makan, cucian, dan taman, kebutuhan rumah tangga, serta furnitur ruang tamu. 
Sedangkan, lima tipe produk dengan volume terkecil adalah dvd blu ray, telephone, buku import, buku teknikal, dan hadiah jam tangan.
- Lima tipe produk dengan panjang terbesar adalah makanan, furnitur kamar tidur, furnitur kantor, kebutuhan rumah tangga, dan furnitur ruang tamu. 
Sedangkan, lima tipe produk dengan panjang terkecil adalah parfum, hadiah jam tangan, akesesori tas, telefon, dan pc.
- Lima tipe produk dengan lebar terbesar adalah furnitur ruang tamu, furnitur, matras, komputer, furnitur dapur, ruang makan, laundry, dan taman, serta kebutuhan rumah tangga. 
Sedangkan, lima tipe produk dengan lebar terkecil adalah aksesori tas, jam tangan, dvd blu ray, telephone, serta servis dan keamanan.
- Lima tipe produk dengan tinggi terbesar adalah furnitur kantor, furnitur dapur, ruang makan, laundry, dan taman, furnitur matras, komputer, serta bisnis dan industri. 
Sedangkan, lima tipe produk dengan tinggi terkecil adalah celana dalam pantai, telefon, buku teknikal, dvd blu ray, serta buku impor.
- Lima tipe produk dengan berat terbesar adalah furnitur, matras, furnitur kantor, furnitur dapur, ruang makan, laundry, dan taman, furnitur kamar tidur, serta kebutuhan rumah tangga. 
Sedangkan, lima tipe produk dengan berat terkecil adalah telefon, baju anak, pakaian olahraga, celana dalam pantai, serta tablet cetak gambar.
        """
    )

# 6 - Banyak Transaksi Kartu Kredit
cc_sort = table_final.sort_values(by='count', ascending=False)

st.write('')
st.write('')
st.write('')
st.subheader('10 Kota dengan Transaksi Kartu Kredit Terbanyak')
fig, ax = plt.subplots()
ax.bar(cc_sort['customer_city'][:10], cc_sort['count'][:10])
ax.set_xlabel('Kota')
for label in ax.get_xticklabels():
    label.set_rotation(30)
    label.set_ha('right')
ax.set_ylabel('Banyak Transaksi Kartu Kredit')
ax.set_ylim(0, 13000)
st.pyplot(fig)

st.write('')
st.write('')
st.write('')
st.subheader('10 Kota dengan Transaksi Kartu Kredit Paling Sedikit')
fig, ax = plt.subplots()
ax.bar(cc_sort['customer_city'][-10:], cc_sort['count'][-10:])
ax.set_xlabel('Kota')
for label in ax.get_xticklabels():
    label.set_rotation(30)
    label.set_ha('right')
ax.set_ylabel('Banyak Transaksi Kartu Kredit')
ax.set_ylim(0, 10)
st.pyplot(fig)
st.caption("Catatan: Jangkauan sumbu Y pada grafik ini dan grafik sebelumnya berbeda untuk alasan keterbacaan grafik. Rasio jangkauan sumbu Y grafik sebelumnya dibandingkan grafik ini adalah 1:1300.")

st.write('')
st.write('')
st.write('')
st.subheader('Bagaimana Pengaruh Lokasi Pengguna terhadap Penggunaan Kartu Kredit Pengguna di Daerah Tersebut?')
with st.expander("Kesimpulan 2"):
    st.write(
        """Lokasi pengguna (daerah/kota) memiliki pengaruh terhadap banyaknya penggunaan kartu kredit dari pengguna dari daerah tersebut. Daerah yang cukup maju (kota-kota besar, pada data merupakan kota-kota di Brazil) memiliki frekuensi penggunaan kartu kredit yang tinggi, sedangkan daerah yang kurang maju memiliki frekuensi penggunaan kartu kredit yang rendah.
        """
    )

# Advanced Analysis
st.write('')
st.write('')
st.write('')
st.subheader('Advanced Analysis')
st.caption('Geoanalysis Data Pengguna Kartu Kredit dalam Peta')

geo = pd.read_csv("../data/geolocation_dataset.csv")
geo = geo.groupby(by='geolocation_city').mean().drop('geolocation_zip_code_prefix', axis=1)
k = cc_sort.merge(geo, how='left', left_on='customer_city', right_on='geolocation_city')
fig = px.scatter_geo(k, lat='geolocation_lat',lon='geolocation_lng', hover_name="customer_city", hover_data=["count"])
fig.update_layout(title = 'E-Commerce Credit Card Usage Count', title_x=0.5)
st.plotly_chart(fig)

st.caption('Catatan: Gambar yang ditunjukkan belum tentu sepenuhnya tepat. Gambar ini merepresentasikan satu daerah dengan merata-ratakan koordinat beberapa tempat pada daerah tersebut.')
st.write('')
st.write('')
st.write('')
st.subheader('Bagaimana Pengaruh Lokasi Pengguna terhadap Penggunaan Kartu Kredit Pengguna di Daerah Tersebut?')
with st.expander("Kesimpulan 2 - add."):
    st.write(
        """
Pengguna kartu kredit banyak terdapat pada region yang ditandai dengan warna merah pada gambar di bawah ini.
        """
    )
    st.image("https://github.com/GashMod-Rey/Analisis_Data_dengan_Python/blob/3645a12f26e2ec9bbcc4a44b9e982cc916249143/plotcc.png")

# Sidebar
with st.sidebar:
    st.markdown("<div style='text-align: center'><h1>This dashboard and data is brought to you by:</h1></div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write('')

    with col2:    
        st.write('')
        st.write('')
        st.write('')

        st.image("https://github.com/GashMod-Rey/Analisis_Data_dengan_Python/blob/3645a12f26e2ec9bbcc4a44b9e982cc916249143/dashboard/github-mark.png")
       
        st.write('')
        st.write('')
        st.write('')
    
    with col3:
        st.write('')

    st.markdown("<div style='text-align: center'><a href='https://drive.google.com/file/d/1MsAjPM7oKtVfJL_wRp1qmCajtSG1mdcK/view?usp=sharing' target='_blank'>[Brazilian E-Commerce Public Dataset]</a></div>", unsafe_allow_html=True)

st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('_________________________________________________________________________________________________________________________________________________________________')
st.caption("Copyright © 2023 | Reynard Matthew Yaputra | Bangkit 2023 Machine Learning Cohort | Data Analyst Enthusiast")