from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

data = MyWatchList.objects.all()

# Create your views here.
def show_watchlist(request):
    movies_watched = 0
    movies_count = 0
    for movie in data:
        movies_count +=1
        if movie.watched:
            movies_watched += 1
    watch_prompt = "Wah, kamu masih sedikit menonton!"

    if movies_watched > movies_count/2:
        watch_prompt = "Selamat, kamu sudah banyak menonton!"

    context = {
        'list_movies': data ,
        'name' : 'Farel Rishad Akasya',
        'student_Id' : '2106631646',
        'watch_prompt' : watch_prompt
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
