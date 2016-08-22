from django.http import HttpResponse


def index(request):
    return HttpResponse("Home page for maidin app.")
