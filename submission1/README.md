# Laporan Proyek Machine Learning - M. Rasyid Ridha



## Domain Proyek

Jabodetabek atau Jakarta, Bogor, Depok, Tangerang, Bekasi merupakan kawasan metropolitan di Indonesia yang terdiri dari beberapa kota dan kabupaten di Provinsi Jawa Barat, Banten, dan DKI Jakarta. Saat ini, Jabodetabek menjadi daerah dengan tingkat kepadatan penduduk tertinggi di Indonesia. Hal ini disebabkan, perkembangan ekonomi di Jabodetabek yang semakin pesat dan infrastruktur yang semakin baik, sehingga banyak masyarakat yang bermigrasi ke wilayah ini dengan harapan untuk mendapatkan kehidupan juga fasilitas yang lebih baik [[1]](https://doi.org/10.12962/j25023659.v8i2.11721).

Dengan adanya migrasi mendorong permintaan atas properti, termasuk rumah. Hal ini menarik perhatian para agen properti dalam persaingan harga rumah di kawasan tersebut, mengingat permintaan akan rumah juga terus meningkat. Ada beberapa macam spesifikasi dan harga rumah di kawasan Jabodetabek, sehingga diperlukan analisis yang tepat untuk mendapatkan rumah yang diinginkan [[2]](https://doi.org/10.59697/jik.v7i2.135.). Dengan tingginya permintaan rumah di wilayah ini menyebabkan harga rumah menjadi aspek penting yang perlu diperhatikan dalam membeli sebuah rumah impian. Faktor dari suatu harga rumah yaitu berupa faktor luas tanah, luas bangunan, jumlah kamar tidur ataupun kamar mandi,  ada/  tidaknya  garasi,  dan  lokasi [[3]](https://doi.org/10.52958/iftk.v17i3.3635).

Hanya saja penentuan harga rumah di Jabodetabek bukanlah tugas yang mudah. Variabilitas harga rumah sangat tinggi, dan harga rumah dapat berubah secara dramatis tergantung pada berbagai faktor. Oleh karena itu, penggunaan model prediktif yang dapat memperhitungkan semua faktor ini dalam penentuan harga menjadi sangat penting. Model ini dapat membantu dalam memberikan perkiraan harga yang komprehensif yang pada gilirannya dapat membantu penjual dalam menentukan harga jual yang tepat dan membantu pembeli dalam membuat keputusan pembelian yang lebih baik.

Salah satu metode yang bisa digunakan adalah dengan menggunakan *machine learning Multiple Linear Regression*. Pada penelitian oleh Cep Haryanto (2023), metode yang digunakan adalah *Multiple Linear Regression* dan *Random Forest Regression*.  Hasil dari penelitian ini diperoleh bahwa algoritma *Random Forest Regression* merupakan algoritma terbaik dalam penelitian ini dengan nilai akurasi sebesar 81,6%. Adapun beberapa faktor yang mempengaruhi harga rumah di antaranya luas lahan, luas bangunan berdiri, banyaknya kamar tidur, kamar mandi, dan garasi [[4]](https://doi.org/10.36040/jati.v7i1.6343). Pada proyek ini menggunakan algoritma *Linear Regression* ,*Random Forest Regression*, dan  algoritma *XGBoost* untuk memprediksi harga. 

## Business Understanding

Dalam sektor perumahan, penentuan harga rumah adalah proses yang kompleks dan melibatkan banyak faktor. Model prediktif dapat memainkan peran penting dalam proses ini dengan memperkirakan harga rumah berdasarkan berbagai faktor. Bagi penjual, model ini dapat membantu dalam menentukan harga jual yang tepat untuk memaksimalkan keuntungan. Bagi pembeli, model ini dapat memberikan perkiraan harga yang adil dan menghindari pembayaran yang berlebihan. Oleh karena itu, pengembangan model prediktif untuk penentuan harga rumah memiliki manfaat yang signifikan dalam konteks bisnis. Pada dataset dari web scrapping situs penjualan rumah belum tentu dapat dianalisa atau dimodelkan langsung karena ada data yang mungkin tidak dibutuhkan untuk prediksi harga atau ada data yang belum lengkap terisi, sehingga dalam hal ini perlu dilakukan *preprocessing* dan *data preparation* terlebih dahulu. Permasalahan selanjutnya adalah memilih algoritma model  yang terbaik untuk memprediksi harga rumah. Selain itu informasi penting yang harus didapatkan adalah mengetahui faktor-faktor yang paling mempengaruhi harga rumah.

### Problem Statements

Berdasarkan permasalahan yang diuraikan sebelumnya, *problem statements* dari proyek kali ini adalah sebagai berikut :

1. Apa informasi yang dapat digali dari dataset harga rumah di Jabodetabek yang akan digunakan untuk membuat model ?

2. Bagaimana cara membuat dan memilih model yang terbaik untuk memprediksi harga rumah ?

3. Apa faktor yang paling penting dalam mempengaruhi penentuan harga rumah ?

### Goals

Secara umum tujuan-tujuan yang hendak dicapai dari proyek ini adalah sebagai berikut :

1. Mendapatkan informasi dari dataset harga rumah di Jabodetabek yang akan digunakan untuk membuat model.

2. Membuat dan memilih model *machine learning* dengan algoritma terbaik untuk memprediksi harga rumah.

3. Mengetahui faktor-faktor yang paling penting dalam mempengaruhi penentuan harga rumah di Jabodetabek.

### Solution statements

Adapun solusi untuk menyelesaikan permasalahan tersebut adalah sebagai berikut :

1. Melakukan *Exploratory Data Analyst* (EDA) untuk mengetahui pola dan informasi yang tersimpan di data mengenai harga rumah di Jabodetabek dengan analisis deskriptif maupun analisis korelasi.
2. Membuat model regresi dengan mencoba 3 algoritma, yaitu *Linear Regression, Random Forest, dan XGBoosting.* Selanjutnya dilakukan evaluasi dengan metrik RMSE (*Root Mean Squared Error*) dan R2 (*R-Squared*) untuk membandingkan dan akhirnya memilih algoritma terbaik dalam konteks ini.
5. Mengidentifikasi faktor-faktor yang paling penting dalam mempengaruhi penentuan harga rumah di Jabodetabek dengan *Feature Importances*. *Feature Importances* bisa dikatakan sebagai tolak ukur besaran kontribusi berbagai data fitur yang dilatih kepada performa model prediksi.

## Data Understanding

Data yang digunakan pada proyek ini bersumber dari Kaggle pada tautan berikut ini [Daftar Harga Rumah Jabodetabek](https://www.kaggle.com/datasets/nafisbarizki/daftar-harga-rumah-jabodetabek). Menurut sumber, data daftar harga rumah ini diakses dari salah satu web listing di Indonesia yaitu [https://rumah123.com](https://rumah123.com/) pada akhir tahun 2022.

### Variabel-variabel pada Daftar Harga Rumah Jabodetabek dalam dataset adalah sebagai berikut:

- url : data link website penjualan rumah
- price_in_rp : harga rumah dalam rupiah
- title : judul promosi penjualan rumah
- address : alamat rumah yang dijual
- district : lokasi kawasan rumah
- city : keterangan kota lokasi rumah
- lat : data geografis rumah berdasarkan garis lintang
- long : data geografis rumah berdasarkan garis bujur
- facilities : fasilitas yang didapatkan di lingkungan perumahan
- property_tipe : jenis properti
- ads_id : nomor id iklan pada website
- bedrooms : jumlah kamar tidur tersedia
- bathrooms : jumlah kamar mandi tersedia
- land_size_m2 : luas tanah yang dijual
- building_size_m2 : luas bangunan yang dijual
- carports : ketersediaan  dan jumlah carport pada rumah
- certificate : jenis dokumen legalitas properti
- electricity : kapasitas daya listrik dengan satuan mah
- maid_bedrooms : jumlah kamar pembantu tersedia
- maid_bathrooms : jumlah kamar mandi pembantu tersedia
- floors : jumlah lantai terbangun
- building_age : umur bangunan
- year_built : tahun pembangunan
- property_condition : keterangan kondisi rumah
- building_orientation : orientasi mata angin bangunan
- garages : jumlah garasi
- furnishing : tingkat kelengkapan atau ketersediaan perabotan dan peralatan

#### Overview Data :

```
- Datasets Name :  jabodetabek_house_price.csv
- Data Overall : 3553 rows x 27 Column
- Source : Kaggle
- Link : https://www.kaggle.com/datasets/nafisbarizki/daftar-harga-rumah-jabodetabek
- License : Unknown
```

Pada tahap Data Understanding dilakukan analisis data eksploratif untuk menganalisis karakteristik, menemukan pola, anomali, dan memeriksa asumsi pada data. Dari 27 kolom fitur, diketahui ada 11 kolom dengan tipe data numerik float64 dan 16 kolom dengan tipe data objek. 

​												Tabel 1. <em> Tipe dan Jumlah Data Pada Dataset Awal </em>

| #    | Column               | Non Null Count | Dtype   |
| ---- | -------------------- | :------------: | ------- |
| 0    | url                  | 3553 non-null  | object  |
| 1    | price_in_rp          | 3553 non-null  | object  |
| 2    | title                | 3553 non-null  | object  |
| 3    | address              | 3553 non-null  | object  |
| 4    | district             | 3553 non-null  | object  |
| 5    | city                 | 3553 non-null  | object  |
| 6    | lat                  | 3553 non-null  | object  |
| 7    | long                 | 3553 non-null  | object  |
| 8    | facilities           | 3553 non-null  | object  |
| 9    | property_type        | 3552 non-null  | object  |
| 10   | ads_id               | 3549 non-null  | object  |
| 11   | bedrooms             | 3519 non-null  | float64 |
| 12   | bathrooms            | 3524 non-null  | float64 |
| 13   | land_size_m2         | 3551 non-null  | float64 |
| 14   | building_size_m2     | 3551 non-null  | float64 |
| 15   | carports             | 3553 non-null  | float64 |
| 16   | certificate          | 3412 non-null  | object  |
| 17   | electricity          | 3553 non-null  | object  |
| 18   | maid_bedrooms        | 3553 non-null  | float64 |
| 19   | maid_bathrooms       | 3553 non-null  | float64 |
| 20   | floors               | 3547 non-null  | float64 |
| 21   | building_age         | 2108 non-null  | float64 |
| 22   | year_built           | 2108 non-null  | float64 |
| 23   | property_condition   | 3107 non-null  | object  |
| 24   | building_orientation | 1906 non-null  | object  |
| 25   | garages              | 3553 non-null  | float64 |
| 26   | furnishing           | 3166 non-null  | object  |

Fitur **price_in_rp** adalah data target atau variabel dependen dalam proyek ini. Pada hasil pemeriksaan tipe data **price_in_rp** dideteksi sebagai data object padahal ini merupakan data target yang mesti diprediksi sehingga diperlukan mengubahnya menjadi data numerik. Untuk fitur **Electricity** seharusnya bukan object tapi data numerik, ini disebabkan ada satuan 'mah' di belakang angka pada data sehingga terbaca sebagai object. Oleh karena itu harus diubah menjadi format numerik integer dengan menghapus satuan 'mah' terlebih dahulu. Selain itu untuk lebih sesuai data pada fitur **bedrooms, bathrooms, floors, carports, maid_bedrooms, maid_bathrooms,** dan **garages** seharusnya berpola integer karena tidak mungkin dengan koma. Hanya saja konversi tidak bisa dilakukan karena masih banyak *missing value.* 

Berikut ini jumlah persentase *missing value* pada fitur-fitur yang divisualisasikan oleh Gambar 1.![](https://github.com/rasyidperkim/dicoding-ml-terapan/blob/c2305563248af15f57bde50440fdc2364f67542d/image/missing-value.png?raw=true)

​											Gambar 1. *Grafik Persentase Missing Value Pada Masing-masing Fitur*

Berdasarkan Gambar 1, ada 3 fitur yang memiliki *missing value* lebih dari 11 % data sehingga dihapus saja karena terlalu banyak *missing value* yang akan berpengaruh ke model jika diimputisasi. Selain itu pada **price_in_rp** sebagai target fitur juga ada *missing value* yang akan dihapus pada baris data tersebut.

**Analisis Deskriptif**

Analisis deskriptif adalah jenis analisis data yang digunakan untuk menggambarkan, menampilkan, dan meringkas sekumpulan data. Pada dataset, informasi ini dapat dilihat pada Tabel 2 berikut :

​																	Tabel 2. <em> Deskripsi Data </em>

| Parameters | price_in_rp  | bedrooms    | bathrooms   | land_size_m2 | building_size_m2 | carports    | maid_bedrooms | maid_bathrooms | floors      |
| ---------- | ------------ | ----------- | ----------- | ------------ | ---------------- | ----------- | ------------- | -------------- | ----------- |
| count      | 3.461000e+03 | 3428.000000 | 3433.000000 | 3459.000000  | 3459.000000      | 3461.000000 | 3461.000000   | 3461.000000    | 3455.000000 |
| mean       | 2.813270e+14 | 3.329055    | 2.624818    | 204.362243   | 185.878867       | 1.196475    | 0.495810      | 0.368969       | 1.764110    |
| std        | 3.131527e+15 | 2.698811    | 2.722220    | 402.216592   | 248.244429       | 1.115368    | 0.682394      | 0.534321       | 0.638186    |
| min        | 4.200000e+08 | 1.000000    | 1.000000    | 12.000000    | 1.000000         | 0.000000    | 0.000000      | 0.000000       | 1.000000    |
| 25%        | 8.000000e+09 | 2.000000    | 2.000000    | 75.000000    | 65.500000        | 1.000000    | 0.000000      | 0.000000       | 1.000000    |
| 50%        | 1.500000e+10 | 3.000000    | 2.000000    | 108.000000   | 110.000000       | 1.000000    | 0.000000      | 0.000000       | 2.000000    |
| 75%        | 3.600000e+10 | 4.000000    | 3.000000    | 187.500000   | 200.000000       | 2.000000    | 1.000000      | 1.000000       | 2.000000    |
| max        | 4.270000e+16 | 99.000000   | 99.000000   | 8000.000000  | 6000.000000      | 15.000000   | 7.000000      | 5.000000       | 5.000000    |

Dari data yang ditampilkan oleh Tabel 2, dapat diambil informasi :

1. Berdasarkan count, ada *missing value* pada bedrooms, bathrooms, land_size_m2, building_size_m2, dan floors.
2. Untuk imputisasi pada *missing value* sebaiknya tidak menggunakan mean pada bedrooms, bathrooms, dan floor karena isi datanya harus berupa integer tanpa koma.
3. Dari nilai minimum, ada data dari land_size_m2 dan building_size_m2  yang secara ukuran janggal
4. land_size_m2 harus lebih besar dari building_size_m2, sehingga jika ada yang tidak demikian perlu dihapus.
5. Pada semua fitur, nilai 75 % dan nilai max sangat jauh, sehingga harus dilakukan penghapusan *outlier* agar model tidak terganggu

Dengan informasi ini harus dilakukan EDA (*Exploratory Data Analysis*).

#### **EDA (Exploratory Data Analysis)**

Disini  perlu dilakukan pembersihan dan perbaikan data sehingga analisa menjadi lebih tepat. Pertama perlu dimeriksa data duplikat karena ada kemungkinan pengiklan mempublikasi iklan mereka secara berulang yang mana direkam dengan url yang berbeda padahal isinya sama. Setelah dilakukan pemeriksaan terdapat 92 data duplikat yang selanjutnya dihapus.

Dari hasil penelusuran dan analisis, ditemukan informasi sebagai berikut :

1. Terdapat kategori yang memiliki jumlah yang terlalu banyak yaitu **url, title, address, district, lat, long, facilities, ads_id**
2. Terdapat kategori yang hanya memiliki satu data yaitu **property_type.**

Maka kategori tersebut dihapus dari dataset dan dipilih kategori yang cocok. Selain itu harus diperiksa data yang janggal dimana ada data yang luas bangunan lebih besar daripada luas lahan. Selain itu juga ada penghapusan data yang tidak rasional yaitu misalnya ada dari list  bangunan berukuran 1 m2 dengan harga Rp. 170.000.000.000 dan bangunan dengan ukuran 18 m2 dengan harga Rp. 35.900.000.000 akan dihapus karena dianggap janggal. Informasi lainnya ada 2 fitur memiliki catatan bercampur dari kategori (misalnya, **property_condition** memiliki label dari **furnishing,** begitu juga dengan **furnishing**) sehingga bisa menyebabkan inkonsistensi untuk mengurutkan kategori ini. Kedua kondisi pasangan dan jumlah pengamatan cocok dan saling tertukar kategorinya. Isian data tertukar antara kolom **furnishing** dan **property_condition **sehingga harus diselesaikan terlebih daulu.

**Missing Value and Outlier Treatment**

Penanganan *missing value* pada dataset ini digunakan beberapa cara.

1. Untuk data target *feature* yaitu **price_in_rp** yang kosong akan dihapus.
2. Untuk data kategorikal seperti **furnishing**, **property_condition**, **certificate** dengan mengimputasi data *missing value* dengan menggunakan modus dari masing-masing variabel.
3. Untuk data numerik berpola integer (tanpa koma) seperti **bedrooms** ,**bathrooms** , **floors**, **electricity** dengan menggunakan median dari masing-masing variabel. Untuk data numerik seperti **land_size_m2** dan **building_size_m2** yang kosong perlu dihapus.

Setelah dilakukan pemrosesan maka dataset ini sudah bersih dari *missing value*, dan selanjutnya penanganan *outlier*.

![boxplot all numeric features](https://github.com/rasyidperkim/dicoding-ml-terapan/blob/39e563100391aa463d803979e48e76f79c38f0ca/boxplot%20outlier.png?raw=true)

​						Gambar 3. *Grafik Boxplot Untuk Mengetahui Sebaran Data pada Masing-masing Fitur*

*Outlier* ini bisa terjadi karena terdapat data rumah yang sangat mewah dengan harga yang sangat tinggi atau bisa karena kesalahan penginputan data.*Outlier* dapat mempengaruhi hasil analisis dan model statistik. Oleh karena itu, *outlier* tersebut perlu dilakukan penanganan. Salah satu metode yang umum digunakan untuk menangani *outlier* adalah **metode IQR (Interquartile Range).** 

Metode IQR bekerja dengan menghitung IQR, yaitu rentang antara kuartil pertama (25%) dan kuartil ketiga (75%). *Outlier* kemudian diidentifikasi sebagai nilai yang berada di bawah Q1 - 1.5 I QR atau di atas Q3 + 1.5 I QR. *Outlier* ini kemudian digantikan dengan nilai batas bawah atau batas atas tersebut.

Berikut Persamaannya :

```
Batas bawah = Q1 - 1.5 * IQR
Batas atas = Q3 + 1.5 * IQR
```

Setelah *missing value* dan *outlier* ditangani, dataset menjadi bersih dan memiliki 1807 sampel. Selanjutnya, proses analisis data dilakukan dengan teknik Univariate EDA.

#### Univariate Analysis

Univariat Analysis adalah analisis statistika yang hanya menggunakan satu variabel saja. Untuk fitur numerik bisa dilihat pada histogram masing-masing fiturnya.

![numerical features univariat](https://github.com/rasyidperkim/dicoding-ml-terapan/blob/4ea60e30d234b4c4148c80e2398ff2b04ef4b26a/numerical_features.png?raw=true)

​										Gambar 4. *Diagram bar Untuk Analisis Univariat* pada data numerik

Berikut interpretasi dari grafik yang bisa diambil :
* price_in_rp: Sebagian besar properti pada data ini memiliki harga di bawah 1.5 miliar Rupiah, dengan beberapa properti memiliki harga hingga 4.8 miliar Rupiah. Distribusi ini memiliki skew kanan, yang berarti ada beberapa properti dengan harga yang sangat tinggi yang mendorong rata-rata ke atas.

* bedrooms, bathrooms: Sebagian besar properti memiliki 2-3 kamar tidur dan 1-2 kamar mandi. Ada beberapa properti dengan lebih banyak kamar tidur dan kamar mandi

* land_size_m2, building_size_m2: Sebagian besar properti memiliki ukuran lahan dan bangunan di bawah 200 m2, dengan beberapa properti memiliki ukuran lahan dan bangunan yang jauh lebih besar. Distribusi ini juga skew ke kanan.

* carports: Semua properti memiliki 1 carport.

* electricity: Daya listrik sebagian besar antara 1300 dan 2200, dengan beberapa properti memiliki daya listrik yang lebih rendah atau lebih tinggi.

* maid_bedrooms, maid_bathrooms: Sebagian besar properti tidak memiliki kamar tidur atau kamar mandi pembantu. Beberapa properti memiliki 1 atau 2 kamar tidur pembantu.

* floors: Sebagian besar properti memiliki 1 atau 2 lantai, dengan beberapa properti memiliki 3 lantai.

* garages: Sebagian besar properti tidak memiliki garasi, beberapa memiliki 1 atau 2 garasi.

Selanjutnya perlu dilakukan analisis multivariat.

#### Multivariate Analysis

Multivariate EDA menunjukkan hubungan antara dua atau lebih variabel pada data. Multivariate EDA yang menunjukkan hubungan antara dua variabel biasa disebut sebagai bivariate EDA. Dalam hal ini diketahui hubungan data target dengan data pada fitur lainnya.

**Categorical Features**

![boxplot of house price](https://github.com/rasyidperkim/dicoding-ml-terapan/blob/3eb8a706d73e5ae081211a89f9a522549b358b3c/boxplot%20category%20outlier.png?raw=true)

​									Gambar 5. *Diagram bar Untuk Analisis Multivariat pada data kategori*

Berikut informasi yang didapatkan dari fitur kategorikal:

- city : Kota tempat properti berada memiliki pengaruh yang signifikan terhadap harga properti. Rata-rata properti di Jakarta cenderung memiliki harga yang lebih tinggi dibandingkan dengan kota-kota lain. Hal ini bisa jadi karena Jakarta sebagai ibukota dan memang pusat bisnis dan komersial, sehingga nilai properti di sana cenderung lebih tinggi. Namun, perlu diingat bahwa ada juga variasi harga yang besar seperti di kota Bekasi dan Depok, seperti ditunjukkan oleh *outlier* pada boxplot.
- certificate: Harga properti juga bervariasi berdasarkan jenis sertifikat. Properti dengan "SHM - Sertifikat Hak Milik" cenderung memiliki harga yang lebih tinggi dibandingkan dengan properti dengan sertifikat lainnya, hanya saja hubungan ini tidak terlalu signifikan bagi harga.
- property_condition: Kondisi properti juga berpengaruh terhadap harga. Properti yang dalam kondisi "Bagus Sekali" cenderung memiliki harga yang lebih tinggi dibandingkan dengan properti dalam kondisi lain. Hanya saja hubungan ini tidak terlalu signifikan bagi harga.
- furnishing: Perlengkapan properti atau furnishing juga berpengaruh terhadap harga. Properti yang dilengkapi perabotan cenderung memiliki harga yang lebih tinggi dibandingkan dengan properti yang tidak dilengkapi perabotan. Ini mungkin karena biaya tambahan untuk mebel dan dekorasi yang sudah ada di properti tersebut.Hanya saja hubungan ini tidak terlalu signifikan bagi harga.

**Numerical Features**

Untuk mengamati hubungan antara fitur numerik, dapat dilihat dari korelasi antara fitur numerik dengan fitur target (price_in_rp).

![Matriks korelasi](https://github.com/rasyidperkim/dicoding-ml-terapan/blob/40bf8205057cf7bfb85c2491899cc9ea6589e16b/korelasi%20matriks.png?raw=true)

​															Gambar 6. *Matriks Korelasi Fitur Numerik*

Dari matriks korelasi, dapat dilihat korelasi antara setiap pasangan fitur. Nilai korelasi berkisar antara -1 hingga 1, di mana 1 berarti korelasi positif sempurna, -1 berarti korelasi negatif sempurna, dan 0 berarti tidak ada korelasi. Beberapa poin yang dapat diambil adalah:

* Harga rumah memiliki korelasi yang sangat kuat dengan ukuran lahan dan ukuran rumah. Kamar tidur, kamar mandi, dan kapasitas listrik juga memiliki korelasi yang kuat dengan harga.

* Ukuran lahan dan ukuran rumah memiliki korelasi yang sangat kuat, makin besar luas lahan biasanya cenderung makin besar juga luas bangunan.

* Kapasitas listrik juga memiliki korelasi positif yang cenderung kuat dengan ukuran lahan dan ukuran rumah, yang berarti properti dengan ukuran lahan dan bangunan yang lebih besar cenderung memiliki daya listrik yang lebih besar.

* Semua fitur memiliki korelasi positif terhadap harga rumah.

Dengan mempertimbangkan semua analisis ini, berikut adalah beberapa insight awal untuk fitur yang harus dipilih untuk model prediksi:

1. Semua Fitur numerik kecuali carport, garages, maid_bathrooms, dan floors harus dipertimbangkan karena mereka memiliki korelasi positif yang kuat hingga moderat dengan harga dan dapat memberikan informasi yang berharga untuk prediksi.
2. Fitur kategorikal 'City' harus dipertimbangkan karena mereka menunjukkan korelasi positif dan variasi yang signifikan dalam harga berdasarkan kategori mereka.

Selanjutnya pada tahap Data Preparation dipilih fitur yang dianggap paling informatif dan berpengaruh dalam prediksi penentuan harga.

## Data Preparation

*Data preparation* merupakan tahapan penting dalam proses pengembangan model machine learning. Ini adalah tahap di mana kita melakukan proses transformasi pada data sehingga menjadi bentuk yang cocok untuk proses pemodelan. Pada tahapan ini, terdapat beberapa proses sebagai berikut :

1. **Outlier Treatment**, yaitu penanganan data outlier (pecilan) dengan menggunakan metode IQR (*Interquartile Range)* . Metode IQR bekerja dengan menghitung IQR, yaitu rentang antara kuartil pertama (25%) dan kuartil ketiga (75%). *Outlier* kemudian diidentifikasi sebagai nilai yang berada di bawah Q1 - 1.5 I QR atau di atas Q3 + 1.5 I QR. 

2. **Encoding**: Encoding adalah proses konversi data kategorikal menjadi bentuk numerik. Alasan penggunaan tahapan ini adalah agar data kategorikal setelah dikonversi dapat dipahami oleh algoritma sehingga menjadi bagian dari model.Ada dua teknik encoding yang dipakai dalam proyek ini :

   * Untuk variabel kategorikal nominal (tanpa urutan) seperti City, menggunakan *One-Hot Encoding* yaitu membangun variabel biner (0 dan 1) baru untuk setiap kategori dalam fitur yang diberikan. Hasil dari encoding ini pada fitur City menghasilkan kolom baru city_Depok, city_Bekasi, city_Tangerang, city_Jakarta, dan city_Bogor. Misalnya pada data yang berlokasi di kota Bekasi memiliki nilai 1 pada kolom city_Bekasi dan nilai 0 pada kolom hasil encoding lainnya.
   * Untuk variabel kategorikal ordinal (variabel yang memiliki urutan) seperti certificate, property_condition, dan furnishing, perlu di-*encode* terlebih dahulu dengan teknik Ordinal Encoding agar dapat diterima oleh *machine learning*. Dalam metode ini, setiap kategori unik dalam fitur diberi nilai integer. Misalnya, pada Furnishing terdapat fitur dengan tiga kategori: 'Unfurnished, 'Semi Furnished', dan 'Furnished', lalu dijadikan nilai 1 untuk 'Unfurnished', 2 untuk 'Semi Furnished', dan 3 untuk 'Furnished' sesuai urutan yang telah diatur. 

3. **Feature selection** : proses pemilihan fitur yang paling relevan dari dataset untuk digunakan dalam model *machine learning*. Alasan penggunaan tahapan ini adalah untuk meningkatkan efisiensi komputasi dan dalam beberapa kasus dapat meningkatkan kinerja model. **F_classif** dan **chi2** adalah dua metode yang digunakan dalam *feature selection* untuk menentukan fitur mana yang memiliki pengaruh paling besar terhadap target. Kedua metode ini adalah metode statistik yang mengukur hubungan antara setiap fitur dan target.

   * **F_classif**: Metode ini mengukur hubungan Linear antara setiap fitur dan target. Nilai F yang dihasilkan oleh metode ini adalah rasio variabilitas antar kelompok dengan variabilitas dalam kelompok. Dengan kata lain, fitur dengan nilai F yang lebih tinggi memiliki variasi yang lebih besar antara kategori target, yang berarti mereka mungkin lebih informatif. Persamaan untuk nilai F adalah:
     $$
     F = (SSB / k-1) / (SSW / N-k)
     $$
       Dimana : 

     - F adalah nilai F-statistik.
     - SSB adalah *Sum of Squares Between groups*. Ini adalah variasi total antara grup dan dihitung sebagai: SSB = ΣNi (Yi. - Y..)^2, dimana Ni adalah jumlah sampel dalam grup i, Yi. adalah rata-rata sampel dalam grup i, dan Y.. adalah rata-rata total sampel.
     - k adalah jumlah kelompok, k-1 sama dengan df atau derajat kebebasan
     - SSW adalah Sum of Squares Within groups. Ini adalah variasi total dalam grup dan dihitung sebagai: SSW = ΣΣ (Yij - Yi.)^2, dimana Yij adalah sampel j dalam grup i.
     - N adalah jumlah total sampel. N - k sama dengan df2 yaitu derajat kebebasan dalam kelompok

   * **chi2**: Metode ini mengukur ketergantungan antara setiap fitur dan target. Ini adalah uji Chi-kuadrat, yang menguji hipotesis nol bahwa fitur dan target adalah independen. Nilai Chi-kuadrat yang lebih tinggi menunjukkan bahwa fitur dan target tidak independen, yang berarti fitur tersebut mungkin informatif. Rumus untuk nilai Chi-kuadrat adalah:
     $$
     X^2 = Σ [ (O-E)^2 / E ]
     $$
     ​																								

     ​	Dimana O adalah observasi (frekuensi yang diobservasi) dan E adalah ekspektasi (frekuensi yang diharapkan).

     

4. **Train-Test Split**: Untuk keperluan validasi model, data perlu dipisahkan menjadi data *training* dan data *testing*. Dalam proyek ini rasio pembagian dataset adalah 80 % untuk data *training* dan 20 % untuk data *testing.*

5. **Standardization**: Tahap ini dilakukan karena algoritma *machine learning* memiliki performa lebih baik dan konvergen lebih cepat ketika dimodelkan pada data dengan skala yang relatif sama.

   

Hasil 5 urutan teratas dari Feature Selection ditunjukkan oleh Tabel 3 berikut.

​																		Tabel 3. <em> Lima Fitur Terpilih</em>

| No.  | Top 5 Feature    | F Score | Chi-2 Score |
| :--: | ---------------- | ------- | ----------- |
|  1   | building_size_m2 | 28.63   | 96675.52    |
|  2   | land_size_m2     | 26.62   | 119407.96   |
|  3   | electricity      | 9.32    | 403257.69   |
|  4   | bathrooms        | 9.30    | 827.27      |
|  5   | bedrooms         | 8.55    | 273.27      |

Dari hasil analisa padaTabel 3 diketahui bahwa build_size_m2 dan land_size_m2 atau ukuran bangunan dan lahan memiliki pengaruh yang sangat signifikan dan informatif terhadap harga rumah. Hanya saja metode ini tidak mempertimbangkan interaksi antara fitur. Oleh karena itu dalam model ini dimasukkan 5 fitur teratas ditambah 5 fitur dari kota/city yang dianggap memiliki hubungan signifikan terhadap harga.

1. building_size_m2			
2. land_size_m2
3. electricity
4. bathrooms
5. bedrooms
6. city_Depok
7. city_Bekasi
8. city_Tangerang
9. city_Jakarta
10. city_Bogor

Sedangkan untuk Train Test Split digunakan proporsi 80:20 yaitu 80 % dari jumlah data untuk data latihan dan 20% untuk data ujian. Proporsi 80:20 cukup normal karena jumlah data kita tidak terlalu besar. Untuk standarisasi, digunakan teknik *StandardScaler* dari library Scikitlearn. *StandardScaler* melakukan proses standarisasi fitur dengan mengurangkan *mean* (nilai rata-rata) kemudian membaginya dengan standar deviasi untuk menggeser distribusi.  *StandardScaler* menghasilkan distribusi dengan standar deviasi sama dengan 1 dan *mean* sama dengan 0. 

## Modelling

Pada tahap ini akan dibuat model regresi untuk memprediksi harga rumah. Algoritma yang digunakan adalah sebagai berikut :

#### 1. **Linear Regression**

Metode ini mencoba menemukan hubungan linear antara fitur dan target. Dalam kata lain, ia mencoba menyesuaikan garis terbaik yang menggambarkan hubungan antara fitur dan target. Model ini sudah lazim digunakan untuk memprediksi nilai kontinu termasuk dalam hal ini prediksi harga rumah.

Kelebihan metode ini adalah sederhana dan mudah diinterpretasikan. *Linear Regression* juga efisien dari segi komputasi. Kekurangan dari *Linear Regression* yaitu mengasumsikan hubungan linear antara fitur dan target, yang mungkin tidak selalu benar. Selain itu, model ini mungkin tidak berkinerja baik jika ada fitur yang berkorelasi erat (multikolinearitas).

Tahapan dalam penggunaan metode ini yaitu membangun Linear Regression model dan parameternya kemudian melakukan pelatihan model

Parameter yang digunakan pada proses pemodelan ini adalah 

1. `fit_intercept`: Parameter ini menentukan apakah akan ada penyesuaian terhadap intersep dalam model. Parameter ini diatur sebagai `True` untuk memperhitungkan intersep dalam model *Linear Regression*.  Intersep dalam model regresi linear akan memberikan perkiraan harga dasar (tanpa mempertimbangkan fitur-fitur lain) saat semua fitur memiliki nilai nol. Ini adalah komponen yang penting dalam model regresi linear karena bisa jadi ada faktor-faktor lain selain fitur-fitur yang mempengaruhi harga rumah, seperti faktor-faktor ekonomi atau geografis.
2. `n_jobs`: Parameter ini menentukan jumlah pekerja yang digunakan dalam pelatihan model. Jika diaFRtur sebagai -1, semua CPU yang tersedia akan digunakan. Jika diatur sebagai nilai positif, akan digunakan jumlah pekerja sesuai dengan nilai yang ditentukan.

#### 2. **Random Forest**

*Random Forest* termasuk algoritma *ensemble* yang menggabungkan banyak pohon keputusan untuk membuat prediksi. Setiap *tree* (pohon) dalam *forest* (hutan) dilatih pada subset data dengan penggantian sampel, dan pada setiap titik split dalam pohon, hanya subset fitur yang dipilih secara acak yang dipertimbangkan. Prediksi dari semua pohon kemudian dirata-rata untuk mendapatkan prediksi akhir.

- Kelebihan dari *Random Forest* adalah
  - Dapat menangani fitur kategorikal dan numerik, dan tidak mengasumsikan hubungan linear antara fitur dan target.
  - Dapat mengatasi data training dalam jumlah sangat besar secara efisien.
  - Metode yang efektif untuk mengestimasi hilangnya data.
  - Menyediakan metode eksperimental untuk mendeteksi interaksi variabel.
- Kekurangan  dari *Random Forest* adalah
  - Waktu pemrosesan yang lama karena menggunakan data yang banyak dan membangun model tree yang banyak pula untuk membentuk random trees karena menggunakan single processor sehingga membutuhkan lebih banyak sumber daya komputasi dibandingkan regresi linear.
  - Interpretasi yang sulit dan membutuhkan mode penyetelan yang tepat untuk data.
  - Ketika digunakan untuk regresi, mereka tidak dapat memprediksi di luar kisaran dalam data test.

Tahapan dalam penggunaan metode ini yaitu membangun model *Random Forest* beserta parameter dan melakukan pelatihan model.

Parameter yang digunakan dalam model ini yaitu :

1. `max_depth`: Parameter ini mengontrol kedalaman maksimum setiap pohon keputusan dalam Random Forest. Nilai 10 menunjukkan bahwa setiap pohon dalam ensemble akan memiliki kedalaman maksimum 10. Kedalaman yang lebih besar memungkinkan model untuk mempelajari pola yang lebih kompleks, tetapi juga meningkatkan risiko overfitting.
2. `min_samples_leaf`: Jumlah sampel minimum yang diperlukan untuk membentuk satu leaf (simpul daun) pada pohon keputusan. Nilai 2 menunjukkan bahwa setiap simpul daun harus memiliki setidaknya 2 sampel.
3. `n_estimators`: Parameter ini menentukan jumlah pohon keputusan yang akan dibangun . Dalam kasus ini, model akan terdiri dari 400 pohon keputusan. Semakin banyak pohon yang digunakan, semakin stabil dan kurang rentan terhadap variabilitas data.
4. `random_state`: Parameter ini digunakan untuk mengatur seed dari generator angka acak. Hal ini memastikan bahwa pengacakan data atau pemilihan fitur yang acak dilakukan dengan cara yang konsisten setiap kali model dilatih. Dengan menggunakan nilai `123`, model akan menghasilkan hasil yang sama setiap kali kode dijalankan, asalkan konfigurasi model dan data yang digunakan tidak berubah.

#### 3. **XGBoost**

*XGBoost*, atau *Extreme Gradient Boosting*, adalah algoritma yang menggunakan teknik *gradient boosting* untuk menghasilkan model prediktif dalam bentuk *ensemble* pohon keputusan yang sederhana. *XGBoost* membangun model secara berurutan, di mana setiap pohon baru mencoba memperbaiki kesalahan yang dibuat oleh pohon sebelumnya. Peningkatan gradien adalah algoritma pembelajaran yang diawasi, yang mencoba memprediksi variabel target secara akurat dengan menggabungkan perkiraan serangkaian model yang lebih sederhana dan lebih lemah.  Pelatihan berlangsung berulang, menambahkan pohon baru yang memprediksi residu atau kesalahan pohon sebelumnya yang kemudian digabungkan dengan pohon sebelumnya untuk membuat prediksi akhir. Ini disebut peningkatan gradien karena menggunakan algoritma turunan gradien untuk meminimalkan kerugian saat menambahkan model baru. 

Kelebihan *XGBoost* adalah :

- sangat efisien dan fleksibel, yang dapat menangani fitur kategorikal dan numerik.
- memiliki metode built-in untuk menangani missing values.

Kekurangan *XGBoost* adalah :

- Sama seperti *Random Forest*, *XGBoost* bisa menjadi model yang kompleks dan membutuhkan lebih banyak sumber daya komputasi.
- Model ini sulit untuk diinterpretasikan dan lebih rentan terhadap overfitting jika parameter tidak ditentukan dengan benar.

Tahapan dalam penggunaan metode ini yaitu Inisialisasi objek XGBRegressor beserta parameter kemudian melakukan pelatihan model.

Parameter yang digunakan dalam model ini yaitu :

1. `learning_rate`: Parameter ini mengontrol laju pembelajaran (learning rate) dalam XGBoost. Nilai 0.1 menunjukkan bahwa setiap iterasi, model akan memperbarui bobotnya sebesar 0.1 kali gradien penurunan fungsional kesalahan. Learning rate mengatur seberapa cepat model belajar dari data. Nilai yang lebih rendah dapat menghasilkan prediksi yang lebih akurat, tetapi juga memperlambat proses pelatihan.
2. `max_depth`: Parameter ini mengontrol kedalaman maksimum setiap pohon keputusan dalam XGBoost. Nilai 3 menunjukkan bahwa setiap pohon dalam ensemble akan memiliki kedalaman maksimum 3. Semakin dalam pohon, semakin kompleks dan mungkin overfitting.
3. `min_child_weight`: Jumlah minimum sampel yang diperlukan untuk membentuk sebuah leaf (simpul daun) pada pohon. Nilai 4 menunjukkan bahwa setiap simpul daun harus memiliki setidaknya 4 sampel. Penyesuaian parameter ini harus dilakukan dengan hati-hati untuk menghindari model yang terlalu sederhana.
4. `n_estimators`: Parameter ini menentukan jumlah pohon keputusan yang akan dibangun dalam ensemble XGBoost. Dalam kasus ini, model akan terdiri dari 50 pohon keputusan. Semakin banyak pohon yang digunakan, semakin kompleks model dan semakin tinggi potensi overfitting. Namun, terlalu sedikit pohon dapat menyebabkan model yang terlalu sederhana.

Model terbaik dipilih setelah evaluasi masing-masing model tersebut.

## Evaluation

Model yang digunakan adalah model regresi atau prediksi sehingga metrik untuk evaluasi yang lebih cocok digunakan yaitu :

- *Root Mean Squared Error* (RMSE)
- *R-Squared* (R2)

#### 1. Root Mean Squared Error (RMSE)

RMSE merupakan salah satu cara untuk mengevaluasi model regresi dengan mengukur tingkat akurasi hasil perkiraan suatu model. RMSE dihitung dengan mengkuadratkan error (prediksi – observasi) dibagi dengan jumlah data (= rata-rata), lalu diakarkan. Semakin kecil nilai RMSE, semakin dekat nilai yang diprediksi dan diamati. Kelebihan dari RMSE yaitu memiliki tingkat sensitivitas yang cukup tinggi. Sedangkan kekurangannya RMSE tidak menggambarkan kesalahan rata-rata saja namun memiliki implikasi lain yang lebih sulit untuk diurai dan dipahami. Berikut ini formula yang digunakan :

$$
\text{RMSE} = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2}
$$
Diketahui:

- n = Jumlah Data
- yi = *Actual Value* / Nilai Sebenarnya
- ŷi = *Predicted Value* / Nilai Prediksi

Metrik RMSE (*Root Mean Squard Error*) dipilih daripada MSE karena memberikan kesalahan dalam unit yang sama dengan variabel target, sehingga lebih mudah diinterpretasikan. RMSE juga memberikan bobot lebih pada kesalahan yang besar, karena mengambil akar kuadrat dari nilai MSE. 

#### 2. R-Squared (R<sup>2</sup>)

*R<sup>2</sup>* merupakan angka yang berkisar antara 0 sampai 1 yang mengindikasikan besarnya kombinasi variabel independen secara bersama – sama mempengaruhi nilai variabel dependen. Semakin mendekati angka satu, model yang dikeluarkan oleh regresi tersebut akan semakin baik.

Jika diperhatikan rumus R *squared* dibawah sangat dipengaruhi oleh nilai Y prediksi atau nilai Y dari hasil rumus dengan nilai Y aktual. Kenyataan yang sering muncul adalah nilai R *squared* akan semakin membaik (nilainya akan terus mendekati nilai 1) jika ditambah variabel. Semakin banyak jumlah variabel yang menentukan nilai Y prediksi, maka nilai SSres akan semakin besar yang berakibat pada besarnya nilai R *squared*.
$$
R^2 = 1 - \frac{{SS_{\text{res}}}}{{SS_{\text{tot}}}}
$$
Diketahui:

- SSres : Kuadrat dari selisih nilai Y prediksi dengan nilai rata-rata Y = ∑ (Ypred – Yrata-rata)²
- SStot : Kuadrat dari selisih nilai Y aktual dengan nilai rata-rata Y = ∑ (Yaktual – Yrata-rata)²

 Dengan R<sup>2</sup> yaitu ukuran seberapa baik variabel target dapat dijelaskan oleh fitur-fitur yang digunakan dalam model. 

Hasil evaluasi metrik terhadap ketiga model di atas ditunjukkan oleh Tabel 4 di bawah ini.

​														Tabel 4 *Nilai Evaluasi Metrik Tiga Model*

| index | Model             | RMSE Train                    | RMSE Test                     | R<sup>2</sup> Train | R<sup>2</sup> Test |
| ----- | ----------------- | ----------------------------- | ----------------------------- | ------------------- | ------------------ |
| 0     | Linear Regression | 5.73095807  x 10<sup>9</sup>  | 4.91038672 x  10<sup>9</sup>  | 0\.884              | 0\.911             |
| 1     | Random Forest     | 3.109166155 x  10<sup>9</sup> | 4.57687932  x  10<sup>9</sup> | 0\.961              | 0\.923             |
| 2     | XGB               | 4.399870222 x  10<sup>9</sup> | 4.6633852 x  10<sup>9</sup>   | 0\.922              | 0\.92              |

Setelah melalui berbagai tahapan evaluasi sesuai dengan hasil perhitungan metriks pada Tabel 4 di atas maka diputuskan bahwa model terbaik yang akan digunakan adalah Random Forest karena memiliki performa yang baik pada data pengujian (RMSE paling rendah dan R<sup>2</sup> paling tinggi).

Selanjutnya untuk mengetahui faktor-faktor yang paling penting dalam mempengaruhi penentuan harga rumah di Jabodetabek dengan bantuan *feature importance* dari *Random Forest*, dan visualisasi hasilnya dapat dilihat pada Gambar 7.

![feature importance](https://github.com/rasyidperkim/dicoding-ml-terapan/blob/1c8e099e2d49f1e8eb0768ce49f963b91821515e/random%20forest%20impotance.png?raw=true)

​											Gambar 7 *Faktor-Faktor Paling Penting Dalam Mempengaruhi Harga Rumah*

Pada Gambar 7, luas bangunan dan luas lahan adalah faktor paling penting dalam penentuan harga rumah, jauh melampaui nilai faktor lainnya. Kemudian faktor jumlah kamar tidur, kapasitas listrik, dan lokasi rumah yaitu fitur kota adalah urutan faktor selanjutnya. Dengan demikian pertimbangan jual beli rumah harus lebih memperhatikan faktor-faktor tersebut terutama dari yang paling penting.

### Conclusion

Penentuan harga rumah di Jabodetabek bukanlah tugas yang mudah. Variabilitas harga rumah sangat tinggi, dan harga rumah dapat berubah secara dramatis tergantung pada berbagai faktor. Oleh karena itu, penggunaan model prediktif yang dapat memperhitungkan semua faktor ini dalam penentuan harga menjadi sangat penting. Harga rumah dapat berubah secara dramatis tergantung pada berbagai faktor. Oleh karena itu, penggunaan model prediktif yang dapat memperhitungkan semua faktor ini dalam penentuan harga menjadi sangat penting. Dengan adanya model prediksi dapat membantu penjual dalam memberikan perkiraan harga yang komprehensif yang pada gilirannya dapat membantu penjual dalam menentukan harga jual yang tepat dan membantu pembeli dalam membuat keputusan pembelian yang lebih baik.

Salah satu tujuan dalam proyek ini yaitu mendapatkan informasi dari dataset harga rumah di Jabodetabek yang akan digunakan untuk membuat model. Setelah dilakukan eksplorasi analisa data, didapatkan informasi atau *insight* di antaranya harga penjualan rumah di Jakarta cenderung lebih tinggi dibanding kota Jabodetabek lainnya. Selain faktor lokasi, harga rumah memiliki korelasi yang sangat kuat dengan ukuran lahan dan ukuran rumah. kamar tidur, kamar mandi, dan kapasitas listrik juga memiliki korelasi yang kuat dengan harga.

Setelah itu  tujuan lainnya membuat dan memilih model *machine learning* dengan algoritma terbaik untuk memprediksi harga rumah. Dalam membuat model prediksi harga rumah ini harus dilakukan persiapan data terlebih dahulu seperti penanganan data *outlier* dengan metode IQR, *Encoding, Feature Selection, Train-Test Split, dan Standarization.* Kemudian setelah itu parameter masing-masing model  diatur dan pelatihan model dijalankan. Pada model *Linear Regression*, parameter yang diatur adalah fit_intercept menjadi True dan n_jobs dengan nilai -1. Sedangkan pada model *Random Forest*, parameter yang diatur adalah max_depth : 10, min_samples_leaf:2, n_estimators:400, dan random_state:123. Adapun pada model XGBoost, pengaturan parameter yaitu learning_rate:0,1, max_depth:3, min_child_weight:4, dan random_state:123. Setelah proses evaluasi maka diputuskan bahwa model terbaik yang akan digunakan adalah *Random Forest* karena memilki RMSE paling rendah dan R<sup>2</sup> paling tinggi dibandingkan dua model lainnya.  Adapun tujuan ketiga yaitu mengetahui faktor-faktor yang paling penting dalam mempengaruhi penentuan harga rumah di Jabodetabek, telah berhasil diketahui dengan fitur importance milik Random Forest yaitu luas bangunan dan luas lahan.

Secara umum proyek ini berhasil menjawab permasalahan dan dalam implementasinya perlu diperhitungkan faktor-faktor lainnya baik teknis maupun non teknis. Selain pengaturan *hyperparameter* untuk mendapat tuning parameter yang lebih baik, hendaknya dapat ditambahkan data-data yang lebih banyak dan valid agar model pembelajaran mesin ini memiliki akurasi lebih tinggi.

### Reference

[1] A. D. Prastiwi, "Urban Heat Island di Kota Tangerang Selatan," *Jurnal Geosaintek*, vol. 8, no. 2, hal. 182, 2022. [Online]. Tersedia: https://doi.org/10.12962/j25023659.v8i2.11721.

[2] I. Maula, L. U. Hasanah, dan A. Tholib, "Analisis prediksi harga rumah di Jabodetabek menggunakan Multiple Linear Regression," *Jurnal Informatika Kaputama (JIK)*, vol. 7, no. 2, hal. 216-224, 2023. [Online]. Tersedia: https://doi.org/10.59697/jik.v7i2.135.

[3] M. L. Mu’tashim, S. A. Damayanti, H. N. Zaki, T. Muhayat, dan R. Wirawan, "Analisis prediksi harga rumah sesuai spesifikasi menggunakan Multiple Linear Regression," *Jurnal Informatik*, vol. 17, hal. 238-245, 2021. [Online]. Tersedia: https://doi.org/10.52958/iftk.v17i3.3635.

[4] C. Haryanto, N. Rahaningsih, dan F. Muhammad Basysyar, "Komparasi algoritma machine learning dalam memprediksi harga rumah," *JATI (Jurnal Mahasiswa Teknik Informatika)*, vol. 7, no. 1, hal. 533-539, 2023. [Online]. Tersedia: https://doi.org/10.36040/jati.v7i1.6343.
