# Bike Rental - Submissions Dashboard ✨

Ini adalah submission pada course "Belajar Analisis Data dengan Python". Untuk menyelesaikan course ini peserta diminta untuk menganalisa data dan membuat sebuah dashboard dari dataset Bike Sharing. 

## 1. Struktur File
submission
```
├───dashboard
|   ├───day_df.csv
|   └───dashboard.py
├───data
|   ├───hour.csv
|   ├───day.csv
|   └───Readme.txt
├───bike_sharing.ipynb
├───README.md
└───requirements.txt
```
## 2. Proses Analisis Data
1. Data Wrangling: 
 - Gathering data
 - Assessing data
 - Cleaning data
2. Exploratory Data Analysis:
 - Defined business questions for data exploration
 - Create Data exploration
3. Data Visualization:
 - Create Data Visualization that answer business questions
4. Dashboard:
 - Set up the DataFrame which will be used
 - Make filter components on the dashboard
 - Complete the dashboard with various data visualizations

## Setup Virtual Environment
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install numpy pandas scipy matplotlib seaborn jupyter streamlit babel
```

## Run Streamlit
```
streamlit run dashboard.py
```
