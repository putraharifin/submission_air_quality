# Proyek Analisis Data — Beijing Multi-Site Air Quality Dataset

## Deskripsi

Proyek ini menganalisis **Beijing Multi-Site Air Quality Dataset** yang berisi data kualitas udara dan meteorologi dari 12 stasiun pemantauan di Beijing selama periode **Maret 2013–Februari 2017**.

Versi proyek terbaru menggunakan **empat pertanyaan analisis** dan dashboard telah disesuaikan dengan hasil analisis pada notebook terbaru.

---

## Identitas

- **Nama:** Muhammad Putra Harifin Pane
- **Email:** putraharifin@gmail.com
- **ID Dicoding:** putraharifin25
- **Dataset:** Beijing Multi-Site Air Quality Dataset

---

# Pertanyaan Analisis

## Pertanyaan 1 — Perbedaan PM2.5 Antarstasiun

**Bagaimana perbedaan rata-rata konsentrasi PM2.5 bulanan antar-12 stasiun pemantauan Beijing selama Maret 2013–Februari 2017, dan stasiun mana yang memiliki rata-rata PM2.5 tertinggi?**

Analisis dilakukan dengan melihat:

- rata-rata PM2.5 setiap stasiun;
- ranking stasiun berdasarkan PM2.5;
- perubahan rata-rata PM2.5 secara bulanan;
- perbandingan pola PM2.5 antarstasiun.

### Hasil

Tiga stasiun dengan rata-rata PM2.5 tertinggi adalah:

| Stasiun | Rata-rata PM2.5 |
|---|---:|
| Dongsi | 86,14 µg/m³ |
| Nongzhanguan | 85,08 µg/m³ |
| Wanshouxigong | 85,07 µg/m³ |

Sedangkan beberapa stasiun dengan rata-rata relatif rendah adalah:

| Stasiun | Rata-rata PM2.5 |
|---|---:|
| Dingling | 66,85 µg/m³ |
| Huairou | 69,50 µg/m³ |

### Insight

Dongsi, Nongzhanguan, dan Wanshouxigong merupakan stasiun dengan tingkat PM2.5 historis tertinggi. Dingling termasuk stasiun dengan tingkat PM2.5 relatif rendah.

Tren PM2.5 menunjukkan adanya pola siklikal dengan episode polusi berat yang berulang pada periode tertentu.

---

# Pertanyaan 2 — Hubungan PM2.5 dengan Kondisi Meteorologi

**Bagaimana hubungan kondisi meteorologi (TEMP, PRES, DEWP, RAIN, dan WSPM) dengan rata-rata PM2.5 selama Maret 2013–Februari 2017?**

Variabel yang dianalisis:

- TEMP
- PRES
- DEWP
- RAIN
- WSPM

### Hasil Korelasi

| Variabel | Korelasi dengan PM2.5 |
|---|---:|
| WSPM | -0,27 |
| TEMP | -0,13 |
| DEWP | 0,11 |
| RAIN | -0,01 |

### Insight

WSPM memiliki korelasi negatif paling kuat terhadap PM2.5, yaitu sekitar **-0,27**.

Artinya, ketika kecepatan angin meningkat, konsentrasi PM2.5 cenderung lebih rendah. Sebaliknya, kondisi angin rendah dapat berkaitan dengan akumulasi polutan.

RAIN hampir tidak menunjukkan hubungan linier terhadap PM2.5 dengan korelasi sekitar **-0,01**.

### Pola Musiman

Hasil analisis menunjukkan:

- **Winter:** rata-rata PM2.5 sekitar 95,74 µg/m³
- **Summer:** rata-rata PM2.5 sekitar 64,52 µg/m³

Winter menjadi periode yang perlu mendapatkan perhatian lebih karena memiliki rata-rata PM2.5 tertinggi.

---

# Pertanyaan 3 — PM2.5 Berdasarkan Kategori Kecepatan Angin

**Bagaimana perbedaan rata-rata PM2.5 pada kategori kecepatan angin selama Maret 2013–Februari 2017, dan kategori kecepatan angin mana yang menunjukkan konsentrasi PM2.5 tertinggi sebagai dasar rekomendasi pemantauan kondisi polusi?**

Kategori kecepatan angin dibuat berdasarkan kuartil distribusi WSPM:

1. Rendah
2. Sedang
3. Tinggi
4. Sangat Tinggi

Kategori tersebut bersifat **eksploratif** dan bukan kategori regulasi resmi.

### Hasil

Kategori:

**Rendah**

memiliki rata-rata PM2.5 tertinggi, yaitu:

**102,44 µg/m³**

Sedangkan kategori:

**Sangat Tinggi**

memiliki rata-rata PM2.5 sekitar:

**45,32 µg/m³**

### Insight

Terdapat pola bahwa kondisi kecepatan angin rendah berkaitan dengan konsentrasi PM2.5 yang lebih tinggi.

Hal tersebut dapat dijelaskan secara analitis sebagai kondisi stagnasi atmosfer yang memungkinkan polutan lebih mudah terakumulasi.

---

# Pertanyaan 4 — Distribusi Tingkat PM2.5 per Stasiun

**Bagaimana distribusi tingkat konsentrasi PM2.5 pada 12 stasiun selama Maret 2013–Februari 2017, dan stasiun mana yang memiliki proporsi observasi PM2.5 tinggi hingga sangat tinggi paling besar?**

Kategori PM2.5 dibuat berdasarkan kuartil distribusi keseluruhan:

1. Rendah
2. Sedang
3. Tinggi
4. Sangat Tinggi

Kategori tersebut bersifat **eksploratif dan bukan standar baku/regulasi kualitas udara**.

### Hasil

Dongsi mempunyai proporsi kategori:

**Tinggi + Sangat Tinggi = 53,11%**

Gucheng dan Wanshouxigong juga termasuk stasiun yang memiliki proporsi kategori PM2.5 tinggi.

Sebaliknya, Dingling memiliki profil PM2.5 yang relatif lebih rendah.

---

# Insight Operasional — Top 10 Periode dan Stasiun

Analisis juga melihat kombinasi bulan dan stasiun dengan rata-rata PM2.5 tertinggi.

Hasil menunjukkan bahwa:

- Desember 2015 mendominasi daftar periode dengan PM2.5 tertinggi;
- Februari 2014 juga banyak muncul dalam daftar periode ekstrem;
- Wanshouxigong memiliki rekor rata-rata bulanan tertinggi sebesar **168,67 µg/m³ pada Desember 2015**;
- Dingling yang biasanya relatif lebih rendah tetap dapat mengalami episode ekstrem, contohnya **158,69 µg/m³ pada Februari 2014**.

Hal ini menunjukkan bahwa episode polusi ekstrem dapat berdampak pada beberapa wilayah secara bersamaan, termasuk wilayah yang secara historis memiliki tingkat polusi lebih rendah.

---

# Data Quality Assessment

Beberapa aspek kualitas data diperiksa pada tahap assessing:

1. Missing value
2. Duplicate data
3. Nilai numerik yang tidak konsisten
4. Konsistensi timestamp
5. Outlier

## Masalah yang ditemukan

### Missing Value

Beberapa variabel memiliki missing value, terutama pada variabel kualitas udara.

### Duplicate

Pemeriksaan dilakukan untuk mengetahui apakah terdapat baris data yang identik.

### Invalid Value

Nilai negatif pada variabel yang secara konsep tidak boleh bernilai negatif diperlakukan sebagai missing.

Namun, nilai negatif pada `TEMP` dan `DEWP` tidak otomatis dianggap invalid karena temperatur dan dew point dapat bernilai negatif pada musim dingin.

### Outlier

Outlier PM2.5 tidak langsung dihapus karena nilai ekstrem dapat merepresentasikan episode polusi nyata yang penting untuk dianalisis.

---

# Data Cleaning

Tahapan cleaning yang dilakukan:

1. Menghapus duplicate penuh jika ditemukan.
2. Membentuk kolom `datetime` dari:
   - `year`
   - `month`
   - `day`
   - `hour`
3. Mengurutkan data berdasarkan:
   - `station`
   - `datetime`
4. Mengubah nilai negatif pada variabel non-negatif menjadi `NaN`.
5. Melakukan interpolasi linear per stasiun untuk data numerik.
6. Mengisi missing numerik yang masih tersisa menggunakan median masing-masing stasiun.
7. Mengisi missing `wd` menggunakan forward fill dan backward fill.
8. Membuat kolom:
   - `year_month`
   - `month_num`
   - `season`
9. Membuat kategori:
   - `wind_category`
   - `pm25_group`

---

# Dashboard Streamlit

Fitur Dashboard
Dashboard menyediakan:
- filter stasiun;
- filter periode;
- KPI rata-rata PM2.5;
- KPI PM2.5 maksimum;
- stasiun dengan rata-rata PM2.5 tertinggi;
- rata-rata PM2.5 pada Winter;
- ranking rata-rata PM2.5 antarstasiun;
- tren rata-rata PM2.5 bulanan;
- heatmap korelasi;
- korelasi variabel meteorologi terhadap PM2.5;
- analisis kategori kecepatan angin;
- distribusi kategori PM2.5 per stasiun;
- Top 10 kombinasi bulan dan stasiun;
- kesimpulan Q1–Q4;
- action items;
- tabel data terfilter.

Struktur Folder
Struktur proyek yang digunakan:

submission_air_quality/
│
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
├── notebook.ipynb
├── dashboard.py
├── requirements.txt
├── README.md
└── url.txt

Menjalankan Dashboard
Pastikan 12 file CSV berada di dalam folder:
data/

Kemudian install dependency:
pip install -r requirements.txt

Setelah itu jalankan:

```bash
streamlit run dashboard/dashboard.py
```

Streamlit akan memberikan alamat lokal untuk membuka dashboard.
Menjalankan Notebook
Pastikan seluruh dataset tersedia pada folder yang sesuai dengan path yang digunakan notebook.
Notebook menjalankan tahapan:
1. Gathering Data
2. Assessing Data
3. Cleaning Data
4. Exploratory Data Analysis
5. Visualization
6. Analisis Lanjutan
7. Conclusion
8. Recommendation
Kesimpulan
Berdasarkan hasil analisis terbaru:
1. Lokasi
Dongsi, Nongzhanguan, dan Wanshouxigong merupakan stasiun dengan tingkat polusi historis tertinggi.
Dingling termasuk stasiun dengan tingkat polusi relatif rendah.
2. Meteorologi
WSPM memiliki korelasi negatif paling kuat terhadap PM2.5, yaitu sekitar -0,27.
3. Kecepatan Angin
Kategori angin Rendah memiliki rata-rata PM2.5 tertinggi sebesar 102,44 µg/m³.
Sebaliknya, kategori Sangat Tinggi memiliki rata-rata sekitar 45,32 µg/m³.
4. Distribusi Polusi
Dongsi memiliki proporsi kategori PM2.5 Tinggi + Sangat Tinggi terbesar, yaitu 53,11%.
5. Musiman
Winter merupakan periode dengan rata-rata PM2.5 tertinggi, sedangkan Summer memiliki rata-rata yang lebih rendah.
6. Episode Ekstrem
Episode polusi ekstrem tidak hanya terjadi pada stasiun yang secara historis memiliki tingkat polusi tinggi. Stasiun seperti Dingling juga dapat mengalami episode ekstrem.
Action Items
1. Prioritas Mitigasi Berbasis Lokasi
Memusatkan inspeksi sumber emisi lokal dan meningkatkan pemantauan di sekitar:
- Dongsi
- Nongzhanguan
- Wanshouxigong
2. Sistem Peringatan Dini Berbasis Angin
Mengintegrasikan prakiraan WSPM ke dalam sistem peringatan kualitas udara.
Kondisi angin rendah atau stagnan dapat menjadi indikator meningkatnya risiko akumulasi PM2.5.
3. Kesiapsiagaan Musim Dingin
Meningkatkan kesiapan intervensi pada periode:
Desember–Februari
karena periode tersebut memiliki risiko episode polusi yang lebih tinggi.
4. Manajemen Polusi Lintas Wilayah
Stasiun yang biasanya relatif bersih seperti Dingling tetap perlu mendapatkan peringatan ketika terjadi episode polusi ekstrem berskala luas.
Requirements
Dependency yang diperlukan:
pandas
numpy
matplotlib
seaborn
plotly
streamlit
jupyter
nbformat

Install menggunakan:
pip install -r requirements.txt

Deployment
Dashboard dapat di-deploy menggunakan Streamlit Community Cloud setelah project di-upload ke GitHub.
Setelah deployment berhasil, URL dashboard dapat dimasukkan ke:
url.txt

Contoh:
https://nama-aplikasi.streamlit.app

URL tersebut hanyalah contoh dan tidak boleh digunakan sebelum aplikasi benar-benar berhasil di-deploy.
Catatan
Kategori:
- wind_category
- pm25_group
merupakan kategori eksploratif yang dibuat berdasarkan kuartil distribusi data.
Kategori tersebut bukan kategori regulasi resmi kualitas udara.
Dashboard menghitung kembali agregasi berdasarkan filter yang dipilih pengguna, sedangkan insight dan angka utama pada bagian kesimpulan mengikuti hasil analisis notebook terbaru.

### Catatan penting

Untuk dashboard ini, struktur foldernya harus seperti ini agar bagian pembacaan data otomatis bekerja:

```text
project/
├── dashboard.py
└── data/
    ├── PRSA_Data_Aotizhongxin_20130301-20170228.csv
    ├── PRSA_Data_Changping_20130301-20170228.csv
    ├── ...
    └── PRSA_Data_Wanshouxigong_20130301-20170228.csv

Jangan meletakkan 12 CSV di folder dashboard/ jika dashboard.py berada satu level di atasnya. Gunakan folder data/ seperti di atas.


## Sumber dataset

Beijing Multi-Site Air Quality Dataset, UCI Machine Learning Repository:
https://archive.ics.uci.edu/dataset/501/beijing+multi+site+air+quality+data