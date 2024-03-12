import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

data_bike_day = pd.read_csv('https://raw.githubusercontent.com/yulindarizky07/finalproject/main/Dashboard/day_cleaned.csv')
data_bike_hour = pd.read_csv('https://raw.githubusercontent.com/yulindarizky07/finalproject/main/Dashboard/hour_cleaned.csv')

def pertanyaan_1():
    st.markdown("## Pertanyaan 1")
    st.markdown("#### Bagaimana hubungan antara musim dan jumlah sewa sepeda harian  ?")
    st.write("Untuk mendapatkan jawaban dari pertanyaan di atas, akan ditampilkan visualisasi yang menunjukkan hubungan antara musim dan jumlah sewa sepeda harian.")

    # Membuat plot menggunakan data harian
    st.set_option('deprecation.showPyplotGlobalUse', False)  # Agar tidak muncul warning

    # Menghitung rata-rata jumlah sewa sepeda harian per musim
    seasonal_averages_day = data_bike_day.groupby('season')['cnt'].mean()
    season_names = ['Spring', 'Summer', 'Fall', 'Winter']

    # Membuat bar chart menggunakan Matplotlib
    fig_day, ax_day = plt.subplots(figsize=(10, 6))
    sns.barplot(x=season_names, y=seasonal_averages_day, palette="viridis", ax=ax_day)
    plt.title('Rata-rata Sewa Sepeda Harian Berdasarkan Musim')
    plt.xlabel('Musim')
    plt.ylabel('Rata-rata Sewa Sepeda Harian')
    
    # Menampilkan grafik di Streamlit
    st.pyplot(fig_day)

    st.write("Grafik di atas menunjukkan tren rata-rata jumlah sewa sepeda harian berdasarkan musim. Anda dapat melihat bagaimana musim mempengaruhi jumlah sewa sepeda harian secara keseluruhan.")
    st.write("Musim yang menawarkan kondisi cuaca yang lebih hangat dan nyaman, seperti Summer (Musim Panas) dan Fall (Musim Gugur),"
         "cenderung mengalami tingkat penyewaan sepeda yang lebih tinggi dibandingkan dengan musim yang lebih dingin seperti Winter (Musim Dingin)."
         "Ini bisa dikaitkan dengan faktor-faktor seperti suhu yang lebih menyenangkan, kondisi jalan yang lebih aman, dan hari yang lebih panjang,"
         "yang secara keseluruhan menciptakan kondisi yang lebih mengundang untuk bersepeda.")


def pertanyaan_2():
    st.markdown("## Pertanyaan 2")
    st.markdown("#### Apakah terdapat pola terkait waktu, misalnya berdasarkan bulan atau jam, dalam frekuensi penyewaan sepeda setiap hari?")
    st.write("Untuk mendapatkan jawaban dari pertanyaan di atas, akan ditampilkan visualisasi yang menunjukkan pola terkait waktu dalam frekuensi penyewaan sepeda setiap hari.")

    st.set_option('deprecation.showPyplotGlobalUse', False)  # Agar tidak muncul warning

    # Plot pola harian berdasarkan bulan
    st.subheader("Pola Harian Berdasarkan Bulan")
    fig_monthly, ax_monthly = plt.subplots(figsize=(12, 6))
    sns.lineplot(x="mnth", y="cnt", data=data_bike_day, ci=None, ax=ax_monthly)
    plt.title("Pola Sewa Sepeda Harian Berdasarkan Bulan")
    plt.xlabel("Bulan")
    plt.ylabel("Sewa Sepeda Harian")
    st.pyplot(fig_monthly)

    # Plot pola harian berdasarkan jam
    st.subheader("Pola Harian Berdasarkan Jam")
    fig_hourly, ax_hourly = plt.subplots(figsize=(12, 6))
    sns.lineplot(x="hr", y="cnt", data=data_bike_hour, ci=None, ax=ax_hourly)
    plt.title("Pola Sewa Sepeda Harian Berdasarkan Jam")
    plt.xlabel("Jam")
    plt.ylabel("Sewa Sepeda Harian")
    st.pyplot(fig_hourly)
    st.write("Grafik di atas menunjukkan pola harian dalam frekuensi penyewaan sepeda berdasarkan bulan dan jam. Anda dapat melihat fluktuasi sepanjang hari dan perubahan sepanjang bulan.")
    st.write("Pertama, terdapat variasi musiman yang signifikan. Bulan-bulan hangat menunjukkan aktivitas penyewaan yang lebih tinggi, menegaskan bahwa kondisi cuaca dan kenyamanan bersepeda memainkan peran kunci dalam mempengaruhi keputusan penyewaan sepeda."
         "Kedua, dalam skala harian, terlihat adanya pola permintaan ganda yang berkorelasi dengan jam-jam berangkat dan pulang kerja. Hal ini menyoroti peran penting sepeda dalam mobilitas perkotaan sebagai sarana transportasi komuter.")

def main():
    st.title("Bike Sharing Dashboard")
    st.sidebar.image('https://raw.githubusercontent.com/yulindarizky07/finalproject/main/Dashboard/bicycle.png')
    
    # Pilihan menu
    menu_options = ["Pertanyaan 1", "Pertanyaan 2"]
    selected_menu = st.sidebar.selectbox("Pilih Pertanyaan", menu_options)

    # Navigasi antar pertanyaan
    if selected_menu == "Pertanyaan 1":
        pertanyaan_1()
    elif selected_menu == "Pertanyaan 2":
        pertanyaan_2()

if __name__ == "__main__":
    main()
