import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(
    page_title="E-Commerce Public Dashboard",
    page_icon="🛒",
    layout="wide"
)

@st.cache_data
def load_data():
    file_path = Path(__file__).parent / "main_data.csv"
    df = pd.read_csv(file_path)

    date_columns = [
        "order_purchase_timestamp",
        "order_delivered_customer_date",
        "order_estimated_delivery_date"
    ]

    for col in date_columns:
        df[col] = pd.to_datetime(df[col])

    return df

main_df = load_data()

# Filter Interaktif Sidebar
st.sidebar.header("Filter Data")

min_date = main_df["order_purchase_timestamp"].min().date()
max_date = main_df["order_purchase_timestamp"].max().date()

selected_dates = st.sidebar.date_input(
    "Rentang Tanggal Pemesanan",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

state_options = sorted(main_df["customer_state"].dropna().unique())

selected_states = st.sidebar.multiselect(
    "Negara Bagian Pelanggan",
    options=state_options,
    default=state_options
)

if len(selected_dates) != 2:
    st.warning("Silakan pilih tanggal awal dan akhir.")
    st.stop()

start_date, end_date = selected_dates

filtered_df = main_df[
    (
        main_df["order_purchase_timestamp"].dt.date
        >= start_date
    )
    &
    (
        main_df["order_purchase_timestamp"].dt.date
        <= end_date
    )
    &
    (
        main_df["customer_state"].isin(selected_states)
    )
].copy()

if filtered_df.empty:
    st.warning(
        "Tidak ada data untuk kombinasi filter yang dipilih. "
        "Silakan ubah rentang tanggal atau negara bagian."
    )
    st.stop()

st.sidebar.caption(
    f"Menampilkan {filtered_df['order_id'].nunique():,} "
    "pesanan sesuai filter."
)


st.title("🛒 E-Commerce Public Dashboard")
st.markdown(
    "Analisis penjualan produk, ketepatan pengiriman, "
    "dan kontribusi penjualan berdasarkan negara bagian "
    "pada tahun 2017."
)

st.divider()

total_sales = main_df["price"].sum()
total_orders = main_df["order_id"].nunique()

delivery_df = main_df.drop_duplicates(subset="order_id").copy()

delivery_df["is_late"] = (
    delivery_df["order_delivered_customer_date"].dt.normalize()
    >
    delivery_df["order_estimated_delivery_date"].dt.normalize()
)

late_percentage = delivery_df["is_late"].mean() * 100

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Total Nilai Penjualan",
        value=f"${total_sales:,.2f}"
    )

with col2:
    st.metric(
        label="Total Pesanan",
        value=f"{total_orders:,}"
    )

with col3:
    st.metric(
        label="Persentase Keterlambatan",
        value=f"{late_percentage:.2f}%"
    )

# Visualisasi 1: Penjualan Berdasarkan Kategori
st.divider()
st.subheader("Penjualan Berdasarkan Kategori Produk")

st.markdown(
    "Perbandingan lima kategori produk dengan total nilai "
    "penjualan tertinggi dan terendah selama tahun 2017."
)

category_sales = (
    main_df[
        main_df["product_category_name_english"] != "unknown"
    ]
    .groupby("product_category_name_english", as_index=False)
    .agg(total_sales=("price", "sum"))
    .sort_values("total_sales", ascending=False)
)

top_5 = category_sales.head(5).sort_values("total_sales")
bottom_5 = category_sales.tail(5).sort_values("total_sales")

col1, col2 = st.columns(2)

with col1:
    fig_top = px.bar(
        top_5,
        x="total_sales",
        y="product_category_name_english",
        orientation="h",
        title="5 Kategori Penjualan Tertinggi",
        labels={
            "total_sales": "Total Penjualan ($)",
            "product_category_name_english": "Kategori Produk"
        },
        color_discrete_sequence=["steelblue"]
    )

    fig_top.update_layout(showlegend=False)
    st.plotly_chart(fig_top, use_container_width=True)

with col2:
    fig_bottom = px.bar(
        bottom_5,
        x="total_sales",
        y="product_category_name_english",
        orientation="h",
        title="5 Kategori Penjualan Terendah",
        labels={
            "total_sales": "Total Penjualan ($)",
            "product_category_name_english": "Kategori Produk"
        },
        color_discrete_sequence=["salmon"]
    )

    fig_bottom.update_layout(showlegend=False)
    st.plotly_chart(fig_bottom, use_container_width=True)

st.info(
    "Kategori bed_bath_table memiliki nilai penjualan tertinggi "
    "($490.596,92$), sedangkan diapers_and_hygiene memiliki "
    "nilai penjualan terendah ($76,00$)."
)

# Visualisasi 2: Ketepatan Pengiriman
st.divider()
st.subheader("Analisis Ketepatan Pengiriman")

st.markdown(
    "Persentase pesanan yang diterima tepat waktu atau lebih awal "
    "dibandingkan dengan pesanan yang melewati estimasi pengiriman "
    "selama tahun 2017."
)

delivery_summary = (
    delivery_df["is_late"]
    .value_counts()
    .reindex([False, True], fill_value=0)
    .reset_index()
)

delivery_summary.columns = ["is_late", "total_orders"]

delivery_summary["status"] = delivery_summary["is_late"].map({
    False: "Tepat Waktu / Lebih Awal",
    True: "Terlambat"
})

fig_delivery = px.pie(
    delivery_summary,
    names="status",
    values="total_orders",
    hole=0.55,
    color="status",
    color_discrete_map={
        "Tepat Waktu / Lebih Awal": "#2E8B57",
        "Terlambat": "#E74C3C"
    }
)

fig_delivery.update_traces(
    textinfo="percent",
    textposition="inside",
    hovertemplate=(
        "<b>%{label}</b><br>"
        "Jumlah Pesanan: %{value:,}<br>"
        "Persentase: %{percent}<extra></extra>"
    )
)

fig_delivery.update_layout(
    height=420,
    legend_title_text="Status Pengiriman"
)

col1, col2 = st.columns([2, 1])

with col1:
    st.plotly_chart(fig_delivery, use_container_width=True)

with col2:
    st.markdown("#### ")

    late_orders = int(delivery_df["is_late"].sum())
    ontime_orders = len(delivery_df) - late_orders

    st.metric("Total Pesanan", f"{len(delivery_df):,}")
    st.metric("Tepat Waktu / Lebih Awal", f"{ontime_orders:,}")
    st.metric("Terlambat", f"{late_orders:,}")

st.info(
    f"Dari {len(delivery_df):,} pesanan yang diterima pelanggan, "
    f"sebanyak {late_orders:,} pesanan ({late_percentage:.2f}%) "
    "mengalami keterlambatan. Sebagian besar pesanan diterima "
    "sesuai atau sebelum estimasi pengiriman."
)

# Visualisasi 3: Penjualan Berdasarkan Negara Bagian
st.divider()
st.subheader("Kontribusi Penjualan Berdasarkan Negara Bagian")

st.markdown(
    "Analisis kontribusi total nilai penjualan berdasarkan "
    "negara bagian pelanggan selama tahun 2017."
)

state_sales = (
    main_df.groupby("customer_state", as_index=False)
    .agg(total_sales=("price", "sum"))
    .sort_values("total_sales", ascending=False)
)

state_sales["contribution_pct"] = (
    state_sales["total_sales"] / state_sales["total_sales"].sum() * 100
)

top_n = st.slider(
    "Jumlah negara bagian yang ditampilkan",
    min_value=5,
    max_value=len(state_sales),
    value=10,
    step=1
)

top_states = (
    state_sales.head(top_n)
    .sort_values("total_sales", ascending=True)
)

fig_state = px.bar(
    top_states,
    x="total_sales",
    y="customer_state",
    orientation="h",
    color="total_sales",
    color_continuous_scale="Blues",
    custom_data=["contribution_pct"],
    labels={
        "total_sales": "Total Penjualan ($)",
        "customer_state": "Negara Bagian"
    },
    title=f"{top_n} Negara Bagian dengan Penjualan Tertinggi"
)

fig_state.update_traces(
    hovertemplate=(
        "<b>%{y}</b><br>"
        "Total Penjualan: $%{x:,.2f}<br>"
        "Kontribusi: %{customdata[0]:.2f}%"
        "<extra></extra>"
    )
)

fig_state.update_layout(
    height=max(450, top_n * 35),
    showlegend=False,
    coloraxis_showscale=False,
    yaxis_title=None
)

st.plotly_chart(fig_state, use_container_width=True)

top_3_states = state_sales.head(3)
top_3_contribution = top_3_states["contribution_pct"].sum()

st.markdown("#### Tiga Negara Bagian dengan Kontribusi Terbesar")

col1, col2, col3 = st.columns(3)

for col, (_, row) in zip(
    [col1, col2, col3],
    top_3_states.iterrows()
):
    with col:
        st.metric(
            label=row["customer_state"],
            value=f"${row['total_sales']:,.2f}",
            delta=f"{row['contribution_pct']:.2f}% dari total"
        )

st.info(
    f"Tiga negara bagian dengan kontribusi penjualan terbesar "
    f"adalah SP, RJ, dan MG, dengan total kontribusi "
    f"{top_3_contribution:.2f}% dari keseluruhan nilai penjualan."
)
