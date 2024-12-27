from django.shortcuts import render, get_object_or_404, redirect
from .models import Framework
from .forms import ImageForm
from .models import Image

def index(request):
    frameworks = Framework.objects.all()
    return render(request, 'framework/index.html', {'frameworks': frameworks})

def detail(request, framework_id):
    detailframework = get_object_or_404(Framework, pk=framework_id)
    return render(request, 'framework/detail.html', {'framework': detailframework})

def framework_detail(request, id):
    framework = get_object_or_404(Framework, id=id)
    return render(request, 'framework/detail.html', {'framework': framework})


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = ImageForm()
    return render(request, 'framework/upload_image.html', {'form': form})

def image_list(request):
    images = Image.objects.all()
    return render(request, 'framework/image_list.html', {'images': images})