from django.shortcuts import render

# Create your views here.


def show_menubase(request):

    return render(request, "menu_base.html")