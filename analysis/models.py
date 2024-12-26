from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='images/')
    summary = models.TextField()
    pdf = models.FileField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Profile(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='images/')
    summary = models.TextField()
    resume = models.FileField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name