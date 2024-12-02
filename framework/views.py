from django.shortcuts import render, get_object_or_404
from .models import Framework

def index(request):
    frameworks = Framework.objects.all()
    return render(request, 'framework/index.html', {'frameworks': frameworks})

def detail(request, framework_id):
    detailframework = get_object_or_404(Framework, pk=framework_id)
    return render(request, 'framework/detail.html', {'framework': detailframework})

def framework_detail(request, id):
    framework = get_object_or_404(Framework, id=id)
    return render(request, 'framework/detail.html', {'framework': framework})