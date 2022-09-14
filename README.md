
# Assignment 2 PBP
Nama: Farel Rishad Akasya

NPM: 2106631646

Kelas: PBP-C

1. Bagan


2. Alasan menggunakan virtual environment
Penggunaan virtual environment bertujuan untuk mengerjakan suatu project yang mengandung versi berbeda dari sebuah library. Virtual environment memungkinkan kita untuk update versi sebuah library tanpa mengubah versi library yang lainnya di project yang sama. 

Kita masih dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, tetapi tindakan tersebut rentan untuk merusak project lain yang membutuhkan versi library yang berbeda karena akan mengupdate versi yang dibutuhkan pada project lain tersebut.

3. Cara implementasi
Pertama, saya membuat function show_catalog yang menerima parameter request dan mengeluarkan hasil render dan ditampilkan pada katalog.html. Data yang diambil pada fungsi tersebut merupakan data katalog dari model CatalogItem.

Kedua, urls.py diisi diisi route/katalog untuk menjalankan fungsi show_katalog pada file katalog/views.py untuk dialihkan ke views yang bersesuaian.

Ketiga, saya passing variabel context pada views.py via render method untuk dimasukkan dalam template HTML.

Keempat, saya menghubungkan repository github dengan heroku  dan menambah HEROKU_API_KEY dan HEROKU_APP_NAME sebagai secrets pada github dan heroku.

