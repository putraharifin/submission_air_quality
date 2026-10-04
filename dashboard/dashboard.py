import glob
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Air Quality Beijing Dashboard",
    page_icon="🌫️",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"

@st.cache_data
def load_data():
    files = sorted(DATA_DIR.glob("PRSA_Data_*.csv"))
    if len(files) != 12:
        raise FileNotFoundError(
            f"Ditemukan {len(files)} file. Pastikan 12 file PRSA_Data_*.csv ada di folder data/."
        )

    frames = []
    for file in files:
        temp = pd.read_csv(file)
        frames.append(temp)

    df = pd.concat(frames, ignore_index=True)
    df["datetime"] = pd.to_datetime(
        df[["year", "month", "day", "hour"]], errors="coerce"
    )

    non_negative_cols = ["PM2.5", "PM10", "SO2", "NO2", "CO", "O3", "PRES", "RAIN", "WSPM"]
    for col in non_negative_cols:
        df.loc[df[col] < 0, col] = np.nan

    df = df.drop_duplicates().sort_values(["station", "datetime"])

    numeric_cols = [
        "PM2.5", "PM10", "SO2", "NO2", "CO", "O3",
        "TEMP", "PRES", "DEWP", "RAIN", "WSPM"
    ]
    for col in numeric_cols:
        df[col] = df.groupby("station")[col].transform(
            lambda s: s.interpolate(method="linear", limit_direction="both")
        )
        df[col] = df[col].fillna(df.groupby("station")[col].transform("median"))

    df["wd"] = df.groupby("station")["wd"].transform(lambda s: s.ffill().bfill())
    df["wd"] = df["wd"].fillna(df["wd"].mode().iloc[0])

    df["season"] = df["month"].map({
        12: "Winter", 1: "Winter", 2: "Winter",
        3: "Spring", 4: "Spring", 5: "Spring",
        6: "Summer", 7: "Summer", 8: "Summer",
        9: "Autumn", 10: "Autumn", 11: "Autumn"
    })
    df["year_month"] = df["datetime"].dt.to_period("M").astype(str)
    return df

st.title("🌫️ Air Quality Beijing — Interactive Dashboard")
st.caption("Analisis PM2.5 pada 12 stasiun pemantauan, periode Maret 2013–Februari 2017.")

try:
    df = load_data()
except FileNotFoundError as e:
    st.error(str(e))
    st.stop()

# Sidebar
st.sidebar.header("Filter")
stations = sorted(df["station"].unique())
selected_stations = st.sidebar.multiselect(
    "Stasiun",
    stations,
    default=stations
)

min_date = df["datetime"].min().date()
max_date = df["datetime"].max().date()
date_range = st.sidebar.date_input(
    "Rentang tanggal",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

if len(date_range) == 2:
    start_date, end_date = date_range
else:
    start_date, end_date = min_date, max_date

filtered = df[
    df["station"].isin(selected_stations)
    & (df["datetime"].dt.date >= start_date)
    & (df["datetime"].dt.date <= end_date)
].copy()

if filtered.empty:
    st.warning("Tidak ada data untuk filter yang dipilih.")
    st.stop()

# KPI
avg_pm25 = filtered["PM2.5"].mean()
max_pm25 = filtered["PM2.5"].max()
worst_station = (
    filtered.groupby("station")["PM2.5"].mean().idxmax()
    if not filtered.empty else "-"
)
worst_value = (
    filtered.groupby("station")["PM2.5"].mean().max()
    if not filtered.empty else np.nan
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Rata-rata PM2.5", f"{avg_pm25:.2f}")
c2.metric("PM2.5 Maksimum", f"{max_pm25:.2f}")
c3.metric("Stasiun Tertinggi", worst_station)
c4.metric("Rata-rata Stasiun Tertinggi", f"{worst_value:.2f}")

st.divider()

# Trend
monthly = (
    filtered.groupby(["year_month", "station"], as_index=False)["PM2.5"]
    .mean()
    .rename(columns={"PM2.5": "PM2.5_mean"})
)

fig_trend = px.line(
    monthly,
    x="year_month",
    y="PM2.5_mean",
    color="station",
    title="Tren Rata-rata PM2.5 Bulanan per Stasiun",
    labels={"year_month": "Bulan", "PM2.5_mean": "Rata-rata PM2.5"}
)
fig_trend.update_layout(hovermode="x unified")
st.plotly_chart(fig_trend, use_container_width=True)

# Ranking
ranking = (
    filtered.groupby("station", as_index=False)["PM2.5"]
    .mean()
    .sort_values("PM2.5", ascending=True)
)

fig_rank = px.bar(
    ranking,
    x="PM2.5",
    y="station",
    orientation="h",
    title="Ranking Rata-rata PM2.5 per Stasiun",
    labels={"PM2.5": "Rata-rata PM2.5", "station": "Stasiun"}
)
st.plotly_chart(fig_rank, use_container_width=True)

# Seasonal
season_order = ["Spring", "Summer", "Autumn", "Winter"]
season = (
    filtered.groupby("season", as_index=False)["PM2.5"]
    .mean()
)
season["season"] = pd.Categorical(
    season["season"], categories=season_order, ordered=True
)
season = season.sort_values("season")

fig_season = px.bar(
    season,
    x="season",
    y="PM2.5",
    title="Rata-rata PM2.5 Menurut Musim",
    labels={"PM2.5": "Rata-rata PM2.5", "season": "Musim"}
)
st.plotly_chart(fig_season, use_container_width=True)

# Correlation
weather_cols = ["TEMP", "PRES", "DEWP", "RAIN", "WSPM"]
corr = filtered[["PM2.5"] + weather_cols].corr()
corr_pm25 = corr[["PM2.5"]].sort_values("PM2.5", ascending=False)

st.subheader("Korelasi PM2.5 dengan Faktor Meteorologi")
st.dataframe(corr_pm25.style.format("{:.3f}"), use_container_width=True)

st.subheader("Data Ringkas")
st.dataframe(
    filtered[["datetime", "station", "PM2.5", "TEMP", "PRES", "DEWP", "RAIN", "WSPM"]]
    .sort_values("datetime", ascending=False)
    .head(100),
    use_container_width=True
)
