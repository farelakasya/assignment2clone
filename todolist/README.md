
# Assignment 4 & 5 PBP
Nama: Farel Rishad Akasya

NPM: 2106631646

Kelas: PBP-C

Link : https://assignment-2-pbp-farel.herokuapp.com/todolist/login/?next=/todolist/


# Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen ?

Cross-Site Request Forgery (CSRF) Token adalah nilai rahasia, unik, dan tidak terduga yang dihasilkan oleh aplikasi sisi server untuk melindungi sumber daya yang rentan. Token dihasilkan dan dikirimkan oleh aplikasi sisi server dalam permintaan HTTP berikutnya yang dibuat oleh klien. Setelah permintaan tersebut dibuat, aplikasi sisi server membandingkan dua token yang ada di sesi pengguna dan dalam permintaan. Jika token tidak ada atau tidak cocok dengan nilai dalam sesi pengguna, permintaan akan ditolak, sesi pengguna dihentikan dan peristiwa dicatat sebagai potensi serangan CSRF.
Bila tidak ada {% csrf_token %}, Django tidak mengizinkan dan akan mengeluarkan error message.

# Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Ya, kita dapat membuat <form> secara manual dengan cara menambahkan tag <form method=”POST”> . Lalu tambahkan {% csrf_token %}. Tambahkan <input> untuk memasukkan data dari pengguna. Lalu tambahkan <button type=”submit”> untuk submit form.

# Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Ketika user submit form, browser akan mengirim “POST” request kepada server. Dalam views, akan mengambil data dengan method request.POST.get(“inputName”) dan akan menciptakan object menggunakan Task.objects.create(FIELDS=INPUT, dst) dan kita dapat mengaksesnya menggunakan Task.objects.filter(user=request.user) untuk menampilkan data kepada user yang sesuai. Kita dapat render data yang ada menggunakan {% for task in todolist %} untuk me-loop yang dibutuhkan.


# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Create app todolist dengan python3 manage.py startapp todolist pada terminal.
2. Tambahkan path pada project_django dengan menambahkan todolist pada INSTALLED_APPS pada project_django/settings.py dan path('todolist/', include('todolist.urls'))  pada urlpatterns dalam project_django/urls.py.
3. Buat sebuah model Task dengan atribut user, date, title, description, dan is_finished pada todolist/models.py
4. Migrasikan skema model ke dalam local django database dengan python3 manage.py makemigrations dan python2 manage.py migrate.
5. Buat folder untuk menyimpan template html dengan namatemplates dan isi dengan create_task.html, login.html, register.html, dan todolist.html. 
6. Pada todolist/views.py, buatlah fungsi show_todolist untuk memberi response berupa tampilan , register_user, login_user, logout_user, create_task, delete_task, dan update_task.
7. Pada todolist/urls.py, buat  routing terhadap berbagai fungsi yang ada pada todolist/views.py
8. Deploy Heroku

# Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

Internal CSS ditulis di dalam tag <style> di bagian atas (header) file HTML dan berguna untuk membuat tampilan pada satu halaman website dan tidak digunakan pada halaman website yang lain.Keunggulan internal css adalah tidak perlu memuat file lainnya karena sudah ada di file HTML. Class dan ID bisa digunakan oleh internal stylesheet. Kelemahannya adalah website menjadi lebih lambat dan tidak efisien ketika ingin menggunakan CSS yang sama dalam beberapa file.

External CSS ditulis terpisah dari kode HTML. External CSS ditulis pada file khusus yang berekstensi .css. File eksternal CSS biasanya diletakkan setelah bagian <head> pada halaman. Keunggulan external CSS adalah file HTML menjadi lebih bersih dan mudah untuk dibaca serta css file bisa digunakan untuk beberapa halaman. Kelemahannya adalah download time menjadi lebih lama.

Inline CSS adalah kode CSS yang ditulis langsung pada atribut elemen HTML untuk menata elemen HTML tertentu. Untuk style CSS ini, Anda hanya perlu menambahkan atribut style ke setiap tag HTML, tanpa menggunakan selector. Keunggulannya adalah request HTTP kecil sehingga load cepat. Kelemahannya adalah tidak efisien karena Inline style CSS hanya bisa diterapkan pada satu elemen HTML.

# Jelaskan tag HTML5 yang kamu ketahui.

<body> membuat badan dokumen. <header> menandakan kepala dokumen atau sebuah seksi
<img> menandakan gambar. <table> membuat tabel data. <tr> membuat baris pada tabel

# Jelaskan tipe-tipe CSS selector yang kamu ketahui.

:read-only
menandakan atribut input hanya bisa dibaca.

:out-of-range
menandakan elemen input di luar jangkauan.

:fullscreen
mengambil elemen dalam mode layar penuh.

:disabled
mengambil input yang disabled.

:active
mengambil link yang aktif.

# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Saya menggunakan tailwind dan mencari template yang sesuai dengan keinginan. Lalu, saya copy template tersebut dan ubah class menjadi sesuai. Lalu, untuk pembuatan card pada todolist.html, saya mengimplementasikan for loop untuk membuat card baru setiap dibuat task baru.








