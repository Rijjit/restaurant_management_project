from django.shortcuts import render


# Create your views here.
def home_page(request):
    context ={
        "restaurant_name" : "The Sebs'"
    }
    return render(request, "home-html", context)