# Import library yang dibutuhkan
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
from PIL import Image

# set style seaborn
sns.set(style='dark')

# menyiapkan dataframe
day_df = pd.read_csv("dashboard/day_df.csv")
day_df.head()

# Menyiapkan daily_rent_df
def create_daily_rent_df(df):
    daily_rent_df = df.groupby(by='date(day)').agg({
        'count': 'sum'
    }).reset_index()
    return daily_rent_df

# Menyiapkan daily_registered_rent_df
def create_daily_registered_rent_df(df):
    daily_registered_rent_df = df.groupby(by='date(day)').agg({
        'registered': 'sum'
    }).reset_index()
    return daily_registered_rent_df

# Menyiapkan daily_casual_rent_df
def create_daily_casual_rent_df(df):
    daily_casual_rent_df = df.groupby(by='date(day)').agg({
        'casual': 'sum'
    }).reset_index()
    return daily_casual_rent_df

# Menyiapkan annually_rent_df
def create_annually_rent_df(df):
    annually_rent_df = df.groupby(by='year').agg({
    'count': 'sum'
    }).reset_index()
    return annually_rent_df

# Menyiapkan monthly_rent_df
def create_monthly_rent_df(df):
    monthly_rent_df = df.groupby(by='month').agg({
        'count': 'sum'
    })
    ordered_months = [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    ]
    monthly_rent_df = monthly_rent_df.reindex(ordered_months, fill_value=0)
    return monthly_rent_df

# Menyiapkan weekday_rent_df
def create_weekday_rent_df(df):
    weekday_rent_df = df.groupby(by='weekday').agg({
        'count': 'sum'
    }).reset_index()
    return weekday_rent_df

# Menyiapkan workingday_rent_df
def create_workingday_rent_df(df):
    workingday_rent_df = df.groupby(by='workingday').agg({
        'count': 'sum'
    }).reset_index()
    return workingday_rent_df

# Menyiapkan season_rent_df
def create_season_rent_df(df):
    season_rent_df = df.groupby(by='season').sum().reset_index()
    return season_rent_df

# Membuat komponen filter
min_date = pd.to_datetime(day_df['date(day)']).dt.date.min()
max_date = pd.to_datetime(day_df['date(day)']).dt.date.max()

# upload logo
image = Image.open("OIG.png")
with st.sidebar:
    st.image(image)
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value= min_date,
        max_value= max_date,
        value=[min_date, max_date]
    )

# memasukan data yang sudah difilter ke main_df
main_df = day_df[(day_df['date(day)'] >= str(start_date)) & 
                (day_df['date(day)'] <= str(end_date))]

# Menyiapkan berbagai dataframe
daily_rent_df = create_daily_rent_df(main_df)
daily_registered_rent_df = create_daily_registered_rent_df(main_df)
daily_casual_rent_df = create_daily_casual_rent_df(main_df)
annually_rent_df = create_annually_rent_df(main_df)
season_rent_df = create_season_rent_df(main_df)
monthly_rent_df = create_monthly_rent_df(main_df)
weekday_rent_df = create_weekday_rent_df(main_df)
workingday_rent_df = create_workingday_rent_df(main_df)

# membuat dashboard lengkap


# Judul
st.header('Dashboard Rental Bike :bike:')

# Membuat jumlah penyewaan harian
st.subheader('Daily Rentals')
col1, col2, col3 = st.columns(3)

# kolom 1 total registered user
with col1:
    daily_rent_registered = daily_registered_rent_df['registered'].sum()
    st.metric('Registered User', value= daily_rent_registered)    

# kolom 2 total casual user
with col2:
    daily_rent_casual = daily_casual_rent_df['casual'].sum()
    st.metric('Casual User', value= daily_rent_casual)

# kolom 3 total keseluruhan
with col3:
    daily_rent_total = daily_rent_df['count'].sum()
    st.metric('Total User', value= daily_rent_total)
    
# Membuat penyewaan pertahun
st.subheader('Annually Rental')
fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(
    x='year',
    y='count',
    data=annually_rent_df,
    hue='year',
    palette='Accent',
    legend=False,
    ax=ax)

ax.set_xlabel(None)
ax.set_ylabel(None)
ax.tick_params(axis='x', labelsize=12)
ax.get_yaxis().get_major_formatter().set_scientific(False)
st.pyplot(fig)
    
# Membuat jumlah penyewaan bulanan
st.subheader('Monthly Rentals')
fig, ax = plt.subplots(figsize=(24, 8))
ax.plot(
    monthly_rent_df.index,
    monthly_rent_df['count'],
    marker='o', 
    linewidth=2,
    color='tab:blue'
)

for index, row in enumerate(monthly_rent_df['count']):
    ax.text(index, row + 1, str(row), ha='center', va='bottom', fontsize=12)

ax.tick_params(axis='x', labelsize=25, rotation=45)
ax.tick_params(axis='y', labelsize=20)
st.pyplot(fig)

# Membuat jumlah penyewaan saat weekday, workingday dan holiday
st.subheader('Weekday, Workingday, and Holiday Rentals')

fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(15,11))

# Berdasarkan workingday
sns.barplot(
    x='workingday',
    y='count',
    data=workingday_rent_df,
    ax=axes[0],
    hue='workingday',
    palette='Accent',
    legend=False)
axes[0].set_title('Jumlah Pengguna Sepeda Berdasarkan Hari Kerja atau Hari Libur', loc='center', fontsize=20)
axes[0].set_xlabel('Hari Kerja')
axes[0].set_ylabel(None)

day_df['weekday'] = pd.Categorical(day_df['weekday'], categories=
    ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    ordered=True)

daily_count = day_df.groupby(by='weekday', observed=True).agg({
    'count': 'mean'
})

# Berdasarkan weekday
sns.barplot(
    x='weekday',
    y='count',
    data=daily_count,
    ax=axes[1],
    hue='weekday',
    palette='Accent',
    legend=False)

axes[1].set_title('Jumlah Pengguna Sepeda Berdasarkan Hari', loc='center', fontsize=20)
axes[1].set_xlabel('Hari')
axes[1].set_ylabel(None)

# Menambahkan label
for p in axes[1].patches:
    axes[1].annotate(f'{p.get_height():.0f}', (p.get_x() + p.get_width() / 2., p.get_height()),
                     ha='center', va='center', xytext=(0, 10), textcoords='offset points')

plt.tight_layout()
st.pyplot(fig)

# Membuat jumlah penyewaan berdasarkan musim
st.subheader('Seasonly Rentals')

fig, ax = plt.subplots(figsize=(10,6))
sns.barplot(
    x='season',
    y='count',
    data=season_rent_df,
    hue='season',
    palette='Set2',
    legend=False)

ax.set_title('Jumlah Pengguna Sepeda Tiap Musim')
ax.set_xlabel('Musim')
ax.set_ylabel(None)
ax.get_yaxis().get_major_formatter().set_scientific(False)
ax.tick_params(axis='x', labelsize=12)
st.pyplot(fig)

st.caption('Copyright (c) Fajar Kurnia 2023')
