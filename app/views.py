from django.shortcuts import render
from .models import MyModel

def home(request):
    return render(request, 'home.html')

def show_all_records(request):
    all_records = MyModel.objects.all()
    return render(request, 'all_records.html', {'records': all_records})
