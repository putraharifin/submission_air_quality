# Beijing Multi-Site Air Quality Analysis

## Deskripsi Proyek

Proyek ini merupakan analisis data kualitas udara menggunakan **Beijing Multi-Site Air Quality Dataset**. Dataset berisi data kualitas udara dan kondisi meteorologi dari beberapa stasiun pemantauan di Beijing pada periode **Maret 2013 hingga Februari 2017**.

Analisis difokuskan pada konsentrasi **PM2.5** dan hubungannya dengan lokasi stasiun, waktu, musim, serta beberapa faktor meteorologi.

Selain notebook analisis, proyek ini menyediakan **dashboard interaktif menggunakan Streamlit** untuk membantu pengguna melihat hasil analisis dengan lebih mudah.

---

## Struktur Proyek

Struktur proyek yang digunakan adalah sebagai berikut:

```text
submission_air_quality/
├── data/
│   ├── PRSA_Data_Aotizhongxin_20130301-20170228.csv
│   ├── PRSA_Data_Changping_20130301-20170228.csv
│   ├── PRSA_Data_Dingling_20130301-20170228.csv
│   ├── PRSA_Data_Dongsi_20130301-20170228.csv
│   ├── PRSA_Data_Guanyuan_20130301-20170228.csv
│   ├── PRSA_Data_Gucheng_20130301-20170228.csv
│   ├── PRSA_Data_Huairou_20130301-20170228.csv
│   ├── PRSA_Data_Nongzhanguan_20130301-20170228.csv
│   ├── PRSA_Data_Shunyi_20130301-20170228.csv
│   ├── PRSA_Data_Tiantan_20130301-20170228.csv
│   ├── PRSA_Data_Wanliu_20130301-20170228.csv
│   └── PRSA_Data_Wanshouxigong_20130301-20170228.csv
│
├── dashboard
|  ├── dashboard.py
|  ├── main_data.csv
|
├── notebook.ipynb
├── requirements.txt
├── README.md
└── url.txt
```

---

## Cara Menjalankan Proyek

### 1. Clone atau download repository

Setelah repository tersedia di komputer, masuk ke folder proyek:

```bash
cd submission_air_quality
```

### 2. Install dependencies

Disarankan menggunakan virtual environment.

```bash
pip install -r requirements.txt
```

### 3. Menjalankan Notebook

Jalankan Jupyter Notebook:

```bash
jupyter notebook
```

Kemudian buka file:

```text
notebook.ipynb
```

### 4. Menjalankan Dashboard

Jika `dashboard.py` berada di root folder proyek:

```bash
streamlit run dashboard.py
```

Setelah dijalankan, Streamlit akan memberikan alamat lokal untuk membuka dashboard melalui browser.

---

## Pertanyaan Bisnis

Analisis ini berfokus pada beberapa pertanyaan utama:

1. **Stasiun mana yang memiliki konsentrasi rata-rata PM2.5 paling tinggi?**
2. **Bagaimana hubungan kondisi meteorologi dengan konsentrasi PM2.5?**
3. **Bagaimana konsentrasi PM2.5 berubah berdasarkan kecepatan angin?**
4. **Bagaimana tingkat konsentrasi PM2.5 berbeda antarstasiun berdasarkan kategorinya?**

Pertanyaan tersebut digunakan sebagai dasar untuk melakukan eksplorasi data, visualisasi, serta menyusun rekomendasi berdasarkan hasil analisis.

---

## Dataset

Dataset yang digunakan adalah:

**Beijing Multi-Site Air Quality Dataset**

Dataset terdiri dari data pengukuran dari **12 stasiun pemantauan** di Beijing:

- Aotizhongxin
- Changping
- Dingling
- Dongsi
- Guanyuan
- Gucheng
- Huairou
- Nongzhanguan
- Shunyi
- Tiantan
- Wanliu
- Wanshouxigong


### Periode Pengamatan

**1 Maret 2013 – 28 Februari 2017**

Data mencakup pengukuran kualitas udara dan kondisi meteorologi setiap jam dari beberapa stasiun pemantauan di Beijing.

#### Variabel Kualitas Udara

Variabel berikut menunjukkan konsentrasi berbagai polutan di udara:

- **PM2.5** — partikel udara sangat kecil dengan diameter hingga 2,5 mikrometer. Partikel ini dapat masuk jauh ke dalam saluran pernapasan.
- **PM10** — partikel udara dengan diameter hingga 10 mikrometer, umumnya berasal dari debu, tanah, dan aktivitas pembakaran.
- **SO2 (Sulfur Dioxide)** — gas sulfur dioksida yang terutama berkaitan dengan pembakaran bahan bakar yang mengandung sulfur.
- **NO2 (Nitrogen Dioxide)** — gas nitrogen dioksida yang banyak dihasilkan dari proses pembakaran, termasuk kendaraan dan aktivitas industri.
- **CO (Carbon Monoxide)** — gas karbon monoksida yang terbentuk dari pembakaran bahan bakar yang tidak sempurna.
- **O3 (Ozone)** — ozon di permukaan tanah yang dapat terbentuk melalui reaksi kimia antara polutan di udara dengan bantuan sinar matahari.

#### Variabel Meteorologi

Variabel berikut menggambarkan kondisi cuaca yang dapat membantu menjelaskan perubahan konsentrasi polutan:

- **TEMP (Temperature)** — suhu udara dalam derajat Celsius (°C).
- **PRES (Pressure)** — tekanan udara, yang dapat memengaruhi kondisi dan pergerakan udara.
- **DEWP (Dew Point)** — suhu titik embun, yaitu suhu ketika uap air di udara mulai mengalami kondensasi.
- **RAIN (Rainfall)** — jumlah curah hujan yang tercatat, dalam milimeter (mm).
- **WSPM (Wind Speed)** — kecepatan angin, dalam meter per detik (m/s).
- **WD (Wind Direction)** — arah datangnya angin, yang menunjukkan dari arah mana angin bertiup.

Secara sederhana, **variabel kualitas udara menunjukkan seberapa banyak polutan yang terdapat di udara**, sedangkan **variabel meteorologi menggambarkan kondisi cuaca yang dapat berkaitan dengan perubahan konsentrasi polutan tersebut**.

---

## Proses Analisis

Tahapan analisis dilakukan melalui beberapa proses berikut.

### 1. Gathering Data

Data dari seluruh stasiun dikumpulkan dari file CSV yang tersedia.

Setiap file mewakili satu stasiun pemantauan. Seluruh data kemudian digabungkan menjadi satu dataset untuk mempermudah proses analisis lintas stasiun dan waktu.

### 2. Assessing Data

Data diperiksa untuk mengetahui:

- struktur dan tipe data;
- missing value;
- duplikasi data;
- nilai yang tidak valid;
- konsistensi data waktu;
- distribusi variabel numerik.

### 3. Cleaning Data

Beberapa proses yang dilakukan antara lain:

- menghapus data duplikat;
- membuat kolom `datetime` dari `year`, `month`, `day`, dan `hour`;
- mengurutkan data berdasarkan stasiun dan waktu;
- menangani nilai negatif pada variabel yang secara logis tidak boleh negatif;
- melakukan interpolasi linear untuk missing value numerik berdasarkan stasiun;
- menggunakan median stasiun sebagai fallback untuk missing value numerik yang masih tersisa;
- menangani missing value pada arah angin (`wd`);
- membuat fitur turunan seperti `year_month`, `month_num`, dan `season`;
- membuat kategori kecepatan angin;
- membuat kategori konsentrasi PM2.5.

Nilai negatif pada `TEMP` dan `DEWP` tidak dianggap sebagai kesalahan karena suhu dan dew point dapat bernilai negatif pada musim dingin.

Outlier PM2.5 juga tidak dihapus secara otomatis karena nilai ekstrem dapat merepresentasikan kondisi polusi yang memang terjadi.

---

## Exploratory Data Analysis

### 1. Perbandingan Konsentrasi PM2.5 Antarstasiun

Hasil analisis menunjukkan adanya perbedaan konsentrasi PM2.5 antarstasiun.

Beberapa hasil utama:

| Stasiun | Rata-rata PM2.5 (µg/m³) |
|---|---:|
| Dongsi | 86.14 |
| Nongzhanguan | 85.08 |
| Wanshouxigong | 85.07 |
| Dingling | 66.85 |
| Huairou | 69.50 |

Berdasarkan hasil tersebut, **Dongsi memiliki rata-rata PM2.5 paling tinggi** di antara stasiun yang dibandingkan, sedangkan Dingling memiliki rata-rata yang relatif lebih rendah.

---

### 2. Hubungan Faktor Meteorologi dengan PM2.5

Analisis korelasi dilakukan untuk melihat hubungan antara PM2.5 dan beberapa variabel meteorologi.

Hasil utama menunjukkan:

| Variabel | Korelasi dengan PM2.5 |
|---|---:|
| WSPM | -0.27 |
| TEMP | -0.13 |
| DEWP | 0.11 |
| RAIN | -0.01 |

WSPM memiliki korelasi negatif paling besar secara absolut dibandingkan variabel meteorologi yang dianalisis.

Namun, hasil korelasi ini **tidak menunjukkan hubungan sebab-akibat**. Nilai korelasi hanya digunakan untuk melihat pola hubungan dalam data.

---

### 3. Perbedaan PM2.5 Berdasarkan Musim

Rata-rata konsentrasi PM2.5 berdasarkan musim menunjukkan:

| Musim | Rata-rata PM2.5 (µg/m³) |
|---|---:|
| Winter | 95.74 |
| Summer | 64.52 |

Konsentrasi PM2.5 cenderung lebih tinggi pada musim dingin dibandingkan musim panas.

Pola ini menunjukkan bahwa periode musim dingin perlu mendapat perhatian lebih dalam pemantauan kualitas udara.

---

### 4. PM2.5 Berdasarkan Kecepatan Angin

Kecepatan angin (`WSPM`) dibagi ke dalam beberapa kategori berdasarkan kuartil untuk melihat pola konsentrasi PM2.5 pada kondisi angin yang berbeda.

Hasil eksplorasi menunjukkan:

- kategori kecepatan angin rendah memiliki rata-rata PM2.5 sekitar **102.44 µg/m³**;
- kategori kecepatan angin sangat tinggi memiliki rata-rata PM2.5 sekitar **45.32 µg/m³**.

Secara eksploratif, konsentrasi PM2.5 cenderung lebih tinggi ketika kecepatan angin berada pada kategori rendah.

Kategori ini dibuat berdasarkan distribusi data dan **bukan merupakan kategori baku kualitas udara**.

---

### 5. Distribusi Kategori PM2.5 Antarstasiun

Konsentrasi PM2.5 juga dikelompokkan berdasarkan kuartil keseluruhan data untuk melihat seberapa sering masing-masing stasiun berada pada kategori konsentrasi yang relatif tinggi.

Salah satu hasil utama adalah:

- **Dongsi memiliki sekitar 53.11% pengamatan pada kategori "Tinggi + Sangat Tinggi".**

Gucheng dan Wanshouxigong juga menunjukkan proporsi kategori PM2.5 tinggi yang relatif besar, sedangkan Dingling cenderung memiliki proporsi yang lebih rendah.

Kategori ini digunakan untuk **analisis eksploratif** dan bukan sebagai klasifikasi regulasi kualitas udara.

---

## Visualisasi

Analisis menggunakan beberapa jenis visualisasi untuk membantu memahami pola data, antara lain:

- bar chart perbandingan rata-rata PM2.5 antarstasiun;
- line chart tren PM2.5 berdasarkan waktu;
- visualisasi rata-rata PM2.5 berdasarkan musim;
- heatmap korelasi;
- bar chart hubungan korelasi variabel meteorologi dengan PM2.5;
- visualisasi PM2.5 berdasarkan kategori kecepatan angin;
- stacked bar chart distribusi kategori PM2.5 antarstasiun;
- visualisasi periode dengan konsentrasi PM2.5 tertinggi.

---

## Dashboard Interaktif

Proyek ini menyediakan dashboard berbasis **Streamlit** yang memungkinkan pengguna mengeksplorasi hasil analisis secara interaktif.

Dashboard menggunakan tampilan **dark theme** agar visualisasi dan informasi lebih mudah dibaca.

### Fitur Dashboard

Dashboard menyediakan beberapa bagian utama:

1. **Gambaran Umum**
   - jumlah stasiun;
   - periode pengamatan;
   - rata-rata PM2.5;
   - informasi ringkas mengenai data yang sedang ditampilkan.

2. **Perbandingan Konsentrasi PM2.5 Antarstasiun**
   - melihat stasiun dengan rata-rata PM2.5 tertinggi dan terendah.

3. **Tren Konsentrasi PM2.5**
   - melihat perubahan konsentrasi PM2.5 berdasarkan waktu;
   - melihat pola berdasarkan bulan dan musim.

4. **Hubungan PM2.5 dengan Kondisi Meteorologi**
   - heatmap korelasi;
   - perbandingan korelasi variabel meteorologi terhadap PM2.5.

5. **PM2.5 dan Kecepatan Angin**
   - melihat perbedaan rata-rata PM2.5 berdasarkan kategori kecepatan angin.

6. **Distribusi Kategori PM2.5**
   - membandingkan proporsi kategori PM2.5 antarstasiun.

7. **Periode dengan PM2.5 Tertinggi**
   - menampilkan periode dengan konsentrasi PM2.5 rata-rata tertinggi.

8. **Temuan Utama**
   - merangkum beberapa hasil penting dari analisis.

9. **Rekomendasi Tindakan**
   - memberikan rekomendasi berdasarkan pola yang ditemukan dari data.

10. **Tabel Data**
    - menyediakan data yang telah diproses untuk ditinjau secara lebih detail.

Dashboard ditujukan untuk membantu pengguna yang tidak terbiasa membaca notebook analisis agar dapat memahami pola utama kualitas udara melalui visualisasi interaktif.

---

## Temuan Utama

Berdasarkan hasil eksplorasi data, beberapa temuan utama adalah:

1. **Dongsi memiliki rata-rata PM2.5 yang relatif tinggi**, yaitu sekitar 86.14 µg/m³.
2. Nongzhanguan dan Wanshouxigong juga menunjukkan rata-rata PM2.5 yang relatif tinggi.
3. Konsentrasi PM2.5 cenderung lebih tinggi pada **musim dingin** dibandingkan musim panas.
4. Kecepatan angin (`WSPM`) menunjukkan korelasi negatif dengan PM2.5.
5. Pada kategori kecepatan angin rendah, rata-rata PM2.5 lebih tinggi dibandingkan kategori kecepatan angin sangat tinggi.
6. Dongsi memiliki proporsi pengamatan kategori **Tinggi + Sangat Tinggi** yang cukup besar.
7. Beberapa periode dengan konsentrasi PM2.5 ekstrem terjadi pada akhir tahun 2015 dan awal tahun 2014.
8. Pada Desember 2015, Wanshouxigong memiliki rata-rata bulanan PM2.5 sekitar **168.67 µg/m³**.
9. Pada Februari 2014, Dingling memiliki rata-rata bulanan PM2.5 sekitar **158.69 µg/m³**.
10. Pola kualitas udara menunjukkan bahwa lokasi stasiun dan periode waktu perlu dipertimbangkan ketika melakukan pemantauan kualitas udara.

---

## Rekomendasi

Berdasarkan hasil analisis, beberapa tindakan yang dapat dipertimbangkan adalah:

### 1. Memprioritaskan pemantauan pada stasiun dengan PM2.5 tinggi

Stasiun seperti **Dongsi, Nongzhanguan, dan Wanshouxigong** dapat menjadi prioritas dalam pemantauan dan evaluasi sumber emisi karena menunjukkan rata-rata PM2.5 yang relatif tinggi.

### 2. Meningkatkan kesiapsiagaan pada musim dingin

Karena rata-rata PM2.5 lebih tinggi pada musim dingin, periode tersebut dapat menjadi fokus untuk meningkatkan pemantauan dan kesiapsiagaan terhadap episode polusi.

### 3. Menggunakan kondisi angin sebagai indikator pendukung

Kecepatan angin dapat digunakan sebagai salah satu indikator tambahan dalam sistem pemantauan atau peringatan dini, terutama ketika kondisi angin rendah bertepatan dengan peningkatan konsentrasi PM2.5.

### 4. Melakukan pengelolaan kualitas udara secara lintas wilayah

Perbedaan antarstasiun menunjukkan bahwa kualitas udara tidak hanya perlu dilihat dari satu lokasi. Stasiun dengan konsentrasi relatif rendah tetap perlu dipantau karena episode polusi dapat terjadi pada periode tertentu.

---

## Teknologi yang Digunakan

Proyek ini menggunakan beberapa teknologi dan library berikut:

- **Python**
- **Pandas** — manipulasi dan analisis data
- **NumPy** — operasi numerik
- **Matplotlib** — visualisasi data
- **Seaborn** — visualisasi statistik
- **Plotly** — visualisasi interaktif
- **Streamlit** — pembuatan dashboard interaktif
- **Jupyter Notebook** — dokumentasi proses analisis

---

## Sumber Dataset

Dataset yang digunakan berasal dari:

**Beijing Multi-Site Air Quality Data Set**

Dataset tersedia melalui UCI Machine Learning Repository:

https://archive.ics.uci.edu/dataset/501/beijing+multi+site+air+quality+data

---

## Catatan

Analisis kategori PM2.5 dan kategori kecepatan angin dalam proyek ini dibuat untuk tujuan **eksplorasi pola data**.

Kategori tersebut tidak dimaksudkan sebagai pengganti standar atau regulasi resmi kualitas udara.

Selain itu, hubungan korelasi yang ditemukan dalam analisis tidak dapat digunakan untuk menyimpulkan hubungan sebab-akibat secara langsung.

---

## Kesimpulan

Analisis menunjukkan adanya variasi konsentrasi PM2.5 berdasarkan **lokasi stasiun, waktu, musim, dan kondisi meteorologi**.

Stasiun seperti Dongsi, Nongzhanguan, dan Wanshouxigong menunjukkan konsentrasi PM2.5 yang relatif tinggi. Konsentrasi juga cenderung meningkat pada musim dingin dan pada kondisi kecepatan angin yang rendah.

Hasil tersebut dapat digunakan sebagai dasar untuk menentukan prioritas pemantauan, meningkatkan kesiapsiagaan pada periode dengan risiko polusi lebih tinggi, serta membantu memahami pola kualitas udara di berbagai lokasi di Beijing.