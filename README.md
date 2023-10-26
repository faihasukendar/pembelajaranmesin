# Laporan Proyek Machine Learning
### Nama : Faiha Atsaa S
### Nim : 211351053
### Kelas : Malam B

## Domain Proyek

Memudahkan kita untuk mengestimasi harga rumah di boston berdasarkan 8 attribut tanpa harus benar benar mengunjungi lokasinya


## Business Understanding

Dengan adanya aplikasi ini, sangat memudahkan kita untuk melakukan estimasi harga rumah di boston berdasarkan attribut yang di tawarkan. Sehingga kita bisa menyiapkan dana yang sesuai dan hanya perlu sekali saja pergi ke boston keetika pindah tidak untuk bulak balik cek harga pasar.

Bagian laporan ini mencakup:

### Problem Statements

Seringkali ketika ingin membeli rumah di luar negri, alih alih sekali deal kita harus malah bulak balik mencari rumah yang cocok sehingga tabungan kita untuk membeli rumah malah habis terpakai untuk ongkos

### Goals

Dengan hadirnya aplikasi ini memudahkan kita mendapat estimasi harga rumah yang cocok dengan kita dan dapat menghemat biaya akomodasi kita sehingga hanya perlu sekali berangkat ke boston untuk proses transaksi dan pindahan.


   ### Solution statements
    - Karena model aplikasi ini berbentuk sebuah estimasi maka digunakanlah algoritma linear regresi untuk menemukan harga yang tepat

## Data Understanding
Data ini berdasarkan dataset dari kaggle tentang harga rumah di boston.<br> 

[Boston House Data](https://www.kaggle.com/datasets/fedesoriano/the-boston-houseprice-data).


### Variabel-variabel pada Boston House Price Dataset adalah sebagai berikut:
CRIM = Nilai tingkat kriminal daerah yang di inginkan pertahun nya (tipe data float)
ZN = Tingkat Kepadatan Penduduk per 25.000 sq.ft (tipe data float)
CHAS = Apakah daerah yang di inginkan dekat dengan sungai (tipe data int)
NOX = Tingkat Keasaman Tanah daeeah yang di inginkan (tipe data float)
RM = Jumlah Ruangan Hunian pada rumah yang di inginkan (tipe data int)
AGE = Usia Bangunannya (tipe data float)
DIS = sJarak dari pusat pekerjaan terdekat (tipe data float)
TAX = Keseluruhan pajak bangunan per $10,000 (tipe data float)

## Data Preparation
Seteleh menentukan dataset yang akan dibuatkan model Machine Learningnya selanjutnya kita ketikan library python yang ingin di gunakan
```bash
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
```
Setelah itu kita buka file datasetnya
```bash
df = pd.read_csv('the-boston-houseprice-data/boston.csv')
```
Kita cek apakah datanya sudah terbaca atau belum
```bash
df.head()
```
Kita bisa lihat informasi table nya dengan cara
```bash
df.info()
```
Maka akan muncul
```bash
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 506 entries, 0 to 505
Data columns (total 14 columns):
 #   Column   Non-Null Count  Dtype  
---  ------   --------------  -----  
 0   CRIM     506 non-null    float64
 1   ZN       506 non-null    float64
 2   INDUS    506 non-null    float64
 3   CHAS     506 non-null    int64  
 4   NOX      506 non-null    float64
 5   RM       506 non-null    float64
 6   AGE      506 non-null    float64
 7   DIS      506 non-null    float64
 8   RAD      506 non-null    int64  
 9   TAX      506 non-null    float64
 10  PTRATIO  506 non-null    float64
 11  B        506 non-null    float64
 12  LSTAT    506 non-null    float64
 13  MEDV     506 non-null    float64
dtypes: float64(12), int64(2)
memory usage: 55.5 KB
```
Terlihat lah setiap kolom dan tipe datanya<br>
Selanjutnya kita bisa visualisasikan data tersebut dalam bentuk heatmap
```bash
plt.figure(figsize=(10,8))
sns.heatmap(df.corr(), annot=True)
```
![alt text](https://github.com/faihasukendar/pembelajaranmesin/blob/main/heatmap.png)
Bisa dilihat bahwa data dari setiap kolomnya tervisualisai

Sebenarnya masih banyak cara untuk memvisualisasikan data pada proses EDA ini tapi mari kita lanjutkan ke proses modeling.

## Modeling
Pertama kita tentukan dulu fitur untuk X dan label untuk Y
```bash
features = ['CRIM','ZN','CHAS','NOX','RM','AGE','DIS','TAX']
x = df[features]
y = df['MEDV']
```
Jika sudah ditentukan maka bisa kita lanjutkan dengan melakukan data train dan test
```bash
x_train, X_test, y_train, y_test = train_test_split(x,y,random_state=70)
```
Jika sudah maka kita masukan algortima linear regresi dengan nilai X dan Y
```bash
lr = LinearRegression()
lr.fit(x_train,y_train)
pred = lr.predict(X_test)
```
Sampai tahap ini proses modeling sudah selesai dan bisa dilakukan pengetesan dengan cara
```bash
input_data = np.array([[0.00632, 18.0, 0, 0.538, 6.575, 65.2, 4.0900, 296.0]])

prediction = lr.predict(input_data)
print('Estimasi Harga Rumah :', prediction)
```
Maka akan muncul harga estimasinya


## Evaluation
Data ini di evaluasi melalui nilai akurasinya

![alt text](https://github.com/faihasukendar/pembelajaranmesin/blob/main/akurasi.png)


## Deployment
[The Boston House Price](https://faihautsml.streamlit.app/)<br>
![alt text](https://github.com/faihasukendar/pembelajaranmesin/blob/main/tampilan.png)
