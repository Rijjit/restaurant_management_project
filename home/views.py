from django.shortcuts import render


# Create your views here.
def home_page(request):
    context ={
        "restaurant_name" : settings.RESTAURANT_NAME,
        "restaurant_phone" : settings.RESTAURANT_PHONE
    }
    return render(request, "home-html", context)

def contact(request):
    return render(request, 'contact.html', {
        'restaurant_name' : settings.RESTAURANT_NAME,
        'restaurant_phone' : settings.RESTAURANT_PHONE
    })

def menu(request):
    menu_items = [
        {"name": "Cheese Pizza", "price": "Rs. 250.00"},
        {"name": "White Sauce Pasta", "price": "Rs. 199.00"},
        {"name": "Chicken Burger", "price": "Rs. 199.00"},
        {"name": "Cold Coffee", "price": "Rs. 99.00"},
    ]
    return render(request, 'menu.html', {"menu_items": menu_items})

def about(request):
    return render(request, 'about.html', {"restaurant_name": settings.RESTAURANT_NAME})

def custom_404(request, exception):
    return render(request, '404.html', status=404)
