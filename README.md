# Bike Rental - Submissions Dashboard ✨

Ini adalah submission pada course "Belajar Analisis Data dengan Python". Untuk menyelesaikan course ini peserta diminta untuk menganalisa data dan membuat sebuah dashboard dari dataset Bike Sharing. Dashboard tersebut bisa diakses [disini](https://bike-sharing-rentals-t9vx6fhdqb79nnzawm4ya4.streamlit.app/) 

## 1. Struktur File
submission
```
├───dashboard
|   ├───capture1.JPG
|   ├───capture2.JPG
|   ├───capture3.JPG
|   ├───capture4.JPG
|   ├───capture5.JPG
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

## 3. Screanshot
![alt text](https://github.com/fajarkrna/bike-sharing-rentals/blob/95e64d649809639cf7a4c06c9162057d029b9348/dashboard/Capture1.JPG)
![alt text](https://github.com/fajarkrna/bike-sharing-rentals/blob/95e64d649809639cf7a4c06c9162057d029b9348/dashboard/Capture2.JPG)
![alt text](https://github.com/fajarkrna/bike-sharing-rentals/blob/95e64d649809639cf7a4c06c9162057d029b9348/dashboard/Capture3.JPG)
![alt text](https://github.com/fajarkrna/bike-sharing-rentals/blob/95e64d649809639cf7a4c06c9162057d029b9348/dashboard/Capture4.JPG)
![alt text](https://github.com/fajarkrna/bike-sharing-rentals/blob/95e64d649809639cf7a4c06c9162057d029b9348/dashboard/Capture5.JPG)

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
