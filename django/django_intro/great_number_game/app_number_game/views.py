from django.shortcuts import render, redirect
# from django.http import JsonResponse
import random

def index(request):
    if 'num' not in request.session:
        request.session['num'] = random.randint(1,100) # random number between 1-100
    print(request.session['num'])
    context = {
        'num' : request.session['num'],
    }
    return render(request, 'index.html',context)

def guess(request):
    if request.method == 'POST':
        request.session['guess']  = int(request.POST.get('guess'))
    return redirect('/')

def reset(request):
    request.session.flush()
    return redirect('/')