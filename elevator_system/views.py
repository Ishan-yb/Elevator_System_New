from django.http import HttpResponse


def home_page(request):
    print('My_first_view')
    return HttpResponse("this is home page")
