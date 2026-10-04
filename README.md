# Proyek Analisis Data — Air Quality Dataset

## Isi proyek
- `notebook.ipynb` — notebook analisis lengkap mengikuti template submission.
- `dashboard/dashboard.py` — dashboard interaktif Streamlit.
- `data/` — tempat 12 file `PRSA_Data_*.csv`.
- `requirements.txt` — dependensi Python.
- `README.md` — panduan menjalankan proyek.

## Dataset
Letakkan 12 file Air Quality Dataset berikut ke folder `data/`:
1. PRSA_Data_Aotizhongxin_20130301-20170228.csv
2. PRSA_Data_Changping_20130301-20170228.csv
3. PRSA_Data_Dingling_20130301-20170228.csv
4. PRSA_Data_Dongsi_20130301-20170228.csv
5. PRSA_Data_Guanyuan_20130301-20170228.csv
6. PRSA_Data_Gucheng_20130301-20170228.csv
7. PRSA_Data_Huairou_20130301-20170228.csv
8. PRSA_Data_Nongzhanguan_20130301-20170228.csv
9. PRSA_Data_Shunyi_20130301-20170228.csv
10. PRSA_Data_Tiantan_20130301-20170228.csv
11. PRSA_Data_Wanliu_20130301-20170228.csv
12. PRSA_Data_Wanshouxigong_20130301-20170228.csv

## Menjalankan notebook
1. Buat virtual environment (opsional).
2. Install dependency:
   `pip install -r requirements.txt`
3. Pastikan 12 CSV berada di `data/`.
4. Jalankan Jupyter:
   `jupyter notebook`
5. Buka `notebook.ipynb` dan pilih **Run All**.
6. Simpan notebook setelah semua cell selesai sehingga notebook submission berisi output tabel dan visualisasi.

## Menjalankan dashboard
Dari root folder proyek:
```bash
streamlit run dashboard/dashboard.py
```

Dashboard menyediakan:
- filter stasiun,
- filter rentang tanggal,
- KPI rata-rata dan maksimum PM2.5,
- tren PM2.5 bulanan,
- ranking stasiun,
- perbandingan musiman,
- korelasi PM2.5 dengan faktor meteorologi,
- tabel data.

## Catatan analisis
Missing value numerik diimputasi secara berurutan per stasiun menggunakan interpolasi linear berbasis waktu, kemudian median stasiun untuk nilai yang masih kosong. Nilai ekstrem tidak otomatis dihapus karena episode polusi ekstrem merupakan informasi yang relevan.

Kategori PM2.5 pada analisis lanjutan merupakan **kategori eksploratif**, bukan klaim sebagai standar regulasi resmi.

## Submission
Sebelum membuat ZIP final, masukkan 12 CSV asli ke folder `data/`, jalankan notebook sampai selesai, lalu zip seluruh folder proyek.
