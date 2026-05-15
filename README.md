# prediksi_harga_kos

```
prediksi-kos-ml/
├── data/               # File CSV mentah dan hasil cleaning
├── notebooks/          # File .ipynb untuk eksperimen ML & EDA
├── models/             # File .joblib atau .pkl (model yang sudah jadi)
├── app/
│   ├── static/         # CSS, gambar, atau file aset Flask
│   ├── templates/      # File HTML untuk Flask
│   ├── main.py         # Kode utama Flask
│   └── database.py     # Konfigurasi database SQLAlchemy
├── requirements.txt
└── README.md
```
akan ada 3 branch yaitu:
- feature-ml -> nela
- feature-ui -> hubert
- feature-performance -> chelsea
setiap orang akan fokus pada:

```
prediksi-kos-ml/
├── data/
│   ├── raw_kos.csv         # Data mentah
│   └── cleaned_kos.csv     # Data siap pakai untuk ML
├── notebooks/
│   ├── 01_eda.ipynb        # Analisis tren harga & grafik Seaborn
│   └── 02_training.ipynb   # Proses training model regresi
└── models/
    └── model_kos.pkl       # File model yang sudah di-export

```
```
prediksi-kos-ml/
├── app/
│   ├── static/             # File CSS untuk desain & Logo
│   │   └── style.css
│   ├── templates/          # File HTML (Jika pakai Flask/FastAPI)
│   │   ├── index.html      # Halaman input kriteria
│   │   └── result.html     # Halaman hasil Top 5
│   └── main.py             # Menulis fungsi untuk render tampilan

```
```
prediksi-kos-ml/
├── app/
│   ├── database.py         # Skrip koneksi SQLAlchemy/SQLite
│   └── main.py             # Optimasi load model & hitung latensi
├── tests/
│   └── test_performance.py # Skrip untuk cek latensi < 100ms
├── requirements.txt        # Daftar library (Protector yang jaga versinya)
└── README.md               # Dokumentasi cara install & jalankan


