from django.shortcuts import render, HttpResponse, redirect
# from django.http import JsonResponse


def index(request):
    if 'count' not in request.session:
        request.session['count'] = 1
    else:
        request.session['count'] += 1
        
    context = {
        'count' : request.session['count'],
    }
    return render(request,'index.html', context)

def destroy_session(request):
    request.session.flush()
    
    return redirect('/')