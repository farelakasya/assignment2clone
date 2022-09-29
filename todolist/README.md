# Assignment 4 PBP
Nama: Farel Rishad Akasya

NPM: 2106631646

Kelas: PBP-C

Link : https://assignment-2-pbp-farel.herokuapp.com/mywatchlist/html/


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

