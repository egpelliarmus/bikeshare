import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset (pastikan path dataset sesuai)
df_day = pd.read_csv('dashboard/data_daily.csv')  # Contoh data harian
df_hour = pd.read_csv('dashboard/data_hourly.csv')  # Contoh data per jam

# Judul Dashboard
st.title('Bike Rentals Dashboard')

# Section 1: Analisis Musim
st.header('1. Bike Rentals by Season')

# Pengelompokkan berdasar musim dan menghitung rata-rata pengguna
season_avg = df_day.groupby('Season')['Count'].mean()
season_avg = season_avg[['Winter', 'Spring', 'Summer', 'Fall']]

# Plot Pie Chart
fig1, ax1 = plt.subplots(figsize=(7, 7))
ax1.pie(season_avg, labels=season_avg.index, autopct='%1.1f%%', colors=['lightblue', 'lightgreen', 'lightcoral', 'lightskyblue'], startangle=90, shadow=True)
ax1.set_title("Percentage of Average Bike Rentals by Season")

# Tampilkan plot di Streamlit
st.pyplot(fig1)

# Insight Musim
st.markdown("""
**Insight:**
- Penyewaan sepeda tertinggi terjadi pada musim gugur (31,4%), diikuti oleh musim panas (27,8%) dan musim dingin (26,3%), sementara musim semi mencatat jumlah penyewaan terendah (14,5%).
- Ini menunjukkan bahwa faktor musiman memengaruhi permintaan penyewaan sepeda, di mana musim gugur dan musim panas cenderung lebih ramai, mungkin karena cuaca yang lebih nyaman untuk bersepeda.
""")

# Section 2: Analisis Cuaca
st.header('2. Bike Rentals by Weather Condition')

# Pengelompokkan berdasar cuaca dan menghitung rata-rata pengguna
weather_avg = df_day.groupby('Weathersit')['Count'].mean()

# Plot Bar Chart
fig2, ax2 = plt.subplots(figsize=(8, 6))
weather_avg.plot(kind='bar', color='orange', ax=ax2)
ax2.set_title("Average Bike Rentals by Weather Condition")
ax2.set_xlabel("Weather Condition")
ax2.set_ylabel("Average Rentals")
ax2.set_xticklabels(['Clear', 'Cloudy', 'Rainy/Snowy'], rotation=0)

# Tampilkan plot di Streamlit
st.pyplot(fig2)

# Insight Cuaca
st.markdown("""
**Insight:**
- Penyewaan sepeda tertinggi terjadi pada kondisi cuaca cerah atau dengan awan tipis, dengan jumlah penyewaan lebih dari 4.500.
- Cuaca berkabut dan mendung memiliki tingkat penyewaan kedua tertinggi, sedangkan kondisi hujan ringan atau salju mencatat penyewaan terendah.
- Cuaca memainkan peran penting dalam keputusan konsumen untuk menyewa sepeda, di mana cuaca cerah lebih menarik bagi penyewa.
""")

# Section 3: Analisis Pola Jam pada Hari Kerja vs Akhir Pekan
st.header('3. Hourly Bike Rentals: Weekday vs Weekend')

# Pivot tabel untuk jam dan hari kerja
hourly_trend = df_hour.pivot_table(values='Count', index='Hour', columns='Weekday', aggfunc='mean')

# Plot Line Chart
fig3, ax3 = plt.subplots(figsize=(10, 6))
hourly_trend.plot(kind='line', ax=ax3)
ax3.set_title("Hourly Bike Rentals: Weekday vs Weekend")
ax3.set_xlabel("Hour of the Day")
ax3.set_ylabel("Average Number of Rentals")
ax3.legend(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])

# Tampilkan plot di Streamlit
st.pyplot(fig3)

# Insight Pola Jam
st.markdown("""
**Insight:**
- Penyewaan sepeda cenderung memuncak dua kali sehari, yaitu pada pukul 8 pagi dan 5 sore, baik pada hari kerja maupun akhir pekan.
- Namun, akhir pekan memiliki jumlah penyewaan lebih tinggi di siang hari, sementara hari kerja memiliki pola puncak yang lebih tajam.
- Ini menunjukkan perilaku bersepeda terkait dengan aktivitas rutin sehari-hari seperti berangkat dan pulang kerja, serta penggunaan yang lebih santai di akhir pekan.
""")
