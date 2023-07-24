# Laporan Proyek Machine Learning - M. Rasyid Ridha



## 1. Project Overview

Ekowisata adalah kegiatan wisata alam di daerah yang bertanggungjawab dengan memperhatikan unsur pendidikan, pemahaman, dan dukungan terhadap usaha-usaha konservasi sumber daya alam, serta peningkatan pendapatan masyarakat lokal [1]. Ekowisata  memiliki berbagai karakteristik tertentu termasuk preferensi wisatawan dalam memilih destinasi wisata. Pemilihan destinasi ekowisata adalah tantangan layanan dalam transaksi online. Hanya sedikit wisatawan yang memiliki informasi yang diperlukan untuk sumber daya lokal tertentu [[2]](https://doi.org/10.46799/jss.v3i3.333). Sistem rekomendasi adalah solusi bagi wisatawan untuk mendapatkan saran tentang destinasi ekowisata yang tepat sesuai dengan preferensi mereka. Sistem rekomendasi pariwisata personalisasi menganalisis tempat yang dikunjungi pengguna dan merekomendasikan tempat yang belum dikunjungi [3]. 

Berdasarkan penelitian sebelumnya oleh Prasetyo, Atina, dan Purwanto (2021), bahwa sistem rekomendasi pariwisata dengan metode *Content Based Recommendation* berbasis *website* dapat memberikan rekomendasi wisata budaya yang tepat berdasarkan atribut yang diinputkan oleh *user* [4] . Oleh karena itu, sistem rekomendasi pada ekowisata ini menjadi sangat menarik untuk terus dikembangkan. Proyek ini penting karena memiliki banyak manfaat. Para wisatawan dapat memanfaatkan rekomendasi ini untuk merencanakan pengalaman ekowisata yang lebih dipersonalisasi. Para pebisnis dapat menggunakan rekomendasi ini untuk meningkatkan penawaran mereka yang sejalan dengan prinsip-prinsip ekowisata. Sedangkan bagi pemerintah, rekomendasi ini dapat mendukung promosi ekowisata dengan praktik pariwisata berkelanjutan di Indonesia.

## 2. Business Understanding

Era digital membawa tantangan bagi wisatawan dalam menyaring dan memilih destinasi wisata dari berbagai informasi yang tersedia. Tantangan utama adalah penyajian informasi ini kepada pengguna secara efektif dan efisien untuk perencanaan perjalanan wisata yang lebih baik.

Wisatawan memerlukan sistem rekomendasi yang memahami preferensi pengguna dan menyajikan rekomendasi destinasi ekowisata yang paling sesuai dengan preferensi mereka. Namun yang perlu dipahami dan diklarifikasi yaitu pemahaman tentang cara kerja sistem rekomendasi dan preferensi pengguna harus berdasarkan dari data yang dimiliki, yaitu data tentang destinasi ekowisata dan penilaian yang diberikan oleh pengguna. 

### 2.1 Problem Statements

Berdasarkan latar belakang yang telah diuraikan sebelumnya,  pernyataan  masalah dari proyek ini adalah sebagai berikut:

- Bagaimana membuat sistem rekomendasi ekowisata berdasarkan kesamaan karakteristik *item*  ?

- Berdasarkan data rating  yang telah diberikan pengguna, bagaimana sistem merekomendasikan destinasi ekowisata yang  mungkin disukai oleh pengguna dan belum pernah dikunjungi pengguna tersebut ?

### 2.2 Goals

Berdasarkan pernyataan masalah, tujuan yang hendak dicapai dari proyek ini adalah sebagai berikut :

1. Menghasilkan sistem rekomendasi ekowisata berdasarkan kesamaan karakteristik *item*.
2. Menghasilkan sistem rekomendasi ekowisata berdasarkan kemiripan penilaian pengguna terhadap tempat-tempat yang sudah pernah dikunjungi sebelumnya.

### 2.3 Solution statements
Adapun solusi yang diajukan untuk menyelesaikan permasalahan tersebut adalah sebagai berikut.

1. Membuat sistem rekomendasi dengan pendekatan ***Content-based Filtering*** berdasarkan kategori ekowisata. Teknik *Content-based Filtering* adalah sebuah teknik untuk merekomendasikan *item* lain yang memiliki karakteristik serupa. Sebagai contoh dalam konteks ini, jika pengguna mencari atau menyukai ekowisata dengan kategori desa wisata, maka destinasi yang akan direkomendasikan adalah destinasi ekowisata lainnya dengan kategori desa wisata. Pada model ini digunakan metode ***Cosine Similarity*** dan ***Jaccard Similarity***.

2. Membuat sistem rekomendasi dengan pendekatan ***Collaborative Filtering*** berdasarkan *rating* dari pengguna. *Collaborative Filtering* adalah metode dalam sistem rekomendasi yang menggunakan informasi dari pengguna lain untuk memberikan rekomendasi kepada pengguna. Sebagai contoh dalam konteks ini, pengguna A menyukai ekowisata dengan kategori X, Y, dan Z, sedangkan pengguna B menyukai kategori X dan Y, maka sistem akan merekomendasikan kategori Z kepada pengguna B, karena kedua pengguna memiliki preferensi yang sama terhadap kategori lainnya yang sudah mereka nilai, sehingga diasumsikan pengguna B juga akan menyukai apa yang disukai oleh pengguna A. Pada model ini digunakan metode *deep learning* dengan ***RecommenderNet.***

   

## 3. Data Understanding
Kumpulan data yang digunakan pada proyek ini bersumber dari Kaggle pada tautan berikut ini [Indonesia's Ecotourism](https://www.kaggle.com/datasets/farazbeniqnomf/indonesiaecotourism). Menurut penjelasan sumber, kumpulan data ini digunakan dalam Proyek *Capstone* "Travelee" sebuah aplikasi yang menyediakan rekomendasi personal untuk destinasi wisata dan salah satunya menyediakan informasi ekowisata. Dalam *Indonesia's Ecotourism* dataset ini terdapat 2 *file* terpisah mengenai tempat wisata dan rating dari user, yaitu `eco_place.csv` dan `eco_rating.csv`. Berikut informasi mengenai jumlah kolom dan data pada setiap *file* dapat dilihat pada Tabel 1.

​							Tabel 1. Jumlah kolom dan data pada masing-masing *file*.

| No.  | Nama File      | Jumlah Kolom | Jumlah Data |
| ---- | -------------- | ------------ | ----------- |
| 1.   | eco_place.csv  | 11           | 182         |
| 2.   | eco_rating.csv | 3            | 849         |

*File* `eco_place.csv` berisi data tentang destinasi ekowisata dan rating. Setiap baris dalam dataset mewakili satu tempat ekowisata. Variabel-variabel pada `eco_place.csv` adalah sebagai berikut:  

1. `place_id`: kode unik untuk setiap tempat ekowisata.

2. `place_name`: Nama tempat ekowisata.

3. `place_description`: Deskripsi singkat tentang tempat ekowisata.

4. `category`: Kategori tempat ekowisata (misalnya, "Budaya","Taman Nasional", "Desa Wisata", dll.).

5. `city`: Kota atau provinsi dari ekowisata tersebut berada.

6. `price`: Harga tiket masuk ke tempat ekowisata.

7. `rating`: skor penilaian tempat ekowisata tersebut.

8. `description_location`: Deskripsi lokasi tempat ekowisata tersebut.

9. `place_img`: URL gambar tempat tersebut.

10. `gallery_photo_img1`, `gallery_photo_img2`, `gallery_photo_img3`: URL gambar lainnya dari tempat tersebut.

11. `place_map`: URL peta tempat tersebut.


Adapun *file* `eco_rating.csv` berisi data tentang *rating* dan pengguna. Variabel-variabel pada `eco_rating.csv` adalah sebagai berikut : 

1. `user_id` : angka unik atau ID pengguna yang memberikan *rating*
2. `place_id` : kode nama tempat ekowisata
3. `user_rating` : nilai *rating* yang diberikan user

Pada tahap ini dilakukan analisis data eksploratif untuk memahami karakteristik item melalui pengecekan data, informasi deskriptif, identifikasi jumlah data unik, dan visualisasi data. Informasi yang didapat antara lain :

1. Variabel yang perlu diperhatikan dalam sistem rekomendasi adalah **place_name** , **category**, dan **rating**.
2. Ada 6 kategori ekowisata dari 47 kota/provinsi yang berbeda pada kumpulan data ini.
3. Jika dihitung tiga urutan terbesar, kategori "Cagar Alam" merupakan jenis ekowisata terbanyak (146 tempat), diikuti oleh "Budaya" (53 tempat), dan "Bahari" (34 tempat). Yogyakarta memiliki jumlah destinasi ekowisata terbanyak (53 tempat), diikuti oleh Bandung (36 tempat), dan Semarang (17 tempat).
4. Jumlah user yang memberi review sebanyak 156 orang yang berbeda.  Jumlah tempat yang diberi review adalah 182 lokasi. Rata-rata jumlah *rating* dalam satu tempat yang diberikan pengguna adalah 5 kali dengan jumlah *rating* terbanyak di suatu tempat bisa mencapai 10 kali. Dalam data ini, satu orang pengguna memberikan *rating* paling sedikit di 4 lokasi.

Hubungan antara variabel dengan sebagian variabel yang lain dapat dilihat pada Gambar 1 berikut :

![multivariat](https://github.com/rasyidperkim/dicoding-ml-terapan/assets/63061466/2a02d769-cb51-40dc-b5f5-b42ab27e767d)

​										Gambar 1. *Hubungan antara variabel*

Dari Gambar 1, beberapa *insight* yang didapatkan antara lain :

1. Yogyakarta, Bandung, Semarang, Jakarta, dan kota-kota lainnya memiliki variasi *rating* yang cukup mirip, dengan rata-rata *rating* sekitar 4.2 hingga 4.6. Sejumlah tempat wisata di Yogyakarta dan Bandung memiliki *rating* yang lebih rendah (sekitar 4.0), dan beberapa tempat di Yogyakarta dan Bandung memiliki *rating* yang lebih tinggi (5).
2. Yogyakarta, Bandung, dan kota-kota lainnya memiliki variasi harga tiket masuk yang cukup mirip, dengan harga sebagian besar tempat wisata berada di bawah 50.000. Jakarta memiliki variasi harga yang lebih besar, dengan beberapa tempat wisata memiliki harga tiket masuk yang sangat tinggi (hingga 900.000).
3. Tidak ada pola yang jelas antara *rating* dan harga. Tempat dengan harga tiket yang tinggi bahkan memiliki *rating* yang cenderung tinggi sedangkan tempat dengan harga tiket masuk tanpa biaya, ada yang memiliki *rating* yang rendah.
4. Tempat wisata dalam kategori "Taman Nasional" cenderung memiliki *rating* yang lebih tinggi, dengan sebagian besar *rating* di atas 4.  Sejumlah tempat dalam kategori "Cagar Alam" dan "Budaya" memiliki variasi *rating* yang cukup mirip, sejumlah tempat memiliki *rating* yang lebih rendah (sekitar 3.5), dan beberapa tempat memiliki *rating* yang lebih tinggi (5).

Berdasarkan pemahaman data yang telah dilakukan, maka kesamaan karakteristik *item* yang dipilih dalam proyek ini dalam memberikan rekomendasi adalah berdasarkan kesamaan kategori ekowisata.

## 4. Data Preparation
Proyek ini menggunakan dua *dataframe* yang berbeda sehingga dalam *data preprocessing* , kedua *dataframe* ini perlu digabungkan. Penggabungan berdasarkan kesamaan fitur yaitu `place_id` dengan fungsi *merge.* Setelah itu penyiapan data yang dilakukan pada proyek ini dapat dijabarkan sebagai berikut:

#### Missing Value and Data Duplicate Treatment

Penanganan *missing value* atau nilai yang hilang dan penanganan data duplikat perlu dilakukan sebelum membuat model. *Missing value* dan data duplikat dapat mempengaruhi kualitas data. Data yang berkualitas baik adalah kunci untuk mendapatkan model yang baik.

Setelah diidentifikasi pada *dataset* yang digunakan dalam proyek ini, fitur `gallery_photo_img3` dan `gallery_photo_img2` banyak terdapat nilai yang hilang. Ini menunjukkan tidak semua data tempat memiliki foto lebih dari satu. Hanya saja kedua fitur ini diabaikan karena tidak relevan sebagai bagian dari model. Sedangkan nilai yang kosong pada `user_id` harus dihapus. Proses ini bertujuan untuk mengantisipasi permasalahan karena tidak adanya data pengguna yang memberi penilaian pada model *Collaborative Filtering.* Selain itu juga ditemukan tiga data duplikat pada *dataframe* *rating* , yang penanganannya cukup dengan dihapus.

#### Feature Engineering

Tahapan ini penting dilakukan karena dengan memilih fitur yang relevan dapat mengurangi jumlah fitur yang perlu dipelajari oleh model, sehingga model menjadi lebih sederhana dan lebih mudah untuk diinterpretasi. Proses yang dilakukan dalam tahap ini yaitu menghapus kolom yang tidak diperlukan karena tidak relevan kemudian dilakukan verifikasi apakah proses ini berhasil. Fitur terpilih dan tipe data hasil proses dapat dilihat pada tabel 2 berikut.

​								Tabel 2 Informasi *Dataframe*  Setelah Pemilihan Fitur yang Relevan

| No   | Column      | Non-Null Count | Dtype   |
| ---- | ----------- | -------------- | ------- |
| 0    | place_id    | 843 non null   | int64   |
| 1    | place_name  | 843 non null   | object  |
| 2    | category    | 843 non null   | object  |
| 3    | rating      | 843 non null   | float64 |
| 4    | user_id     | 843 non null   | float64 |
| 5    | user_rating | 843 non null   | float64 |

Berdasarkan Tabel 2 dapat diketahui bahwa fitur yang awalnya berjumlah 13, kini menjadi 6. Sudah tidak ada lagi *missing value* pada dataframe ini. Tipe data masing-masing fitur sudah tepat. Jumlah data saat ini ada 843 baris karena hasil penggabungan dengan dataframe dari  `eco_rating.csv` yang mana terdapat data pengguna yang sama memberikan penilaian pada lokasi yang berbeda. Untuk membuat model hanya merekomendasikan tempat yang berbeda perlu dilakukan identifikasi jumlah ekowisata yang unik berdasarkan `place_id`, dan diketahui ada sebanyak 181 data ekowisata yang berbeda sehingga `place_id `yang sama perlu dihapus.

Langkah selanjutnya adalah standarisasi data pada fitur `category`. Proses ini perlu dilakukan sebelum melakukan vektorisasi teks agar format setiap value pada `category` seragam. Proses yang dilakukan pada langkah ini antara lain:

1. Menjadikan data pada `category` sebagai *lowercase* sebelum menggunakan vectorizer untuk menjaga konsistensi, normalisasi, dan reduksi dimensi dalam pemrosesan teks.
2. Mengubah tanda spasi pada `category` menjadi underscore agar menjadi sebuah kata yang terhubung. Tujuannya untuk menghindari terlalu banyak kategori berdasarkan jumlah kata yang dapat menyebabkan ambiguitas.

Langkah terakhir dalam tahap ini adalah mengonversi *data series* menjadi bentuk *list* pada kolom `place_id`, `place_name`, dan `category`. Hal ini diperlukan untuk pembuatan *dataframe* baru yang akan dilakukan penerapan sistem rekomendasi. Alasan utama untuk melakukan ini adalah karena model rekomendasi biasanya bekerja dengan set data yang berisi daftar item yang telah berinteraksi dengan pengguna, bukan dengan *data series*.

Setelah tahapan ini, penyiapan data dilakukan terpisah untuk model yang menggunakan *Content-based Filtering* dan untuk model yang menggunakan *Collaborative Filtering.*

### 4.1 Data Preparation for Content-Based Filtering

Tahapan dalam penyiapan data untuk model dengan *Content-based Filtering* adalah pembuatan *dictionary* untuk menentukan pasangan *key-value* pada `place_id`, `place_name`, dan `place_category` yang telah disiapkan sebelumnya.  *Dictionary* dapat merepresentasikan data dalam format yang mudah dipahami dan diolah oleh model. Setiap *item* dapat diwakili sebagai vektor fitur, di mana setiap fitur adalah pasangan *key-value* dalam *dictionary*. *Key* mewakili fitur tertentu (misalnya kategori), dan *value* atau nilai mewakili bobot atau pentingnya fitur tersebut untuk *item*. Tabel 3 berikut merepresentasikan data yang telah diolah fiturnya, nama kolom menunjukkan *key* dan baris data menunjukkan *value.*

​													Tabel 3. *Dictionary* Data Untuk Model

|   no |   id |                place_name |                  category |
| ---: | ---: | ------------------------: | ------------------------: |
|    0 |    2 |        Desa Wisata Munduk |               desa_wisata |
|    1 |    3 |   Desa Wisata Penglipuran |        budaya desa_wisata |
|    2 |    4 | Taman Nasional Bali Barat | taman_nasional cagar_alam |
|    3 |    5 |               Bukit Jamur |                cagar_alam |
|    4 |    6 |                Bukit Moko |                cagar_alam |
|  ... |  ... |                       ... |                       ... |
|  176 |  178 |      Studio Alam Gamplong |             taman_hiburan |
|  177 |  179 |               Watu Goyang |         budaya cagar_alam |
|  178 |  180 |              Watu Lumbung |                cagar_alam |
|  179 |  181 |      Wisata Alam Kalibiru |         budaya cagar_alam |
|  180 |  182 |          Wisata Kaliurang |                cagar_alam |

Berdasarkan informasi yang dapat dilihat pada Tabel 3, telah ada  3 *key* dan 181 *value*. Pada nilai `category`, daftar data dipisahkan oleh tanda spasi. Data telah siap untuk dijadikan model dengan *Content-based Filtering*.

### 4.2 Data Preparation for Collaborative Filtering

Tahapan dalam penyiapan data untuk model dengan *Collaborative  Filtering* adalah mengubah `user_id` dan `place_id` menjadi *list* tanpa nilai yang sama kemudian dilakukan penyandian atau ***encoding*** pada *list* tersebut. Selanjutnya dilakukan penyandian dan pemasangan indeks integer pada masing-masing *list* . *Collaborative Filtering* biasanya bekerja dengan matriks yang *sparse* (banyak nilai nol) yang mewakili peringkat atau interaksi pengguna *item*. *Encoding* membantu penanganan matriks ini dengan lebih efisien.  Selanjutnya `user_id` dan `place_id` dipetakan ke *dataframe* yang berkaitan. 

Tahapan berikutnya adalah ***Train-Test Data Split***. Pada tahap ini, *dataset* dibagi menjadi dua bagian, yaitu data *training* (train) dan data *test* atau data validasi (val). Tahap ini bertujuan untuk mempersiapkan data *rating* yang akan digunakan dalam pelatihan dan pengujian model *Collaborative Filtering*. Pembagian *dataset* dengan komposisi 70:30 karena jumlah data yang dimiliki sedikit. 70 % untuk data *train* dan 30 % untuk data validasi. Untuk pertama data diacak terlebih dahulu agar mendapatkan variasi data pada saat melakukan pembagian *dataset*. Setelah tahapan ini data telah siap untuk dijadikan model dengan *Collaborative Filtering*.

## 5. Modelling

Dalam membuat sistem rekomendasi berdasarkan kesamaan karakteristik *item* menggunakan metode *Content-based Filtering*. Sedangkan, pembuatan sistem rekomendasi destinasi ekowisata yang dipersonalisasi dengan kemungkinan disukai oleh calon wisatawan yang belum pernah mengunjungi tempat tersebut menggunakan metode *Collaborative Filtering*. Berikut penjelasan mengenai lebih lanjut mengenai penggunaan metode tersebut:

### 5.1 *Content-based Filtering* (CBF)

*Content-Based Filtering* (CBF) adalah salah satu metode sistem rekomendasi yang menggunakan informasi atau konten dari item (misalnya, genre film, genre buku, jenis produk, atau tempat wisata) yang akan direkomendasikan untuk menentukan kesesuaian atau relevansi dengan preferensi pengguna. Cara kerja CBF dapat dilihat pada Gambar 2 di bawah ini.

![content base filtering](https://github.com/rasyidperkim/dicoding-ml-terapan/assets/63061466/2b1e942e-87d1-4b55-aa9a-9ee7286542d8)

​											Gambar 2 *Alur Proses Model Rekomendasi CBF*

Berdasarkan Gambar 2 dapat diketahui proses berdasarkan pilihan pengguna terhadap karakteristik item tertentu yang kemudian hasil rekomendasi dari filter berdasarkan karakter item yang sama. Kelebihan dari pendekatan ini di antaranya adalah mudah untuk diinterpretasikan dan dapat diterapkan pada kondisi dimana sistem belum memiliki data yang bersumber dari *user*, karena pendekatan ini hanya memanfaatkan informasi karakteristik *item* yang ada. Sedangkan kelemahannya adalah teknik ini membutuhkan deskripsi *item*/fitur yang baik. Dalam pembuatan model dengan *Content-based Filtering* (CBF) menggunakan metode *Cosine Similarity* dan *Jaccard Similarity.* 

#### 5.1.1 Cosine Similarity 

Pada *Cosine similarity* dilakukan vektorisasi TF-IDF dan *cosine similarity* sebagai *similarity function*-nya. *Cosine Similarity* mengukur kesamaan antara dua vektor. Setiap *item* direpresentasikan sebagai vektor fitur, dimana setiap dimensi vektor mewakili suatu atribut atau karakteristik dari *item* tersebut. Ketika pengguna memberikan preferensi terhadap suatu *item*, sistem akan menggunakan vektor fitur dari *item* tersebut dan menghitung *similarity* dengan vektor fitur *item* lainnya. *Item* yang memiliki nilai *similarity* tertinggi akan diurutkan dalam urutan tertentu dan dianggap sebagai *item* yang cocok untuk direkomendasikan. Nilai dari *Cosine Similarity* berkisar antara -1 dan 1. Berikut adalah persamaan matematis dari *Cosine Similarity* :
$$
\cos(\theta) = \frac{A \cdot B}{\lVert A \rVert \lVert B \rVert}
$$
Dimana :

- A dan B adalah dua vektor yang dibandingkan.
- ||A|| dan ||B|| adalah norma (panjang) dari vektor A dan B.

Sebagai contoh pengujian dari hasil *Top-5 Recommendations* pada rekomendasi tempat wisata selain "Taman Nasional Bali Barat" dengan kategori  "taman_nasional" dan "cagar_alam" dapat dilihat pada Tabel 4.

​									Tabel 4 Ujicoba pertama Rekomendasi dengan *Cosine Similarity* 

|      |                            place_name | category                  |
| ---: | ------------------------------------: | ------------------------- |
|    1 |        Taman Nasional Bukit Tigapuluh | cagar_alam taman_nasional |
|    2 |    Taman Hutan Raya Wan Abdul Rachman | cagar_alam taman_nasional |
|    3 |                Kawah Rengganis Cibuni | cagar_alam taman_nasional |
|    4 | Taman Hutan Raya Sultan Syarif Hasyim | cagar_alam taman_nasional |
|    5 |             Taman Nasional Tesso Nilo | cagar_alam taman_nasional |

Berdasarkan tabel 4, model merekomendasikan dengan tepat 5 dari 5 rekomendasi yang diminta.

Kemudian dilakukan pengujian ulang dari hasil *Top-5 Recommendations* pada rekomendasi tempat wisata selain "Danau Toba" yang memiliki 3 kategori  "budaya" ,  cagar_alam", dan "desa_wisata". Hasil rekomendasi dapat dilihat pada Tabel 5.

​									Tabel 5 Ujicoba kedua Rekomendasi dengan *Cosine Similarity* 

|      |                         place_name | category               |
| ---: | ---------------------------------: | ---------------------- |
|    1 |            Desa Wisata Penglipuran | budaya desa_wisata     |
|    2 |             Desa Wisata Cinangneng | budaya desa_wisata     |
|    3 | Desa Wisata Kampung Cai Ranca Upas | cagar_alam desa_wisata |
|    4 |                 Desa Wisata Ngadas | cagar_alam desa_wisata |
|    5 |               Desa Wisata Nglinggo | desa_wisata            |

Berdasarkan tabel 5, model merekomendasikan dengan tepat 5 dari 5 rekomendasi yang diminta.

Dengan demikian model CBF menggunakan *Cosine Similarity* pada proyek ini sudah berhasil merekomendasikan dengan tepat.

#### 5.1.2 Jaccard Similarity 

Dalam *Jaccard Similarity* harus membuat fungsi yang menghitung skor kesamaan *Jaccard* antara dua set. Meskipun lebih sederhana  dan lebih mudah untuk dihitung, *Jaccard* tidak cocok untuk data yang jarang (*sparse data*) karena dapat menghasilkan banyak pasangan item yang tidak memiliki kesamaan. Skor kesamaan *Jaccard* dihitung sebagai ukuran irisan dua set dibagi oleh ukuran gabungan dua set tersebut. Skor ini berkisar antara 0 (tidak ada kesamaan) hingga 1 (set identik). Berikut adalah persamaan matematis dari *Jaccard*.
$$
J(A,B) = \frac{{|A ∩ B|}}{{|A ∪ B|}} = \frac{{|A ∩ B|}}{{|A|+|B|-|A ∩ B|}}
$$
Dimana:

- A dan B adalah dua set yang dibandingkan.
- |A ∩ B| adalah jumlah elemen yang ada di kedua set (irisan dari A dan B).
- |A ∪ B| adalah jumlah elemen yang ada di set A atau B atau keduanya (gabungan dari A dan B).

Sebagai contoh pengujian dari hasil *Top-5 Recommendations* pada rekomendasi tempat wisata selain "Taman Nasional Bali Barat" dengan kategori  "taman_nasional" dan cagar_alam" dapat dilihat di Tabel 6.

​													Tabel 6 Ujicoba pertama Rekomendasi dengan *Jaccard Similarity* 

|      |                     place_name | category                  |
| ---: | -----------------------------: | ------------------------- |
|    1 |  Taman Nasional Kerinci Seblat | taman_nasional cagar_alam |
|    2 |          Taman Nasional Berbak | cagar_alam taman_nasional |
|    3 | Taman Nasional Bukit Tigapuluh | cagar_alam taman_nasional |
|    4 |         Kawah Rengganis Cibuni | cagar_alam taman_nasional |
|    5 |                    Kawah Putih | cagar_alam taman_nasional |

Berdasarkan tabel 6, model merekomendasikan dengan tepat 5 dari 5 rekomendasi yang diminta.

Kemudian dilakukan pengujian ulang dari hasil *Top-5 Recommendations* pada rekomendasi tempat wisata selain "Danau Toba" yang memiliki 3 kategori  "budaya" ,  cagar_alam", dan "desa_wisata". Hasil rekomendasi dapat dilihat pada Tabel 7.

​												Tabel 7 Ujicoba kedua Rekomendasi dengan *Jaccard Similarity* 

|      |                         place_name | category                         |
| ---: | ---------------------------------: | -------------------------------- |
|    1 |                 Desa Wisata Ngadas | cagar_alam desa_wisata           |
|    2 | Desa Wisata Kampung Cai Ranca Upas | cagar_alam desa_wisata           |
|    3 |         Taman Nasional Ujung Kulon | budaya cagar_alam taman_nasional |
|    4 |         Taman Nasional Meru Betiri | budaya cagar_alam taman_nasional |
|    5 |            Taman Wisata Tirta Alam | budaya cagar_alam                |

Berdasarkan tabel 7, model merekomendasikan dengan tepat 5 dari 5 rekomendasi yang diminta meskipun sebagian ada dengan tambahan kategori "taman nasional". Dengan demikian model CBF menggunakan *Jaccard Similarity* pada proyek ini sudah berhasil merekomendasikan dengan tepat.

Hasil *Top-5 Recommendations* antara dua metode berbeda, hal ini karena *Similarity Score* yang dihasilkan menggunakan rumus perhitungan yang berbeda.

### 5.2 Collaborative Filtering (CF)

*Collaborative Filtering* (CF) adalah metode dalam sistem rekomendasi yang menggunakan informasi dari pengguna lain untuk memberikan rekomendasi kepada pengguna. Metode ini mencari pola dan hubungan antara preferensi pengguna secara kolektif untuk membuat rekomendasi yang sesuai [[5\]](https://ieeexplore.ieee.org/abstract/document/10054282). Cara kerja CF dapat dilihat pada Gambar 3.

![collaborative filtering](https://github.com/rasyidperkim/dicoding-ml-terapan/assets/63061466/d01237a2-77d9-4f76-88f9-88c5d6a98ad5)

​															Gambar 3. *Alur Proses Model CF*

Berdasarkan Gambar 3, cara kerja *Collaborative Filtering* melibatkan pengumpulan data preferensi pengguna (dalam konteks ini *rating* dari pengguna) terhadap *item-item* (tempat wisata) yang ada. Berdasarkan data ini, dilakukan identifikasi pada pengguna lain yang memiliki pola preferensi yang mirip dengan pengguna yang akan direkomendasikan. Kemudian, *item-item* yang disukai oleh pengguna lainnya yang memiliki kemiripan preferensi dijadikan sebagai item yang direkomendasikan.

Kelebihan dari model CF di antaranya adalah dapat memberikan rekomendasi yang lebih personilisasi sesuai dengan preferensi dari *user* dan dapat diterapkan pada kondisi dimana sistem tidak memiliki deskripsi *item* yang baik atau data dengan *sparsitas* yang tinggi. Sedangkan kelemahannya adalah teknik ini membutuhkan banyak data *feedback* dari *user* yang berbeda-beda. Selain itu kelemahan metode ini adalah menghasilkan rekomendasi yang monoton, yaitu selalu merekomendasikan item yang sama kepada pengguna.

Dalam pemilihan metode, model rekomendasi yang digunakan dalam proyek ini adalah *RecommenderNet*. *RecommenderNet* menggunakan arsitektur *neural network* untuk menerapkan *Collaborative Filtering*.  *RecommenderNet* menerima dua input, yaitu `user_id` dan `place_id`, yang kemudian diproses melalui layer *embedding* dan diaktivasi dengan sigmoid. Fungsi sigmoid memiliki nilai output antara 0 dan 1, yang dapat digunakan untuk mewakili probabilitas bahwa pengguna menyukai item tersebut. Layer *embedding* ini digabungkan untuk memprediksi preferensi pengguna terhadap item. Setelah melalui proses pelatihan, model tersebut dapat memberikan rekomendasi item kepada pengguna berdasarkan preferensi dan interaksinya dengan *item* sebelumnya. Dalam model ini, `Binary Crossentropy` digunakan sebagai fungsi kerugian (*loss function*) untuk menghitung kesalahan model. Penggunaan *loss function* ini menentukan bagaimana cara mengukur kesalahan dari model tersebut. Selain itu, parameter  *optimizer* juga digunakan untuk menentukan algoritma optimisasi yang akan digunakan dalam proses pelatihan model. Dalam kasus ini, Adam dipilih sebagai *optimizer* dengan `learning_rate:0.001` karena dapat memperbarui bobot dan bias dengan mengikuti gradien, sambil tetap mempertahankan kecepatan dan performa dari model. Pada proyek ini digunakan `batch_size:8` dan `epochs:100` berdasarkan eksperimen. Ini berarti bahwa dalam setiap iterasi pelatihan, 8 data akan diproses secara bersamaan dan pelatihan akan dilakukan 100 kali pada seluruh data pelatihan. *Batch size* yang kecil dapat membuat pelatihan menjadi lebih cepat dan *epochs* yang banyak membuat model menjadi lebih baik.

Dalam pengujian diambil sampel salah satu ID dan didapatkan *Top-5 recommendations* sebagai berikut :

```
Rekomendasi Untuk Pengguna dengan ID: 7
------------------------------------------------------------
Top 5 Rekomendasi Tempat Ekowisata
------------------------------------------------------------
Curug Cipanas : Cagar Alam
Kebun Binatang Bandung : Cagar Alam
Stone Garden Citatah : Budaya,Cagar Alam
Taman Wisata Alam Cikole : Budaya,Cagar Alam
Ledok Sambi : Cagar Alam
```

Rekomendasi ini didasarkan pada prediksi rating yang diberikan oleh model sistem rekomendasi berdasarkan preferensi dan riwayat penilaian pengguna. Daftar ekowisata di atas merupakan rekomendasi teratas yang diurutkan berdasarkan prediksi rating tertinggi.

Penting untuk dicatat bahwa hasil pemberian rekomendasi ini bersifat contoh dan mungkin berbeda untuk pengguna lain atau dalam kasus yang berbeda.

## 6. Evaluation
### 6.1 Evaluation of Content-Based Filtering

Metrik evaluasi dalam model *Content-Based Filtering* pada proyek ini menggunakan metrik *Precision*. *Precision* mengacu pada proporsi kasus positif yang diidentifikasi dengan benar dari keseluruhan hasil yang diberikan oleh sistem atau model. Metrik ini digunakan untuk mengukur sejauh mana sistem atau model dapat menghasilkan hasil yang akurat dan relevan dalam mengklasifikasikan kasus positif. Persamaan *Precision* adalah sebagai berikut:
$$
Precision = \frac{{\text{{TP}}}}{{\text{{ TP + FP}}}}
$$
dimana:

- TP (*True Positives*) adalah jumlah *item* yang direkomendasikan dan benar-benar relevan dengan pengguna.
- FP  (*False Positives*) adalah jumlah *item* yang direkomendasikan tetapi tidak benar-benar relevan dengan pengguna.

Berdasarkan hasil perhitungan manual, 10 *item* benar-benar relevan dari 10 *item* yang direkomendasikan kepada pengguna dan tidak ada *item* yang tidak relevan dengan pengguna. Maka nilai *precise* sistem rekomendasi tersebut adalah 10/(10+0) = 1.0. *Nilai precise* 1.0 atau menunjukkan bahwa sistem rekomendasi tersebut sangat presisi dalam merekomendasikan item yang relevan dengan pengguna, baik dengan *Cosine Similarity* maupun *Jaccard Similarity*, sehingga dapat dikatakan model *Content-based Filtering* pada proyek ini dalam merekomendasikan sudah bagus.

Dengan adanya kesamaan presisi antara dua metode, maka pertimbangan selanjutnya dalam pemilihan metode *Similarity* dengan membandingkan kecepatan waktu eksekusi yang hasilnya dapat dilihat pada Tabel 8

​										Tabel 8. Perbandingan Kecepatan Waktu Eksekusi Pemberian Rekomendasi

|  No  | Method             | Time (seconds) |
| :--: | :----------------- | :------------- |
|  1   | Cosine Similarity  | 0.012577       |
|  2   | Jaccard Similarity | 0.004255       |

Berdasarkan Tabel 8, *Jaccard Similarity* (0,004 detik) memberikan waktu yang lebih cepat dalam memberikan eksekusi dibandingkan *Cosine Similarity* (0,013 detik). Dengan demikian dalam konteks proyek ini metode yang dipilih dari *Content -based Filtering* adalah *Jaccard Similarity*.



### 6.2 Evaluation of Collaborative Filtering

Dalam evaluasi model CF digunakan metrik MAE (*Mean Absolute Error*) dan RMSE (*Root Mean Square Error*) yang biasa digunakan dalam model *machine learning*. Penggunaan metrik ini bertujuan untuk mengukur rata-rata selisih antara *item* yang diprediksi oleh model dengan *item* sebenarnya. Dengan penggunaan metrik tersebut, dapat dievaluasi seberapa baik model dalam memprediksi preferensi pengguna terhadap item secara akurat. Semakin rendah MAE dan RMSE maka itu menunjukkan model semakin akurat.

Berikut ini persamaan *Mean Absolute Error* (MAE)
$$
MAE = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y_i}|
$$
Dan persamaan *Root Mean Squared Error* (RMSE)
$$
\text{RMSE} = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2}
$$
Dimana :

- n = Jumlah data atau sampel
- yi = *Actual Value* / Nilai Sebenarnya (ground truth) dari data ke-i
- ŷi = *Predicted Value* / Nilai Prediksi dari data ke-i

Hasil dari evaluasi MAE dapat dilihat pada Gambar 4 berikut :
![mae](https://github.com/rasyidperkim/dicoding-ml-terapan/assets/63061466/1e6b9566-c42b-4e87-87dd-ba719cc6a92d)

Gambar 4 *Evaluasi Model Dengan MAE*

Berdasarkan Gambar 4 diketahui model memiliki nilai *Mean Absolute Error* (MAE) yang relatif rendah pada data training sebesar 0.03 dan data validasi sebesar 0.12. Untuk sistem rekomendasi nilai tersebut sudah cukup bagus.

![rmse](https://github.com/rasyidperkim/dicoding-ml-terapan/assets/63061466/efc577dc-406b-4bcd-8c1d-779e587cbd62)

Gambar 5 *Evaluasi Model Dengan RMSE*

Berdasarkan Gambar 5, diketahui proses training model cukup *smooth* dan model konvergen pada *epochs* sekitar 100. Dari proses ini, diperoleh nilai *error* akhir berdasarkan RMSE sekitar 0.04 dan *error* pada data validasi sebesar 0.13. Nilai tersebut cukup bagus untuk sistem rekomendasi.

Dengan demikian dapat dikatakan model Collaborative Filtering pada proyek ini dalam merekemondasikan sudah cukup bagus.

## 7. Conclution

Wisatawan memerlukan sistem rekomendasi yang memahami preferensi pengguna dan menyajikan rekomendasi destinasi ekowisata yang paling sesuai dengan preferensi mereka. Berdasarkan permasalahan itu, dalam proyek ini telah berhasil dibangun sebuah sistem rekomendasi ekowisata. Proses pengembangan sistem rekomendasi melibatkan tahapan-tahapan seperti penyiapan data yang meliputi penanganan *missing value* dan data duplikat, rekayasa fitur seperti seleksi fitur dan standarisasi, pembuatan dictionary, *encoding*, dan data *train-test split*. Selanjutnya dilakukan pembangunan model, dan evaluasi kinerja. Hasil yang didapatkan sebagai berikut:

- Metode *Content-based Filtering* dapat digunakan untuk membuat sistem rekomendasi destinasi ekowisata berdasarkan kesamaan karakteristik *item*. Pada pendekatan menggunakan *Cosine Similarity* dan *Jaccard Similarity*, model sudah dapat merekomendasikan tempat ekowisata berdasarkan kesamaan atau kemiripan kategori dengan benar. *Nilai precise* 1.0 atau 100% menunjukkan bahwa sistem rekomendasi tersebut sangat presisi dalam merekomendasikan item yang relevan dengan pengguna, baik dengan *Cosine Similarity* maupun *Jaccard Similarity*. *Jaccard Similarity* (0,004 detik) memberikan waktu yang lebih cepat dalam memberikan eksekusi dibandingkan *Cosine Similarity* (0,013 detik). Dengan demikian dalam konteks proyek ini metode yang dipilih dari *Content-based Filtering* adalah *Jaccard Similarity*.
- Metode *Collaborative Filtering* dapat digunakan untuk membuat sistem rekomendasi destinasi ekowisata yang belum pernah dikunjungi dan mungkin disukai oleh pengguna berdasarkan kesamaan preferensi pemberian rating tempat ekowisata di masa lalu oleh pengguna. Berdasarkan pendekatan yang dilakukan menggunakan *RecommenderNet*  dengan `learning_rate:0.001` ,`batch_size:8`, dan `epochs:100` menunjukkan bahwa metode tersebut memiliki nilai *Mean Absolute Error* (MAE) yang relatif rendah pada data training sebesar 0.03 dan data validasi sebesar 0.12. Pada nilai *Root Mean Square Error* (RMSE) juga memiliki nilai relatif rendah yaitu data training sebesar 0.04 dan data validasi sebesar 0.13, sehingga dapat dikatakan model ini dalam merekemondasikan sudah cukup bagus.

Harapan ke depan model ini dapat digunakan dan diterapkan pada organisasi atau perusahaan. Selain itu model dapat dikembangkan lebih lanjut berdasarkan data demografi personal sehingga lebih mendekati personalisasi dan pengalaman pengguna yang baik. Selain itu model ini dapat dikembangkan lebih jauh menggunakan teknik *Hybrid Recommender System*.

## Referensi

[1] Republik Indonesia. Kementerian Dalam Negeri. (2009). *Peraturan Menteri Dalam Negeri Nomor 33 Tahun 2009 tentang Pedoman Pengembangan Ekowisata di Daerah.*

[2] Lapatta, N. T. (2022). *Ecotourism Recommendations based on Sentiments Using Skyline Query and Apache-Spark*. Journal of Social Science, 3(3), 333. https://doi.org/10.46799/jss.v3i3.333

[3] Kontogianni, E., Alepis, & Patsakis, C. (2022). *Promoting smart tourism personalised services via a combination of deep learning techniques. Expert Systems with Applications*, 187, 115964.

[4] Prasetyo, B., Atina, V., & Purwanto, E. (2021). *Sistem Rekomendasi Pariwisata dengan Metode Content Based Recommendation Berbasis Website (Studi Kasus: Dinas Pariwisata dan Budaya Surakarta)*. *Duta.com*, 14(1), 2086-9436.

[5] Prakash Goteti, L. N. S. (2022). *Design and Implementation of Item Based Collaborative Filtering - A Case Study*. In EEE 7th International Conference on Recent Advances and Innovations in Engineering (ICRAIE) (pp. 83-86). Mangalore, India. doi: 10.1109/ICRAIE56454.2022.10054282.

**---Ini adalah bagian akhir laporan---**
