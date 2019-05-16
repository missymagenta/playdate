from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Places
from django.utils import timezone

def home(request):
    return render(request,'places/home.html')

@login_required()
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['image']:
            place = Places()
            place.title = request.POST['title']
            place.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                place.url = request.POST['url']
            else:
                place.url = 'http://' + request.POST['url']
            place.image = request.FILES['image']
            place.pub_date = timezone.datetime.now()
            place.hunter = request.user
            place.save()
            return redirect('home')

        else:
            return render(request, 'places/create.html', {'error': 'All fields are required'})

    else:
        return render(request,'places/create.html')
