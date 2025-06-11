from django.shortcuts import render, HttpResponse

# Create your views here.

def home_view(request):
    context = {
        'isim': 'Umut',
    }

    return render(request, 'home.html', context)