from django.shortcuts import render
from datetime import datetime

# Create your views here.
def hello_world(request):
    return render(
        request,
        'hello_world.html',
        {
            'title':'Hello',
            'message':'Your Hello page.',
            'year':datetime.now().year,
        }
    )