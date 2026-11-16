# E-Commerce Public Dataset Analysis

## Deskripsi Proyek

Proyek ini bertujuan untuk menganalisis data transaksi e-commerce menggunakan Dataset **E-Commerce Public Dataset**. Analisis difokuskan pada nilai penjualan berdasarkan kategori produk, ketepatan waktu pengiriman, dan kontribusi penjualan berdasarkan negara bagian pelanggan selama tahun 2017.

Hasil analisis disajikan melalui dashboard interaktif menggunakan **Streamlit** dan **Plotly**.

## Pertanyaan Bisnis

1. Kategori produk apa yang memiliki total nilai penjualan tertinggi dan terendah berdasarkan pesanan berstatus delivered selama tahun 2017, untuk menentukan kategori yang perlu diprioritaskan dalam strategi pemasaran dan evaluasi pengelolaan produk?
2. Berapa persentase pesanan berstatus delivered yang diterima pelanggan melewati estimasi tanggal pengiriman selama tahun 2017, untuk mengevaluasi ketepatan layanan pengiriman dan menentukan kebutuhan perbaikan operasional logistik?
3. NNegara bagian pelanggan mana yang memberikan kontribusi total nilai penjualan terbesar dari pesanan berstatus delivered selama tahun 2017, untuk menentukan wilayah prioritas pemasaran dan mengevaluasi peluang pengembangan pasar?

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
## Setup Environment - Shell/Terminal (macOS/Linux)

### 1. Clone Repository

```bash
git clone https://github.com/ChenMLing/e-commercepublic-dataset.git
cd e-commercepublic-dataset
```

### 2. Membuat Virtual Environment

```bash
python3 -m venv .venv
```

### 3. Mengaktifkan Virtual Environment

```bash
source .venv/bin/activate
```

### 4. Menginstal Library

```bash
python -m pip install -r requirements.txt
```

## Setup Environment - Windows

```bash
git clone https://github.com/ChenMLing/e-commercepublic-dataset.git
cd e-commercepublic-dataset
py -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
```

## Run Streamlit App

```bash
streamlit run dashboard.py
```

Dashboard akan terbuka melalui browser, biasanya pada alamat:

http://localhost:8501

Nomor port dapat berbeda apabila port tersebut sedang digunakan.

## Dashboard Online

Dashboard juga dapat diakses melalui Streamlit Community Cloud:

https://e-commercepublic-dataset.streamlit.app

## Menonaktifkan Virtual Environment

Setelah selesai, jalankan:

```bash
deactivate
```

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

## Sumber Data
*E-Commerce Public Dataset*
https://drive.google.com/file/d/1MsAjPM7oKtVfJL_wRp1qmCajtSG1mdcK/view
