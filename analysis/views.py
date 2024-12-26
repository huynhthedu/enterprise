from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Profile
from .forms import ArticleForm, ProfileForm

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'analysis/article_list.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'analysis/article_detail.html', {'article': article})

def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'analysis/article_form.html', {'form': form})


def profile_detail(request):
    profile = get_object_or_404(Profile, pk=1)  # Assuming only one profile
    return render(request, 'analysis/profile_detail.html', {'profile': profile})

def profile_edit(request):
    profile = get_object_or_404(Profile, pk=1)  # Assuming only one profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_detail')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'analysis/profile_form.html', {'form': form})