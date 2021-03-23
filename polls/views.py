from django.shortcuts import render


def index(request):
    return render(request, 'polls/index.html')


def page2(request):
    return render(request, 'polls/page2.html')
