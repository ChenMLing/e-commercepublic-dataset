# E-Commerce Pubic Dataset Analysis

## Deskripsi Proyek

Proyek ini bertujuan untuk menganalisis data transaksi e-commerce menggunakan Dataset **E-Commerce Public Dataset**. Analisis difokuskan pada nilai penjualan berdasarkan kategori produk, ketepatan waktu pengiriman, dan kontribusi penjualan berdasarkan negara bagian pelanggan selama tahun 2017.

Hasil analisis disajikan melalui dashboard interaktif menggunakan **Streamlit** dan **Plotly**.

## Pertanyaan Bisnis

1. Kategori produk apa yang memiliki total nilai penjualan tertinggi dan terendah berdasarkan pesanan yang dilakukan selama tahun 2017?
2. Berapa persentase pesanan yang dikirimkan melewati estimasi tanggal pengiriman dari seluruh pesanan yang telah diterima pelanggan dan dilakukan selama tahun 2017?
3. Negara bagian pelanggan mana yang memberikan kontribusi total nilai penjualan terbesar berdasarkan pesanan yang dilakukan selama tahun 2017?

## Dataset

Dataset yang digunakan adalah **E-Commerce Public Dataset**, yang tersedia di:

https://drive.google.com/file/d/1MsAjPM7oKtVfJL_wRp1qmCajtSG1mdcK/view

Analisis menggunakan lima dataset utama:

- `orders_dataset.csv`
- `order_items_dataset.csv`
- `products_dataset.csv`
- `product_category_name_translation.csv`
- `customers_dataset.csv`

Data yang dianalisis dibatasi pada pesanan berstatus `delivered` dengan tanggal pemesanan selama tahun 2017. Nilai penjualan dihitung dari kolom `price`, tanpa biaya pengiriman (`freight_value`).

## Instalasi dan Menjalankan Dashboard
### 1. Persyaratan
Pastikan Python sudah terinstal pada komputer.

### 2. Unduh Repository
Unduh repository proyek dari GitHub atau gunakan perintah:
```bash
git clone https://github.com/ChenMLing/e-commercepublic-dataset.git
```
Kemudian masuk ke folder proyek:
```bash
cd olist-ecommerce-dashboard
```

### 3. Instal Library
Jalankan perintah berikut pada terminal:
```bash
python -m pip install -r requirements.txt
```

### 4. Jalankan Dashboard Streamlit
Jalankan perintah:
```bash
python -m streamlit run dashboard/dashboard.py
```
Dashboard akan terbuka melalui browser, biasanya pada alamat:
http://localhost:8501

Port dapat berbeda jika port tersebut sedang digunakan.

## Fitur Dashboard
Dashboard menyediakan:
1. **Ringkasan KPI:** total nilai penjualan, total pesanan, dan persentase keterlambatan pengiriman.
2. **Analisis kategori produk:** visualisasi lima kategori dengan nilai penjualan tertinggi dan terendah.
3. **Analisis ketepatan pengiriman:** donut chart yang menunjukkan persentase pesanan tepat waktu dan terlambat.
4. **Analisis wilayah:** grafik kontribusi penjualan berdasarkan negara bagian dengan slider interaktif.

## Hasil Analisis
- Kategori `bed_bath_table` menghasilkan nilai penjualan tertinggi sebesar **$490.596,92**, sedangkan `diapers_and_hygiene` terendah sebesar **$76,00**.
- Dari **43.426 pesanan**, sebanyak **5,65%** mengalami keterlambatan pengiriman, sedangkan **94,35%** diterima tepat waktu atau lebih awal.
- São Paulo (`SP`) memiliki kontribusi penjualan terbesar sebesar **35,83%**. Bersama Rio de Janeiro (`RJ`) dan Minas Gerais (`MG`), ketiganya menyumbang **62,40%** dari total nilai penjualan.

## Teknologi yang Digunakan
- Python
- Pandas
- Matplotlib
- Seaborn
- Plotly
- Streamlit
- Jupyter Notebook / Google Colab

## Dashboard Online
Tautan dashboard publik akan ditambahkan setelah deployment berhasil dilakukan.

## Sumber Data
*E-Commerce Public Dataset*
https://drive.google.com/file/d/1MsAjPM7oKtVfJL_wRp1qmCajtSG1mdcK/view
