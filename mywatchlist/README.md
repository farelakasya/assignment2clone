
# Assignment 3 PBP
Nama: Farel Rishad Akasya

NPM: 2106631646

Kelas: PBP-C

Link : https://assignment-2-pbp-farel.herokuapp.com/mywatchlist/html/


# Jelaskan perbedaan antara JSON, XML, dan HTML!
HTML adalah bahasa markup yang berfungsi untuk menyusun struktur website. HTML terdiri dari kombinasi teks dan simbol yang disimpan dalam sebuah file.

JSON adalah turunan JavaScript yang digunakan dalam transfer data dan penyimpanan data.  JSON digunakan untuk mengirim data dengan cara menguraikan data dan dikirim melalui internet. JSON menyimpan elemennya secara efisien akan tetapi tidak rapi untuk dilihat. JSON lebih ringkas karena tidak memerlukan tag pembuka dan penutup. 

XML memiliki data yang lebih terstruktur dan pengguna dapat menggunakannya untuk catatan. XML mudah dibaca oleh manusia dan mesin, tetapi kurang efisien. XML bersifat dinamis sedangkan HTML bersifat statis.

# Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery diperlukan untuk mempermudah ketika mengimplementasikan platform untuk menampilkan dan mengedit data yang disimpan dalam database back-end oleh aplikasi front-end. 

# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1. Membuat aplikasi mywatchlist 
Saya menyalakan virtual environment dan menjalankan perintah python3 manage.py startapp watchlist. 

2. Menambahkan path mywatchlist
Menambahkan mywatchlist pada file project_django/urls.py dengan kode

…

path('mywatchlist/',include('mywatchlist.urls'))

]

Dan pada project_django/settings.py menambahkan kode

INSTALLED_APPS = [
	
    ….
	
    ‘mywatchlist’,

]

3. Membuat model bernama MyWatchList dan atributnya
Membuat model MyWatchlist di  mywatchlist/models.py dengan atribut-atribut watched, title, rating, release_date, review dengan field masing-masing yang sesuai. Lalu, migrasikan data dengan menjalankan python manage.py makemigration dan python manage.py migrate.

4. Memasukkan data pada objek MyWatchList
Membuat folder fixtures dalam mywatchlist lalu membuat file json bernama 'initial_watchlist_data.json'. Isi file json tersebut dengan data film yang ingin dimasukkan. 

5. Membuat fitur untuk menyajikan data dalam tiga format
Buatlah fungsi individu penampilan data-data dalam format html, json, dan xml. Route agar masing-masing format data dapat ditampilkan dengan membuat path dalam mywatchlist/urls.py. 

6. Membuat routing sehingga data di atas dapat diakses melalui URL
Menambahkan ‘&& python manage.py loaddata movies_catalog.json’ di  Procfile. 

Screenshot Postman

HTML
![](https://raw.githubusercontent.com/farelakasya/assignment2clone/mywatchlist/assets/html.png)

JSON
![](https://raw.githubusercontent.com/farelakasya/assignment2clone/mywatchlist/assets/json.png)

XML
![](https://raw.githubusercontent.com/farelakasya/assignment2clone/mywatchlist/assets/xml.png)
