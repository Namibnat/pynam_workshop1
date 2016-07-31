from django.shortcuts import render
from datetime import datetime


def list(request):
    thedate = datetime.now()
    content = {'date': thedate}
    return render(request, 'list.html', content)
