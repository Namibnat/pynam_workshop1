from django.shortcuts import render
from datetime import datetime


def list(request):
    """
    This is the view for our main page

    Dynamically changes the date on our
    website every time the user refreshes the page
    """
    thedate = datetime.now()
    content = {'date': thedate}
    return render(request, 'list.html', content)
