from django.shortcuts import render, HttpResponse, redirect # add redirect to import statement
from  django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

def test(request):
    return HttpResponse("This is a test equivalent of @app.route('/test')!")

def example_method(request):
    return HttpResponse("bears") # no values passed via URL

def example_method_two(request, my_val): # my_val would be a number from the URL
    pass                                # given the example above, my_val would be 23

def example_method_three(request, name): # name would be a string from the URL
    pass                                # given the example above, name would be 'pooh'

def one_more(request, id, color): 	    # id would be a number, and color a string from the URL
    pass                                # given the example above, id would be 17 and color would be 'brown'

def another_method(request):
    return redirect("/redirected_route")

def redirected_method(request):
    return JsonResponse({'response': "Json response from redirected_method", "status":True})

def hello_name(request, name):
    context = {
        "htmlname": name,
        'namelist': ['Alice','Bob','Charlie', 'David'] ,
    }
    return render(request, "helloname.html", context)