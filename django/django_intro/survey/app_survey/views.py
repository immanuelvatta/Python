from django.shortcuts import render, redirect


def index(request):
    return render(request, 'survey.html')

def results(request):
    name = request.POST['name']
    location = request.POST['location']
    fav_language = request.POST['fav_language']
    comment = request.POST['comment']
    context = {
        'name': name,
        'location': location,
        'fav_language': fav_language,
        'comment': comment,
    }
    return render(request, 'result.html', context)


def go_back(request):
    return redirect('/')