# -*- coding: utf-8 -*-
"""Submission2_Rekomendasi.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wVumq1RfPWQU7LrZFwLybMIVDsSL_euB

## Data Understanding

### Import Libraries
"""

# Commented out IPython magic to ensure Python compatibility.
# Import library yang dibutuhkan
import warnings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from pathlib import Path

# %matplotlib inline
warnings.filterwarnings("ignore")
sns.set()

"""Selanjutnya memanggil dataset dengan format csv

#### Load Data
"""

# menyimpan masing-masing file ke dalam variabel dataframe
eco_place = 'https://raw.githubusercontent.com/rasyidperkim/dicoding-ml-terapan/main/dataset/eco_place.csv'
eco_rating = 'https://raw.githubusercontent.com/rasyidperkim/dicoding-ml-terapan/main/dataset/eco_rating.csv'

# menjadikan file csv sebagai dataframe
df_place = pd.read_csv(eco_place)
df_rating = pd.read_csv(eco_rating)

"""Dalam proyek Rekomendasi *Ecotourism* ini, kita memiliki 2 file terpisah mengenai tempat wisata dan rating dari user.

File eco_place.csv berisi data tentang berbagai tempat wisata alam dan rating. Setiap baris dalam dataset mewakili satu tempat wisata ekologis dengan detail sebagai berikut:

0. `place_id`: ID unik untuk setiap tempat.
1. `place_name`: Nama tempat wisata.
2. `place_description`: Deskripsi singkat tentang tempat wisata.
3. `category`: Kategori tempat wisata (misalnya, "Budaya,Taman Nasional", "Desa Wisata", dll.).
4. `city`: Kota atau Provinsi dari wisata tersebut berada.
5. `price`: Harga tiket masuk ke tempat wisata.
6. `rating`: Peringkat tempat wisata tersebut.
7. `description_location`: Deskripsi lokasi tempat wisata tersebut.
8. `place_img`: URL gambar tempat tersebut.
9. `gallery_photo_img1`, `gallery_photo_img2`, `gallery_photo_img3`: URL gambar lainnya dari tempat tersebut.
10. `place_map`: URL peta tempat tersebut.


File eco_rating.csv berisi data tentang rating dan user dengan detail sebagai berikut :
0. `user_id` : angka unik atau ID user yang memberikan rating
1. `place_id` : kode nama tempat wisata ekologis
2. `user_rating` : nilai rating yang diberikan user

### Data Overview

Berikut adalah sampel 5 data teratas dari dataframe df_place
"""

# menampilkan 5 data teratas untuk dataframe place
df_place.head()

# menampilkan 5 data teratas untuk dataframe rating
df_rating.head()

df_rating[df_rating['user_id'] == 47]

"""Selanjutnya dilakukan Exploratory Data Analysis.

## Exploratory Data Analysis (EDA)

Pada tahapan ini data akan melalui proses Exploratory Data Analysis (EDA). Bertujuan untuk mendapatkan insight data.

### 1.1 Proses EDA pada datafame Place

#### 1.1.1. Pengecekan tipe data pada setiap kolom.
"""

#Melihat informasi data mulai dari jumlah data, tipe data, memory yang digunakan dll.
df_place.info()

"""Dari informasi ini dapat diringkaskan :
1. Ada 182 data, dengan 1 fitur bertipe data float, 1 fitur bertipe data betipe integer, dan 11 data bertipe objek.
2. Dari tipe data sudah benar kecuali untuk fitur **price** harusnya memiliki tipe data integer. Hal ini karena berisi teks 'Rp' di depan angka dan kata 'Gratis' sehingga dibaca sebagai objek.
3. Variabel yang relevan dijadikan dalam sistem rekomendasi adalah **place_name** , **category**, dan **rating**
"""

#Mengubah tipe data price dari string menjadi integer
df_place['price'] = df_place['price'].replace('Gratis', '0').str.replace('Rp', '').str.replace(',', '').astype(int)

"""#### 1.1.2. Menampilkan informasi deskriptif pada setiap kolom numerik"""

# Deskripsikan data numerik
df_place.describe()

"""Dari informasi ini dapat diringkaskan :

**rating:**
1. Nilai rata-rata adalah 4.42, dengan nilai minimum 3.4 dan maksimum 5.
2. Nilai tengah (median) adalah 4.4, dan sebagian besar nilai berada di antara 4.3 dan 4.6 (kuartil pertama dan ketiga).
3. Standar deviasi sebesar 0.22 menunjukkan bahwa nilai rating cenderung berdekatan dengan rata-rata.

**price**:
1. Harga masuk objek wisata berbasis ekologis dari gratis hingga yang tertinggi mencapai Rp. 900.000, dengan rata-rata Rp. 28,060.44
2.  Nilai tengah (median) adalah Rp. 10.000, dan sebagian besar nilai berada di antara Rp. 5.000 dan Rp.20.000 (kuartil pertama dan ketiga).
3. Standar deviasi sebesar Rp. 84,926.87 menunjukkan bahwa terdapat variasi yang cukup besar dalam harga tiket masuk. Ada beberapa tempat dengan harga tiket masuk yang jauh lebih tinggi dari rata-rata, yang mungkin meningkatkan standar deviasi.

#### 1.1.3. Menampilkan jumlah data unik dari setiap kolom
"""

# Tampilkan jumlah data unik setiap kolom
print(df_place.nunique())

"""Dari informasi ini dapat diringkaskan :
1. Ada 20 kategori jenis *ecotourism* pada dataset ini
2. Ada 47 kota dari lokasi *ecotourism* pada dataset ini

#### 1.1.4. Analisis Univariat
"""

#Tampilkan detail data kategori
print('Jumlah kategori: \n')
print(df_place['category'].value_counts())

"""Untuk variabel `category`, terlebih dahulu harus dilakukan pemisahan kategori yang dituliskan bersama dalam satu baris menjadi kategori yang terpisah. Misalnya, baris dengan kategori "Budaya,Taman Nasional" akan dipisahkan menjadi dua baris: satu dengan kategori "Budaya" dan satu lagi dengan kategori "Taman Nasional". Hal ini akan memungkinkan penghitungan frekuensi yang lebih akurat untuk setiap kategori."""

category_freq = df_place['category'].str.split(',', expand=True).stack()

"""Setelah itu dapat dilakukan perhitungan frekuensi data kategori dan kota"""

#Tampilkan detail data kategori
print('Jumlah kategori: \n')
print(category_freq.value_counts())
print('--------------------------------------------------------')
print('Jumlah kota: \n')
print(df_place['city'].value_counts())

"""Dari output ini didapatkan informasi :
**Category**
1. Terdapat 6 kategori untuk ecotourism pada dataset ini.
2. Kategori "Cagar Alam" memiliki jumlah tempat wisata ekologis terbanyak (146 tempat), diikuti oleh "Budaya" (53 tempat), dan "Bahari" (34 tempat).
3. Kategori "Desa Wisata" memiliki jumlah tempat wisata ekologis paling sedikit (14 tempat) di antara semua kategori.

**City**
1. Yogyakarta memiliki jumlah tempat wisata ekologis terbanyak (53 tempat), diikuti oleh Bandung (36 tempat), dan Semarang (17 tempat).
2. Sejumlah kota hanya memiliki satu tempat wisata ekologis, seperti Jember, Pekanbaru, Wonosobo, Banten, dan lainnya.

#### 1.1.5 Analisis Multivariat

Pada tahap ini akan dilakukan visualisasi untuk menganalisa hubungan antara kota dengan rating, kota dengan harga, rating dengan harga, dan rating dengan kategori. Untuk kota dijadikan 5 kategori saja yaitu kota selain Yogyakarta, Bandung, Semarang, dan Jakarta diberi label 'Lainnya'
"""

# Gabung semua kota lainnya kecuali Yogyakarta, Bandung, Semarang, dan Jakarta
df_place['city_grouped'] = df_place['city'].where(df_place['city'].isin(['Yogyakarta', 'Bandung', 'Semarang', 'Jakarta']), 'Lainnya')

# Buat subplots
fig, ax = plt.subplots(2, 2, figsize=(15, 10))

# 1. hubungan antara kota dengan rating
sns.boxplot(x='city_grouped', y='rating', data=df_place, ax=ax[0, 0])
ax[0, 0].set_title('Relationship between City and Rating')

# 2. hubungan antara kota dengan harga
sns.boxplot(x='city_grouped', y='price', data=df_place, ax=ax[0, 1])
ax[0, 1].set_title('Relationship between City and Price')

# 3. hubungan antara rating dengan harga
sns.scatterplot(x='rating', y='price', data=df_place, ax=ax[1, 0])
ax[1, 0].set_title('Relationship between Rating and Price')

# 4.hubungan antara rating dengan kategori
df_place['category_split'] = df_place['category'].str.split(',', expand=True)[0]
sns.boxplot(x='category_split', y='rating', data=df_place, ax=ax[1, 1])
ax[1, 1].set_title('Relationship between Category and Rating')

# tampilkan plot
plt.tight_layout()
plt.show()

"""Dari visualisasi data, berikut beberapa insight yang didapatkan:

1. Hubungan antara Kota dan Rating:
* Yogyakarta, Bandung, Semarang, Jakarta, dan kota-kota lainnya memiliki variasi rating yang cukup mirip, dengan median rating sekitar 4.2 hingga 4.6.
* Sejumlah tempat wisata di Yogyakarta dan Bandung memiliki rating yang lebih rendah (sekitar 4), dan beberapa tempat di Bandung memiliki rating yang lebih tinggi (5).

2. Hubungan antara Kota dan Harga:

* Yogyakarta, Bandung, dan kota-kota lainnya memiliki variasi harga tiket masuk yang cukup mirip, dengan harga sebagian besar tempat wisata berada di bawah 50,000.
* Jakarta memiliki variasi harga yang lebih besar, dengan beberapa tempat wisata memiliki harga tiket masuk yang sangat tinggi (hingga 900,000).
* Beberapa tempat wisata di Semarang juga memiliki harga tiket masuk yang relatif tinggi (hingga sekitar 200,000).

3. Hubungan antara Rating dan Harga:

* Tidak ada pola yang jelas antara rating dan harga. Sebagian besar tempat wisata, baik yang memiliki rating tinggi maupun rendah, memiliki harga tiket masuk di bawah 200,000. Hanya ada beberapa tempat dengan harga yang sangat tinggi, dan rating mereka bervariasi.

4. Hubungan antara Kategori dan Rating:

* Tempat wisata dalam kategori "Budaya" dan "Cagar Alam" memiliki variasi rating yang cukup mirip, dengan median rating sekitar 4.4 hingga 4.5. Sejumlah tempat dalam kategori ini memiliki rating yang lebih rendah (sekitar 3.5), dan beberapa tempat memiliki rating yang lebih tinggi (5).
* Tempat wisata dalam kategori "Taman Nasional" cenderung memiliki rating yang lebih tinggi, dengan sebagian besar rating di atas 4.
* Tempat wisata dalam kategori "Desa Wisata" memiliki variasi rating yang lebih besar, dengan beberapa tempat memiliki rating yang lebih rendah (sekitar 3.9) dan beberapa tempat memiliki rating yang lebih tinggi (4.7).

### 1.2 Proses EDA pada datafame Rating

#### 1.2.1 Pengecekan tipe data pada setiap kolom.
"""

#Melihat informasi data mulai dari jumlah data, tipe data, memory yang digunakan dll.
df_rating.info()

"""Dari informasi ini dapat dilihat ada kesamaan kolom place_id pada dataframe place. Tipe data sudah sesuai semua sehingga tidak perlu ada yang kita konversi

#### 1.2.2 Menampilkan informasi deskriptif pada setiap kolom numerik
"""

df_rating.describe()

"""Berdasarkan output ini dapat dilihat informasi sebagai berikut :
1. data user_id berjumlah 849 sedangkan nilai maksimal pada data ini 156. Dengan demikian ada user_id yang memberikan rating pada lokasi yang berbeda-beda.
2. Terdapat kesamaan nama kolom place_id pada dataframe place. Hanya saja pada place_id dengan angka 1 pada dataframe place tidak ada pada data ini karena angka minimal adalah 2. Sebaliknya place_id dengan angka 183, tidak ada pada dataframe place.
3. Nilai rata-rata user_rating adalah 3.51, dengan nilai minimum 2 dan maksimum 5. Standar deviasi sebesar 0.95 menunjukkan bahwa terdapat variasi dalam peringkat yang diberikan oleh pengguna. Pada dataframe place, rating paling rendah adalah 3.4 dan tidak ada yang bernilai 2

#### 1.2.3 Analisis Univariat
"""

# menampilkan informasi seputar rating oleh user
print('Jumlah user yang memberi review: ', len(df_rating.user_id.unique()))
print('Jumlah tempat yang diberi review: ', len(df_rating.place_id.unique()))
print('Jumlah rating yang berbeda: ', len(df_rating.user_rating.unique()))
print('Rata-rata jumlah rating di suatu tempat:', df_rating['place_id'].value_counts().median())
print('Jumlah rating terbanyak di suatu tempat:', max(df_rating['place_id'].value_counts().values))
print('Jumlah rating terbanyak oleh 1 user:', max(df_rating['user_id'].value_counts().values))
print('Jumlah rating tersedikit oleh 1 user:', min(df_rating['user_id'].value_counts().values))
print('Rata-rata jumlah rating oleh 1 user:', df_rating['user_id'].value_counts().median())

"""### Data Preprocessing"""

# Menggabungkan data tempat dan rating pengguna
data = df_place.merge(df_rating, on='place_id', how='left')

"""## Data Preparation

#### Missing Value and Data Duplicate Treatment

Penanganan data null atau duplikat pada data place. Tahap ini bertujuan untuk membersihkan data sebelum menjadi model Content Based Filtering dan Collaborative Filtering, untuk mereduksi kesalahan rekomendasi
"""

# Periksa missing values pada dataframe
data.isnull().sum()

"""Pada `gallery_photo_img3` dan `gallery_photo_img2` banyak terdapat *missing values* yang berarti tidak semua data tempat memiliki foto lebih dari satu. Hanya saja kedua feature ini diabaikan karena tidak relevan sebagai bagian dari model. Sedangkan data null pada `user_id` harus dihapus. Proses ini bertujuan untuk mengantisipasi permasalahan karena tidak adanya data user yang memberi rating pada model Collaborative Filtering."""

# Hapus baris dengan data user_id null
data = data.dropna(subset=['user_id'])

# Periksa jika ada data duplikat pada dataframe
print(f'Jumlah Data Duplikat: {df_rating.duplicated().sum()}')

"""Dengan adanya 3 data duplikat pada df_rating, maka kita hapus data duplikasi tersebut"""

# hapus data duplikat
data.drop_duplicates(keep='first', inplace=True)

# Periksa data duplikat pada dataframe rating
print(f'Jumlah Data Duplikat: {data.duplicated().sum()}')

"""### Feature Engineering

Melakukan pemrosesan data yang diperlukan seperti menghapus kolom yang tidak diperlukan, dan mengubah format data jika diperlukan.
"""

# Hapus kolom yang tidak diperlukan
data = data.drop(['place_description', 'price', 'city', 'description_location', 'place_img', 	'gallery_photo_img1', 'gallery_photo_img2',	'gallery_photo_img3', 'place_map', 'city_grouped', 'category_split'], axis=1)

#Memeriksa informasi data hasil gabungan
data.info()

# Cetak jumlah unik pengguna dan ekowisata
num_users = data.user_id.nunique()
num_places = data.place_id.nunique()

print("Jumlah Pengguna:", num_users)
print("Jumlah Ekowisata:", num_places)

# Membuat dataframe baru 'eco_tour' dengan data yang sama seperti 'data'
eco_tour = data.copy()

# Menghapus data duplikat berdasarkan kolom 'place_id' dan menyimpan hasilnya di 'eco_tour'
eco_tour.drop_duplicates(subset='place_id', keep='first', inplace=True)

# Memeriksa hasil penghapusan duplikat
eco_tour

"""Standarisasi kolom `category`: Proses ini perlu dilakukan sebelum melakukan vektorisasi teks agar format setiap value pada `category` seragam. Proses yang dilakukan pada tahapan ini antara lain:
1. Menjadikan data pada `category` sebagai lowercase sebelum menggunakan vectorizer untuk menjaga konsistensi, normalisasi, dan reduksi dimensi dalam pemrosesan teks.
2. Mengubah tanda spasi pada `category` menjadi underscore agar menjadi sebuah kata yang terhubung. Tujuannya untuk menghindari terlalu banyak kategori berdasarkan jumlah kata yang dapat menyebabkan ambiguinitas.
"""

# mengubah format teks menjadi lowercase
eco_tour['category'] = eco_tour['category'].apply(lambda x: x.lower())

# mengubah spasi antar kata menjadi underscore
eco_tour['category'] = eco_tour['category'].str.replace(' ', '_')

# nilai dalam kolom category diubah menjadi array yang berisi string
eco_tour['category'] = eco_tour['category'].str.split(',').astype(str)

# nilai dalam kolom category diubah menjadi array yang berisi string
eco_tour['category'] = eco_tour['category'].apply(lambda x: eval(x))

# Convert the list of categories into a space-separated string
eco_tour['category'] = eco_tour['category'].apply(lambda x: ' '.join(x))

# mengecek perubahan
print(eco_tour['category'].value_counts())

"""Mengubah data ke dalam bentuk list pada kolom `place_id`, `place_name`, dan `category`. Bertujuan untuk pembuatan dataframe baru yang akan dijadikan sebagai data penerapan sistem rekomendasi."""

# Mengonversi data series menjadi bentuk list
place_id = eco_tour['place_id'].tolist()
place_name = eco_tour['place_name'].tolist()
place_category = eco_tour['category'].tolist()

"""#### Data Preparation for Content-Based Filtering

Tahap berikutnya, pembuatan dictionary untuk menentukan pasangan key-value pada data place_id, place_name, dan place_category yang telah disiapkan sebelumnya.
"""

# Membuat dictionary untuk list
data_new = pd.DataFrame({
    'id': place_id,
    'place_name': place_name,
    'category': place_category
})
data_new

"""#### **Data Preparation for Collaborative Filtering**"""

#menyalin dan membuat dataframe baru 'df'
df = data.copy()

# Mengubah user_id menjadi list tanpa nilai yang sama
user_ids = df['user_id'].unique().tolist()
print('list user id: ', user_ids)

# Melakukan encoding user_id
user_to_user_encoded = {x: i for i, x in enumerate(user_ids)}
print('encoded user id : ', user_to_user_encoded)

# Melakukan proses encoding angka ke ke user_id
user_encoded_to_user = {i: x for i, x in enumerate(user_ids)}
print('encoded angka ke user_id: ', user_encoded_to_user)

# Mengubah place_id menjadi list tanpa nilai yang sama
place_ids = df['place_id'].unique().tolist()

# Melakukan proses encoding place_id
place_to_place_encoded = {x: i for i, x in enumerate(place_ids)}

# Melakukan proses encoding angka ke place_id
place_encoded_to_place = {i: x for i, x in enumerate(place_ids)}

# Mapping user_id ke dataframe user
df['user'] = df['user_id'].map(user_to_user_encoded)

# Mapping place_id ke dataframe resto
df['place'] = df['place_id'].map(place_to_place_encoded)

# Mendapatkan jumlah user
num_users = len(user_to_user_encoded)
print(num_users)

# Mendapatkan jumlah tempat ekowisata
num_place = len(place_encoded_to_place)
print(num_place)

# Mengubah rating menjadi nilai float
df['rating'] = df['rating'].values.astype(np.float32)

# Nilai minimum rating
min_rating = min(df['rating'])

# Nilai maksimal rating
max_rating = max(df['rating'])

print('Number of User: {}, Number of place: {}, Min Rating: {}, Max Rating: {}'.format(
    num_users, num_place, min_rating, max_rating
))

"""Tahap persiapan telah selesai. Hal yang telah dilakukan :
* Memahami data rating yang dimiliki.
* Menyandikan (encode) fitur `user` dan `place_id` ke dalam indeks integer.
* Memetakan `user_id` dan `place_id` ke dataframe yang berkaitan.
* Mengecek beberapa hal dalam data.

Train-Test Data Split

Pada tahap ini, dataset dibagi menjadi dua bagian, yaitu data training (train) dan data testing. Tahap ini bertujuan untuk mempersiapkan data ratings yang akan digunakan dalam pelatihan dan pengujian model Collaborative Filtering. Pembagian dataset dengan komposisi 70:30. 70 % untuk data train dan 30 % untuk data test. Untuk pertama data diacak terlebih dahulu agar random
"""

# Mengacak dataset
df = df.sample(frac=1, random_state=42)

# Membuat variabel x untuk mencocokkan data user dan tempat ekowisata menjadi satu value
x = df[['user', 'place']].values

# Membuat variabel y untuk membuat rating dari hasil
y = df['rating'].apply(lambda x: (x - min_rating) / (max_rating - min_rating)).values

# Membagi menjadi 70% data train dan 30% data validasi
train_indices = int(0.7 * df.shape[0])
x_train, x_val, y_train, y_val = (
    x[:train_indices],
    x[train_indices:],
    y[:train_indices],
    y[train_indices:]
)

"""## Modeling and Result

### 1. Content Based Filtering

#### TF-IDF Vectorizer
"""

from sklearn.feature_extraction.text import TfidfVectorizer

# Membuat objek TfidfVectorizer
tf = TfidfVectorizer()

# Melakukan perhitungan idf pada data category
tfidf_matrix = tf.fit_transform(data_new['category'])

# Mapping array dari fitur index integer ke fitur nama
tf_feat = tf.get_feature_names_out()

tf_feat

# Membuat dataframe untuk melihat tf-idf matrix
df_tfidf = pd.DataFrame(tfidf_matrix.todense(), columns=tf_feat, index=data_new.place_name)

# Mengambil sampel 6 kolom secara acak dan 10 baris secara acak
sample_df = df_tfidf.sample(n=10, axis=0).sample(n=6, axis=0)

# Menampilkan hasil
sample_df.head()

"""#### **Cosine Similarity**"""

# Menghitung cosine similarity pada matrix tf-idf
cosine_sim = cosine_similarity(tfidf_matrix)

# Membuat dataframe dari variabel cosine_sim dengan baris dan kolom berupa nama ekowisata
cosine_sim_df = pd.DataFrame(cosine_sim, index=data_new['place_name'], columns=data_new['place_name'])

# Melihat similarity matrix pada setiap ekowisata
cosine_sim_df.sample(5, axis=1).sample(10, axis=0)

"""Vektor TF-IDF telah dihitung untuk setiap ekowisata. Dalam kasus ini, kita mendapatkan matriks dengan 181 baris (satu untuk setiap ekowisata) dan 6 kolom (satu untuk setiap kategori).

Sekarang dilakukan pembuatan fungsi yang dapat memberikan rekomendasi ekowisata berdasarkan kesamaan kategori. Untuk itu diperlukan pembuatan dua pemetaan: satu untuk memetakan nama ekowisata ke indeksnya, dan satu lagi untuk memetakan indeks ke kategori.
"""

# Buat mapping dari nama ekowisata ke index
indices = pd.Series(data_new.index, index=data_new['place_name']).drop_duplicates()

# Fungsi yang menerima nama ekowisata untuk input dan menghasilkan ekowisata yang paling mirip sebagai output
def get_recommendations(place_name, similarity_data=cosine_sim_df, items=data_new[['place_name', 'category']], k=5):
    if place_name not in data_new['place_name'].values:
        return "Maaf data belum ada di database..."
    # Ambil index yang cocok dengan nama ekowisata
    idx = indices[place_name]

    # Mengambil data dengan menggunakan argpartition untuk melakukan partisi secara tidak langsung sepanjang sumbu yang diberikan
    # Dataframe diubah menjadi numpy
    # Range(start, stop, step)
    index = similarity_data.loc[:,place_name].to_numpy().argpartition(
        range(-1, -k, -1))

    # Mengambil data dengan similarity terbesar dari index yang ada
    closest = similarity_data.columns[index[-1:-(k+2):-1]]

    # Drop place_name agar ekowisata yang dicari tidak muncul dalam daftar rekomendasi
    closest = closest.drop(place_name, errors='ignore')

    return pd.DataFrame(closest).merge(items).head(k)

data_new[data_new.place_name.isin(['Taman Nasional Bali Barat', 'Danau Toba', 'Desa Wisata Munduk'])]

"""Percobaan fungsi ini dengan memasukkan sebuah nama ekowisata sebagai input."""

# Uji coba rekomendasi 1
get_recommendations('Taman Nasional Bali Barat')

# Uji coba rekomendasi 2
get_recommendations('Danau Toba')

# Uji coba rekomendasi 3
get_recommendations('Desa Wisata Munduk')

# Uji coba rekomendasi 4 dengan data yang belum ada di dataframe
get_recommendations('Pulau Kembang')

"""#### **Jaccard Similarity**"""

# Fungsi untuk menghitung Jaccard similarity antara 2 setlis
def jaccard_similarity(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection = len(set1.intersection(set2))
    union = len(set1) + len(set2) - intersection
    return intersection / union if union != 0 else 0


# Pengujian Fungsi
jaccard_similarity(['desa_wisata'], ['budaya', 'desa_wisata'])

"""Fungsi kesamaan Jaccard telah berhasil dibuat dan diuji. Ia mengembalikan skor 0,5 untuk dua list ['desa_wisata'] dan ['budaya', 'desa_wisata'], yang sesuai dengan ekspektasi. Langkah selanjutnya adalah untuk menerapkan fungsi ini ke data untuk membuat sistem rekomendasi."""

# Fungsi yang menerima nama ekowisata untuk input dan menghasilkan ekowisata yang paling mirip sebagai output
def recommend_places(place_name, data_new, top_n=5):
    if place_name not in data_new['place_name'].values:
        return "Maaf data belum ada di database..."

    place_categories = data_new[data_new['place_name'] == place_name]['category'].values[0]
    data_new['similarity_score'] = data_new['category'].apply(lambda x: jaccard_similarity(x, place_categories))

    # Pengecualian hasil output dengan input
    data_new = data_new[data_new['place_name'] != place_name]

    # Urutkan skor similarity score dan menampilkan top-n
    recommendations = data_new.sort_values(by='similarity_score', ascending=False).head(top_n)

    return recommendations[['place_name', 'category', 'similarity_score']]

# Uji coba rekomendasi 1
recommend_places('Taman Nasional Bali Barat', data_new)

# Uji coba rekomendasi 2
recommend_places('Danau Toba', data_new)

# Uji coba rekomendasi 3
recommend_places('Desa Wisata Munduk', data_new)

"""### 2. Collaborative Filtering"""

class RecommenderNet(tf.keras.Model):

  # Inisialisasi fungsi
  def __init__(self, num_users, num_place, embedding_size, **kwargs):
    super(RecommenderNet, self).__init__(**kwargs)
    self.num_users = num_users
    self.num_place = num_place
    self.embedding_size = embedding_size
    self.user_embedding = layers.Embedding( # layer embedding user
        num_users,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = keras.regularizers.l2(1e-6)
    )
    self.user_bias = layers.Embedding(num_users, 1) # layer embedding user bias
    self.place_embedding = layers.Embedding( # layer embeddings place
        num_place,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = keras.regularizers.l2(1e-6)
    )
    self.place_bias = layers.Embedding(num_place, 1) # layer embedding place bias

  def call(self, inputs):
    user_vector = self.user_embedding(inputs[:,0]) # memanggil layer embedding 1
    user_bias = self.user_bias(inputs[:, 0]) # memanggil layer embedding 2
    place_vector = self.place_embedding(inputs[:, 1]) # memanggil layer embedding 3
    place_bias = self.place_bias(inputs[:, 1]) # memanggil layer embedding 4

    dot_user_place = tf.tensordot(user_vector, place_vector, 2)

    x = dot_user_place + user_bias + place_bias

    return tf.nn.sigmoid(x) # activation sigmoid

model = RecommenderNet(num_users, num_place, 50) # inisialisasi model

# model compile
model.compile(
    loss = tf.keras.losses.BinaryCrossentropy(),
    optimizer = keras.optimizers.Adam(learning_rate=0.001),
    metrics=[tf.keras.metrics.MeanAbsoluteError(), tf.keras.metrics.RootMeanSquaredError()])

# Memulai training

history = model.fit(
    x = x_train,
    y = y_train,
    batch_size = 8,
    epochs = 100,
    validation_data = (x_val, y_val)
)

plt.plot(history.history['mean_absolute_error'])
plt.plot(history.history['val_mean_absolute_error'])
plt.title('Mean Absolute Error')
plt.ylabel('MAE')
plt.xlabel('EPOCH')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

plt.plot(history.history['root_mean_squared_error'])
plt.plot(history.history['val_root_mean_squared_error'])
plt.title('model_metrics')
plt.ylabel('root_mean_squared_error')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

"""Perhatikanlah, proses training model cukup smooth dan model konvergen pada epochs sekitar 100. Dari proses ini, kita memperoleh nilai error akhir sebesar sekitar 0.04 dan error pada data validasi sebesar 0.14. Nilai tersebut cukup bagus untuk sistem rekomendasi."""

place_df = data
df_test = df_rating.copy()

# Mengambil sample user
user_id = df_test.user_id.sample(1).iloc[0]
place_visited_by_user = df_test[df_test.user_id == user_id]

# Operator bitwise (~) untuk tempat yang diasumsikan belum dikunjungi
place_not_visited = data[~data['user_id'].isin(place_visited_by_user.place_id.values)]['user_id']
place_not_visited = list(
    set(place_not_visited)
    .intersection(set(place_to_place_encoded.keys()))
)

place_not_visited = [[place_to_place_encoded.get(x)] for x in place_not_visited]
user_encoder = user_to_user_encoded.get(user_id)
user_place_array = np.hstack(
    ([[user_encoder]] * len(place_not_visited), place_not_visited)
)

ratings = model.predict(user_place_array).flatten()

top_ratings_indices = ratings.argsort()[-1:][::-1]
recommended_place_ids = [
    place_encoded_to_place.get(place_not_visited[x][0]) for x in top_ratings_indices
]

print('Rekomendasi Untuk Pengguna dengan ID: {}'.format(user_id))
print('===' * 15)
print('Tempat Ekowisata dengan rating tertinggi dari Pengguna')
print('----' * 14)

top_place_user = (
    place_visited_by_user.sort_values(
        by = 'user_rating',
        ascending=False
    )
    .head(5)
    .place_id.values
)

place_df_rows = place_df[place_df['user_id'].isin(top_place_user)]
for row in place_df_rows.itertuples():
    print(row.place_name, ':', row.category)

print('----' * 15)
print('Top 5 Rekomendasi Tempat Ekowisata')
print('----' * 15)

recommended_place = place_df[place_df['user_id'].isin(recommended_place_ids)]
for row in recommended_place.itertuples():
    print(row.place_name, ':', row.category)

"""### Evaluation

Pada sistem rekomendasi *content-based filtering* (CBF), kita dapat melihat dari 3 kali percobaan dan dari 2 teknik, model sudah dapat merekomendasikan kategori dengan kesamaan yang benar. Perbandingan selanjutnya adalah lama eksekusi dalam satuan detik
"""

import time

# Mulai menghitung waktu untuk get_recommendations
start_time = time.time()
get_recommendations('Desa Wisata Munduk')
cosine_time = time.time() - start_time

# Mulai menghitung waktu untuk recommend_places
start_time = time.time()
recommend_places('Desa Wisata Munduk', data_new)
jaccard_time = time.time() - start_time


# Data untuk dataframe
data_eval = {
    'Method': ['Cosine Similarity', 'Jaccard Similarity'],
    'Time (seconds)': [cosine_time, jaccard_time]
}

# Membuat dataframe
df_evaluate = pd.DataFrame(data_eval)

df_evaluate

"""Pada sistem rekomendasi *Collaborative filtering* (CF) kita mendapatkan MAE sebesar 0.0306 pada data training dan 0.1254 pada data validasi, serta RMSE seebsar 0.0405 pada data training dan 0.1331 pada data uji. Hasil ini sudah cukup baik untuk sistem rekomendasi dan ketika diujicoba sudah memberikan rekomendasi dengan kesamaan preferensi pengguna sebelumnya

## Conclusion

Berdasarkan hasil yang didapatkan, maka dapat disimpulkan sebagai berikut:

* Metode *Content-based Filtering* dapat digunakan untuk membuat sistem rekomendasi tempat ekowisata. Pada pendekatan menggunakan cosine similarity dan jaccard similarity, model sudah dapat merekomendasikan tempat ekowisata berdasarkan kesamaan atau kemiripan kategori dengan benar

* Metode *Collaborative Filtering* dapat digunakan untuk membuat sistem rekomendasi tempat ekowisata yang belum pernah dikunjungi dan mungkin disukai oleh pengguna  berdasarkan preferensi pemberian rating tempat wisata di masa lalu oleh pengguna. Berdasarkan pendekatan yang dilakukan menggunakan RecommenderNet menunjukkan bahwa metode tersebut memiliki nilai *Mean Absolute Error* (MAE) yang relatif rendah pada data training sebesar 0.03 dan data validasi sebesar 0.12. Pada nilai *Root Mean Square Error* (RMSE) juga memiliki nilai relatif rendah yaitu data training sebesar 0.04 dan data validasi sebesar 0.13, sehingga dapat dikatakan model ini dalam merekemondasikan sudah cukup bagus.

Harapan ke depan model ini dapat digunakan dan diterapkan pada organisasi atau perusahaan berdasarkan demografi personal sehingga lebih mendekati personalisasi dan pengalaman pengguna yang baik. Selain itu model ini dapat dikembangkan lebih jauh menggunakan teknik *Hybrid Recommender System*.
"""