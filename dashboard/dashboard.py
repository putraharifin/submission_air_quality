import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path


# =========================================================
# KONFIGURASI HALAMAN
# =========================================================

st.set_page_config(
    page_title="Beijing Air Quality Dashboard",
    page_icon="🌏",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# DARK THEME
# =========================================================

st.markdown("""
<style>

    /* ================================
       GLOBAL BACKGROUND
       ================================ */

    .stApp {
        background-color: #0f172a;
        color: #f8fafc;
    }

    .main {
        background-color: #0f172a;
        color: #f8fafc;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }


    /* ================================
       SIDEBAR
       ================================ */

    section[data-testid="stSidebar"] {
        background-color: #111827;
        border-right: 1px solid #1f2937;
    }

    section[data-testid="stSidebar"] * {
        color: #f8fafc !important;
    }

    section[data-testid="stSidebar"] .stCaption {
        color: #cbd5e1 !important;
    }


    /* ================================
       TITLE
       ================================ */

    .dashboard-title {
        font-size: 2.4rem;
        font-weight: 700;
        margin-bottom: 0.2rem;
        color: #f8fafc;
    }

    .dashboard-subtitle {
        font-size: 1.05rem;
        color: #cbd5e1;
        margin-bottom: 1.5rem;
        line-height: 1.6;
    }


    /* ================================
       SECTION TITLE
       ================================ */

    .section-title {
        font-size: 1.55rem;
        font-weight: 700;
        color: #f8fafc;
        margin-top: 2rem;
        margin-bottom: 0.3rem;
    }

    .section-description {
        color: #cbd5e1;
        font-size: 0.95rem;
        margin-bottom: 1rem;
        line-height: 1.6;
    }


    /* ================================
       INSIGHT BOX
       ================================ */

    .insight-box {
        background-color: #1e293b;
        border-left: 5px solid #60a5fa;
        padding: 1rem 1.2rem;
        border-radius: 8px;
        margin: 0.8rem 0 1.2rem 0;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
    }

    .insight-title {
        font-weight: 700;
        color: #f8fafc;
        margin-bottom: 0.3rem;
    }

    .insight-text {
        color: #dbeafe;
        line-height: 1.7;
    }


    /* ================================
       RECOMMENDATION BOX
       ================================ */

    .recommendation-box {
        background-color: #1e293b;
        color: #f8fafc;
        padding: 1rem 1.2rem;
        border-radius: 8px;
        margin-bottom: 0.8rem;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
        line-height: 1.7;
    }

    .recommendation-box b {
        color: #93c5fd;
    }


    /* ================================
       SMALL NOTE
       ================================ */

    .small-note {
        color: #cbd5e1;
        font-size: 0.85rem;
    }


    /* ================================
       METRIC CARDS
       ================================ */

    div[data-testid="stMetric"] {
        background-color: #1e293b;
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid #334155;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
    }

    div[data-testid="stMetric"] label {
        color: #cbd5e1 !important;
    }

    div[data-testid="stMetric"] [data-testid="stMetricValue"] {
        color: #f8fafc !important;
    }

    div[data-testid="stMetric"] [data-testid="stMetricDelta"] {
        color: #93c5fd !important;
    }


    /* ================================
       EXPANDER
       ================================ */

    div[data-testid="stExpander"] {
        background-color: #1e293b;
        border: 1px solid #334155;
        border-radius: 8px;
    }

    div[data-testid="stExpander"] * {
        color: #f8fafc;
    }


    /* ================================
       DATAFRAME
       ================================ */

    div[data-testid="stDataFrame"] {
        border: 1px solid #334155;
        border-radius: 8px;
    }


    /* ================================
       SELECTBOX / MULTISELECT
       ================================ */

    div[data-baseweb="select"] > div {
        background-color: #1e293b;
        border-color: #475569;
    }

    div[data-baseweb="select"] span {
        color: #f8fafc !important;
    }


    /* ================================
       DATE INPUT
       ================================ */

    div[data-testid="stDateInput"] input {
        background-color: #1e293b;
        color: #f8fafc;
        border-color: #475569;
    }


    /* ================================
       CAPTION
       ================================ */

    .stCaption {
        color: #94a3b8 !important;
    }


    /* ================================
       MARKDOWN TEXT
       ================================ */

    .stMarkdown {
        color: #f8fafc;
    }


    /* ================================
       DIVIDER
       ================================ */

    hr {
        border-color: #334155;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# LOAD DATA
# =========================================================

@st.cache_data
def load_data():

    possible_dirs = [
        Path("data"),
        Path("."),
        Path("../data")
    ]

    files = []

    for directory in possible_dirs:
        if directory.exists():
            found = sorted(directory.glob("PRSA_Data_*.csv"))
            if found:
                files = found
                break

    if not files:
        raise FileNotFoundError(
            "File dataset tidak ditemukan. "
            "Pastikan folder 'data' berisi file PRSA_Data_*.csv."
        )

    frames = []

    for file in files:
        temp = pd.read_csv(file)

        # Nama stasiun berasal dari nama file
        station = file.stem.replace(
            "PRSA_Data_", ""
        ).replace(
            "_20130301-20170228", ""
        )

        temp["station"] = station
        frames.append(temp)

    df = pd.concat(frames, ignore_index=True)

    # -----------------------------------------------------
    # Cleaning
    # -----------------------------------------------------

    df = df.drop_duplicates()

    df["datetime"] = pd.to_datetime(
        df[["year", "month", "day", "hour"]],
        errors="coerce"
    )

    non_negative_columns = [
        "PM2.5",
        "PM10",
        "SO2",
        "NO2",
        "CO",
        "O3",
        "PRES",
        "RAIN",
        "WSPM"
    ]

    for col in non_negative_columns:
        if col in df.columns:
            df.loc[df[col] < 0, col] = np.nan

    df = df.sort_values(
        ["station", "datetime"]
    ).reset_index(drop=True)

    numeric_columns = [
        "PM2.5",
        "PM10",
        "SO2",
        "NO2",
        "CO",
        "O3",
        "PRES",
        "TEMP",
        "DEWP",
        "RAIN",
        "WSPM"
    ]

    numeric_columns = [
        col for col in numeric_columns
        if col in df.columns
    ]

    # Interpolasi berdasarkan stasiun
    df[numeric_columns] = (
        df.groupby("station")[numeric_columns]
        .transform(
            lambda x: x.interpolate(
                method="linear",
                limit_direction="both"
            )
        )
    )

    # Median fallback
    for col in numeric_columns:
        df[col] = df[col].fillna(df[col].median())

    if "wd" in df.columns:
        df["wd"] = df["wd"].fillna("Unknown")

    # -----------------------------------------------------
    # Feature Engineering
    # -----------------------------------------------------

    df["year_month"] = df["datetime"].dt.to_period("M").astype(str)
    df["month_num"] = df["datetime"].dt.month

    def get_season(month):
        if month in [12, 1, 2]:
            return "Winter"
        elif month in [3, 4, 5]:
            return "Spring"
        elif month in [6, 7, 8]:
            return "Summer"
        else:
            return "Autumn"

    df["season"] = df["month_num"].apply(get_season)

    # Kategori kecepatan angin berdasarkan kuartil
    wind_quantiles = df["WSPM"].quantile(
        [0, 0.25, 0.50, 0.75, 1]
    ).values

    wind_quantiles = np.unique(wind_quantiles)

    wind_labels = [
        "Rendah",
        "Sedang",
        "Tinggi",
        "Sangat Tinggi"
    ]

    if len(wind_quantiles) > 2:

        labels = wind_labels[:len(wind_quantiles) - 1]

        df["wind_category"] = pd.cut(
            df["WSPM"],
            bins=wind_quantiles,
            labels=labels,
            include_lowest=True,
            duplicates="drop"
        )

    else:
        df["wind_category"] = "Tidak tersedia"

    # Kategori PM2.5 berdasarkan kuartil
    pm25_quantiles = df["PM2.5"].quantile(
        [0, 0.25, 0.50, 0.75, 1]
    ).values

    pm25_quantiles = np.unique(pm25_quantiles)

    pm_labels = [
        "Rendah",
        "Sedang",
        "Tinggi",
        "Sangat Tinggi"
    ]

    if len(pm25_quantiles) > 2:

        labels = pm_labels[:len(pm25_quantiles) - 1]

        df["pm25_group"] = pd.cut(
            df["PM2.5"],
            bins=pm25_quantiles,
            labels=labels,
            include_lowest=True,
            duplicates="drop"
        )

    else:
        df["pm25_group"] = "Tidak tersedia"

    return df


# =========================================================
# LOAD DATA
# =========================================================

try:
    df = load_data()

except Exception as e:

    st.error(
        f"Dataset tidak dapat dimuat: {e}"
    )

    st.stop()


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="dashboard-title">🌏 Kondisi Kualitas Udara Beijing</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="dashboard-subtitle">
    Dashboard ini menyajikan kondisi PM2.5 pada 12 stasiun pemantauan
    kualitas udara di Beijing selama periode 2013–2017.
    Gunakan filter di sebelah kiri untuk melihat wilayah dan periode tertentu.
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# SIDEBAR FILTER
# =========================================================

st.sidebar.title("🔎 Filter Data")

stations = sorted(df["station"].dropna().unique())

selected_stations = st.sidebar.multiselect(
    "Pilih stasiun",
    options=stations,
    default=stations
)

min_date = df["datetime"].min().date()
max_date = df["datetime"].max().date()

date_range = st.sidebar.date_input(
    "Pilih periode",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

if len(date_range) == 2:

    start_date = pd.Timestamp(date_range[0])
    end_date = pd.Timestamp(date_range[1]) + pd.Timedelta(days=1)

else:

    start_date = pd.Timestamp(min_date)
    end_date = pd.Timestamp(max_date) + pd.Timedelta(days=1)


filtered_df = df[
    (df["station"].isin(selected_stations))
    &
    (df["datetime"] >= start_date)
    &
    (df["datetime"] < end_date)
].copy()


if filtered_df.empty:

    st.warning(
        "Tidak ada data untuk filter yang dipilih."
    )

    st.stop()


# =========================================================
# RINGKASAN UTAMA
# =========================================================

st.markdown(
    '<div class="section-title">📊 Gambaran Umum</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="section-description">
    Empat indikator berikut memberikan gambaran singkat mengenai
    kondisi PM2.5 pada data yang sedang ditampilkan.
    </div>
    """,
    unsafe_allow_html=True
)


average_pm25 = filtered_df["PM2.5"].mean()
max_pm25 = filtered_df["PM2.5"].max()

station_average = (
    filtered_df.groupby("station")["PM2.5"]
    .mean()
    .sort_values(ascending=False)
)

highest_station = station_average.index[0]
highest_station_value = station_average.iloc[0]

winter_data = filtered_df[
    filtered_df["season"] == "Winter"
]

winter_average = (
    winter_data["PM2.5"].mean()
    if not winter_data.empty
    else np.nan
)


col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "Rata-rata PM2.5",
        f"{average_pm25:.2f} µg/m³",
        help=(
            "Nilai rata-rata konsentrasi PM2.5 "
            "dari seluruh data yang sedang dipilih."
        )
    )

with col2:

    st.metric(
        "Nilai PM2.5 Tertinggi",
        f"{max_pm25:.2f} µg/m³",
        help=(
            "Nilai PM2.5 tertinggi yang tercatat "
            "dalam data terpilih."
        )
    )

with col3:

    st.metric(
        "Stasiun dengan Rata-rata Tertinggi",
        highest_station,
        help=(
            f"Rata-rata PM2.5 di {highest_station} "
            f"adalah {highest_station_value:.2f} µg/m³."
        )
    )

with col4:

    if not np.isnan(winter_average):

        st.metric(
            "Rata-rata PM2.5 saat Winter",
            f"{winter_average:.2f} µg/m³",
            help=(
                "Rata-rata PM2.5 pada bulan Desember, "
                "Januari, dan Februari."
            )
        )

    else:

        st.metric(
            "Rata-rata PM2.5 saat Winter",
            "Tidak ada data"
        )


st.caption(
    "Catatan: nilai maksimum dapat dipengaruhi oleh kejadian ekstrem "
    "atau pencatatan dengan konsentrasi sangat tinggi."
)


# =========================================================
# INTERPRETASI RINGKAS
# =========================================================

st.markdown(
    f"""
    <div class="insight-box">
        <div class="insight-title">💡 Apa yang dapat langsung kita lihat?</div>
        <div class="insight-text">
            Dari data yang sedang ditampilkan, rata-rata PM2.5 adalah
            <b>{average_pm25:.2f} µg/m³</b>.
            Stasiun dengan rata-rata tertinggi adalah
            <b>{highest_station}</b> dengan nilai
            <b>{highest_station_value:.2f} µg/m³</b>.
            Informasi berikutnya membantu melihat apakah konsentrasi
            tersebut hanya terjadi pada lokasi tertentu atau juga
            mengikuti pola waktu dan kondisi cuaca.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# LOKASI DENGAN POLUSI TERTINGGI
# =========================================================

st.markdown(
    '<div class="section-title">📍 Di mana konsentrasi PM2.5 paling tinggi?</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="section-description">
    Perbandingan rata-rata PM2.5 antarstasiun membantu menunjukkan
    wilayah mana yang secara umum memiliki konsentrasi PM2.5 lebih tinggi.
    </div>
    """,
    unsafe_allow_html=True
)


station_df = (
    filtered_df.groupby("station", as_index=False)
    .agg(
        average_pm25=("PM2.5", "mean")
    )
    .sort_values(
        "average_pm25",
        ascending=False
    )
)

fig_station = px.bar(
    station_df,
    x="average_pm25",
    y="station",
    orientation="h",
    text="average_pm25",
    labels={
        "average_pm25": "Rata-rata PM2.5 (µg/m³)",
        "station": "Stasiun"
    }
)

fig_station.update_traces(
    texttemplate="%{text:.2f}",
    textposition="outside"
)

fig_station.update_layout(
    height=500,
    margin=dict(l=20, r=40, t=20, b=20),
    showlegend=False
)

st.plotly_chart(
    fig_station,
    use_container_width=True
)


top_station = station_df.iloc[0]

st.markdown(
    f"""
    <div class="insight-box">
        <div class="insight-title">📌 Temuan utama</div>
        <div class="insight-text">
            <b>{top_station["station"]}</b> memiliki rata-rata PM2.5
            tertinggi pada data yang sedang ditampilkan,
            yaitu <b>{top_station["average_pm25"]:.2f} µg/m³</b>.
            Perbedaan antarstasiun menunjukkan bahwa tingkat polusi
            tidak sepenuhnya sama di seluruh wilayah Beijing.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# POLA WAKTU
# =========================================================

st.markdown(
    '<div class="section-title">📅 Kapan konsentrasi PM2.5 cenderung meningkat?</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="section-description">
    Grafik berikut menunjukkan perubahan rata-rata PM2.5 dari bulan ke bulan.
    Pola ini membantu melihat periode ketika konsentrasi polusi cenderung meningkat.
    </div>
    """,
    unsafe_allow_html=True
)


monthly_df = (
    filtered_df.groupby("year_month", as_index=False)
    .agg(
        average_pm25=("PM2.5", "mean")
    )
)

fig_monthly = px.line(
    monthly_df,
    x="year_month",
    y="average_pm25",
    markers=True,
    labels={
        "year_month": "Bulan",
        "average_pm25": "Rata-rata PM2.5 (µg/m³)"
    }
)

fig_monthly.update_layout(
    height=450,
    hovermode="x unified",
    margin=dict(l=20, r=20, t=20, b=20)
)

st.plotly_chart(
    fig_monthly,
    use_container_width=True
)


# ---------------------------------------------------------
# MUSIM
# ---------------------------------------------------------

season_order = [
    "Winter",
    "Spring",
    "Summer",
    "Autumn"
]

season_df = (
    filtered_df.groupby(
        "season",
        as_index=False,
        observed=False
    )
    .agg(
        average_pm25=("PM2.5", "mean")
    )
)

season_df["season"] = pd.Categorical(
    season_df["season"],
    categories=season_order,
    ordered=True
)

season_df = season_df.sort_values("season")


fig_season = px.bar(
    season_df,
    x="season",
    y="average_pm25",
    text="average_pm25",
    labels={
        "season": "Musim",
        "average_pm25": "Rata-rata PM2.5 (µg/m³)"
    }
)

fig_season.update_traces(
    texttemplate="%{text:.2f}",
    textposition="outside"
)

fig_season.update_layout(
    height=400,
    margin=dict(l=20, r=20, t=20, b=20),
    showlegend=False
)

st.plotly_chart(
    fig_season,
    use_container_width=True
)


# =========================================================
# TEMUAN MUSIM
# =========================================================

if not season_df.empty:

    highest_season = season_df.loc[
        season_df["average_pm25"].idxmax()
    ]

    lowest_season = season_df.loc[
        season_df["average_pm25"].idxmin()
    ]

    st.markdown(
        f"""
        <div class="insight-box">
            <div class="insight-title">❄️ Pola musiman</div>
            <div class="insight-text">
                Konsentrasi rata-rata PM2.5 tertinggi terjadi pada
                <b>{highest_season["season"]}</b> dengan nilai
                <b>{highest_season["average_pm25"]:.2f} µg/m³</b>.
                Sementara itu, rata-rata terendah terjadi pada
                <b>{lowest_season["season"]}</b> dengan nilai
                <b>{lowest_season["average_pm25"]:.2f} µg/m³</b>.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# HUBUNGAN DENGAN KONDISI CUACA
# =========================================================

st.markdown(
    '<div class="section-title">🌦️ Kondisi cuaca apa yang berkaitan dengan PM2.5?</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="section-description">
    Korelasi digunakan untuk melihat apakah perubahan beberapa variabel
    cuaca cenderung bergerak bersama dengan perubahan PM2.5.
    Nilai mendekati -1 atau +1 menunjukkan hubungan yang lebih kuat,
    sedangkan nilai mendekati 0 menunjukkan hubungan yang lemah.
    </div>
    """,
    unsafe_allow_html=True
)


weather_columns = [
    "PM2.5",
    "WSPM",
    "TEMP",
    "DEWP",
    "RAIN"
]

weather_columns = [
    col for col in weather_columns
    if col in filtered_df.columns
]

corr = filtered_df[weather_columns].corr()

fig_corr = px.imshow(
    corr,
    text_auto=".2f",
    aspect="auto",
    labels={
        "x": "Variabel",
        "y": "Variabel",
        "color": "Korelasi"
    }
)

fig_corr.update_layout(
    height=500,
    margin=dict(l=20, r=20, t=20, b=20)
)

st.plotly_chart(
    fig_corr,
    use_container_width=True
)


pm25_corr = (
    corr["PM2.5"]
    .drop("PM2.5")
    .sort_values()
    .reset_index()
)

pm25_corr.columns = [
    "variable",
    "correlation"
]


fig_corr_bar = px.bar(
    pm25_corr,
    x="correlation",
    y="variable",
    orientation="h",
    text="correlation",
    labels={
        "correlation": "Koefisien korelasi dengan PM2.5",
        "variable": "Variabel cuaca"
    }
)

fig_corr_bar.update_traces(
    texttemplate="%{text:.2f}",
    textposition="outside"
)

fig_corr_bar.update_layout(
    height=350,
    margin=dict(l=20, r=40, t=20, b=20)
)

st.plotly_chart(
    fig_corr_bar,
    use_container_width=True
)


strongest_relationship = pm25_corr.iloc[
    pm25_corr["correlation"].abs().argmax()
]

st.markdown(
    f"""
    <div class="insight-box">
        <div class="insight-title">🌬️ Hubungan yang paling terlihat</div>
        <div class="insight-text">
            Dari variabel cuaca yang dianalisis, <b>
            {strongest_relationship["variable"]}</b> memiliki hubungan
            paling kuat dengan PM2.5 dengan koefisien sekitar
            <b>{strongest_relationship["correlation"]:.2f}</b>.
            Hasil korelasi menunjukkan hubungan statistik,
            bukan bukti bahwa satu variabel secara langsung menyebabkan
            perubahan variabel lainnya.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# KECEPATAN ANGIN
# =========================================================

st.markdown(
    '<div class="section-title">🌬️ Bagaimana konsentrasi PM2.5 berubah berdasarkan kecepatan angin?</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="section-description">
    Kecepatan angin dibagi menjadi beberapa kelompok berdasarkan
    distribusi data. Tujuannya adalah melihat pola konsentrasi PM2.5
    pada kondisi angin yang relatif lebih rendah atau lebih tinggi.
    </div>
    """,
    unsafe_allow_html=True
)


wind_df = (
    filtered_df.groupby(
        "wind_category",
        observed=False,
        as_index=False
    )
    .agg(
        average_pm25=("PM2.5", "mean"),
        average_wind=("WSPM", "mean"),
        observation_count=("PM2.5", "count")
    )
)

fig_wind = px.bar(
    wind_df,
    x="wind_category",
    y="average_pm25",
    text="average_pm25",
    labels={
        "wind_category": "Kategori kecepatan angin",
        "average_pm25": "Rata-rata PM2.5 (µg/m³)"
    }
)

fig_wind.update_traces(
    texttemplate="%{text:.2f}",
    textposition="outside"
)

fig_wind.update_layout(
    height=420,
    margin=dict(l=20, r=20, t=20, b=20),
    showlegend=False
)

st.plotly_chart(
    fig_wind,
    use_container_width=True
)


if not wind_df.empty:

    highest_wind_pm25 = wind_df.loc[
        wind_df["average_pm25"].idxmax()
    ]

    st.markdown(
        f"""
        <div class="insight-box">
            <div class="insight-title">📌 Pola kecepatan angin</div>
            <div class="insight-text">
                Kelompok kecepatan angin <b>
                {highest_wind_pm25["wind_category"]}</b>
                memiliki rata-rata PM2.5 tertinggi,
                yaitu sekitar <b>
                {highest_wind_pm25["average_pm25"]:.2f} µg/m³</b>.
                Hasil ini dapat digunakan sebagai indikasi awal untuk
                memperhatikan kondisi polusi ketika kecepatan angin berada
                pada kelompok tersebut.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# DISTRIBUSI TINGKAT PM2.5
# =========================================================

st.markdown(
    '<div class="section-title">📈 Seberapa sering setiap stasiun mengalami PM2.5 tinggi?</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="section-description">
    Bagian ini memperlihatkan komposisi kategori PM2.5 pada masing-masing
    stasiun. Semakin besar bagian kategori tinggi dan sangat tinggi,
    semakin sering stasiun tersebut berada pada kondisi PM2.5 yang relatif tinggi
    dibandingkan distribusi keseluruhan data.
    </div>
    """,
    unsafe_allow_html=True
)


distribution = (
    filtered_df.groupby(
        ["station", "pm25_group"],
        observed=False
    )
    .size()
    .reset_index(name="count")
)

distribution["percentage"] = (
    distribution.groupby("station")["count"]
    .transform(lambda x: x / x.sum() * 100)
)


fig_distribution = px.bar(
    distribution,
    x="station",
    y="percentage",
    color="pm25_group",
    text_auto=".1f",
    labels={
        "station": "Stasiun",
        "percentage": "Proporsi (%)",
        "pm25_group": "Kategori PM2.5"
    }
)

fig_distribution.update_layout(
    barmode="stack",
    height=500,
    yaxis=dict(
        range=[0, 100],
        title="Proporsi pengamatan (%)"
    ),
    margin=dict(l=20, r=20, t=20, b=20)
)

st.plotly_chart(
    fig_distribution,
    use_container_width=True
)


# =========================================================
# STASIUN DENGAN PROPORSI TINGGI
# =========================================================

high_categories = [
    "Tinggi",
    "Sangat Tinggi"
]

high_pm25 = distribution[
    distribution["pm25_group"]
    .astype(str)
    .isin(high_categories)
]

high_station = (
    high_pm25.groupby("station")["percentage"]
    .sum()
    .sort_values(ascending=False)
)

if not high_station.empty:

    top_high_station = high_station.index[0]
    top_high_percentage = high_station.iloc[0]

    st.markdown(
        f"""
        <div class="insight-box">
            <div class="insight-title">⚠️ Area yang perlu mendapat perhatian</div>
            <div class="insight-text">
                <b>{top_high_station}</b> memiliki proporsi kategori
                <b>Tinggi + Sangat Tinggi</b> sebesar sekitar
                <b>{top_high_percentage:.2f}%</b> dari pengamatan
                pada data yang sedang ditampilkan.
                Stasiun dengan proporsi tinggi dapat menjadi prioritas
                untuk pemantauan lebih lanjut.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# TOP 10 PERIODE TERBURUK
# =========================================================

st.markdown(
    '<div class="section-title">🔥 Periode dengan konsentrasi PM2.5 tertinggi</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="section-description">
    Tabel berikut menampilkan 10 kombinasi bulan dan stasiun
    dengan rata-rata PM2.5 tertinggi. Informasi ini berguna untuk
    mengetahui periode dan lokasi yang perlu mendapat perhatian lebih.
    </div>
    """,
    unsafe_allow_html=True
)


top10 = (
    filtered_df.groupby(
        ["year_month", "station"],
        as_index=False
    )
    .agg(
        average_pm25=("PM2.5", "mean")
    )
    .sort_values(
        "average_pm25",
        ascending=False
    )
    .head(10)
)

top10["average_pm25"] = top10[
    "average_pm25"
].round(2)

top10.columns = [
    "Bulan",
    "Stasiun",
    "Rata-rata PM2.5 (µg/m³)"
]

st.dataframe(
    top10,
    use_container_width=True,
    hide_index=True
)


# =========================================================
# TEMUAN UTAMA
# =========================================================

st.markdown(
    '<div class="section-title">📝 Temuan Utama</div>',
    unsafe_allow_html=True
)

overall_mean = filtered_df["PM2.5"].mean()

st.markdown(
    f"""
    <div class="recommendation-box">
        <b>1. Lokasi dengan konsentrasi lebih tinggi</b><br>
        {highest_station} merupakan stasiun dengan rata-rata PM2.5
        tertinggi pada filter yang sedang digunakan.
    </div>

    <div class="recommendation-box">
        <b>2. Pola waktu</b><br>
        Konsentrasi PM2.5 berubah sepanjang waktu dan menunjukkan
        perbedaan antarperiode maupun musim.
    </div>

    <div class="recommendation-box">
        <b>3. Kondisi cuaca</b><br>
        Beberapa variabel cuaca memiliki hubungan dengan PM2.5,
        terutama variabel yang menunjukkan koefisien korelasi lebih besar
        secara absolut.
    </div>

    <div class="recommendation-box">
        <b>4. Kecepatan angin</b><br>
        Kelompok kecepatan angin tertentu menunjukkan rata-rata PM2.5
        yang lebih tinggi dibandingkan kelompok lainnya.
    </div>

    <div class="recommendation-box">
        <b>5. Periode perlu perhatian</b><br>
        Beberapa kombinasi bulan dan stasiun memiliki rata-rata PM2.5
        jauh lebih tinggi daripada rata-rata keseluruhan
        ({overall_mean:.2f} µg/m³).
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# REKOMENDASI
# =========================================================

st.markdown(
    '<div class="section-title">💡 Rekomendasi Tindakan</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="recommendation-box">
        <b>1. Prioritaskan pemantauan stasiun dengan PM2.5 tinggi</b><br>
        Stasiun yang secara konsisten memiliki rata-rata atau proporsi
        PM2.5 tinggi dapat menjadi prioritas untuk pemeriksaan sumber emisi.
    </div>

    <div class="recommendation-box">
        <b>2. Tingkatkan kewaspadaan pada periode musim dingin</b><br>
        Periode Desember–Februari perlu mendapat perhatian karena
        konsentrasi PM2.5 cenderung lebih tinggi dalam hasil analisis.
    </div>

    <div class="recommendation-box">
        <b>3. Gunakan informasi kecepatan angin sebagai indikator tambahan</b><br>
        Kondisi angin dapat digunakan bersama informasi PM2.5 untuk
        membantu menentukan periode pemantauan atau peringatan kualitas udara.
    </div>

    <div class="recommendation-box">
        <b>4. Lakukan pengelolaan polusi lintas wilayah</b><br>
        Perbedaan kondisi antarstasiun menunjukkan pentingnya pemantauan
        tidak hanya pada satu lokasi, tetapi juga melihat pola regional.
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# DATA DETAIL
# =========================================================

with st.expander("📋 Lihat data yang sedang digunakan"):

    display_columns = [
        "datetime",
        "station",
        "PM2.5",
        "PM10",
        "SO2",
        "NO2",
        "CO",
        "O3",
        "TEMP",
        "PRES",
        "DEWP",
        "RAIN",
        "WSPM",
        "wd"
    ]

    display_columns = [
        col for col in display_columns
        if col in filtered_df.columns
    ]

    st.dataframe(
        filtered_df[display_columns],
        use_container_width=True,
        hide_index=True
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown(
    """
    <div style="text-align:center; color:#6b7280; font-size:0.85rem;">
        Beijing Multi-Site Air Quality Analysis · 2013–2017<br>
        Dashboard dibuat untuk tujuan analisis dan eksplorasi data.
    </div>
    """,
    unsafe_allow_html=True
)